$ErrorActionPreference = 'Stop'

conan install --requires=fmt/[*] -s="compiler.cppstd=20"
