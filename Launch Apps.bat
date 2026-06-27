@echo off
setlocal enabledelayedexpansion

echo Checking for Python...
python --version >nul 2>&1

if %errorlevel% equ 0 (
    echo [SUCCESS] Python is installed! Running app!
    python "%~dp0runApps.py"
    goto end
) else (
    echo [WARNING] Python is not installed.
    echo Preparing to install Python via winget...
    start /wait winget install --id Python.Python.3.13 --exact --accept-source-agreements --accept-package-agreements --override "/passive PrependPath=1"
    
    if !errorlevel! equ 0 (
        echo [SUCCESS] Python installed!
        echo Please close this window and run the .bat file again so Windows can detect it.
    ) else (
        echo [ERROR] Winget failed to install Python. Please check your internet connection or install manually.
    )
)

:end