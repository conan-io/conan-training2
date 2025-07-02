@echo off

conan install . --build=missing

REM This version should be the one installed in your system
cmake --version  

REM By activating the conanbuild environment, the new cmake version will correspond to the one listed in build requirements

REM Windows

build\Release\generators\conanbuild.bat

cmake --version

cmake --preset=conan-default
cmake --build --preset=conan-release

REM Windows
build\Release\generators\conanrun.bat

build\Release\formatter 
