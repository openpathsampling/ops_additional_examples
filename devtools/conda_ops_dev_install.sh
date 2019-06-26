#!/bin/sh

# This assumes you've already installed conda. Then it installs OPS as a
# developer install.

conda install -y --quiet -c omnia openpathsampling future
conda update -y --quiet --all
conda uninstall -y openpathsampling
git clone https://github.com/openpathsampling/openpathsampling.git
cd openpathsampling && pip install -e . && cd ..

