#!/bin/bash

create_readme_in_empty_dir() {
    d=$1
    echo "3: ${d} is an empty folder"
    touch "${d}/README.md"
}

for d in `ls`; do
    echo "1: ${d}"
    if [ ! -d "${d}" ]; then
        continue
    fi
    echo "2: ${d}"
    find ${d} -type d -print0 | while IFS= read -r -d '' f; do
        [ "$(ls ${f})" ] || create_readme_in_empty_dir "${f}"
    done
done
