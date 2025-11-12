#!/bin/bash

set -e

conan profile detect --force
conan install . --build=missing
cmake --preset=conan-release
cmake --build --preset=conan-release
./build/Release/formatter

