@echo off
setlocal enabledelayedexpansion

set /p GITHUB_TOKEN=<D:\DevTools\github.token
if not exist "!IGE_BUILDER!\.git" (
    if exist "!IGE_BUILDER!" (
        rmdir /s /q "!IGE_BUILDER!"
    )
    mkdir "!IGE_BUILDER!"
    git clone https://!GITHUB_TOKEN!@github.com/indigames/igeBuilder !IGE_BUILDER!
) else (
    cd !IGE_BUILDER!
    git fetch --all
    git checkout main
    git pull
)

set CONAN_REVISIONS_ENABLED=1
conan remote add ige-center http://10.1.0.222:8081/artifactory/api/conan/conan
conan user -p Indi@2019 -r ige-center thai.phi

cd %WORKSPACE%
if exist "project.conf" (
    for /f "usebackq delims=" %%a in ("project.conf") do (
        set ln=%%a
        for /f "tokens=1,2 delims=: " %%b in ("!ln!") do (
                set currkey=%%b
                set currval=%%c
                
                if "!currkey!"=="name" (
                    set PROJECT_NAME=!currval!
                ) else if "!currkey!"=="version" (
                    set PROJECT_VER=!currval!
                )
            )
        )
    )
)
call !IGE_BUILDER!\build-header-only-lib.bat . !PROJECT_NAME! !PROJECT_VER!