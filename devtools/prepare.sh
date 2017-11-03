#!/bin/bash

for base in $*
do
    filename=$(basename "$ipynb")
    base="${filename%.*}"
    echo "$ipynb: looking for ${base}.sh"
    if [ -e "devtools/prepare/${base}.sh" ]
    then
        ./devtools/prepare/${base}.sh
    fi
done
