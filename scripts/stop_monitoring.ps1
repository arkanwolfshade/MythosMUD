#Requires -Version 5.1
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing script requires Write-Host for status messages')]

<#
.SYNOPSIS
    Stops the MythosMUD monitoring stack.

.DESCRIPTION
    This script stops all monitoring services (Prometheus, Grafana, Alertmanager)
    using docker-compose.

.EXAMPLE
    .\stop_monitoring.ps1
    Stops the monitoring stack.

.NOTES
    Author: MythosMUD Development Team
#>

[CmdletBinding()]

# Navigate to monitoring directory
# Join-Path only accepts two arguments, so chain the calls
$monitoringDir = Join-Path (Join-Path $PSScriptRoot "..") "monitoring"
$monitoringDir = (Resolve-Path $monitoringDir -ErrorAction Stop).Path

if (-not (Test-Path $monitoringDir)) {
    Write-Host "ERROR: Monitoring directory not found: $monitoringDir" -ForegroundColor Red
    exit 1
}

Set-Location $monitoringDir

Write-Host "Stopping MythosMUD monitoring stack..." -ForegroundColor Cyan

try {
    docker-compose -f docker-compose.monitoring.yml down

    if ($LASTEXITCODE -eq 0) {
        Write-Host "Monitoring stack stopped successfully" -ForegroundColor Green
    }
    else {
        Write-Host "Warning: Some services may not have stopped cleanly" -ForegroundColor Yellow
    }
}
catch {
    Write-Host "ERROR: Failed to stop monitoring stack" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}
finally {
    Set-Location $PSScriptRoot
}
