#!/bin/bash

# Request and confirm the new package name.
PACKAGE_NAME=`read name from stdin, etc....`

# Rename a couple files that need to be updated
mv mb_sample_package "$PACKAGE_NAME"
mv mb_sample_package.Jenkinsfile "$PACKAGE_NAME.Jenkinsfile"

# Search through all of the other files and find/replace to update the name
# todo: exclude this script from the find/sed command
find . -maxdepth 1 -type f -exec sed -i'' -e "s,mb_sample_package,$PACKAGE_NAME,g" {} \+

# todo: confirm/remove this script (it only needs to run once)
