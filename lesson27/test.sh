#!/bin/bash

set -e

# Create the package
conan create . --build=missing
