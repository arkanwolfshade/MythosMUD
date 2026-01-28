#!/usr/bin/env pwsh

# Cursor CLI Test Failure Remediation Script
# Automated test failure analysis and remediation using Cursor CLI
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing status messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing script requires Write-Host for status messages')]

param(
    [string]$TestPath,

    [string]$TestFile,

    [string]$TestName,

    [string]$Model,

    [switch]$AnalyzeOnly,

    [switch]$OutputReport,

    [string]$ReportPath = "cursor-test-fix-report.txt",

    [switch]$Help
)

if ($Help) {
    Write-Host "Cursor CLI Test Failure Remediation Script"
    Write-Host ""
    Write-Host "Usage: .\cursor-cli-test-fix.ps1 [-TestPath <path>] [-TestFile <file>] [-TestName <name>] [-Model <model>] [-AnalyzeOnly] [-OutputReport] [-ReportPath <path>] [-Help]"
    Write-Host ""
    Write-Host "Parameters:"
    Write-Host "    -TestPath <path>      Path to test directory or file"
    Write-Host "    -TestFile <file>      Specific test file to analyze"
    Write-Host "    -TestName <name>      Specific test name/pattern to analyze"
    Write-Host "    -Model <model>        Model to use (e.g., 'gpt-5.2', 'claude-4.5-opus')"
    Write-Host "    -AnalyzeOnly          Only analyze failures, don't suggest fixes"
    Write-Host "    -OutputReport         Save analysis report to file"
    Write-Host "    -ReportPath <path>    Path for analysis report (default: cursor-test-fix-report.txt)"
    Write-Host "    -Help                 Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "    .\cursor-cli-test-fix.ps1 -TestPath server/tests/unit"
    Write-Host "    .\cursor-cli-test-fix.ps1 -TestFile server/tests/unit/test_auth.py"
    Write-Host "    .\cursor-cli-test-fix.ps1 -TestName test_login_failure -AnalyzeOnly"
    Write-Host "    .\cursor-cli-test-fix.ps1 -TestPath server/tests/unit -OutputReport"
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

# Build analysis prompt
$analysisPrompt = "Analyze test failures"

if ($TestFile) {
    if (-not (Test-Path $TestFile)) {
        Write-Error "Test file not found: $TestFile"
        exit 1
    }
    $analysisPrompt += " in $TestFile"
} elseif ($TestPath) {
    if (-not (Test-Path $TestPath)) {
        Write-Error "Test path not found: $TestPath"
        exit 1
    }
    $analysisPrompt += " in $TestPath"
} else {
    $analysisPrompt += " in the test suite"
}

if ($TestName) {
    $analysisPrompt += " focusing on test: $TestName"
}

$analysisPrompt += ". "

if ($AnalyzeOnly) {
    $analysisPrompt += "Analyze the failures, identify root causes, and provide detailed analysis. Do NOT suggest fixes."
} else {
    $analysisPrompt += "Analyze the failures, identify root causes, and suggest specific fixes. Focus on: "
    $analysisPrompt += "1. Understanding why tests are failing"
    $analysisPrompt += "2. Identifying the root cause"
    $analysisPrompt += "3. Suggesting specific code changes to fix the issues"
    $analysisPrompt += "4. Ensuring fixes maintain test quality and coverage"
}

$analysisPrompt += " Follow project test quality requirements: tests must test server code, not test infrastructure or Python built-ins."

# Build command arguments
$cursorArgs = @("-p", $analysisPrompt)

# Model selection
if ($Model) {
    $cursorArgs += "--model"
    $cursorArgs += $Model
}

# Output format
$cursorArgs += "--output-format"
$cursorArgs += "text"

# Execute analysis
Write-Host "Starting test failure analysis..." -ForegroundColor Cyan
if ($TestFile) {
    Write-Host "Test File: $TestFile" -ForegroundColor Gray
} elseif ($TestPath) {
    Write-Host "Test Path: $TestPath" -ForegroundColor Gray
}
if ($TestName) {
    Write-Host "Test Name: $TestName" -ForegroundColor Gray
}
Write-Host "Mode: $(if ($AnalyzeOnly) { 'Analysis Only' } else { 'Analysis + Fixes' })" -ForegroundColor Gray
Write-Host ""

try {
    if ($OutputReport) {
        Write-Host "Analysis output will be saved to: $ReportPath" -ForegroundColor Cyan
        & cursor agent @cursorArgs | Tee-Object -FilePath $ReportPath
    } else {
        & cursor agent @cursorArgs
    }

    $exitCode = $LASTEXITCODE

    if ($exitCode -eq 0) {
        Write-Host ""
        Write-Host "Test failure analysis completed successfully." -ForegroundColor Green
        if ($OutputReport) {
            Write-Host "Analysis report saved to: $ReportPath" -ForegroundColor Green
        }
    } else {
        Write-Host ""
        Write-Host "Test failure analysis exited with code $exitCode." -ForegroundColor Yellow
    }

    exit $exitCode
} catch {
    Write-Error "Failed to execute test failure analysis: $_"
    exit 1
}
