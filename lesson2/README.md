# Linux and macOS

```bash
conan config home

# check the profiles there
cat $(conan config home)/profiles/default

conan install . --build=missing --settings="build_type=Debug"
cmake --list-presets
cmake --preset=conan-debug
cmake --build --preset=conan-debug
./build/Debug/formatter
```

# Windows

```bash
conan config home

conan install . --build=missing --settings="build_type=Debug"
cmake --build --list-presets
cmake --build --preset conan-debug
./build/Debug/formatter
```