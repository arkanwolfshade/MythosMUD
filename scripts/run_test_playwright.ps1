#!/usr/bin/env pwsh
# Run Playwright runtime E2E, then server integration tests only when Playwright succeeds.
# Ensures make test-playwright fails loudly when bootstrap or specs fail.

[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status output for operators')]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PytestArgs
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path $PSScriptRoot -Parent
Set-Location -LiteralPath $ProjectRoot

$ClientDir = Join-Path $ProjectRoot "client"
Write-Host "[INFO] Running Playwright runtime E2E (client/)..." -ForegroundColor Cyan
Set-Location -LiteralPath $ClientDir
npm run test:e2e:runtime
$playwrightExit = $LASTEXITCODE
Set-Location -LiteralPath $ProjectRoot

if ($playwrightExit -ne 0) {
    Write-Host "[ERROR] Playwright E2E failed (exit $playwrightExit). Integration tests were NOT run." -ForegroundColor Red
    Write-Host "[ERROR] See logs/e2e_test/bootstrap-errors.log and Playwright report under client/playwright-report/." -ForegroundColor Red
    exit $playwrightExit
}

Write-Host "[INFO] Playwright E2E passed; running server integration tests..." -ForegroundColor Cyan
& (Join-Path $ProjectRoot "scripts" "run_integration_tests_playwright.ps1") @PytestArgs
exit $LASTEXITCODE
