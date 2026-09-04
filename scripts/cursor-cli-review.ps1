#!/usr/bin/env pwsh

# Cursor CLI Code Review Script
# Automated code review using Cursor CLI
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing script requires Write-Host for status messages')]

param(
    [string]$Path,

    [string]$Focus = "security",

    [string]$Model,

    [switch]$GitChanges,

    [switch]$OutputReport,

    [string]$ReportPath = "cursor-review-report.txt",

    [switch]$Help
)

if ($Help) {
    Write-Host "Cursor CLI Code Review Script"
    Write-Host ""
    Write-Host "Usage: .\cursor-cli-review.ps1 [-Path <path>] [-Focus <focus>] [-Model <model>] [-GitChanges] [-OutputReport] [-ReportPath <path>] [-Help]"
    Write-Host ""
    Write-Host "Parameters:"
    Write-Host "    -Path <path>          Path to review (file or directory, default: current changes)"
    Write-Host "    -Focus <focus>        Review focus: 'security' (default), 'performance', 'quality', 'all'"
    Write-Host "    -Model <model>        Model to use (e.g., 'gpt-5.2', 'claude-4.5-opus')"
    Write-Host "    -GitChanges           Review git changes instead of specific path"
    Write-Host "    -OutputReport         Save review report to file"
    Write-Host "    -ReportPath <path>    Path for review report (default: cursor-review-report.txt)"
    Write-Host "    -Help                 Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "    .\cursor-cli-review.ps1 -GitChanges"
    Write-Host "    .\cursor-cli-review.ps1 -Path server/services/auth.py -Focus security"
    Write-Host "    .\cursor-cli-review.ps1 -Path server/ -Focus all -OutputReport"
    Write-Host "    .\cursor-cli-review.ps1 -GitChanges -Focus performance -Model gpt-5.2"
    exit 0
}

# Set error action preference
$ErrorActionPreference = "Stop"

# Check if Cursor CLI is installed
try {
    $null = cursor --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Cursor CLI is not installed or not in PATH. Install it with: irm 'https://cursor.com/install?win32=true' | iex"
        exit 1
    }
} catch {
    Write-Error "Cursor CLI is not installed or not in PATH. Install it with: irm 'https://cursor.com/install?win32=true' | iex"
    exit 1
}

# Build review prompt based on focus
$reviewPrompts = @{
    "security" = "Review this code for security issues. Focus on: authentication/authorization, input validation, COPPA compliance, XSS vulnerabilities, SQL injection risks, path traversal, secure storage, and security headers."
    "performance" = "Review this code for performance issues. Focus on: bottlenecks, inefficient algorithms, database query optimization, memory leaks, and optimization opportunities."
    "quality" = "Review this code for quality issues. Focus on: code organization, maintainability, best practices, error handling, logging, and adherence to project standards."
    "all" = "Perform comprehensive code review. Check for: security vulnerabilities, performance issues, code quality, best practices, error handling, logging, and adherence to project standards."
}

if (-not $reviewPrompts.ContainsKey($Focus)) {
    Write-Error "Invalid focus: $Focus. Valid options: security, performance, quality, all"
    exit 1
}

$reviewPrompt = $reviewPrompts[$Focus]

# Determine what to review
if ($GitChanges) {
    $targetPrompt = "Review these git changes for $Focus issues. $reviewPrompt"
} elseif ($Path) {
    if (-not (Test-Path $Path)) {
        Write-Error "Path not found: $Path"
        exit 1
    }
    $targetPrompt = "Review the code at $Path for $Focus issues. $reviewPrompt"
} else {
    # Default: review git changes
    $targetPrompt = "Review these git changes for $Focus issues. $reviewPrompt"
}

# Build command arguments
$cursorArgs = @("-p", $targetPrompt)

# Model selection
if ($Model) {
    $cursorArgs += "--model"
    $cursorArgs += $Model
}

# Output format
$cursorArgs += "--output-format"
$cursorArgs += "text"

# Execute review
Write-Host "Starting code review..." -ForegroundColor Cyan
Write-Host "Focus: $Focus" -ForegroundColor Gray
if ($Path) {
    Write-Host "Path: $Path" -ForegroundColor Gray
} else {
    Write-Host "Target: Git changes" -ForegroundColor Gray
}
Write-Host ""

try {
    if ($OutputReport) {
        Write-Host "Review output will be saved to: $ReportPath" -ForegroundColor Cyan
        & cursor agent @cursorArgs | Tee-Object -FilePath $ReportPath
    } else {
        & cursor agent @cursorArgs
    }

    $exitCode = $LASTEXITCODE

    if ($exitCode -eq 0) {
        Write-Host ""
        Write-Host "Code review completed successfully." -ForegroundColor Green
        if ($OutputReport) {
            Write-Host "Review report saved to: $ReportPath" -ForegroundColor Green
        }
    } else {
        Write-Host ""
        Write-Host "Code review exited with code $exitCode." -ForegroundColor Yellow
    }

    exit $exitCode
} catch {
    Write-Error "Failed to execute code review: $_"
    exit 1
}
