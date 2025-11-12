#!/bin/bash

set -e

conan create math --build=missing
conan create engine --build=missing
conan create game --build=missing

