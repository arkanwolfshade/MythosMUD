@echo off
cd /d "%~dp0"
pushd logs
call clean.bat
popd
pwsh -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\bootstrap_e2e_database.ps1"
if errorlevel 1 (
    echo Error: E2E database bootstrap failed
    pause
    exit /b 1
)
pwsh -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\start_e2e_test.ps1" -Environment local
if errorlevel 1 (
    echo Error: Failed to start server
    pause
    exit /b 1
)
