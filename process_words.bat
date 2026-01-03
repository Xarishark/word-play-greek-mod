@echo off
setlocal

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python could not be found. Please install Python to run this script.
    pause
    exit /b 1
)

echo Running word processing script...
python process_words.py

if %ERRORLEVEL% equ 0 (
    echo Processing complete!
) else (
    echo An error occurred during processing.
    pause
    exit /b 1
)

pause
