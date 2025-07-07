@echo off

REM List all the revisions of a given reference in a remote
conan list "fmt/11.2.0#*" -r=conancenter

REM Install our version range dependencies
conan install . --build=missing

REM Create a lockfile with the pinned versions
conan lock create . 

REM Install the dependencies once we add the version ranges back
REM This time the lockfile will be picked up
conan install . --build=missing
