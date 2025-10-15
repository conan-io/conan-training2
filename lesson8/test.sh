#!/bin/bash

set -e

# Create a template project of a CMake library
# Files already theer
# conan new cmake_lib -d name=hello -d version=1.0 --force

# Create the package
conan create .

# List the created packages
conan list "*:*" 