$ErrorActionPreference = 'Stop'

conan install . --build=missing -s="build_type=Debug" -c="tools.env.virtualenv:powershell=pwsh"
cmake --preset=conan-default
cmake --build --preset=conan-debug
build/Debug/formatter

conan install . --build=missing --options="*:shared=True"
cmake --preset=conan-default
cmake --build --preset=conan-release
# build/Release/formatter this would fail without the conanrun

. ./build/generators/conanrun.ps1

build/Release/formatter

conan list "fmt/11.2.0:*" --format=compact
