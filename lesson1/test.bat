conan profile detect --force
conan install . --build=missing
cmake --list-presets
cmake --preset=conan-default
cmake --build --preset conan-release
build\Release\formatter
