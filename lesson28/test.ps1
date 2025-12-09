$ErrorActionPreference = 'Stop'

conan config install settings_user.yml

conan create . -s compiler=mycompany_compiler -s compiler.version=1.0 --build=missing

