$ErrorActionPreference = 'Stop'

conan create . --build=missing -tf="" -s="compiler.cppstd=17"

