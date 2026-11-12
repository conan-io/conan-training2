$ErrorActionPreference = 'Stop'

# Part 1: Advanced version ranges

# List packages in cache
conan list fmt

# List packages in remote
conan list fmt -r=conancenter

# Install hello with dependencies
conan install hello --build=missing -r=conancenter

# Version conflicts: --update makes the range of parser resolve to the latest fmt in ConanCenter
conan create conflicts/parser --build=missing -r=conancenter --update
conan create conflicts/network --build=missing -r=conancenter

# Check how conan create conflicts/app fails, then uncomment the override in conflicts/app/conanfile.py
powershell -Command "(Get-Content conflicts/app/conanfile.py) -replace '# self.requires', 'self.requires' | Set-Content conflicts/app/conanfile.py"

# parser has no binary for the overridden fmt version: build it
conan create conflicts/app --build=missing -r=conancenter

# Part 2: Advanced lockfiles

# Create lockfile
conan lock create hello

