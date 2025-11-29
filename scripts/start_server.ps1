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
    When specified, enables auto-reload for development. Default is false (hot reloading disabled due to client compatibility issues).

.EXAMPLE
    .\start_server.ps1
    Starts the server with default settings (127.0.0.1:54731 without reload).

.EXAMPLE
    .\start_server.ps1 -ServerHost "0.0.0.0" -Port 8080 -Reload
    Starts the server on all interfaces, port 8080, with auto-reload enabled.

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
    [switch]$Reload = $false,

    [Parameter(HelpMessage = "Environment to run in (local, unit_test, e2e_test, production)")]
    [ValidateSet("local", "unit_test", "e2e_test", "production")]
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
        "unit_test" { ".env.unit_test" }
        "e2e_test" { ".env.e2e_test" }
        "production" { ".env.production" }
        default { ".env.local" }
    }

    if (Test-Path $envFile) {
        Write-Host "Loading environment from $envFile" -ForegroundColor Cyan
        Get-Content $envFile | ForEach-Object {
            if ($_ -match "^([^#][^=]+)=(.*)$") {
                $name = $matches[1].Trim()
                $value = $matches[2].Trim()
                # Use Set-Item for env: drive to handle all variable names correctly
                Set-Item -Path "env:$name" -Value $value -Force
            }
        }
    }
    else {
        Write-Host "Warning: Environment file $envFile not found" -ForegroundColor Yellow
    }
}

# Function to get environment file path based on environment
function Get-EnvFilePath {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$Environment
    )

    $envFile = switch ($Environment) {
        "local" { ".env.local" }
        "unit_test" { ".env.unit_test" }
        "e2e_test" { ".env.e2e_test" }
        "production" { ".env.production" }
        default { ".env.local" }
    }

    return $envFile
}

