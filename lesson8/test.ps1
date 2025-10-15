$ErrorActionPreference = 'Stop'

# Create a template project of a CMake library
# Files already there
# conan new cmake_lib -d name=hello -d version=1.0

# Create the package
conan create .

# List the created packages
conan list "*:*" 