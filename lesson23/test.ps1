$ErrorActionPreference = 'Stop'

conan install . --build=missing --deployer=full_deploy
conan install . -o '*:shared=True' --build=missing --deployer=runtime_deploy --deployer-folder=runtime
conan install . --deployer license_deploy

