$ErrorActionPreference = 'Stop'

# First part: Create packages with basic conanfiles
conan create math --build=missing
conan create engine --build=missing
conan create game --build=missing

# Second part: Create packages with options using library conanfiles
# Replace conanfiles with library versions
Remove-Item math/conanfile.py
Remove-Item engine/conanfile.py
Copy-Item math/conanfile_library.py math/conanfile.py
Copy-Item engine/conanfile_library.py engine/conanfile.py

# Create math with header_only option
conan create math -o="math/*:header_only=True" --build=missing

# Create engine with shared and math header_only options
conan create engine -o="engine/*:shared=True" -o="math/*:header_only=True" --build=missing

# Create game with same options
conan create game -o="engine/*:shared=True" -o="math/*:header_only=True" --build=missing

