#!/bin/bash

set -e

conan create . --build=missing -tf="" -s="compiler.cppstd=17"

