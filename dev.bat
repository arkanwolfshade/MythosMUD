@echo off
cd /d "%~dp0"
pushd logs
call clean.bat
popd
powershell -ExecutionPolicy Bypass -File "%~dp0scripts\start_local.ps1" -Environment local
if errorlevel 1 (
    echo Error: Failed to start server
    pause
    exit /b 1
)
