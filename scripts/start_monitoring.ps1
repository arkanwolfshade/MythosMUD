#Requires -Version 5.1
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing startup script requires Write-Host for status messages')]

<#
.SYNOPSIS
    Starts the MythosMUD monitoring stack (Prometheus, Grafana, Alertmanager).

.DESCRIPTION
    This script checks if Docker Desktop is running, then starts the monitoring stack
    using docker-compose. It provides clear error messages and instructions if Docker
    is not available.

    RECOMMENDED: Start the MythosMUD server first (./scripts/start_server.ps1) before
    running this script, so metrics are immediately available when Prometheus starts
    scraping. However, you can start them in either order - they're independent.

.PARAMETER SkipDockerCheck
    Skip the Docker availability check (not recommended).

.EXAMPLE
    .\start_monitoring.ps1
    Starts the monitoring stack after verifying Docker is running.

.NOTES
    Author: MythosMUD Development Team
    Requires: Docker Desktop installed and running
    Recommended: MythosMUD server should be running (but not required)
#>

[CmdletBinding()]
param(
    [Parameter(HelpMessage = "Skip Docker availability check")]
    [switch]$SkipDockerCheck = $false
)

# Check Docker status
if (-not $SkipDockerCheck) {
    Write-Host "Checking Docker Desktop status..." -ForegroundColor Cyan

    try {
        docker version 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Docker command failed"
        }
        Write-Host "Docker Desktop is running" -ForegroundColor Green
    }
    catch {
        Write-Host ""
        Write-Host "ERROR: Docker Desktop is not running!" -ForegroundColor Red
        Write-Host ""
        Write-Host "To start Docker Desktop:" -ForegroundColor Yellow
        Write-Host "  1. Open Docker Desktop from the Start Menu" -ForegroundColor White
        Write-Host "  2. Wait for Docker Desktop to fully start" -ForegroundColor White
        Write-Host "     (Look for the whale icon in the system tray - it should be steady, not animating)" -ForegroundColor White
        Write-Host "  3. Verify Docker is running by typing: docker ps" -ForegroundColor White
        Write-Host "  4. Run this script again" -ForegroundColor White
        Write-Host ""
        Write-Host "If Docker Desktop is not installed:" -ForegroundColor Yellow
        Write-Host "  Download from: https://www.docker.com/products/docker-desktop/" -ForegroundColor White
        Write-Host ""
        exit 1
    }
}

# Navigate to monitoring directory
# Join-Path only accepts two arguments, so chain the calls
$monitoringDir = Join-Path (Join-Path $PSScriptRoot "..") "monitoring"
$monitoringDir = (Resolve-Path $monitoringDir -ErrorAction Stop).Path

try {
    Set-Location $monitoringDir

    Write-Host "Starting monitoring stack..." -ForegroundColor Cyan
    docker-compose -f docker-compose.monitoring.yml up -d

    if ($LASTEXITCODE -ne 0) {
        throw "docker-compose failed"
    }

    Write-Host "Services available at:" -ForegroundColor Cyan
    Write-Host "  Prometheus:    http://localhost:9090" -ForegroundColor White
    Write-Host "  Grafana:       http://localhost:3000 (admin/admin)" -ForegroundColor White
    Write-Host "  Alertmanager: http://localhost:9093" -ForegroundColor White
    Write-Host ""
    Write-Host "To view logs:" -ForegroundColor Cyan
    Write-Host "  docker-compose -f docker-compose.monitoring.yml logs -f" -ForegroundColor White
    Write-Host ""
    Write-Host "To stop the stack:" -ForegroundColor Cyan
    Write-Host "  docker-compose -f docker-compose.monitoring.yml down" -ForegroundColor White
    Write-Host "  Or run: .\scripts\stop_monitoring.ps1" -ForegroundColor White
    Write-Host ""

    # Wait a moment for services to initialize
    Write-Host "Waiting for services to initialize..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5

    # Check service health
    Write-Host "Checking service health..." -ForegroundColor Cyan
    $services = @(
        @{Name = "Prometheus"; Url = "http://localhost:9090/-/healthy" },
        @{Name = "Grafana"; Url = "http://localhost:3000/api/health" }
    )

    foreach ($service in $services) {
        try {
            $response = Invoke-WebRequest -Uri $service.Url -UseBasicParsing -TimeoutSec 5 -ErrorAction Stop
            if ($response.StatusCode -eq 200) {
                Write-Host "  $($service.Name) is healthy" -ForegroundColor Green
            }
        }
        catch {
            Write-Host "  $($service.Name) is starting (may take a moment)" -ForegroundColor Yellow
        }
    }

    Write-Host ""
}
catch {
    Write-Host ""
    Write-Host "ERROR: Failed to start monitoring stack" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  1. Ensure Docker Desktop is fully started" -ForegroundColor White
    Write-Host "  2. Check if ports 9090, 3000, 9093 are available" -ForegroundColor White
    Write-Host "  3. View logs: docker-compose -f docker-compose.monitoring.yml logs" -ForegroundColor White
    Write-Host ""
    exit 1
}
finally {
    # Return to original directory
    Set-Location $PSScriptRoot
}
