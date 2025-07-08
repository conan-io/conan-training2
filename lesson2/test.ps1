$ErrorActionPreference = 'Stop'

conan install . --build=missing -s="build_type=Debug"
cmake --preset=conan-default
cmake --build --preset=conan-debug
build/Debug/formatter

conan install . --build=missing --options="*:shared=True"
cmake --preset=conan-default
cmake --build --preset=conan-release
build/Release/formatter

build/generators/conanrun.bat

build/Release/formatter

conan list "fmt/11.2.0:*" --format=compact
