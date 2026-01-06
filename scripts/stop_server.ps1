#Requires -Version 5.1
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing script requires Write-Host for status messages')]

<#
.SYNOPSIS
    Stops MythosMUD server processes using multiple detection methods.

.DESCRIPTION
    This script provides robust server shutdown functionality for MythosMUD by:
    - Terminating processes using port 54731
    - Killing processes by name patterns (uvicorn only)
    - Terminating processes by command line patterns (MythosMUD-specific)
    - Force killing MythosMUD-related Python processes if Force flag is set
    - Verifying port is free after shutdown
    - Terminating PowerShell processes that spawned the server
    - Cleaning up orphaned terminal windows

    SECURITY NOTE: This script is designed to preserve non-MythosMUD Python processes
    (such as Playwright MCP servers) by using command line pattern matching instead
    of broad process name termination.

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
    Version: 3.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding()]
param(
    [Parameter(HelpMessage = "Force termination of all Python processes")]
    [switch]$Force
)

# Function to kill entire process trees
function Stop-ProcessTree {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [int]$ProcessId
    )

    if (-not $PSCmdlet.ShouldProcess("process tree for PID $ProcessId", "Stop")) {
        return
    }

    try {
        # Get child processes
        $children = Get-CimInstance -ClassName Win32_Process | Where-Object { $_.ParentProcessId -eq $ProcessId }

        # Kill children first
        foreach ($child in $children) {
            Stop-ProcessTree -ProcessId $child.ProcessId
        }

        # Kill the parent
        Stop-Process -Id $ProcessId -Force
        Write-Host "Terminated process tree for PID: $ProcessId" -ForegroundColor Green
    }
    catch {
        Write-Host "Could not terminate process tree for PID: $ProcessId" -ForegroundColor Yellow
    }
}

