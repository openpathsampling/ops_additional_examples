#!/bin/bash

notebooks="$@"

for base in $notebooks
do
    echo "Looking for ${base}.sh...."
    if [ -e "./devtools/prepare/${base}.sh" ]
    then
        echo "Running devtools/prepare/${base}.sh"
        bash ./devtools/prepare/${base}.sh
    fi
done
