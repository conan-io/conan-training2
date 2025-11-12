$ErrorActionPreference = 'Stop'

conan config install . --target-folder=extensions/commands
conan greetings:hello "Hello World!"
conan profiles:search "x86_64"

