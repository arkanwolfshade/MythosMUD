#!/usr/bin/env pwsh

# MythosMUD E2E Test Environment Startup Script
# Starts both the backend server and Vite dev client with E2E test configuration

param(
    [switch]$Help
)

if ($Help) {
    Write-Host "MythosMUD E2E Test Environment Startup Script"
    Write-Host ""
    Write-Host "Usage: .\start_e2e_test.ps1 [-Help]"
    Write-Host ""
    Write-Host "This script starts BOTH the backend server AND the Vite dev client"
    Write-Host "with the E2E TEST configuration."
    Write-Host ""
    Write-Host "Backend Server: http://localhost:54731"
    Write-Host "Frontend Client: http://localhost:5173"
    Write-Host "Test database location: data/e2e_test/players/e2e_players.db"
    Write-Host ""
    Write-Host "After both services are running, execute E2E tests with:"
    Write-Host "  make test-server-e2e    # Server-side Playwright tests"
    Write-Host "  cd client && npm run test:e2e:runtime    # Client-side tests"
    Write-Host ""
    exit 0
}

Write-Host "MythosMUD E2E Test Server & Client Startup" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Using E2E TEST configuration and database" -ForegroundColor Yellow
Write-Host ""

# Check if we're in the right directory
if (-not (Test-Path "server") -or -not (Test-Path "client")) {
    Write-Error "Server or client directory not found. Please run this script from the project root."
    exit 1
}

# Check if npm is installed
if (-not (Get-Command npm -ErrorAction SilentlyContinue)) {
    Write-Error "npm is not installed or not in PATH. Please install Node.js and npm."
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
Write-Host "Starting backend server in E2E test mode..." -ForegroundColor Green

# Set configuration path for E2E testing
$configPath = Join-Path $PWD "server\server_config.e2e_test.yaml"
$env:MYTHOSMUD_CONFIG_PATH = $configPath

Write-Host "Config file: $configPath" -ForegroundColor Gray
Write-Host "Test database: data/e2e_test/players/e2e_players.db" -ForegroundColor Gray
Write-Host ""

# Start server using the existing start_server.ps1 script
# Pass explicit parameters to ensure it uses E2E test settings
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; `$env:MYTHOSMUD_CONFIG_PATH='$configPath'; .\scripts\start_server.ps1 -Port 54731 -Environment e2e_test" -WindowStyle Normal

Write-Host ""
Write-Host "E2E Test Server starting in new window..." -ForegroundColor Green
Write-Host "Server will be available at: http://localhost:54731" -ForegroundColor Cyan
Write-Host ""

# Wait a moment for server to start initializing
Start-Sleep -Seconds 3

Write-Host "Starting Vite dev server (client) in E2E test mode..." -ForegroundColor Green
Write-Host "Client will be available at: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""

# Start Vite dev server in a new window
$clientPath = Join-Path $PWD "client"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$clientPath'; `$env:VITE_API_URL='http://localhost:54731'; npm run dev" -WindowStyle Normal

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "E2E Test Environment Starting..." -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host "Backend Server: http://localhost:54731" -ForegroundColor Cyan
Write-Host "Frontend Client: http://localhost:5173" -ForegroundColor Cyan
Write-Host ""
Write-Host "Wait for both windows to show 'ready' messages, then run:" -ForegroundColor Yellow
Write-Host "  make test-server-e2e    # Server-side Playwright tests" -ForegroundColor Gray
Write-Host "  OR" -ForegroundColor Gray
Write-Host "  cd client && npm run test:e2e:runtime    # Client-side tests" -ForegroundColor Gray
Write-Host ""
