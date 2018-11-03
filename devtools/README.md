# `devtools`

This directory contains scripts that are useful when running the example
notebook in an automated way, as we do with continuous integration. By doing
CI (including nightly builds), we ensure that the examples stay up-to-date.

The files in this directory might also be useful for other people working
with examples.

## Installation scripts

* `conda_ops_dev_install.sh`: script to install the development version of
  OPS (once conda has already been installed)
* `install_conda.sh`: script to install conda

## Scripts for running notebooks

* `figshare_dl_extract.sh`: shell script that, given a figshare ID,
  downloads and extracts the associated zip file. Requires `curl` and
  `unzip`.
* `prepare/`: directory containing shell scripts that should be run before
  given example notebooks. For `notebook.ipynb`, the script
  `prepare/notebook.sh` will be run if it exists. Use this to
  download/generate data.
* `run_tests.sh`: main script for running tests: takes a list of notebook
  names (without ipynb suffix) as an argument, then runs the associated
  `prepare` script and the notebook.
* `select_notebooks.py`: selects the notebooks to run. Use the `--skip-file`
  or `--skip` arguments to skip some notebooks.
* `skip`: default skip file to use -- list of notebook names to skip.
  (Probably empty.)
