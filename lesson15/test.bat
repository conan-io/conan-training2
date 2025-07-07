@echo off

REM inspect the vendor folder
cd prebuilt && dir vendor_hello_library

REM Create packages for different configurations
conan export-pkg . -s os='Windows' -s arch='x86_64'

REM Inspect the packages created in the cache
conan list hello/0.1#:*

cd prebuilt_remote

REM Create packages with binaries from a remote
conan create . -s os='Windows' -s arch='x86_64'

REM List the packages created in the cache
conan list hello/0.1#:*

cd ../development/mylib

REM Install and build normally
conan install .

cmake --preset=conan-default

cmake --build --preset conan-release

REM Export the binaries to the cache
conan export-pkg .

cd ../consumer

REM Check that the consumer works
conan create .
