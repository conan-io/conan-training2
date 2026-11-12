#!/bin/bash

set -e

# List packages in cache
conan list fmt

# List packages in remote
conan list fmt -r=conancenter

# Install hello with dependencies
conan install hello --build=missing -r=conancenter

# Create lockfile
conan lock create hello

# Version conflicts: --update makes the range of parser resolve to the latest fmt in ConanCenter
conan create conflicts/parser --build=missing -r=conancenter --update
conan create conflicts/network --build=missing -r=conancenter

# Check how conan create conflicts/app fails, then uncomment the override in conflicts/app/conanfile.py
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' 's/# self.requires/self.requires/' conflicts/app/conanfile.py
else
    sed -i 's/# self.requires/self.requires/' conflicts/app/conanfile.py
fi

# parser has no binary for the overridden fmt version: build it
conan create conflicts/app --build=missing -r=conancenter

