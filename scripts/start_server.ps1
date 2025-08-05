#Requires -Version 5.1

<#
.SYNOPSIS
    Starts the MythosMUD server with optional process cleanup.

.DESCRIPTION
    This script starts the MythosMUD FastAPI server by:
    - Terminating any existing server processes
    - Checking if the specified port is available
    - Starting the uvicorn server with the specified parameters
    - Verifying the server is responding before completing

.PARAMETER ServerHost
    The host address to bind the server to. Default is "127.0.0.1".

.PARAMETER Port
    The port number to bind the server to. Default is 54731.

.PARAMETER Reload
    When specified, enables auto-reload for development. Default is true.

.EXAMPLE
    .\start_server.ps1
    Starts the server with default settings (127.0.0.1:54731 with reload).

.EXAMPLE
    .\start_server.ps1 -ServerHost "0.0.0.0" -Port 8080 -Reload:$false
    Starts the server on all interfaces, port 8080, without auto-reload.

.NOTES
    Author: MythosMUD Development Team
    Version: 2.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding()]
param(
    [Parameter(HelpMessage = "Host address to bind server to")]
    [ValidateNotNullOrEmpty()]
    [string]$ServerHost = "",

    [Parameter(HelpMessage = "Port number to bind server to")]
    [ValidateRange(1, 65535)]
    [int]$Port = 0,

    [Parameter(HelpMessage = "Enable auto-reload for development")]
    [switch]$Reload = $true,

    [Parameter(HelpMessage = "Environment to run in (local, test, production)")]
    [ValidateSet("local", "test", "production")]
    [string]$Environment = "local",

    [Parameter(HelpMessage = "Show help information")]
    [switch]$Help
)

# Function to load environment variables
function Load-EnvironmentConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Environment
    )

    $envFile = switch ($Environment) {
        "local" { ".env.local" }
        "test" { ".env.test" }
        "production" { ".env.production" }
        default { ".env.local" }
    }

    if (Test-Path $envFile) {
        Write-Host "Loading environment from $envFile" -ForegroundColor Cyan
        Get-Content $envFile | ForEach-Object {
            if ($_ -match "^([^#][^=]+)=(.*)$") {
                $name = $matches[1].Trim()
                $value = $matches[2].Trim()
                [Environment]::SetEnvironmentVariable($name, $value, "Process")
            }
        }
    } else {
        Write-Host "Warning: Environment file $envFile not found" -ForegroundColor Yellow
    }
}

# Function to read server configuration
function Get-ServerConfig {
    [CmdletBinding()]
    param()

    $configPath = "server\server_config.yaml"
    $defaultHost = "127.0.0.1"
    $defaultPort = 54731

    if (Test-Path $configPath) {
        try {
            # Simple YAML parsing for host and port
            $configContent = Get-Content $configPath -Raw
            if ($configContent -match "host:\s*([^\s#]+)") {
                $defaultHost = $matches[1].Trim()
            }
            if ($configContent -match "port:\s*(\d+)") {
                $defaultPort = [int]$matches[1]
            }
            Write-Host "Loaded config from $configPath" -ForegroundColor Gray
        }
        catch {
            Write-Host "Warning: Could not parse config file, using defaults" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "Warning: Config file not found at $configPath, using defaults" -ForegroundColor Yellow
    }

    Write-Host "Config loaded - Host: $defaultHost, Port: $defaultPort" -ForegroundColor Cyan
    return @{
        Host = $defaultHost
        Port = $defaultPort
    }
}

# Show help if requested
if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path -Full
    exit 0
}

# Load configuration and set defaults
$config = Get-ServerConfig
if ([string]::IsNullOrEmpty($ServerHost)) {
    $ServerHost = $config.Host
}
if ($Port -eq 0) {
    $Port = $config.Port
}

