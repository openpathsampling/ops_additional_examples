#!/usr/bin/env bash

conda install --yes --quiet pytables  # doesn't come with MDTraj?
conda update --yes --quiet all

bash devtools/figshare_dl_extract.sh 4496795
