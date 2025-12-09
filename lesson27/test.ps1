$ErrorActionPreference = 'Stop'

# Create the package
conan create . --build=missing
