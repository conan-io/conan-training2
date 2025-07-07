@echo off

REM create the tool requires for Release, use the --build-require argument 
conan create . --build-require -s:b build_type=Release

REM check package id 
conan list 'secure-scanner/1.0#*:*'

REM create the tool requires for Debug, use the --build-require argument 
conan create . --build-require -s:b build_type=Debug

REM check package id, it will be the same
conan list 'secure-scanner/1.0#*:*' 