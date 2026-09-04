#Requires -Version 5.1
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing script requires Write-Host for status messages')]

<#
.SYNOPSIS
    Stops MythosMUD server processes using multiple detection methods.

.DESCRIPTION
    This script provides robust server shutdown functionality for MythosMUD by:
    - Terminating processes using port 54768
    - Killing processes by name patterns (uvicorn and gunicorn)
    - Terminating processes by command line patterns (MythosMUD-specific)
    - Force killing MythosMUD-related Python processes in THIS repo if Force flag is set
    - Verifying port is free after shutdown
    - Terminating PowerShell processes that spawned the server
    - Cleaning up orphaned terminal windows

    SECURITY NOTE: Processes are terminated only when Win32_Process data shows the
    executable or command line contains THIS repository root (see MythosMudProcessScope.ps1).
    Name-only or broad pattern matches are never sufficient to kill a process.

.PARAMETER Force
    When specified, forces termination of Python processes that match MythosMUD command-line
    patterns and are owned by this repository root (see MythosMudProcessScope.ps1).

.PARAMETER Verbose
    When specified, provides detailed output including remaining connections. This parameter is automatically available due to CmdletBinding.

.EXAMPLE
    .\stop_server.ps1
    Stops MythosMUD server processes gracefully.

.EXAMPLE
    .\stop_server.ps1 -Force -Verbose
    Force-stops MythosMUD-scoped Python processes in this repo and provides detailed output.

.NOTES
    Author: MythosMUD Development Team
    Version: 3.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding()]
param(
    [Parameter(HelpMessage = "Force termination of Python processes that match MythosMUD patterns AND this repo root")]
    [switch]$Force
)

