#!/bin/bash

# Conditional requirements slide
conan install . --build=missing -o="&:with_std_format=True"

# Using the generate() method slide
conan install conanfile_complete.py --build=missing -o="&:with_std_format=True"

# Running after all our changes
conan install conanfile_complete.py --build=missing -o="&:with_std_format=True" -s="compiler.cppstd=20"

# Linux & macos
cmake --preset conan-release
cmake --build --preset conan-release
./build/Release/formatter 