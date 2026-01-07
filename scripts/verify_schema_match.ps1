#!/usr/bin/env pwsh
# MythosMUD Schema Verification Script
# Verifies that db/authoritative_schema.sql matches the current mythos_dev database structure

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir

# Load .env.local if it exists
$EnvFile = Join-Path $ProjectRoot ".env.local"
if (-not (Test-Path $EnvFile)) {
    $EnvFile = Join-Path $ProjectRoot ".env"
}

$DatabaseUrl = $null
$DbUser = "postgres"
$DbPassword = $null
$DbHost = "localhost"
$DbName = "mythos_dev"
$SchemaFile = Join-Path (Join-Path $ProjectRoot "db") "authoritative_schema.sql"

if (Test-Path $EnvFile) {
    Write-Host "Loading environment from $EnvFile" -ForegroundColor Cyan
    Get-Content $EnvFile | Where-Object {
        $_ -match '^\s*[^#]' -and $_ -match '='
    } | ForEach-Object {
        $key, $value = $_ -split '=', 2
        $key = $key.Trim()
        $value = $value.Trim()
        # Remove quotes if present
        # Remove quotes if present (both single and double)
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

# Parse DATABASE_URL if set
if ($script:DatabaseUrl) {
    # Handle both postgresql:// and postgresql+asyncpg:// formats
    $dbUrl = $DatabaseUrl -replace '^postgresql\+asyncpg://', '' -replace '^postgresql://', ''
    if ($dbUrl -match '^([^:]+):([^@]+)@([^:/]+)(:([0-9]+))?/(.+)$') {
        $DbUser = $matches[1]
        $DbPassword = $matches[2]
        $DbHost = $matches[3]
        # $DbPort is parsed but not used - PostgreSQL uses default port if not specified
        $DbName = $matches[6]
        Write-Host "Parsed DATABASE_URL: user=$DbUser, host=$DbHost, database=$DbName" -ForegroundColor Cyan
    }
}

Write-Host "Verifying schema match between $SchemaFile and $DbName..." -ForegroundColor Green

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
    Write-Host "Error: pg_dump is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install PostgreSQL or add it to your PATH" -ForegroundColor Yellow
    exit 1
}

# Check if schema file exists
if (-not (Test-Path $SchemaFile)) {
    Write-Host "Error: Schema file not found: $SchemaFile" -ForegroundColor Red
    Write-Host "Run ./scripts/generate_schema_from_dev.sh to generate it." -ForegroundColor Yellow
    exit 1
}

# Check if database is accessible
$env:PGPASSWORD = $DbPassword
try {
    $pgIsready = if (Get-Command pg_isready -ErrorAction SilentlyContinue) {
        "pg_isready"
    } else {
        # Find pg_isready in same location as pg_dump
        $pgDumpDir = Split-Path -Parent $PgDump
        Join-Path $pgDumpDir "pg_isready.exe"
    }

    & $pgIsready -h $DbHost -U $DbUser -d $DbName 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Warning: Cannot verify database connectivity." -ForegroundColor Yellow
        Write-Host "Schema file exists but cannot verify against database." -ForegroundColor Yellow
        exit 0
    }
} catch {
    Write-Host "Warning: Cannot verify database connectivity." -ForegroundColor Yellow
    Write-Host "Schema file exists but cannot verify against database." -ForegroundColor Yellow
    exit 0
}

# Generate current schema from database
$TempSchema = [System.IO.Path]::GetTempFileName()

try {
    Write-Host "Extracting current schema from database..." -ForegroundColor Green

    $pgDumpArgs = @(
        "-h", $DbHost
        "-U", $DbUser
        "-d", $DbName
        "--schema-only"
        "--no-owner"
        "--no-privileges"
        "--clean"
        "--if-exists"
        "--file=$TempSchema"
    )

    & $PgDump $pgDumpArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error: Failed to extract schema from database" -ForegroundColor Red
        exit 1
    }

    # Read and normalize both schema files for comparison
    # Remove comments, SET statements, pg_dump metadata commands, and empty lines, then sort
    $schemaContent = Get-Content $SchemaFile |
        Where-Object {
            $_ -notmatch '^\s*--' -and
            $_ -notmatch '^\s*SET\s+' -and
            $_ -notmatch '^\\restrict' -and
            $_ -notmatch '^\\unrestrict' -and
            $_ -match '\S'
        } |
        Sort-Object

    $currentContent = Get-Content $TempSchema |
        Where-Object {
            $_ -notmatch '^\s*--' -and
            $_ -notmatch '^\s*SET\s+' -and
            $_ -notmatch '^\\restrict' -and
            $_ -notmatch '^\\unrestrict' -and
            $_ -match '\S'
        } |
        Sort-Object

    # Compare schemas
    $schemaText = $schemaContent -join "`n"
    $currentText = $currentContent -join "`n"

    if ($schemaText -eq $currentText) {
        Write-Host "[OK] Schema matches! $SchemaFile is up-to-date with $DbName" -ForegroundColor Green
        exit 0
    } else {
        Write-Host "[ERROR] Schema drift detected!" -ForegroundColor Red
        Write-Host "The schema file does not match the current database structure." -ForegroundColor Yellow
        Write-Host "Run ./scripts/generate_schema_from_dev.sh to regenerate the schema file." -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Differences (first 20 lines):" -ForegroundColor Yellow

        # Use Compare-Object to show differences
        $diff = Compare-Object -ReferenceObject $schemaContent -DifferenceObject $currentContent | Select-Object -First 20
        foreach ($line in $diff) {
            $side = if ($line.SideIndicator -eq "<=") { "<" } else { ">" }
            $color = if ($line.SideIndicator -eq "<=") { "Red" } else { "Green" }
            $lineText = $line.InputObject.ToString()
            Write-Host ("{0} {1}" -f $side, $lineText) -ForegroundColor $color
        }

        exit 1
    }
} finally {
    # Clean up temp file
    if (Test-Path $TempSchema) {
        Remove-Item $TempSchema -Force -ErrorAction SilentlyContinue
    }
}