# Function to terminate server processes
function Stop-ServerProcesses {
    [CmdletBinding()]
    param()

    Write-Host "Checking for existing server processes..." -ForegroundColor Yellow

    try {
        $serverProcesses = Get-Process | Where-Object {
            $_.ProcessName -like "*python*" -or
            $_.ProcessName -like "*uvicorn*"
        }

        if ($serverProcesses) {
            Write-Host "Found $($serverProcesses.Count) existing server process(es). Terminating..." -ForegroundColor Yellow
            $serverProcesses | ForEach-Object {
                Write-Host "  Terminating process: $($_.ProcessName) (PID: $($_.Id))" -ForegroundColor Gray
                Stop-Process -Id $_.Id -Force
            }
            Start-Sleep -Seconds 2
        }
        else {
            Write-Host "No existing server processes found." -ForegroundColor Green
        }
    }
    catch {
        Write-Host "Error checking for existing processes: $($_.Exception.Message)" -ForegroundColor Yellow
    }
}

# Function to check if port is in use
function Test-PortInUse {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 65535)]
        [int]$Port
    )

    try {
        $connection = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
        if ($connection) {
            Write-Host "Port $Port is still in use. Waiting for it to be released..." -ForegroundColor Yellow
            Start-Sleep -Seconds 3
            return $true
        }
        return $false
    }
    catch {
        Write-Host "Error checking port ${Port}: $($_.Exception.Message)" -ForegroundColor Yellow
        return $false
    }
}

# Function to start the server
function Start-MythosMUDServer {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$ServerHost,

        [Parameter(Mandatory = $true)]
        [ValidateRange(1, 65535)]
        [int]$Port,

        [Parameter(Mandatory = $true)]
        [bool]$Reload
    )

    # Use 127.0.0.1 for health check even if server binds to 0.0.0.0
    $healthCheckUrl = "http://127.0.0.1:" + $Port
    $serverUrl = "http://" + $ServerHost + ":" + $Port
    Write-Host "Starting server on $serverUrl..." -ForegroundColor Cyan

    $reloadFlag = if ($Reload) { "--reload" } else { "" }

    # Run uvicorn from project root with proper module path
    # Use uvicorn's default logging with access log enabled
    $serverCommand = "uv run uvicorn server.main:app --host $ServerHost --port $Port $reloadFlag --access-log"

    Write-Host "Executing: $serverCommand" -ForegroundColor Gray

    try {
        # Start the server process from project root
        Start-Process powershell -ArgumentList "-NoExit", "-Command", $serverCommand -WindowStyle Normal

        # Wait for server to start
        Write-Host "Waiting for server to start..." -ForegroundColor Yellow
        Start-Sleep -Seconds 5

        # Test if server is responding
        $maxAttempts = 10
        $attempt = 0

        while ($attempt -lt $maxAttempts) {
            try {
                $response = Invoke-WebRequest -Uri $healthCheckUrl -UseBasicParsing -TimeoutSec 5
                if ($response.StatusCode -eq 200) {
                    Write-Host "Server is running successfully on $serverUrl" -ForegroundColor Green
                    Write-Host "API Documentation: $serverUrl/docs" -ForegroundColor Cyan
                    Write-Host "Game Status: $serverUrl/game/status" -ForegroundColor Cyan
                    return $true
                }
            }
            catch {
                $attempt++
                Write-Host "Attempt $attempt of $maxAttempts - Server not ready yet..." -ForegroundColor Yellow
                Start-Sleep -Seconds 2
            }
        }

        Write-Host "Server failed to start after $maxAttempts attempts" -ForegroundColor Red
        return $false
    }
    catch {
        Write-Host "Error starting server process: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Main execution
try {
    Write-Host "Starting MythosMUD Server..." -ForegroundColor Green

    # Step 1: Load environment configuration
    Load-EnvironmentConfig -Environment $Environment

    # Step 2: Stop existing processes
    Stop-ServerProcesses

    # Step 2: Check if port is free
    if (Test-PortInUse -Port $Port) {
        Write-Host "Port $Port is still in use. Please check for other processes." -ForegroundColor Red
        exit 1
    }

    # Step 3: Start the server
    $success = Start-MythosMUDServer -ServerHost $ServerHost -Port $Port -Reload $Reload

    if ($success) {
        Write-Host "MythosMUD Server is ready!" -ForegroundColor Green
        Write-Host "Press Ctrl+C in the server window to stop the server." -ForegroundColor Gray
    }
    else {
        Write-Host "Failed to start MythosMUD Server" -ForegroundColor Red
        exit 1
    }

}
catch {
    Write-Host "Error starting server: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
