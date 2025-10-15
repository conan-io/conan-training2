#!/bin/bash

set -e

conan install . --build=missing

# This version should be the one installed in your system
cmake --version  

# By activating the conanbuild environment, the new cmake version will correspond to the one listed in build requirements

# Linux and macOS
. build/Release/generators/conanbuild.sh

cmake --version

cmake --preset=conan-release
cmake --build --preset=conan-release

# Linux and macOS
. build/Release/generators/conanrun.sh

./build/Release/formatter 
