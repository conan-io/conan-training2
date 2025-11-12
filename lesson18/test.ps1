$ErrorActionPreference = 'Stop'

# Add hello package to editable mode
conan editable add hello

# List editable packages
conan editable list

# List all packages (editable packages will be marked)
conan list "*:*"

cd say

# Try to build src
conan build . --build=missing --build=editable

# It built successfully and we can run it
./build/Release/say.exe

cd ..

# And now ensure the usual workflow still works
conan editable remove hello

conan create hello --build=missing

conan create say
