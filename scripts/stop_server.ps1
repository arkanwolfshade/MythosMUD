#Requires -Version 5.1

<#
.SYNOPSIS
    Stops MythosMUD server processes using multiple detection methods.

.DESCRIPTION
    This script provides robust server shutdown functionality for MythosMUD by:
    - Terminating processes using port 54731
    - Killing processes by name patterns (uvicorn, python)
    - Terminating processes by command line patterns
    - Force killing all Python processes if Force flag is set
    - Verifying port is free after shutdown

.PARAMETER Force
    When specified, forces termination of all Python processes regardless of command line.

.PARAMETER Verbose
    When specified, provides detailed output including remaining connections. This parameter is automatically available due to CmdletBinding.

.EXAMPLE
    .\stop_server.ps1
    Stops MythosMUD server processes gracefully.

.EXAMPLE
    .\stop_server.ps1 -Force -Verbose
    Force stops all Python processes and provides detailed output.

.NOTES
    Author: MythosMUD Development Team
    Version: 2.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding()]
param(
    [Parameter(HelpMessage = "Force termination of all Python processes")]
    [switch]$Force
)

# Function to kill processes by port
function Stop-ProcessesByPort {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 65535)]
        [int]$Port
    )

    Write-Host "Checking for processes using port ${Port}..." -ForegroundColor Cyan

    try {
        $connections = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
        if ($connections) {
            foreach ($connection in $connections) {
                try {
                    $process = Get-Process -Id $connection.OwningProcess -ErrorAction SilentlyContinue
                    if ($process) {
                        Write-Host "Found process using port ${Port}: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                        Stop-Process -Id $process.Id -Force
                        Write-Host "Terminated process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Green
                    }
                }
                catch {
                    Write-Host "Could not terminate process on port ${Port}: $($_.Exception.Message)" -ForegroundColor Yellow
                }
            }
        }
        else {
            Write-Host "No processes found using port ${Port}" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "Error checking port ${Port}: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Function to kill processes by name pattern
function Stop-ProcessesByName {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$NamePattern
    )

    Write-Host "Checking for processes matching '$NamePattern'..." -ForegroundColor Cyan

    try {
        $processes = Get-Process | Where-Object { $_.ProcessName -like $NamePattern }
        if ($processes) {
            foreach ($process in $processes) {
                Write-Host "Found process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                try {
                    Stop-Process -Id $process.Id -Force
                    Write-Host "Terminated process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Green
                }
                catch {
                    Write-Host "Could not terminate process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Yellow
                }
            }
        }
        else {
            Write-Host "No processes found matching '$NamePattern'" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "Error checking processes matching '$NamePattern': $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Function to kill processes by command line pattern
function Stop-ProcessesByCommandLine {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$CommandPattern
    )

    Write-Host "Checking for processes with command line containing '$CommandPattern'..." -ForegroundColor Cyan

    try {
        $pythonProcesses = Get-Process | Where-Object { $_.ProcessName -like "*python*" }
        foreach ($process in $pythonProcesses) {
            try {
                $commandLine = (Get-WmiObject -Class Win32_Process -Filter "ProcessId = $($process.Id)").CommandLine
                if ($commandLine -and $commandLine -like "*$CommandPattern*") {
                    Write-Host "Found process with command line '$CommandPattern': $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Stop-Process -Id $process.Id -Force
                    Write-Host "Terminated process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Green
                }
            }
            catch {
                # Ignore errors when getting command line
                Write-Verbose "Could not get command line for process $($process.Id)"
            }
        }
    }
    catch {
        Write-Host "Error checking command line patterns: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Function to wait and verify port is free
function Wait-ForPortFree {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 65535)]
        [int]$Port,

        [Parameter()]
        [ValidateRange(1, 60)]
        [int]$MaxWaitSeconds = 10
    )

    Write-Host "Waiting for port ${Port} to be free..." -ForegroundColor Yellow

    $waitTime = 0
    while ($waitTime -lt $MaxWaitSeconds) {
        $connections = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
        if (-not $connections) {
            Write-Host "Port ${Port} is now free!" -ForegroundColor Green
            return $true
        }
        Start-Sleep -Seconds 1
        $waitTime++
        Write-Host "Still waiting... ($waitTime/$MaxWaitSeconds seconds)" -ForegroundColor Yellow
    }

    Write-Host "Port ${Port} is still in use after ${MaxWaitSeconds} seconds" -ForegroundColor Red
    return $false
}

# Main execution
try {
    Write-Host "Starting robust server shutdown process..." -ForegroundColor Green

    # Method 1: Kill processes by port
    Stop-ProcessesByPort -Port 54731

    # Method 2: Kill processes by name patterns
    Stop-ProcessesByName -NamePattern "*uvicorn*"
    Stop-ProcessesByName -NamePattern "*python*"

    # Method 3: Kill processes by command line patterns
    Stop-ProcessesByCommandLine -CommandPattern "uvicorn"
    Stop-ProcessesByCommandLine -CommandPattern "main:app"

    # Method 4: Force kill all Python processes if Force flag is set
    if ($Force) {
        Write-Host "Force mode: Terminating all Python processes..." -ForegroundColor Red
        $pythonProcesses = Get-Process | Where-Object { $_.ProcessName -like "*python*" }
        foreach ($process in $pythonProcesses) {
            Write-Host "Force terminating: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
            try {
                Stop-Process -Id $process.Id -Force
                Write-Host "Force terminated: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Green
            }
            catch {
                Write-Host "Could not force terminate: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Yellow
            }
        }
    }

    # Wait for processes to fully terminate
    Write-Host "Waiting for processes to fully terminate..." -ForegroundColor Yellow
    Start-Sleep -Seconds 3

    # Verify port is free
    $portFree = Wait-ForPortFree -Port 54731 -MaxWaitSeconds 10

    if ($portFree) {
        Write-Host "`n🎉 MythosMUD Server shutdown complete!" -ForegroundColor Green
    }
    else {
        Write-Host "`n⚠️  Server shutdown may be incomplete. Port 54731 is still in use." -ForegroundColor Yellow
        if ($Verbose) {
            Write-Host "Remaining connections on port 54731:" -ForegroundColor Yellow
            Get-NetTCPConnection -LocalPort 54731 -ErrorAction SilentlyContinue | ForEach-Object {
                Write-Host "  $($_.LocalAddress):$($_.LocalPort) -> $($_.RemoteAddress):$($_.RemotePort) (PID: $($_.OwningProcess))" -ForegroundColor Gray
            }
        }
    }

}
catch {
    Write-Host "Error during shutdown: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
