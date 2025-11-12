$ErrorActionPreference = 'Stop'

conan source .
conan install . --build=missing
conan build .
conan export-pkg .

