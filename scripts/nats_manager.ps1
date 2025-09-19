#Requires -Version 5.1

<#
.SYNOPSIS
    NATS Server Management for MythosMUD

.DESCRIPTION
    This module provides functions to manage the NATS server for MythosMUD,
    including starting, stopping, and monitoring the NATS server process.

.NOTES
    Author: MythosMUD Development Team
    Version: 1.0
    Requires: PowerShell 5.1 or higher
#>

# NATS Server Configuration
# Try to find NATS server in common locations
$NatsServerPath = $null
$PossiblePaths = @(
    "C:\Users\$env:USERNAME\AppData\Local\Microsoft\WinGet\Packages\NATSAuthors.NATSServer_Microsoft.Winget.Source_8wekyb3d8bbwe\nats-server-v2.10.25-windows-amd64\nats-server.exe",
    "C:\nats-server\nats-server.exe",
    "E:\nats-server\nats-server.exe",
    "nats-server"  # If it's in PATH
)

foreach ($path in $PossiblePaths) {
    if ($path -eq "nats-server") {
        # Check if it's in PATH
        try {
            $null = Get-Command $path -ErrorAction Stop
            $NatsServerPath = $path
            break
        }
        catch {
            continue
        }
    }
    elseif (Test-Path $path) {
        $NatsServerPath = $path
        break
    }
}

# If not found, use the first path as default
if (-not $NatsServerPath) {
    $NatsServerPath = $PossiblePaths[0]
}

# Configuration paths (relative to NATS server directory)
$NatsServerDir = Split-Path $NatsServerPath -Parent
$NatsConfigPath = Join-Path $NatsServerDir "nats-server.conf"
$NatsPort = 4222
$NatsHttpPort = 8222
$NatsLogPath = Join-Path $PSScriptRoot "..\logs\development\nats\nats-server.log"

# Function to ensure NATS log directory exists
function Ensure-NatsLogDirectory {
    [CmdletBinding()]
    param()

    $natsLogDir = Split-Path $NatsLogPath -Parent
    if (-not (Test-Path $natsLogDir)) {
        Write-Host "Creating NATS log directory: $natsLogDir" -ForegroundColor Gray
        New-Item -ItemType Directory -Path $natsLogDir -Force | Out-Null
        return $true
    }
    return $false
}

# Function to check if NATS server is installed
function Test-NatsServerInstalled {
    [CmdletBinding()]
    param()

    # Re-detect NATS server path
    $detectedPath = $null
    foreach ($path in $PossiblePaths) {
        if ($path -eq "nats-server") {
            # Check if it's in PATH
            try {
                $null = Get-Command $path -ErrorAction Stop
                $detectedPath = $path
                break
            }
            catch {
                continue
            }
        }
        elseif (Test-Path $path) {
            $detectedPath = $path
            break
        }
    }

    if ($detectedPath) {
        Write-Host "NATS server found at: $detectedPath" -ForegroundColor Green
        return $true
    }
    else {
        Write-Host "NATS server not found in any of the expected locations:" -ForegroundColor Red
        foreach ($path in $PossiblePaths) {
            Write-Host "  - $path" -ForegroundColor Yellow
        }
        Write-Host "Please install NATS server using: winget install NATSAuthors.NATSServer" -ForegroundColor Yellow
        return $false
    }
}

