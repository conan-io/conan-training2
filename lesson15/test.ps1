$ErrorActionPreference = 'Stop'

# inspect the vendor folder
cd prebuilt && dir vendor_hello_library

# Create packages for different configurations
conan export-pkg . -s os='Windows' -s arch='x86_64'

# Inspect the packages created in the cache
conan list hello/0.1#:*

cd prebuilt_remote

# Create packages with binaries from a remote
conan create . -s os='Windows' -s arch='x86_64'

# List the packages created in the cache
conan list hello/0.1#:*

cd ../development/mylib

# Install and build normally
conan install .

cmake --preset=conan-default

cmake --build --preset conan-release

# Export the binaries to the cache
conan export-pkg .

cd ../consumer

# Check that the consumer works
conan create .
