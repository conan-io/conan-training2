#!/bin/bash

# Check how it fails, then change hellolib for hello in the conanfile.py
sed -i '' 's/hellolib/hello/g' conanfile.py

# Create the package again, it succeeds
conan create . 