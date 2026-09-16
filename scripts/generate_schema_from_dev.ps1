#!/usr/bin/env pwsh
# Generate the schema-agnostic DDL baseline (db/schema.sql, #811) from mythos_dev.
#
# db/schema.sql is the single DDL source for all three environments (mythos_dev / mythos_unit /
# mythos_e2e) -- object names are unqualified, and the loader sets search_path to the target
# schema. This script strips the schema qualification pg_dump always emits, so the checked-in
# file stays schema-agnostic without a manual post-processing step.

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Password from DATABASE_URL requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Password from DATABASE_URL environment variable requires plaintext conversion for SecureString parameter')]
param(
    [string]$DB_HOST = "",
    [string]$DB_USER = "",
    [string]$DB_NAME = "",
    [SecureString]$DB_PASSWORD = $null,
    [string]$OUTPUT_FILE = "db/schema.sql"
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

Write-ColorOutput "Generating DDL from $DB_NAME..." "Green"

# Find pg_dump
$PgDump = $null
if (Get-Command pg_dump -ErrorAction SilentlyContinue) {
    $PgDump = "pg_dump"
}
else {
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
}
else {
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
    # dbmate owns this table (creates it itself on first `up`, #811) -- excluded so the
    # checked-in baseline doesn't drift every time someone regenerates after running migrations.
    "--exclude-table=${DB_NAME}.schema_migrations"
    "--file=$OUTPUT_FILE"
)

& $PgDump $pgDumpArgs

if ($LASTEXITCODE -ne 0) {
    Write-ColorOutput "Error: pg_dump failed" "Red"
    exit 1
}

# pg_dump 17+ emits "SET transaction_timeout = 0;" in its preamble, matching whatever GUCs the
# dumping server supports. CI installs postgresql-18 explicitly, but the runner's `service
# postgresql start` has been observed to bring up a different, older pre-installed cluster on
# port 5432 instead -- one that predates this GUC (added in PG17) and rejects it outright. Strip
# it so the exported DDL stays loadable regardless of which cluster actually answers on 5432.
(Get-Content $OUTPUT_FILE) | Where-Object { $_ -notmatch '^SET transaction_timeout = 0;$' } | Set-Content $OUTPUT_FILE

# Strip schema qualification (#811): pg_dump always emits "<schema>.<object>" and a
# DROP/CREATE SCHEMA + DROP/CREATE EXTENSION pgcrypto pair scoped to $DB_NAME. The checked-in
# file must be schema-agnostic -- the schema and pgcrypto already exist (see
# db/databases/databases.sql), and the loader sets search_path to whichever environment it's
# targeting, not necessarily $DB_NAME.
$lines = Get-Content $OUTPUT_FILE
$out = [System.Collections.Generic.List[string]]::new()
$i = 0
while ($i -lt $lines.Count) {
    $line = $lines[$i]
    $trimmed = $line.Trim()
    if ($trimmed -eq "DROP EXTENSION IF EXISTS pgcrypto;" -or $trimmed -eq "DROP SCHEMA IF EXISTS ${DB_NAME};" -or
        $trimmed -eq "SELECT pg_catalog.set_config('search_path', '', false);") {
        $i++
        continue
    }
    if ($trimmed -eq "-- Name: ${DB_NAME}; Type: SCHEMA; Schema: -; Owner: -") {
        while ($i -lt $lines.Count -and $lines[$i].Trim() -ne "CREATE SCHEMA ${DB_NAME};") { $i++ }
        $i++
        while ($i -lt $lines.Count -and $lines[$i].Trim() -eq "") { $i++ }
        continue
    }
    if ($trimmed -eq "-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: -") {
        while ($i -lt $lines.Count -and -not $lines[$i].Trim().StartsWith("CREATE EXTENSION IF NOT EXISTS pgcrypto")) { $i++ }
        $i++
        while ($i -lt $lines.Count -and $lines[$i].Trim() -eq "") { $i++ }
        continue
    }
    $out.Add($line)
    $i++
}
$text = ($out -join "`n") -replace "\b$([regex]::Escape($DB_NAME))\.", ""
Set-Content -Path $OUTPUT_FILE -Value $text -NoNewline

# Add header comment to the generated file
$headerComment = @"
-- MythosMUD schema (schema-agnostic; #811)
-- Generated from: $DB_NAME database
-- Generated on: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")
-- Generated by: scripts/generate_schema_from_dev.ps1
--
-- This is the single DDL source for all three environments (mythos_dev / mythos_unit /
-- mythos_e2e). Object names are unqualified -- the loader MUST ``SET search_path TO
-- <target_schema>;`` (or connect with that search_path already set) before running this file.
-- The target schema itself, and the pgcrypto extension, are created once by
-- db/databases/databases.sql -- this file does not create or drop them.
--
-- To regenerate: make schema changes in $DB_NAME, then run .\scripts\generate_schema_from_dev.ps1
--
-- SET statements for clean execution
SET client_min_messages = WARNING;

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
