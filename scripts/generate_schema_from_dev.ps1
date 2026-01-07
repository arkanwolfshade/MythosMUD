#!/usr/bin/env pwsh
# Generate authoritative database schema from mythos_dev PostgreSQL database
# This script extracts DDL from the mythos_dev database and writes it to db/authoritative_schema.sql

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Password from DATABASE_URL requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Password from DATABASE_URL environment variable requires plaintext conversion for SecureString parameter')]
param(
    [string]$DB_HOST = "",
    [string]$DB_USER = "",
    [string]$DB_NAME = "",
    [SecureString]$DB_PASSWORD = $null,
    [string]$OUTPUT_FILE = "db/authoritative_schema.sql"
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir

# Load .env.local if it exists
$EnvFile = Join-Path $ProjectRoot ".env.local"
if (-not (Test-Path $EnvFile)) {
    $EnvFile = Join-Path $ProjectRoot ".env"
}

$script:DatabaseUrl = $null

if (Test-Path $EnvFile) {
    Write-Host "Loading environment from $EnvFile" -ForegroundColor Cyan
    Get-Content $EnvFile | Where-Object {
        $_ -match '^\s*[^#]' -and $_ -match '='
    } | ForEach-Object {
        $key, $value = $_ -split '=', 2
        $key = $key.Trim()
        $value = $value.Trim()
        # Remove quotes if present
        if ($value.StartsWith('"') -and $value.EndsWith('"')) {
            $value = $value.Substring(1, $value.Length - 2)
        }
        if ($value.StartsWith("'") -and $value.EndsWith("'")) {
            $value = $value.Substring(1, $value.Length - 2)
        }

        if ($key -eq "DATABASE_URL") {
            $script:DatabaseUrl = $value
        }
    }
}

# Parse DATABASE_URL if set, otherwise use parameters or defaults
if ($script:DatabaseUrl) {
    # Handle both postgresql:// and postgresql+asyncpg:// formats
    $dbUrl = $script:DatabaseUrl -replace '^postgresql\+asyncpg://', '' -replace '^postgresql://', ''
    if ($dbUrl -match '^([^:]+):([^@]+)@([^:/]+)(:([0-9]+))?/(.+)$') {
        if (-not $DB_USER) { $DB_USER = $matches[1] }
        if (-not $DB_PASSWORD) {
            # Convert string password from URL to SecureString
            $DB_PASSWORD = ConvertTo-SecureString $matches[2] -AsPlainText -Force
        }
        if (-not $DB_HOST) { $DB_HOST = $matches[3] }
        if (-not $DB_NAME) { $DB_NAME = $matches[6] }
    }
}

# Set defaults if not provided
if (-not $DB_HOST) { $DB_HOST = "localhost" }
if (-not $DB_USER) { $DB_USER = "postgres" }
if (-not $DB_NAME) { $DB_NAME = "mythos_dev" }

function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

Write-ColorOutput "Generating authoritative schema from $DB_NAME..." "Green"

# Find pg_dump
$PgDump = $null
if (Get-Command pg_dump -ErrorAction SilentlyContinue) {
    $PgDump = "pg_dump"
} else {
    # Check common PostgreSQL installation paths
    $drives = @("C", "D", "E", "F")
    $versions = @("18", "17", "16", "15", "14", "13", "12")

    foreach ($drive in $drives) {
        foreach ($version in $versions) {
            $pgDumpPath = "${drive}:\Program Files\PostgreSQL\${version}\bin\pg_dump.exe"
            if (Test-Path $pgDumpPath) {
                $PgDump = $pgDumpPath
                break
            }
        }
        if ($PgDump) { break }
    }
}

if (-not $PgDump) {
    Write-ColorOutput "Error: pg_dump is not installed or not in PATH" "Red"
    Write-ColorOutput "Please install PostgreSQL or add it to your PATH" "Yellow"
    exit 1
}

# Check if database is accessible (optional check)
$pgIsready = if (Get-Command pg_isready -ErrorAction SilentlyContinue) {
    "pg_isready"
} else {
    # Find pg_isready in same location as pg_dump
    $pgDumpDir = Split-Path -Parent $PgDump
    Join-Path $pgDumpDir "pg_isready.exe"
}

if (Test-Path $pgIsready) {
    # Convert SecureString to plain text for environment variable
    if ($DB_PASSWORD) {
        $BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($DB_PASSWORD)
        $plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
        $env:PGPASSWORD = $plainPassword
        [System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
    }
    & $pgIsready -h $DB_HOST -U $DB_USER -d $DB_NAME 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-ColorOutput "Warning: Cannot verify database connectivity. Proceeding anyway..." "Yellow"
    }
    if ($plainPassword) {
        $plainPassword = $null
    }
}

# Create output directory if it doesn't exist
$outputDir = Split-Path -Parent $OUTPUT_FILE
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

# Generate schema dump
Write-ColorOutput "Running pg_dump..." "Green"

# Convert SecureString to plain text for environment variable
if ($DB_PASSWORD) {
    $BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($DB_PASSWORD)
    $plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
    $env:PGPASSWORD = $plainPassword
    [System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
}

$pgDumpArgs = @(
    "-h", $DB_HOST
    "-U", $DB_USER
    "-d", $DB_NAME
    "--schema-only"
    "--no-owner"
    "--no-privileges"
    "--clean"
    "--if-exists"
    "--file=$OUTPUT_FILE"
)

& $PgDump $pgDumpArgs

if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput "Error: pg_dump failed" "Red"
    exit 1
}

# Add header comment to the generated file
$headerComment = @"
-- Authoritative Database Schema
-- Generated from: $DB_NAME database
-- Generated on: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")
-- Generated by: scripts/generate_schema_from_dev.ps1
--
-- This file is the authoritative source of truth for the database schema.
-- It is generated directly from the mythos_dev database using pg_dump.
--
-- To regenerate this file:
--   1. Make schema changes in the mythos_dev database
--   2. Run: .\scripts\generate_schema_from_dev.ps1
--   3. Review the changes
--   4. Commit the updated file to git
--
-- SET statements for clean execution
SET client_min_messages = WARNING;
SET search_path = public;

"@

# Prepend header to the file
$tempFile = [System.IO.Path]::GetTempFileName()
$headerComment | Out-File -FilePath $tempFile -Encoding utf8 -NoNewline
Get-Content $OUTPUT_FILE -Raw | Add-Content -Path $tempFile
Move-Item -Path $tempFile -Destination $OUTPUT_FILE -Force

Write-ColorOutput "Schema generated successfully: $OUTPUT_FILE" "Green"
Write-ColorOutput "Please review the generated file before committing." "Yellow"

# Clean up password from memory
$env:PGPASSWORD = $null
if ($plainPassword) {
    $plainPassword = $null
}
