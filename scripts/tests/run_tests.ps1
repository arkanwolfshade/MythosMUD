#!/usr/bin/env pwsh

<#
.SYNOPSIS
    Run PowerShell tests for NATS Manager functionality

.DESCRIPTION
    This script runs the PowerShell tests for NATS Manager including
    environment variable support and backward compatibility testing.
#>

param(
    [Parameter(HelpMessage = "Show verbose output")]
    [switch]$ShowVerbose,

    [Parameter(HelpMessage = "Run specific test file")]
    [string]$TestFile = "*"
)

# Import Pester module
Import-Module Pester -Force

Write-Host "Running NATS Manager PowerShell Tests" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Get test files
$testFiles = Get-ChildItem -Path $PSScriptRoot -Filter "*.Tests.ps1" | Where-Object { $_.Name -like $TestFile }

if (-not $testFiles) {
    Write-Host "No test files found matching pattern: $TestFile" -ForegroundColor Red
    exit 1
}

$testResults = @()

foreach ($testFile in $testFiles) {
    Write-Host "Running tests in: $($testFile.Name)" -ForegroundColor Yellow

    $testResult = Invoke-Pester -Path $testFile.FullName -PassThru -Quiet

    $testResults += $testResult

    if ($testResult.FailedCount -gt 0) {
        Write-Host "  Failed: $($testResult.FailedCount)" -ForegroundColor Red
        Write-Host "  Passed: $($testResult.PassedCount)" -ForegroundColor Green
    }
    else {
        Write-Host "  All tests passed: $($testResult.PassedCount)" -ForegroundColor Green
    }

    Write-Host ""
}

# Summary
$totalFailed = ($testResults | Measure-Object -Property FailedCount -Sum).Sum
$totalPassed = ($testResults | Measure-Object -Property PassedCount -Sum).Sum

Write-Host "Test Summary:" -ForegroundColor Cyan
Write-Host "=============" -ForegroundColor Cyan
Write-Host "Total Tests: $($totalFailed + $totalPassed)" -ForegroundColor White
Write-Host "Passed: $totalPassed" -ForegroundColor Green
Write-Host "Failed: $totalFailed" -ForegroundColor $(if ($totalFailed -eq 0) { 'Green' } else { 'Red' })

if ($totalFailed -gt 0) {
    exit 1
}
else {
    exit 0
}
