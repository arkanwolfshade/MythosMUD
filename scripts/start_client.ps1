#!/usr/bin/env pwsh

# MythosMUD Client Startup Script
# Starts the React development server for the MythosMUD client

param(
    [string]$Port = "3000",
    [switch]$Help
)

if ($Help) {
    Write-Host "MythosMUD Client Startup Script"
    Write-Host ""
    Write-Host "Usage: .\start_client.ps1 [-Port <port>] [-Help]"
    Write-Host ""
    Write-Host "Parameters:"
    Write-Host "    -Port <port>    Port to run the client on (default: 3000)"
    Write-Host "    -Help           Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "    .\start_client.ps1                    # Start on default port 3000"
    Write-Host "    .\start_client.ps1 -Port 3001        # Start on port 3001"
    Write-Host "    .\start_client.ps1 -Help             # Show help"
    exit 0
}

Write-Host "MythosMUD Client Startup Script" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan

# Check if we're in the right directory
if (-not (Test-Path "client")) {
    Write-Error "Client directory not found. Please run this script from the project root."
    exit 1
}

# Check if Node.js is available
try {
    $nodeVersion = node --version
    Write-Host "Node.js version: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Error "Node.js not found. Please install Node.js and try again."
    exit 1
}

# Check if npm is available
try {
    $npmVersion = npm --version
    Write-Host "npm version: $npmVersion" -ForegroundColor Green
} catch {
    Write-Error "npm not found. Please install npm and try again."
    exit 1
}

# Navigate to client directory
Push-Location "client"

try {
    # Check if node_modules exists
    if (-not (Test-Path "node_modules")) {
        Write-Host "Installing client dependencies..." -ForegroundColor Yellow
        npm install
        if ($LASTEXITCODE -ne 0) {
            Write-Error "Failed to install client dependencies."
            exit 1
        }
        Write-Host "Client dependencies installed successfully." -ForegroundColor Green
    }

    # Set the port environment variable
    $env:PORT = $Port

    Write-Host "Starting MythosMUD client on port $Port..." -ForegroundColor Yellow
    Write-Host "Client will be available at: http://localhost:$Port" -ForegroundColor Cyan
    Write-Host "Make sure the server is running on port 4000" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Press Ctrl+C to stop the client" -ForegroundColor Gray
    Write-Host ""

    # Start the development server
    npm run dev

} catch {
    Write-Error "Failed to start client: $($_.Exception.Message)"
    exit 1
} finally {
    # Return to original directory
    Pop-Location
}
