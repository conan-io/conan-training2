#!/bin/bash

# Check how it fails, then change hellolib for hello in the conanfile.py
# Detect OS and use appropriate sed command
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' 's/hellolib/hello/g' conanfile.py
else
    # Linux and other Unix systems
    sed -i 's/hellolib/hello/g' conanfile.py
fi

# Create the package again, it succeeds
conan create . 