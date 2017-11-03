#!/usr/bin/env bash

figshare_ID=4496795
version=1

mkdir $figshare_ID
curl -Lk -o ${figshare_ID}.tgz \
    https://ndownloader.figshare.com/articles/${figshare_ID}/versions/$version
tar -xzf ${figshare_ID}.tgz -C $figshare_ID

