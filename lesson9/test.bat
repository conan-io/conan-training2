@echo off

REM Create the package
conan create . --build=missing
