#!/bin/bash

# install the dependencies with two profiles, fmt will be built for the raspberry profile
conan install . --build missing --profile:build=default --profile:host=./profiles/raspberry

# activate the build environment so that we use the selected CMake version for building
source build/Release/generators/conanbuild.sh

# build our application for the Raspberry Pi
cmake --preset conan-release
cmake --build --preset conan-release

# check that we built the correct architecture
file ./build/Release/formatter 