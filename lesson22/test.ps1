$ErrorActionPreference = 'Stop'

# Show config home
conan config home

# List profiles before install
conan profile list

# Install configuration from local folder
conan config install install-example

# List profiles after install
conan profile list

# Show the installed profile
conan profile show -pr:a lesson22-profile
