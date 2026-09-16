#!/usr/bin/env pwsh
# MythosMUD Schema Verification Script
# Verifies that the schema-agnostic baseline (db/schema.sql, #811) matches the current
# database structure, for whichever of mythos_dev/mythos_unit/mythos_e2e DATABASE_URL points at.

# Use Write-Output/Write-Error/Write-Warning instead of Write-Host for redirectability and Codacy compliance
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
# SchemaFile set after DbName is known (below)

if (Test-Path $EnvFile) {
    Write-Output "Loading environment from $EnvFile"
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
        Write-Output "Parsed DATABASE_URL: user=$DbUser, host=$DbHost, database=$DbName"
    }
}

# Single schema-agnostic baseline for all three environments (#811)
$allowedDbs = @("mythos_dev", "mythos_unit", "mythos_e2e")
if ($DbName -notin $allowedDbs) {
    Write-Output "Error: Database name must be one of: $($allowedDbs -join ', ')"
    exit 1
}
$SchemaFile = Join-Path $ProjectRoot "db\schema.sql"

Write-Output "Verifying schema match between $SchemaFile and $DbName..."

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
    Write-Output "Error: pg_dump is not installed or not in PATH. Please install PostgreSQL or add it to your PATH."
    exit 1
}

# Check if schema file exists
if (-not (Test-Path $SchemaFile)) {
    Write-Output "Error: Schema file not found: $SchemaFile"
    exit 1
}

# Check if database is accessible
$env:PGPASSWORD = $DbPassword
try {
    $pgIsready = if (Get-Command pg_isready -ErrorAction SilentlyContinue) {
        "pg_isready"
    }
    else {
        # Find pg_isready in same location as pg_dump
        $pgDumpDir = Split-Path -Parent $PgDump
        Join-Path $pgDumpDir "pg_isready.exe"
    }

    & $pgIsready -h $DbHost -U $DbUser -d $DbName 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Output "Error: Cannot connect to $DbName at ${DbHost}. Schema drift cannot be verified -- treating as failure, not a pass."
        exit 1
    }
}
catch {
    Write-Output "Error: Cannot connect to $DbName at ${DbHost}. Schema drift cannot be verified -- treating as failure, not a pass."
    exit 1
}

# Generate current schema from database
$TempSchema = [System.IO.Path]::GetTempFileName()

try {
    Write-Output "Extracting current schema from database..."

    $pgDumpArgs = @(
        "-h", $DbHost
        "-U", $DbUser
        "-d", $DbName
        "--schema-only"
        "--no-owner"
        "--no-privileges"
        "--clean"
        "--if-exists"
        # dbmate-owned (#811), and excluded from the checked-in baseline -- see generate_schema_from_dev.ps1.
        # Migration currency for mythos_dev is enforced separately, at server start
        # (scripts/start_server.ps1's Step 3.5) -- this exclusion is not a coverage gap.
        "--exclude-table=${DbName}.schema_migrations"
        "--file=$TempSchema"
    )

    & $PgDump $pgDumpArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Output "Error: Failed to extract schema from database"
        exit 1
    }

    # db/schema.sql is schema-agnostic (#811): unqualified object names. Strip the qualification
    # pg_dump always emits from the freshly-extracted copy before comparing, or every line would
    # show as drift.
    (Get-Content $TempSchema) -replace "\b$([regex]::Escape($DbName))\.", "" | Set-Content $TempSchema

    # Read and normalize both schema files for comparison
    # Remove comments, SET statements, pg_dump metadata commands, and empty lines, then sort
    $schemaContent = Get-Content $SchemaFile |
    Where-Object {
        $_ -notmatch '^\s*--' -and
        $_ -notmatch '^\s*SET\s+' -and
        $_ -notmatch '^\\restrict' -and
        $_ -notmatch '^\\unrestrict' -and
        $_ -notmatch '^CREATE SCHEMA ' -and
        $_ -notmatch '^CREATE EXTENSION IF NOT EXISTS pgcrypto' -and
        $_ -match '\S'
    } |
    Sort-Object

    $currentContent = Get-Content $TempSchema |
    Where-Object {
        $_ -notmatch '^\s*--' -and
        $_ -notmatch '^\s*SET\s+' -and
        $_ -notmatch '^\\restrict' -and
        $_ -notmatch '^\\unrestrict' -and
        $_ -notmatch '^CREATE SCHEMA ' -and
        $_ -notmatch '^CREATE EXTENSION IF NOT EXISTS pgcrypto' -and
        $_ -notmatch '^DROP EXTENSION IF EXISTS pgcrypto;$' -and
        $_ -notmatch '^DROP SCHEMA IF EXISTS ' -and
        $_ -notmatch "^SELECT pg_catalog\.set_config\('search_path'" -and
        $_ -match '\S'
    } |
    Sort-Object

    # Compare schemas
    $schemaText = $schemaContent -join "`n"
    $currentText = $currentContent -join "`n"

    if ($schemaText -eq $currentText) {
        Write-Output "[OK] Schema matches! $SchemaFile is up-to-date with $DbName"
        exit 0
    }
    else {
        Write-Output "Error: Schema drift detected! The schema file does not match the current database structure. Regenerate the DDL file for $DbName (e.g. scripts/generate_schema_from_dev.ps1)."
        Write-Output ""
        Write-Output "Differences (first 20 lines):"

        # Use Compare-Object to show differences
        $diff = Compare-Object -ReferenceObject $schemaContent -DifferenceObject $currentContent | Select-Object -First 20
        foreach ($line in $diff) {
            $side = if ($line.SideIndicator -eq "<=") { "<" } else { ">" }
            $lineText = $line.InputObject.ToString()
            Write-Output ("{0} {1}" -f $side, $lineText)
        }

        exit 1
    }
}
finally {
    # Clean up temp file
    if (Test-Path $TempSchema) {
        Remove-Item $TempSchema -Force -ErrorAction SilentlyContinue
    }
}
