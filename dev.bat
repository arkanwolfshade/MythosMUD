@echo off
cd /d "%~dp0"
call "%~dp0scripts\clean_logs.bat"
powershell -ExecutionPolicy Bypass -File "%~dp0scripts\start_local.ps1" -Environment local
if errorlevel 1 (
    echo Error: Failed to start server
    pause
    exit /b 1
)
