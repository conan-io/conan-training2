$ErrorActionPreference = 'Stop'

# List packages in cache
conan list fmt

# List packages in remote
conan list fmt -r=conancenter

# Install hello with dependencies
conan install hello --build=missing -r=conancenter

# Create lockfile
conan lock create hello

