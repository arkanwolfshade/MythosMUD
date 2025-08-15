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
$NatsServerPath = "E:\nats-server\nats-server.exe"
$NatsConfigPath = "E:\nats-server\nats-server.conf"
$NatsPort = 4222
$NatsHttpPort = 8222

# Function to check if NATS server is installed
function Test-NatsServerInstalled {
    [CmdletBinding()]
    param()

    if (Test-Path $NatsServerPath) {
        Write-Host "NATS server found at: $NatsServerPath" -ForegroundColor Green
        return $true
    } else {
        Write-Host "NATS server not found at: $NatsServerPath" -ForegroundColor Red
        Write-Host "Please install NATS server to E:\nats-server\" -ForegroundColor Yellow
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
        } else {
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

    try {
        if ($UseConfig -and (Test-Path $NatsConfigPath)) {
            Write-Host "Using configuration file: $NatsConfigPath" -ForegroundColor Gray
            $command = "& '$NatsServerPath' -c '$NatsConfigPath'"
        } else {
            Write-Host "Using default configuration" -ForegroundColor Gray
            $command = "& '$NatsServerPath' -p $NatsPort -m $NatsHttpPort"
        }

        if ($Background) {
            # Start NATS server in background
            Start-Process powershell -ArgumentList "-NoExit", "-Command", $command -WindowStyle Normal
            Write-Host "NATS server started in background" -ForegroundColor Green
        } else {
            # Start NATS server in foreground
            Invoke-Expression $command
        }

        # Wait for server to start
        Start-Sleep -Seconds 3

        # Verify server is running
        if (Test-NatsServerRunning) {
            Write-Host "NATS server started successfully" -ForegroundColor Green
            Write-Host "Client port: $NatsPort" -ForegroundColor Cyan
            Write-Host "HTTP port: $NatsHttpPort" -ForegroundColor Cyan
            return $true
        } else {
            Write-Host "NATS server failed to start" -ForegroundColor Red
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
        } else {
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

    Write-Host ""
    Write-Host "Installation: $(if ($installed) { 'Installed' } else { 'Not Installed' })" -ForegroundColor $(if ($installed) { 'Green' } else { 'Red' })
    Write-Host "Status: $(if ($running) { 'Running' } else { 'Stopped' })" -ForegroundColor $(if ($running) { 'Green' } else { 'Yellow' })
    Write-Host "Client Port ($NatsPort): $(if ($clientPort.TcpTestSucceeded) { 'Open' } else { 'Closed' })" -ForegroundColor $(if ($clientPort.TcpTestSucceeded) { 'Green' } else { 'Red' })
    Write-Host "HTTP Port ($NatsHttpPort): $(if ($httpPort.TcpTestSucceeded) { 'Open' } else { 'Closed' })" -ForegroundColor $(if ($httpPort.TcpTestSucceeded) { 'Green' } else { 'Red' })

    return @{
        Installed = $installed
        Running = $running
        ClientPortOpen = $clientPort.TcpTestSucceeded
        HttpPortOpen = $httpPort.TcpTestSucceeded
    }
}

# Functions are available when script is dot-sourced
# No need to export when used as a script rather than a module
