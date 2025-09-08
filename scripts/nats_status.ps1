#!/usr/bin/env pwsh

#Requires -Version 5.1

<#
.SYNOPSIS
    NATS Server Status Check for MythosMUD

.DESCRIPTION
    This script checks the status of the NATS server for MythosMUD,
    including installation status, running status, and port availability.

.EXAMPLE
    .\nats_status.ps1
    Shows the current status of the NATS server.

.NOTES
    Author: MythosMUD Development Team
    Version: 1.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding()]
param(
    [Parameter(HelpMessage = "Show detailed information")]
    [switch]$Detailed,

    [Parameter(HelpMessage = "Show help information")]
    [switch]$Help
)

if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Full
    exit 0
}

Write-Host "MythosMUD NATS Server Status" -ForegroundColor Cyan
Write-Host "============================" -ForegroundColor Cyan
Write-Host ""

# Import NATS management functions
$natsManagerPath = Join-Path $PSScriptRoot "nats_manager.ps1"
if (Test-Path $natsManagerPath) {
    . $natsManagerPath

    # Get NATS server status
    $status = Get-NatsServerStatus

    Write-Host ""

    if ($Detailed) {
        Write-Host "Detailed Information:" -ForegroundColor Yellow
        Write-Host "====================" -ForegroundColor Yellow
        Write-Host ""

        # Check NATS server executable
        $natsExePath = $null
        $possiblePaths = @(
            "C:\Users\$env:USERNAME\AppData\Local\Microsoft\WinGet\Packages\NATSAuthors.NATSServer_Microsoft.Winget.Source_8wekyb3d8bbwe\nats-server-v2.10.25-windows-amd64\nats-server.exe",
            "C:\nats-server\nats-server.exe",
            "E:\nats-server\nats-server.exe",
            "nats-server"
        )

        foreach ($path in $possiblePaths) {
            if ($path -eq "nats-server") {
                try {
                    $null = Get-Command $path -ErrorAction Stop
                    $natsExePath = $path
                    break
                } catch {
                    continue
                }
            } elseif (Test-Path $path) {
                $natsExePath = $path
                break
            }
        }

        if ($natsExePath) {
            try {
                $version = & $natsExePath --version 2>$null
                Write-Host "NATS Server Version: $version" -ForegroundColor Green
                Write-Host "NATS Server Path: $natsExePath" -ForegroundColor Green
            } catch {
                Write-Host "NATS Server Version: Found but version check failed" -ForegroundColor Yellow
            }
        } else {
            Write-Host "NATS Server Version: Not installed" -ForegroundColor Red
        }

        # Check configuration file
        if ($natsExePath -and $natsExePath -ne "nats-server") {
            $natsConfigPath = Join-Path (Split-Path $natsExePath -Parent) "nats-server.conf"
        } else {
            $natsConfigPath = "nats-server.conf"
        }

        if (Test-Path $natsConfigPath) {
            Write-Host "Configuration File: $natsConfigPath" -ForegroundColor Green
        } else {
            Write-Host "Configuration File: Not found (using defaults)" -ForegroundColor Yellow
        }

        Write-Host ""
        Write-Host "Port Information:" -ForegroundColor Yellow
        Write-Host "=================" -ForegroundColor Yellow

        # Test NATS client port
        $clientPort = 4222
        $clientTest = Test-NetConnection -ComputerName localhost -Port $clientPort -WarningAction SilentlyContinue
        Write-Host "Client Port ($clientPort): $(if ($clientTest.TcpTestSucceeded) { 'Open' } else { 'Closed' })" -ForegroundColor $(if ($clientTest.TcpTestSucceeded) { 'Green' } else { 'Red' })

        # Test NATS HTTP port
        $httpPort = 8222
        $httpTest = Test-NetConnection -ComputerName localhost -Port $httpPort -WarningAction SilentlyContinue
        Write-Host "HTTP Port ($httpPort): $(if ($httpTest.TcpTestSucceeded) { 'Open' } else { 'Closed' })" -ForegroundColor $(if ($httpTest.TcpTestSucceeded) { 'Green' } else { 'Red' })

        Write-Host ""
        Write-Host "Process Information:" -ForegroundColor Yellow
        Write-Host "====================" -ForegroundColor Yellow

        # Check for NATS processes
        $natsProcesses = Get-Process | Where-Object {
            $_.ProcessName -like "*nats*" -or
            $_.ProcessName -like "*nats-server*"
        }

        if ($natsProcesses) {
            foreach ($process in $natsProcesses) {
                Write-Host "Process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Green
            }
        } else {
            Write-Host "No NATS processes found" -ForegroundColor Yellow
        }
    }

    Write-Host ""
    Write-Host "Summary:" -ForegroundColor Yellow
    Write-Host "========" -ForegroundColor Yellow

    if ($status.Installed -and $status.Running -and $status.ClientPortOpen) {
        Write-Host "✅ NATS server is ready for MythosMUD" -ForegroundColor Green
    } elseif ($status.Installed -and $status.Running) {
        Write-Host "⚠️  NATS server is running but ports may be blocked" -ForegroundColor Yellow
    } elseif ($status.Installed) {
        Write-Host "⚠️  NATS server is installed but not running" -ForegroundColor Yellow
    } else {
        Write-Host "❌ NATS server is not installed" -ForegroundColor Red
    }

} else {
    Write-Host "NATS management functions not found at: $natsManagerPath" -ForegroundColor Red
    Write-Host "Please ensure the nats_manager.ps1 file exists in the scripts directory." -ForegroundColor Yellow
}
