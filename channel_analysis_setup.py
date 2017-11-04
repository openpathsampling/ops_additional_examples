#!/usr/bin/env python

"""
Script to run a quick path sampling simulation on a toy model that will
exhibit switching between two channels.
"""

from __future__ import print_function
import openpathsampling as paths

import openpathsampling.engines.toy as toys
import numpy as np

pes = (toys.OuterWalls([1.0,1.0], [0.0,0.0])
       + toys.Gaussian(-0.7, [30.0, 0.5], [-0.6, 0.0])
       + toys.Gaussian(-0.7, [30.0, 0.5], [0.6, 0.0])
       + toys.Gaussian(0.5, [85.0, 70.0], [0.1, 0.0]))
topology = toys.Topology(n_spatial=2, masses=[1.0, 1.0], pes=pes)
engine = toys.Engine(
    {'integ': toys.LangevinBAOABIntegrator(dt=0.02,
                                           temperature=0.1,
                                           gamma=2.5),
     'n_frames_max': 5000,
     'n_steps_per_frame': 10}, topology)
template = toys.Snapshot(coordinates=np.array([[0.0, 0.0]]),
                         velocities=np.array([[0.0, 0.0]]),
                         engine=engine)

def val(snapshot, index):
    return snapshot.xyz[0][index]

cv_x = paths.FunctionCV("xval", val, index=0)
cv_y = paths.FunctionCV("yval", val, index=1)

stateA = paths.CVDefinedVolume(cv_x, float("-inf"), -0.6).named("A")
stateB = paths.CVDefinedVolume(cv_x, 0.6, float("inf")).named("B")

network = paths.TPSNetwork(stateA, stateB)
scheme = paths.OneWayShootingMoveScheme(network=network, engine=engine)

# I'll fake an initial trajectory
trajectory = paths.Trajectory([
    toys.Snapshot(coordinates=np.array([[-.65+k*0.1, 0.0]]),
                  velocities=np.array([[0.1, 0.0]]),
                  engine=engine)
    for k in range(14)
])

initial_conditions = scheme.initial_conditions_from_trajectories(trajectory)

# use this for debugging the equilibration
# equil_store = paths.Storage('equil.nc', 'w')
equil_store = None

# update the user on what we're doing
equil_str = "Running 1000 steps of equilibration."
if equil_store is None:
    equil_str += " Not saving equilibration steps."
print(equil_str)

equil_sim = paths.PathSampling(storage=equil_store,
                               move_scheme=scheme,
                               sample_set=initial_conditions)
simulation.status_update_frequency = 200
equil_sim.run(1000)

equil_conditions = equil_sim.sample_set

# this should be a decorrelated trajectory
equil_traj = equil_conditions[0].trajectory
init_traj = initial_conditions[0].trajectory
assert(not equil_traj.is_correlated(init_traj))

print("Setting up the full simulation and running 10000 steps.")

simulation = paths.PathSampling(
    storage=paths.Storage('channel_analysis_sim.nc', 'w'),
    move_scheme=scheme,
    sample_set=equil_conditions
)
simulation.save_frequency = 200
simulation.status_update_frequency = 200

simulation.run(10000)

simulation.storage.save(cv_y)
simulation.storage.close()
