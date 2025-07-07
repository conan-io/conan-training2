@echo off

REM Create a template project of a CMake library
conan new cmake_lib -d name=hello -d version=1.0

REM Create the package
conan create .

REM List the created packages
conan list "*:*" 