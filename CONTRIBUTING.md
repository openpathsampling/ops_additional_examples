# Contributing extra examples

Have an example that we can't fit into the OPS core? Great! This is the
place for it. Here's how to add new examples here.

For now, we're putting the example notebooks (along with any preliminary
python scripts to generate data) directly in the main directory.  If your
example needs anything else in order to run (download data files? run a
preliminary script? switch to a special branch of OPS?), you should do that
as part of a script located at `devtools/prepare/NOTEBOOK.sh`, for the
notebook named `NOTEBOOK.ipynb`. This script will be automatically found,
and run from the root directory as part of our automated testing suite.

You can assume that we have a developer install of OpenPathSampling with the
latest `master` as the default setup. From there, you can add remotes and
change branches in your prepare script.

To debug problems getting your notebooks to run in the automated test
pipeline, you can (temporarily) override the `NOTEBOOKS` variable set in the
`script` section of `.gitlab-ci.yml`. Copy the commented example line (to
preserve the original), uncomment it, and use your notebook's name. Multiple
notebooks can be run by space-separating their names. Tests are run using
[ipynbtest](https://github.com/jhprinz/ipynb-test); see that documentation
for more.
