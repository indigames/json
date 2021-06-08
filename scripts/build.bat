@echo off

set CALL_DIR=%CD%
set PROJECT_DIR=%~dp0..
set CONAN_REVISIONS_ENABLED=1

cd %PROJECT_DIR%
python %~dp0../build.py

cd %CALL_DIR%
