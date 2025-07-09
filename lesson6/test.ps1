$ErrorActionPreference = 'Stop'

# List all the revisions of a given reference in a remote
conan list "fmt/11.2.0#*" -r=conancenter

# Install our version range dependencies
conan install . --build=missing

# Create a lockfile with the pinned versions
conan lock create . 

# Install the dependencies once we add the version ranges back
# This time the lockfile will be picked up
conan install . --build=missing
