$ErrorActionPreference = 'Stop'

conan install . --build=missing

# This version should be the one installed in your system
cmake --version  

# By activating the conanbuild environment, the new cmake version will correspond to the one listed in build requirements

# Windows

build\Release\generators\conanbuild.bat

cmake --version

cmake --preset=conan-default
cmake --build --preset=conan-release

# Windows
build\Release\generators\conanrun.bat

build\Release\formatter 
