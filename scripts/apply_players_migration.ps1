# Apply players table migration to align with SQLAlchemy model
# This script applies the migration to all databases (mythos_dev, mythos_unit, mythos_e2e)

param(
    [string]$Database = "all",  # "all", "mythos_dev", "mythos_unit", "mythos_e2e"
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [string]$Password = "Cthulhu1"
)

$ErrorActionPreference = "Stop"

# PostgreSQL psql executable path
$psqlPath = "E:\Program Files\PostgreSQL\18\bin\psql.exe"

if (-not (Test-Path $psqlPath)) {
    Write-Host "[ERROR] psql not found at: $psqlPath" -ForegroundColor Red
    exit 1
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent (Split-Path -Parent $scriptDir)
$migrationFile = Join-Path $projectRoot "db\migrations\migrate_players_to_correct_schema.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

$databases = @()
if ($Database -eq "all") {
    $databases = @("mythos_dev", "mythos_unit", "mythos_e2e")
}
else {
    $databases = @($Database)
}

$env:PGPASSWORD = $Password

foreach ($db in $databases) {
    Write-Host "`n[INFO] Applying migration to database: $db" -ForegroundColor Yellow

    try {
        # Check if database exists
        $dbExists = & $psqlPath -h $DbHost -p $Port -U $User -lqt | Select-String -Pattern "^\s*$db\s"
        if (-not $dbExists) {
            Write-Host "[WARN] Database $db does not exist. Skipping..." -ForegroundColor Yellow
            continue
        }

        # Apply migration
        Write-Host "   Executing migration SQL..." -ForegroundColor Cyan
        $result = Get-Content $migrationFile | & $psqlPath -h $DbHost -p $Port -U $User -d $db 2>&1

        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] Migration applied successfully to $db" -ForegroundColor Green
        }
        else {
            Write-Host "[ERROR] Migration failed for $db" -ForegroundColor Red
            Write-Host $result -ForegroundColor Red
            exit 1
        }
    }
    catch {
        Write-Host "[ERROR] Error applying migration to $db : $_" -ForegroundColor Red
        exit 1
    }
}

Write-Host "`n[SUCCESS] All migrations completed successfully!" -ForegroundColor Green
$env:PGPASSWORD = $null
