#!/bin/bash

set -e

conan source .
conan install . --build=missing
conan build .
conan export-pkg .

# List the created package
conan list hello/1.0

