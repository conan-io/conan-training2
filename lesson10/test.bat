@echo off

REM Check how it fails, then change hellolib for hello in the conanfile.py
powershell -Command "(Get-Content conanfile.py) -replace 'hellolib', 'hello' | Set-Content conanfile.py"

REM Create the package again, it succeeds
conan create . 