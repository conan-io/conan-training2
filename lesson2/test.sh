#!/bin/bash

set -e

conan install . --build=missing -pr=debug
cmake --preset=conan-debug
cmake --build --preset=conan-debug
./build/Debug/formatter

conan install . --build=missing --options="*:shared=True"
cmake --preset=conan-release
cmake --build --preset=conan-release
./build/Release/formatter

. build/Release/generators/conanrun.sh

./build/Release/formatter

conan list "fmt/11.2.0:*" --format=compact