# Function to kill processes by port
function Stop-ProcessesByPort {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 65535)]
        [int]$Port
    )

    if (-not $PSCmdlet.ShouldProcess("processes using port $Port", "Stop")) {
        return
    }

    Write-Host "Checking for processes using port ${Port}..." -ForegroundColor Cyan

    try {
        $connections = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
        if ($connections) {
            foreach ($connection in $connections) {
                try {
                    $process = Get-Process -Id $connection.OwningProcess -ErrorAction SilentlyContinue
                    if ($process) {
                        Write-Host "Found process using port ${Port}: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                        Stop-ProcessTree -ProcessId $process.Id
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

# Function to stop NATS server
function Stop-NatsServerForMythosMUD {
    [CmdletBinding(SupportsShouldProcess)]
    param()

    if (-not $PSCmdlet.ShouldProcess("NATS server", "Stop")) {
        return
    }

    Write-Host "Stopping NATS server..." -ForegroundColor Cyan

    # Import NATS management functions
    $natsManagerPath = Join-Path $PSScriptRoot "nats_manager.ps1"
    if (Test-Path $natsManagerPath) {
        . $natsManagerPath
        Stop-NatsServer
    }
    else {
        Write-Host "Warning: NATS manager not found, stopping NATS processes manually..." -ForegroundColor Yellow
        # Manual NATS process cleanup
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
    }
}

# Function to kill processes by name pattern
function Stop-ProcessesByName {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$NamePattern
    )

    if (-not $PSCmdlet.ShouldProcess("processes matching '$NamePattern'", "Stop")) {
        return
    }

    Write-Host "Checking for processes matching '$NamePattern'..." -ForegroundColor Cyan

    try {
        $processes = Get-Process | Where-Object { $_.ProcessName -like $NamePattern }
        if ($processes) {
            foreach ($process in $processes) {
                Write-Host "Found process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                try {
                    Stop-ProcessTree -ProcessId $process.Id
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
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$CommandPattern
    )

    if (-not $PSCmdlet.ShouldProcess("processes with command line containing '$CommandPattern'", "Stop")) {
        return
    }

    Write-Host "Checking for processes with command line containing '$CommandPattern'..." -ForegroundColor Cyan

    try {
        $pythonProcesses = Get-Process | Where-Object { $_.ProcessName -like "*python*" }
        foreach ($process in $pythonProcesses) {
            try {
                $commandLine = (Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $($process.Id)").CommandLine
                if ($commandLine -and $commandLine -like "*$CommandPattern*") {
                    Write-Host "Found process with command line '$CommandPattern': $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Stop-ProcessTree -ProcessId $process.Id
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

# Function to kill PowerShell processes that spawned the server
function Stop-PowerShellServerProcess {
    [CmdletBinding(SupportsShouldProcess)]
    param()

    if (-not $PSCmdlet.ShouldProcess("PowerShell server processes", "Stop")) {
        return
    }

    Write-Host "Checking for PowerShell processes running server..." -ForegroundColor Cyan

    try {
        $powerShellProcesses = Get-Process | Where-Object { $_.ProcessName -like "*powershell*" }
        foreach ($process in $powerShellProcesses) {
            try {
                $commandLine = (Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $($process.Id)").CommandLine
                if ($commandLine -and ($commandLine -like "*uvicorn*" -or $commandLine -like "*start_server.ps1*" -or $commandLine -like "*server.main:app*" -or $commandLine -like "*mythosmud*" -or $commandLine -like "*uv run*")) {
                    Write-Host "Found PowerShell server process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Write-Host "  Command line: $commandLine" -ForegroundColor Gray
                    Stop-ProcessTree -ProcessId $process.Id
                }
            }
            catch {
                Write-Verbose "Could not get command line for PowerShell process $($process.Id)"
            }
        }
    }
    catch {
        Write-Host "Error checking PowerShell processes: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Function to close orphaned terminal windows
function Close-OrphanedTerminalWindows {
    [CmdletBinding()]
    param()

    Write-Host "Checking for orphaned terminal windows..." -ForegroundColor Cyan

    try {
        # This is more complex on Windows, but we can try to identify windows by title
        $processes = Get-Process | Where-Object { $_.ProcessName -like "*powershell*" -or $_.ProcessName -like "*cmd*" }
        foreach ($process in $processes) {
            try {
                $commandLine = (Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $($process.Id)").CommandLine
                if ($commandLine -and ($commandLine -like "*mythosmud*" -or $commandLine -like "*uvicorn*" -or $commandLine -like "*start_server.ps1*" -or $commandLine -like "*server.main*")) {
                    Write-Host "Found orphaned terminal: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Write-Host "  Command line: $commandLine" -ForegroundColor Gray
                    Stop-ProcessTree -ProcessId $process.Id
                }
            }
            catch {
                Write-Verbose "Could not check terminal process $($process.Id)"
            }
        }
    }
    catch {
        Write-Host "Error checking terminal windows: $($_.Exception.Message)" -ForegroundColor Yellow
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
        [int]$MaxWaitSeconds = 15
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

    # Method 1: Stop NATS server
    Stop-NatsServerForMythosMUD

    # Method 2: Kill PowerShell processes that spawned the server
    Stop-PowerShellServerProcess

    # Method 3: Kill processes by port
    Stop-ProcessesByPort -Port 54731

    # Method 3: Kill processes by name patterns
    Stop-ProcessesByName -NamePattern "*uvicorn*"
    # Note: Removed broad Python process killing to avoid affecting Playwright MCP server
    # Python processes are now targeted more specifically via command line patterns below

    # Method 4: Kill processes by command line patterns
    Stop-ProcessesByCommandLine -CommandPattern "uvicorn"
    Stop-ProcessesByCommandLine -CommandPattern "main:app"
    Stop-ProcessesByCommandLine -CommandPattern "start_server.ps1"
    Stop-ProcessesByCommandLine -CommandPattern "uv run"

    # Method 5: Close orphaned terminal windows
    Close-OrphanedTerminalWindows

    # Method 6: Force kill MythosMUD-related Python processes if Force flag is set
    if ($Force) {
        Write-Host "Force mode: Terminating MythosMUD-related Python processes..." -ForegroundColor Red
        $pythonProcesses = Get-Process | Where-Object { $_.ProcessName -like "*python*" }
        foreach ($process in $pythonProcesses) {
            try {
                $commandLine = (Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $($process.Id)").CommandLine
                # Only kill Python processes that are running MythosMUD-related code
                if ($commandLine -and (
                        $commandLine -like "*uvicorn*" -or
                        $commandLine -like "*main:app*" -or
                        $commandLine -like "*start_server.ps1*" -or
                        $commandLine -like "*uv run*" -or
                        $commandLine -like "*mythosmud*" -or
                        $commandLine -like "*server.main*"
                    )) {
                    Write-Host "Force terminating MythosMUD process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Write-Host "  Command line: $commandLine" -ForegroundColor Gray
                    Stop-ProcessTree -ProcessId $process.Id
                }
                else {
                    Write-Host "Skipping non-MythosMUD Python process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Cyan
                    if ($commandLine) {
                        Write-Host "  Command line: $commandLine" -ForegroundColor Gray
                    }
                }
            }
            catch {
                Write-Host "Could not check command line for process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Yellow
            }
        }
    }

    # Wait for processes to fully terminate
    Write-Host "Waiting for processes to fully terminate..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5

    # Add multiple verification attempts
    $maxRetries = 3
    $retryCount = 0
    $portFree = $false

    while (-not $portFree -and $retryCount -lt $maxRetries) {
        $portFree = Wait-ForPortFree -Port 54731 -MaxWaitSeconds 15
        if (-not $portFree) {
            $retryCount++
            Write-Host "Port still in use, retrying... (Attempt $retryCount/$maxRetries)" -ForegroundColor Yellow
            # Force kill any remaining processes
            Stop-ProcessesByPort -Port 54731
            Start-Sleep -Seconds 2
        }
    }

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
