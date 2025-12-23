#!/bin/bash

set -e

conan install --requires=fmt/[*] -s="compiler.cppstd=20"
