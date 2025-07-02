@echo off

conan install . --build=missing -o="&:with_std_format=True"

conan install conanfile_complete.py --build=missing -o="&:with_std_format=True" -s="compiler.cppstd=20"

cmake --preset=conan-default
cmake --build --preset=conan-debug
build\Release\formatter 