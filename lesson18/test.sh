#!/bin/bash

set -e

# Add hello package to editable mode
conan editable add hello

cd say

# Try to build src
conan build . --build=missing --build=editable

# It built successfully and we can run it
./build/Release/say

cd ..

# And now ensure the usual workflow still works
conan editable remove hello

conan create hello --build=missing

conan create say
