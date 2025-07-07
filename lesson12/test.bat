@echo off

REM test the already created package for the default profile
conan test test_package hello/1.0

REM test the already created package for Debug
REM use a profile or you can also use -s="build_type=Debug"
conan test test_package hello/1.0 --profile=./debug 