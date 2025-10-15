#!/bin/bash

set -e

# create the tool requires for Release, use the --build-require argument 
conan create . --build-require -s:b build_type=Release

# check package id 
conan list 'secure-scanner/1.0#*:*'

# create the tool requires for Debug, use the --build-require argument 
conan create . --build-require -s:b build_type=Debug

# check package id, it will be the same
conan list 'secure-scanner/1.0#*:*' 