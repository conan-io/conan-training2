#!/bin/bash

set -e

conan install conanfile_complete.py --build=missing -o="&:with_std_format=True" -s="compiler.cppstd=20"

cmake --preset conan-release
cmake --build --preset conan-release

./build/Release/formatter
