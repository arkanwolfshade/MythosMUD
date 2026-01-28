#!/usr/bin/env pwsh

# Cursor CLI Agent Wrapper Script
# Provides convenient wrapper for common Cursor CLI agent tasks
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing script requires Write-Host for status messages')]

param(
    [Parameter(Position = 0)]
    [string]$Prompt,

    [string]$Model,

    [switch]$NonInteractive,

    [switch]$Plan,

    [switch]$Ask,

    [string]$OutputFormat = "text",

    [switch]$Help
)

if ($Help) {
    Write-Host "Cursor CLI Agent Wrapper Script"
    Write-Host ""
    Write-Host "Usage: .\cursor-cli-agent.ps1 [<prompt>] [-Model <model>] [-NonInteractive] [-Plan] [-Ask] [-OutputFormat <format>] [-Help]"
    Write-Host ""
    Write-Host "Parameters:"
    Write-Host "    <prompt>              The prompt to send to the agent (optional if using interactive mode)"
    Write-Host "    -Model <model>        Model to use (e.g., 'gpt-5.2', 'claude-4.5-opus')"
    Write-Host "    -NonInteractive        Run in non-interactive (print) mode"
    Write-Host "    -Plan                 Use Plan mode (design approach before coding)"
    Write-Host "    -Ask                  Use Ask mode (read-only exploration)"
    Write-Host "    -OutputFormat <fmt>   Output format: 'text' (default) or 'json'"
    Write-Host "    -Help                 Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "    .\cursor-cli-agent.ps1 'analyze test failures in server/tests/unit'"
    Write-Host "    .\cursor-cli-agent.ps1 -NonInteractive -Prompt 'review security of auth module'"
    Write-Host "    .\cursor-cli-agent.ps1 -Plan -Prompt 'refactor the persistence layer'"
    Write-Host "    .\cursor-cli-agent.ps1 -Ask -Prompt 'explore the authentication flow'"
    Write-Host "    .\cursor-cli-agent.ps1                    # Start interactive session"
    exit 0
}

# Set error action preference
$ErrorActionPreference = "Stop"

# Check if Cursor CLI is installed
try {
    $cursorVersion = cursor --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Cursor CLI is not installed or not in PATH. Install it with: irm 'https://cursor.com/install?win32=true' | iex"
        exit 1
    }
}
catch {
    Write-Error "Cursor CLI is not installed or not in PATH. Install it with: irm 'https://cursor.com/install?win32=true' | iex"
    exit 1
}

# Build command arguments
$args = @()

# Determine mode
if ($Plan) {
    $args += "--mode=plan"
}
elseif ($Ask) {
    $args += "--mode=ask"
}

# Non-interactive mode (print mode)
if ($NonInteractive) {
    if (-not $Prompt) {
        Write-Error "Non-interactive mode requires a prompt. Use -Prompt parameter."
        exit 1
    }
    $args += "-p"
    $args += $Prompt
}
else {
    # Interactive mode
    if ($Prompt) {
        $args += $Prompt
    }
}

# Model selection
if ($Model) {
    $args += "--model"
    $args += $Model
}

# Output format
if ($OutputFormat) {
    $args += "--output-format"
    $args += $OutputFormat
}

# Execute Cursor CLI
Write-Host "Executing Cursor CLI agent..." -ForegroundColor Cyan
Write-Host "Command: cursor agent $($args -join ' ')" -ForegroundColor Gray
Write-Host ""

try {
    & cursor agent @args
    $exitCode = $LASTEXITCODE

    if ($exitCode -eq 0) {
        Write-Host ""
        Write-Host "Cursor CLI agent completed successfully." -ForegroundColor Green
    }
    else {
        Write-Host ""
        Write-Host "Cursor CLI agent exited with code $exitCode." -ForegroundColor Yellow
    }

    exit $exitCode
}
catch {
    Write-Error "Failed to execute Cursor CLI agent: $_"
    exit 1
}
