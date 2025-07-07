@echo off

REM The structure is based on a call to conan new header_lib -d=name=hello -d=version=1.0

REM Compile the header-only library, it does not matter what configuration you run, the resulting package id will be the same
conan create . --build=missing
