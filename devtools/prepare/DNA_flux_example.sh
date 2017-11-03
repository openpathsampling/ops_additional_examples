#!/usr/bin/env bash

figshare_ID=4508975
version=1

mkdir $figshare_ID
curl -Lk -o ${figshare_ID}.tgz \
    https://ndownloader.figshare.com/articles/${figshare_ID}/versions/$version
ls -l
tar -xzf ${figshare_ID}.tgz -C $figshare_ID