# Function to read server configuration from environment
function Get-ServerConfig {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$EnvFile
    )

    $defaultHost = "127.0.0.1"
    $defaultPort = 54731

    if (Test-Path $EnvFile) {
        try {
            # Parse .env file for SERVER_HOST and SERVER_PORT
            $envContent = Get-Content $EnvFile -Raw
            if ($envContent -match "SERVER_HOST\s*=\s*([^\s#]+)") {
                $defaultHost = $matches[1].Trim()
            }
            if ($envContent -match "SERVER_PORT\s*=\s*(\d+)") {
                $defaultPort = [int]$matches[1]
            }
            Write-Host "Loaded config from $EnvFile" -ForegroundColor Gray
        }
        catch {
            Write-Host "Warning: Could not parse .env file, using defaults" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "Warning: .env file not found at $EnvFile, using defaults" -ForegroundColor Yellow
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

# Configuration is now handled in the main execution block below
# (Pydantic BaseSettings loads from .env files automatically)

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

# Function to start NATS server
function Start-NatsServerForMythosMUD {
    [CmdletBinding()]
    param()

    Write-Host "Checking NATS server..." -ForegroundColor Cyan

    # Import NATS management functions
    $natsManagerPath = Join-Path $PSScriptRoot "nats_manager.ps1"
    if (Test-Path $natsManagerPath) {
        . $natsManagerPath

        # Check if NATS is running
        if (-not (Test-NatsServerRunning)) {
            Write-Host "Starting NATS server for MythosMUD..." -ForegroundColor Yellow
            $natsStarted = Start-NatsServer -UseConfig -Background
            if ($natsStarted) {
                Write-Host "NATS server started successfully" -ForegroundColor Green
            }
            else {
                Write-Host "Warning: Failed to start NATS server" -ForegroundColor Yellow
            }
        }
        else {
            Write-Host "NATS server is already running" -ForegroundColor Green
        }
    }
    else {
        Write-Host "Warning: NATS manager not found at $natsManagerPath" -ForegroundColor Yellow
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
        [bool]$Reload,

        [Parameter(Mandatory = $false)]
        [string]$EnvFile = ""
    )

    # Use 127.0.0.1 for health check even if server binds to 0.0.0.0
    $healthCheckUrl = "http://127.0.0.1:" + $Port
    $serverUrl = "http://" + $ServerHost + ":" + $Port
    Write-Host "Starting server on $serverUrl..." -ForegroundColor Cyan

    if ($Reload) {
        # Use uvicorn CLI with reload for optimal development experience
        # This provides better reload control and faster iteration than programmatic reload
        # Explicitly watch server directory to ensure command handler changes are detected
        # Note: --reload-dir ensures uvicorn watches the entire server directory tree
        $serverCommand = "uv run uvicorn server.main:app --host $ServerHost --port $Port --reload --reload-dir server"
        Write-Host "Using uvicorn with auto-reload enabled (watching server directory)" -ForegroundColor Cyan
    }
    else {
        # Build command arguments for non-reload mode
        $commandArgs = @("uv", "run", "uvicorn", "server.main:app", "--host", $ServerHost, "--port", $Port.ToString())
        $serverCommand = ($commandArgs | ForEach-Object { if ($_ -contains ' ') { "`"$_`"" } else { $_ } }) -join ' '
    }

    Write-Host "Executing: $serverCommand" -ForegroundColor Gray

    try {
        # Build command that loads environment variables first, then starts server
        # This ensures the spawned process has access to secrets from .env file
        $envLoadCommand = ""
        if ($EnvFile -and (Test-Path $EnvFile)) {
            # Escape single quotes in path for PowerShell string
            $escapedEnvFile = $EnvFile -replace "'", "''"
            $envLoadCommand = "Get-Content '$escapedEnvFile' | ForEach-Object { if (`$_ -match '^([^#][^=]+)=(.*)$') { Set-Item -Path `"env:`$(`$matches[1].Trim())`" -Value `$matches[2].Trim() -Force } }; "
            Write-Host "Environment file will be loaded in spawned process: $EnvFile" -ForegroundColor Cyan
        }

        # Set MYTHOSMUD_ENV in the spawned process to ensure logging uses correct directory
        $mythosmudEnv = [Environment]::GetEnvironmentVariable("MYTHOSMUD_ENV", "Process")
        if ($mythosmudEnv) {
            $envLoadCommand += "`$env:MYTHOSMUD_ENV='$mythosmudEnv'; "
            Write-Host "MYTHOSMUD_ENV=$mythosmudEnv will be set in spawned process" -ForegroundColor Cyan
        }

        $fullCommand = $envLoadCommand + $serverCommand

        # Start the server process from project root with environment variables loaded
        Start-Process powershell -ArgumentList "-NoExit", "-Command", $fullCommand -WindowStyle Normal

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

    # Step 1: Get environment file path
    $envFile = Get-EnvFilePath -Environment $Environment
    $absoluteEnvFile = Join-Path $PWD $envFile

    # Verify .env file exists
    if (-not (Test-Path $absoluteEnvFile)) {
        Write-Error "Environment file not found: $absoluteEnvFile"
        Write-Host ""
        Write-Host "Available environment files:" -ForegroundColor Yellow
        Write-Host "  - .env.local (for local development)" -ForegroundColor Gray
        Write-Host "  - .env.unit_test (for unit tests)" -ForegroundColor Gray
        Write-Host "  - .env.e2e_test (for E2E tests)" -ForegroundColor Gray
        Write-Host ""
        Write-Host "Copy the appropriate .env.*.example file to create your environment file:" -ForegroundColor Cyan
        Write-Host "  cp .env.local.example .env.local" -ForegroundColor Gray
        exit 1
    }

    # Step 2: Load environment configuration
    Load-EnvironmentConfig -Environment $Environment

    # Step 2.5: Set LOGGING_ENVIRONMENT for Pydantic configuration
    # The Pydantic config uses this to determine log directories
    [Environment]::SetEnvironmentVariable("LOGGING_ENVIRONMENT", $Environment, "Process")
    Write-Host "Set LOGGING_ENVIRONMENT=$Environment for Pydantic config" -ForegroundColor Cyan

    # Step 3: Read config from .env file for display purposes
    $config = Get-ServerConfig -EnvFile $absoluteEnvFile
    if ([string]::IsNullOrEmpty($ServerHost)) {
        $ServerHost = $config.Host
    }
    if ($Port -eq 0) {
        $Port = $config.Port
    }

    # Step 4: Stop existing processes
    Stop-ServerProcesses

    # Step 5: Start NATS server
    Start-NatsServerForMythosMUD

    # Step 6: Check if port is free
    if (Test-PortInUse -Port $Port) {
        Write-Host "Port $Port is still in use. Please check for other processes." -ForegroundColor Red
        exit 1
    }

    # Step 7: Start the server
    $success = Start-MythosMUDServer -ServerHost $ServerHost -Port $Port -Reload $Reload -EnvFile $absoluteEnvFile

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
