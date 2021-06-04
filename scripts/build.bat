@echo off

set CALL_DIR=%CD%
set PROJECT_DIR=%~dp0..

cd %PROJECT_DIR%
set CONAN_REVISIONS_ENABLED=1
conan create . ige/test

cd %CALL_DIR%