# Function to check if NATS server is running
function Test-NatsServerRunning {
    [CmdletBinding()]
    param()

    try {
        # Check if NATS port is in use
        $connection = Get-NetTCPConnection -LocalPort $NatsPort -ErrorAction SilentlyContinue
        if ($connection) {
            Write-Host "NATS server is running on port $NatsPort" -ForegroundColor Green
            return $true
        }
        else {
            Write-Host "NATS server is not running on port $NatsPort" -ForegroundColor Yellow
            return $false
        }
    }
    catch {
        Write-Host "Error checking NATS server status: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to start NATS server
function Start-NatsServer {
    [CmdletBinding()]
    param(
        [Parameter(HelpMessage = "Use configuration file")]
        [switch]$UseConfig = $true,

        [Parameter(HelpMessage = "Start in background")]
        [switch]$Background = $true
    )

    if (-not (Test-NatsServerInstalled)) {
        return $false
    }

    if (Test-NatsServerRunning) {
        Write-Host "NATS server is already running" -ForegroundColor Yellow
        return $true
    }

    Write-Host "Starting NATS server..." -ForegroundColor Cyan

    # Ensure NATS log directory exists
    Ensure-NatsLogDirectory | Out-Null

    try {
        # Get the actual NATS server path
        $actualNatsPath = $null
        foreach ($path in $PossiblePaths) {
            if ($path -eq "nats-server") {
                try {
                    $null = Get-Command $path -ErrorAction Stop
                    $actualNatsPath = $path
                    break
                }
                catch {
                    continue
                }
            }
            elseif (Test-Path $path) {
                $actualNatsPath = $path
                break
            }
        }

        if (-not $actualNatsPath) {
            Write-Host "NATS server executable not found" -ForegroundColor Red
            return $false
        }

        if ($UseConfig -and (Test-Path $NatsConfigPath)) {
            Write-Host "Using configuration file: $NatsConfigPath" -ForegroundColor Gray
            $command = "& '$actualNatsPath' -c '$NatsConfigPath' -l '$NatsLogPath'"
        }
        else {
            Write-Host "Using default configuration" -ForegroundColor Gray
            $command = "& '$actualNatsPath' -p $NatsPort -m $NatsHttpPort -l '$NatsLogPath'"
        }

        if ($Background) {
            # Start NATS server in background
            Start-Process powershell -ArgumentList "-NoExit", "-Command", $command -WindowStyle Normal
            Write-Host "NATS server started in background" -ForegroundColor Green
        }
        else {
            # Start NATS server in foreground
            Invoke-Expression $command
        }

        # Wait for server to start (longer wait for background processes)
        if ($Background) {
            Start-Sleep -Seconds 5
        }
        else {
            Start-Sleep -Seconds 3
        }

        # Verify server is running
        if (Test-NatsServerRunning) {
            Write-Host "NATS server started successfully" -ForegroundColor Green
            Write-Host "Client port: $NatsPort" -ForegroundColor Cyan
            Write-Host "HTTP port: $NatsHttpPort" -ForegroundColor Cyan
            return $true
        }
        else {
            Write-Host "NATS server may still be starting up. Check status with: .\scripts\nats_status.ps1" -ForegroundColor Yellow
            return $false
        }
    }
    catch {
        Write-Host "Error starting NATS server: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to stop NATS server
function Stop-NatsServer {
    [CmdletBinding()]
    param()

    Write-Host "Stopping NATS server..." -ForegroundColor Cyan

    try {
        # Find NATS server processes
        $natsProcesses = Get-Process | Where-Object {
            $_.ProcessName -like "*nats*" -or
            $_.ProcessName -like "*nats-server*"
        }

        if ($natsProcesses) {
            foreach ($process in $natsProcesses) {
                Write-Host "Stopping NATS process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Yellow
                Stop-Process -Id $process.Id -Force
            }
        }

        # Also check for processes using NATS ports
        $portProcesses = Get-NetTCPConnection -LocalPort $NatsPort -ErrorAction SilentlyContinue
        if ($portProcesses) {
            foreach ($connection in $portProcesses) {
                try {
                    $process = Get-Process -Id $connection.OwningProcess -ErrorAction SilentlyContinue
                    if ($process) {
                        Write-Host "Stopping process using NATS port: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Yellow
                        Stop-Process -Id $process.Id -Force
                    }
                }
                catch {
                    Write-Verbose "Could not stop process on NATS port"
                }
            }
        }

        # Wait for processes to terminate
        Start-Sleep -Seconds 2

        # Verify server is stopped
        if (-not (Test-NatsServerRunning)) {
            Write-Host "NATS server stopped successfully" -ForegroundColor Green
            return $true
        }
        else {
            Write-Host "NATS server may still be running" -ForegroundColor Yellow
            return $false
        }
    }
    catch {
        Write-Host "Error stopping NATS server: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Function to restart NATS server
function Restart-NatsServer {
    [CmdletBinding()]
    param(
        [Parameter(HelpMessage = "Use configuration file")]
        [switch]$UseConfig = $true,

        [Parameter(HelpMessage = "Start in background")]
        [switch]$Background = $true
    )

    Write-Host "Restarting NATS server..." -ForegroundColor Cyan

    # Stop server
    Stop-NatsServer

    # Wait a moment
    Start-Sleep -Seconds 2

    # Start server
    return Start-NatsServer -UseConfig:$UseConfig -Background:$Background
}

# Function to get NATS server status
function Get-NatsServerStatus {
    [CmdletBinding()]
    param()

    Write-Host "NATS Server Status" -ForegroundColor Cyan
    Write-Host "==================" -ForegroundColor Cyan

    # Check installation
    $installed = Test-NatsServerInstalled

    # Check if running
    $running = Test-NatsServerRunning

    # Check ports
    $clientPort = Test-NetConnection -ComputerName localhost -Port $NatsPort -WarningAction SilentlyContinue
    $httpPort = Test-NetConnection -ComputerName localhost -Port $NatsHttpPort -WarningAction SilentlyContinue

    # Ensure log directory exists and check log file
    Ensure-NatsLogDirectory | Out-Null
    $logExists = Test-Path $NatsLogPath

    Write-Host ""
    Write-Host "Installation: $(if ($installed) { 'Installed' } else { 'Not Installed' })" -ForegroundColor $(if ($installed) { 'Green' } else { 'Red' })
    Write-Host "Status: $(if ($running) { 'Running' } else { 'Stopped' })" -ForegroundColor $(if ($running) { 'Green' } else { 'Yellow' })
    Write-Host "Client Port ($NatsPort): $(if ($clientPort.TcpTestSucceeded) { 'Open' } else { 'Closed' })" -ForegroundColor $(if ($clientPort.TcpTestSucceeded) { 'Green' } else { 'Red' })
    Write-Host "HTTP Port ($NatsHttpPort): $(if ($httpPort.TcpTestSucceeded) { 'Open' } else { 'Closed' })" -ForegroundColor $(if ($httpPort.TcpTestSucceeded) { 'Green' } else { 'Red' })
    Write-Host "Log File: $(if ($logExists) { 'Exists' } else { 'Missing' }) at $NatsLogPath" -ForegroundColor $(if ($logExists) { 'Green' } else { 'Yellow' })

    return @{
        Installed      = $installed
        Running        = $running
        ClientPortOpen = $clientPort.TcpTestSucceeded
        HttpPortOpen   = $httpPort.TcpTestSucceeded
        LogFileExists  = $logExists
    }
}

# Functions are available when script is dot-sourced
# No need to export when used as a script rather than a module
