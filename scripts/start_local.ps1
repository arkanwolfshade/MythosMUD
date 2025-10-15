#!/usr/bin/env pwsh

# MythosMUD Development Startup Script
# Starts both the server and client for development

param(
    [string]$ServerPort = "54731",
    [string]$ClientPort = "5173",
    [switch]$ServerOnly,
    [switch]$ClientOnly,
    [switch]$Help
)

if ($Help) {
    Write-Host "MythosMUD Development Startup Script"
    Write-Host ""
    Write-Host "Usage: .\start_local.ps1 [-ServerPort <port>] [-ClientPort <port>] [-ServerOnly] [-ClientOnly] [-Help]"
    Write-Host ""
    Write-Host "Parameters:"
    Write-Host "    -ServerPort <port>    Port to run the server on (default: 54731)"
    Write-Host "    -ClientPort <port>    Port to run the client on (default: 5173)"
    Write-Host "    -ServerOnly           Start only the server"
    Write-Host "    -ClientOnly           Start only the client"
    Write-Host "    -Help                 Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "    .\start_local.ps1                           # Start both server and client"
    Write-Host "    .\start_local.ps1 -ServerOnly              # Start only the server"
    Write-Host "    .\start_local.ps1 -ClientOnly              # Start only the client"
    Write-Host "    .\start_local.ps1 -ServerPort 4001         # Start server on port 4001"
    Write-Host "    .\start_local.ps1 -ClientPort 3001         # Start client on port 3001"
    Write-Host "    .\start_local.ps1 -Help                    # Show help"
    exit 0
}

# Set error action preference
$ErrorActionPreference = "Stop"

Write-Host "MythosMUD Development Startup Script" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# Check if we're in the right directory
if (-not (Test-Path "server") -or -not (Test-Path "client")) {
    Write-Error "Server or client directory not found. Please run this script from the project root."
    exit 1
}

# Function to start server
function Start-Server {
    Write-Host "Starting MythosMUD server on port $ServerPort..." -ForegroundColor Yellow
    Write-Host "Server will be available at: http://localhost:$ServerPort" -ForegroundColor Cyan
    Write-Host "NATS server will be started automatically" -ForegroundColor Cyan
    Write-Host "Using local development configuration" -ForegroundColor Cyan
    Write-Host ""

    # Start server in background with local development configuration
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; .\scripts\start_server.ps1 -Port $ServerPort -Environment local" -WindowStyle Normal
}

# Function to start client
function Start-Client {
    Write-Host "Starting MythosMUD client on port $ClientPort..." -ForegroundColor Yellow
    Write-Host "Client will be available at: http://localhost:$ClientPort" -ForegroundColor Cyan
    Write-Host ""

    # Start client in background
    Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; .\scripts\start_client.ps1 -Port $ClientPort" -WindowStyle Normal
}

# Determine what to start
if ($ServerOnly) {
    Start-Server
}
elseif ($ClientOnly) {
    Start-Client
}
else {
    # Start both
    Write-Host "Starting MythosMUD development environment..." -ForegroundColor Green
    Write-Host ""

    Start-Server
    Start-Sleep -Seconds 2  # Give server a moment to start

    Start-Client

    Write-Host ""
    Write-Host "Development environment started!" -ForegroundColor Green
    Write-Host "Server: http://localhost:$ServerPort" -ForegroundColor Cyan
    Write-Host "Client: http://localhost:$ClientPort" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Press any key to exit this script (servers will continue running)..." -ForegroundColor Gray
}
