#!/usr/bin/env pwsh
# MythosMUD Test Environment Setup Script
# Ensures all required test environment files exist before running tests

param(
    [switch]$Force,
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

# Get project root directory
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$TestEnvPath = Join-Path -Path $ProjectRoot -ChildPath "server" | Join-Path -ChildPath "tests" | Join-Path -ChildPath ".env.unit_test"
$ExampleEnvPath = Join-Path -Path $ProjectRoot -ChildPath "env.unit_test.example"

Write-Host "MythosMUD Test Environment Setup" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green

# Check if test environment file exists
if (Test-Path $TestEnvPath) {
    if ($Force) {
        Write-Host "[INFO] Force mode enabled - recreating test environment file" -ForegroundColor Yellow
    }
    else {
        Write-Host "[OK] Test environment file already exists: $TestEnvPath" -ForegroundColor Green
        Write-Host "[INFO] Use -Force to recreate the file" -ForegroundColor Cyan
        exit 0
    }
}

# Check if example file exists
if (-not (Test-Path $ExampleEnvPath)) {
    Write-Error "[ERROR] Example environment file not found: $ExampleEnvPath"
    Write-Host "[SOLUTION] Ensure env.unit_test.example exists in the project root" -ForegroundColor Red
    exit 1
}

# Create test environment file
try {
    Write-Host "[INFO] Creating test environment file..." -ForegroundColor Yellow
    Copy-Item $ExampleEnvPath $TestEnvPath -Force

    if (Test-Path $TestEnvPath) {
        Write-Host "[OK] Test environment file created successfully: $TestEnvPath" -ForegroundColor Green

        # Validate the created file
        $Content = Get-Content $TestEnvPath -Raw
        $RequiredVars = @(
            'SERVER_PORT=',
            'DATABASE_URL=',
            'DATABASE_NPC_URL=',
            'MYTHOSMUD_ADMIN_PASSWORD='
        )

        $MissingVars = @()
        foreach ($Var in $RequiredVars) {
            if ($Content -notmatch [regex]::Escape($Var)) {
                $MissingVars += $Var
            }
        }

        if ($MissingVars.Count -gt 0) {
            Write-Warning "[WARNING] Test environment file may be missing required variables: $($MissingVars -join ', ')"
        }
        else {
            Write-Host "[OK] Test environment file validation passed" -ForegroundColor Green
        }

        if ($Verbose) {
            Write-Host "[INFO] File contents:" -ForegroundColor Cyan
            Get-Content $TestEnvPath | Select-Object -First 10 | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
            Write-Host "  ... (truncated)" -ForegroundColor Gray
        }

    }
    else {
        Write-Error "[ERROR] Failed to create test environment file"
        exit 1
    }

}
catch {
    Write-Error "[ERROR] Failed to create test environment file: $_"
    exit 1
}

Write-Host ""
Write-Host "Test environment setup completed successfully!" -ForegroundColor Green
Write-Host "You can now run tests with: uv run pytest" -ForegroundColor Cyan
