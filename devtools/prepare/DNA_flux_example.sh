#!/usr/bin/env bash

figshare_ID=4508975
version=1

mkdir $figshare_ID
curl -Lk -o ${figshare_ID}.zip \
    https://ndownloader.figshare.com/articles/${figshare_ID}/versions/$version
ls -l
unzip -d $figshare_ID ${figshare_ID}.zip

