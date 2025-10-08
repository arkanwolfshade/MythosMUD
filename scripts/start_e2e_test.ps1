#!/usr/bin/env pwsh

# MythosMUD E2E Test Server Startup Script
# Starts the server with test database configuration for E2E testing

param(
    [switch]$Help
)

if ($Help) {
    Write-Host "MythosMUD E2E Test Server Startup Script"
    Write-Host ""
    Write-Host "Usage: .\start_e2e_test.ps1 [-Help]"
    Write-Host ""
    Write-Host "This script starts ONLY the backend server with the E2E TEST configuration."
    Write-Host "Playwright will auto-start the Vite dev server (client) during tests."
    Write-Host "Test database location: data/e2e_test/players/e2e_unit_test_players.db"db"
    Write-Host ""
    exit 0
}

Write-Host "MythosMUD E2E Test Server Startup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Using E2E TEST configuration and database" -ForegroundColor Yellow
Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "server") -or -not (Test-Path "client")) {
    Write-Error "Server or client directory not found. Please run this script from the project root."
    exit 1
}

# Load E2E test secrets if .env.e2e_test exists
$envFile = ".env.e2e_test"
if (Test-Path $envFile) {
    Write-Host "Loading E2E test secrets from $envFile" -ForegroundColor Cyan
    Get-Content $envFile | ForEach-Object {
        if ($_ -match "^([^#][^=]+)=(.*)$") {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()
            [Environment]::SetEnvironmentVariable($name, $value, "Process")
        }
    }
}
else {
    Write-Host "Warning: $envFile not found - using defaults from conftest.py" -ForegroundColor Yellow
    Write-Host "Create it from env.e2e_test.example for custom secrets" -ForegroundColor Gray
}

# Stop any running servers first
Write-Host "Stopping any existing servers..." -ForegroundColor Yellow
& .\scripts\stop_server.ps1

Write-Host ""
Write-Host "Starting server in E2E test mode..." -ForegroundColor Green

# Set configuration path for E2E testing
$configPath = Join-Path $PWD "server\server_config.e2e_test.yaml"
$env:MYTHOSMUD_CONFIG_PATH = $configPath

Write-Host "Config file: $configPath" -ForegroundColor Gray
Write-Host "Test database: data/e2e_test/players/e2e_unit_test_players.db" -ForegroundColor Gray
Write-Host ""

# Start server using the existing start_server.ps1 script
# Pass explicit parameters to ensure it uses E2E test settings
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; `$env:MYTHOSMUD_CONFIG_PATH='$configPath'; .\scripts\start_server.ps1 -Port 54731 -Environment e2e_test" -WindowStyle Normal

Write-Host ""
Write-Host "E2E Test Server starting in new window..." -ForegroundColor Green
Write-Host "Server will be available at: http://localhost:54731" -ForegroundColor Cyan
Write-Host "Once server shows 'Application startup complete', run E2E tests with:" -ForegroundColor Yellow
Write-Host "  cd client" -ForegroundColor Gray
Write-Host "  npm run test:e2e:runtime" -ForegroundColor Gray
Write-Host ""
