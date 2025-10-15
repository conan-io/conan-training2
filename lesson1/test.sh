#!/bin/bash

set -e

conan profile detect --force
conan install . --build=missing
cmake --list-presets
cmake --preset=conan-release
cmake --build --preset=conan-release
./build/Release/formatter
