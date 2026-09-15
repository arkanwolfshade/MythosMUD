# Apply the #829 Arkham street-grid migration to target databases.
#
# The base DML already carries the rebuilt city, so a database loaded from scratch needs
# nothing here. This is for databases loaded BEFORE #829, which still hold the old
# 117-room Arkham: it converges them in place without the destructive world-seed reload,
# so players, items and quest state survive.
#
# The migration is idempotent and wrapped in a transaction - safe to re-run, and a
# failure leaves the database untouched.
#
# Usage:
#   .\scripts\apply_arkham_grid_migration.ps1 -TargetDbs mythos_dev
#   .\scripts\apply_arkham_grid_migration.ps1 -TargetDbs mythos_dev, mythos_e2e
#
# Regenerate the SQL with:
#   python scripts/gen_arkham_grid_migration.py --baseline <ref-before-829>

param(
    [string]$EnvFile,
    [string[]]$TargetDbs = @("mythos_dev")
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot

# Flatten in case TargetDbs was passed as a single comma-joined string.
if ($TargetDbs.Count -eq 1 -and $TargetDbs[0] -match ",") {
    $TargetDbs = $TargetDbs[0] -split "\s*,\s*"
}

if (-not $EnvFile) {
    $EnvFile = if ($TargetDbs | Where-Object { $_ -match "mythos_unit|mythos_e2e" }) {
        Join-Path $ProjectRoot ".env.unit_test"
    } else {
        Join-Path $ProjectRoot "env.local"
    }
}

if (-not (Test-Path $EnvFile)) { throw "env file not found: $EnvFile" }

# DATABASE_URL is where every other apply_*_migration.ps1 script gets its credentials
# (see apply_arena_migration.ps1, apply_coc_spells_migration.ps1). This script instead
# fell back to $env:POSTGRES_* / hardcoded defaults and never set $env:PGPASSWORD, so
# psql had no password and blocked on an interactive prompt with no terminal to answer
# it -- indistinguishable from a hang, since it never times out or errors on its own.
$envContent = Get-Content $EnvFile -Raw
if ($envContent -notmatch 'DATABASE_URL=(.+)') { throw "DATABASE_URL not found in $EnvFile" }
$databaseUrl = $matches[1].Trim()
if ($databaseUrl -notmatch 'postgresql\+?asyncpg?://([^:]+):([^@]+)@([^:]+):(\d+)/(.+)') {
    throw "invalid PostgreSQL URL format: $databaseUrl"
}
$UrlUser, $UrlPassword, $UrlHost, $UrlPort = $matches[1], $matches[2], $matches[3], $matches[4]

$PgHost = if ($env:POSTGRES_HOST) { $env:POSTGRES_HOST } else { $UrlHost }
$PgPort = if ($env:POSTGRES_PORT) { $env:POSTGRES_PORT } else { $UrlPort }
$PgUser = if ($env:POSTGRES_USER) { $env:POSTGRES_USER } else { $UrlUser }

$Psql = (Get-Command psql -ErrorAction SilentlyContinue).Source
if (-not $Psql) {
    $Psql = Get-ChildItem "C:\Program Files\PostgreSQL\*\bin\psql.exe" -ErrorAction SilentlyContinue |
        Sort-Object FullName -Descending | Select-Object -First 1 -ExpandProperty FullName
}
if (-not $Psql) { throw "psql not found on PATH or under C:\Program Files\PostgreSQL" }

Write-Host "Applying Arkham street-grid migration (#829)" -ForegroundColor Cyan
Write-Host "  psql:    $Psql"
Write-Host "  env:     $EnvFile"
Write-Host "  targets: $($TargetDbs -join ', ')"

$env:PGPASSWORD = $UrlPassword
try {
    foreach ($db in $TargetDbs) {
        # Schema name matches the database name, as elsewhere in this repo.
        $env_suffix = $db -replace "^mythos_", ""
        $sql = Join-Path $ProjectRoot "data/db/migrations/20260913_arkham_street_grid_$env_suffix.sql"
        if (-not (Test-Path $sql)) { throw "migration not found: $sql" }

        Write-Host "`nApplying to '$db' ..." -ForegroundColor Yellow
        & $Psql -h $PgHost -p $PgPort -U $PgUser -d $db -v ON_ERROR_STOP=1 -q -f $sql
        if ($LASTEXITCODE -ne 0) { throw "[ERROR] Failed to apply the Arkham grid migration to '$db'" }
        Write-Host "[OK] $db" -ForegroundColor Green
    }
}
finally {
    Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue
}

Write-Host "`nArkham street-grid migration complete." -ForegroundColor Cyan