. (Join-Path $PSScriptRoot 'MythosMudProcessScope.ps1')

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
                        Stop-MythosMudProjectProcessTree -ProcessId $process.Id
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
                if (-not (Test-MythosMudProjectProcess -ProcessId $process.Id)) {
                    Write-Host "Skipping NATS PID $($process.Id): not owned by this MythosMUD repo" -ForegroundColor Yellow
                    continue
                }
                Write-Host "Stopping NATS process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Yellow
                Stop-MythosMudProjectProcessTree -ProcessId $process.Id
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
                    Stop-MythosMudProjectProcessTree -ProcessId $process.Id
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
                    if (-not (Test-MythosMudProjectProcess -ProcessId $process.Id)) {
                        Write-Verbose "Skipping PID $($process.Id): command matched '$CommandPattern' but not this repo"
                        continue
                    }
                    Write-Host "Found process with command line '$CommandPattern': $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Stop-MythosMudProjectProcessTree -ProcessId $process.Id
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
                # Do not kill the E2E launcher (start_e2e_test.ps1); it calls this script and must survive to start the server.
                if ($commandLine -and $commandLine -like "*start_e2e_test.ps1*") {
                    continue
                }
                if (-not (Test-MythosMudProjectProcess -ProcessId $process.Id)) {
                    continue
                }
                # Exclude path-only hits (e.g. ...\MythosMUD-worktrees\... matching *mythosmud*): require server entry cues.
                if ($commandLine -and (
                        $commandLine -like "*uvicorn*" -or
                        $commandLine -like "*gunicorn*" -or
                        $commandLine -like "*start_server.ps1*" -or
                        $commandLine -like "*start_local.ps1*" -or
                        $commandLine -like "*server.main:app*" -or
                        $commandLine -like "*uv run*"
                    )) {
                    Write-Host "Found PowerShell server process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Write-Host "  Command line: $commandLine" -ForegroundColor Gray
                    Stop-MythosMudProjectProcessTree -ProcessId $process.Id
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
                $cimProc = Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $($process.Id)" -ErrorAction SilentlyContinue
                $commandLine = $null
                $executablePath = $null
                if ($cimProc) {
                    $commandLine = $cimProc.CommandLine
                    $executablePath = $cimProc.ExecutablePath
                }
                if (-not $executablePath) {
                    $executablePath = $process.Path
                }
                # Do not kill the E2E launcher (start_e2e_test.ps1) or the terminal running e2e.bat (cmd /c e2e.bat).
                if ($commandLine -and ($commandLine -like "*start_e2e_test.ps1*" -or $commandLine -like "*e2e.bat*")) {
                    continue
                }
                if (-not (Test-MythosMudProjectProcess -ProcessId $process.Id)) {
                    continue
                }
                if ($commandLine -and (
                        $commandLine -like "*uvicorn*" -or
                        $commandLine -like "*gunicorn*" -or
                        $commandLine -like "*start_server.ps1*" -or
                        $commandLine -like "*start_local.ps1*" -or
                        $commandLine -like "*server.main*" -or
                        $commandLine -like "*uv run*"
                    )) {
                    Write-Host "Found orphaned terminal: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    if ($executablePath) {
                        Write-Host "  Executable path: $executablePath" -ForegroundColor Gray
                    }
                    else {
                        Write-Host "  Executable path: (unavailable)" -ForegroundColor Gray
                    }
                    Write-Host "  Command line: $commandLine" -ForegroundColor Gray

                    $shouldStop = $false
                    $canPrompt = [Environment]::UserInteractive -and -not [Console]::IsInputRedirected
                    if ($canPrompt) {
                        $prompt = "Terminate this process? [Y]es / [N]o (leave running, default: N)"
                        $answer = Read-Host $prompt
                        if ($null -ne $answer -and $answer.Trim() -match '^(?i:y|yes)$') {
                            $shouldStop = $true
                        }
                    }
                    else {
                        Write-Host "Non-interactive input: skipping orphaned terminal termination for PID $($process.Id). Re-run stop_server.ps1 in an interactive console to confirm." -ForegroundColor Yellow
                    }

                    if ($shouldStop) {
                        Stop-MythosMudProjectProcessTree -ProcessId $process.Id
                    }
                    else {
                        if ($canPrompt) {
                            Write-Host "Leaving process $($process.Id) running." -ForegroundColor Yellow
                        }
                    }
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
    Stop-ProcessesByPort -Port 54768

    # Method 3: Kill processes by name patterns
    Stop-ProcessesByName -NamePattern "*uvicorn*"
    Stop-ProcessesByName -NamePattern "*gunicorn*"
    # Note: Removed broad Python process killing to avoid affecting Playwright MCP server
    # Python processes are now targeted more specifically via command line patterns below

    # Method 4: Kill processes by command line patterns
    Stop-ProcessesByCommandLine -CommandPattern "uvicorn"
    Stop-ProcessesByCommandLine -CommandPattern "gunicorn"
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
                        $commandLine -like "*gunicorn*" -or
                        $commandLine -like "*main:app*" -or
                        $commandLine -like "*start_server.ps1*" -or
                        $commandLine -like "*start_local.ps1*" -or
                        $commandLine -like "*uv run*" -or
                        $commandLine -like "*server.main*"
                    )) {
                    if (-not (Test-MythosMudProjectProcess -ProcessId $process.Id)) {
                        continue
                    }
                    Write-Host "Force terminating MythosMUD process: $($process.ProcessName) (PID: $($process.Id))" -ForegroundColor Red
                    Write-Host "  Command line: $commandLine" -ForegroundColor Gray
                    Stop-MythosMudProjectProcessTree -ProcessId $process.Id
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
        $portFree = Wait-ForPortFree -Port 54768 -MaxWaitSeconds 15
        if (-not $portFree) {
            $retryCount++
            Write-Host "Port still in use, retrying... (Attempt $retryCount/$maxRetries)" -ForegroundColor Yellow
            # Force kill any remaining processes
            Stop-ProcessesByPort -Port 54768
            Start-Sleep -Seconds 2
        }
    }

    if ($portFree) {
        Write-Host "`nMythosMUD Server shutdown complete!" -ForegroundColor Green
    }
    else {
        Write-Host "`nWARNING: Server shutdown may be incomplete. Port 54768 is still in use." -ForegroundColor Yellow
        if ($Verbose) {
            Write-Host "Remaining connections on port 54768:" -ForegroundColor Yellow
            Get-NetTCPConnection -LocalPort 54768 -ErrorAction SilentlyContinue | ForEach-Object {
                Write-Host "  $($_.LocalAddress):$($_.LocalPort) -> $($_.RemoteAddress):$($_.RemotePort) (PID: $($_.OwningProcess))" -ForegroundColor Gray
            }
        }
    }

}
catch {
    Write-Host "Error during shutdown: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
