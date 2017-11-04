#!/usr/bin/env bash

# USAGE
#   bash figshare_dl_extract.sh FIGSHARE_ID [FIGSHARE_VERSION]
# 
# FIGSHARE_ID is the numeric ID of the figshare document
# FIGSHARE_VERSION (optional) is the figshare version number; default 1
#
# Resulting files will be extracted into CWD

figshare_ID=$1

if [ $# -gt 1 ]; then 
    version=$2
else
    version=1
fi

mkdir $figshare_ID
curl -Lk -o ${figshare_ID}.zip \
    https://ndownloader.figshare.com/articles/${figshare_ID}/versions/$version
unzip -d $figshare_ID ${figshare_ID}.zip

