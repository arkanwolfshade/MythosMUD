#Requires -Version 5.1

<#
.SYNOPSIS
    Starts the complete MythosMUD development environment.

.DESCRIPTION
    This script starts both the FastAPI server and React client for development:
    - Starts the FastAPI server using start_server.ps1
    - Starts the React development server
    - Provides URLs for all development services

.EXAMPLE
    .\start_dev.ps1
    Starts both the FastAPI server and React client for development.

.NOTES
    Author: MythosMUD Development Team
    Version: 2.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding()]
param()

try {
    Write-Host "Starting MythosMUD Development Environment..." -ForegroundColor Green

    # Start the FastAPI server using the startup script
    Write-Host "Starting FastAPI server on http://127.0.0.1:8000..." -ForegroundColor Yellow
    & ".\start_server.ps1" -ServerHost "127.0.0.1" -Port 8000 -Reload

    # Wait a moment for server to start
    Start-Sleep -Seconds 3

    # Start the React client in background
    Write-Host "Starting React client on http://localhost:5173..." -ForegroundColor Yellow
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd client; npm run dev"

    # Wait a moment for client to start
    Start-Sleep -Seconds 5

    Write-Host "Development servers should now be running:" -ForegroundColor Green
    Write-Host "  - FastAPI Server: http://127.0.0.1:8000" -ForegroundColor Cyan
    Write-Host "  - React Client: http://localhost:5173" -ForegroundColor Cyan
    Write-Host "  - API Documentation: http://127.0.0.1:8000/docs" -ForegroundColor Cyan

    Write-Host "Press any key to exit..." -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

}
catch {
    Write-Host "Error starting development environment: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
