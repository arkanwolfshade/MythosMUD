# Apply player_id UUID migration to mythos_dev and mythos_unit databases
# This script applies the migration to convert players.player_id from VARCHAR to UUID

param(
    [string]$DatabaseUrl = "postgresql://postgres:Cthulhu1@localhost:5432",
    [switch]$DryRun
)

Write-Host "Applying player_id UUID migration to databases..." -ForegroundColor Green

$databases = @("mythos_dev", "mythos_unit")
$migrationFile = "db/migrations/010_migrate_player_id_to_uuid.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "ERROR: Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

# Set PostgreSQL password for all psql commands
$env:PGPASSWORD = "Cthulhu1"

foreach ($db in $databases) {
    Write-Host "`nProcessing database: $db" -ForegroundColor Yellow

    if ($DryRun) {
        Write-Host "  [DRY RUN] Would apply migration to $db" -ForegroundColor Cyan
        continue
    }

    # Check if database exists
    $checkDb = "SELECT 1 FROM pg_database WHERE datname = '$db';"
    $dbExists = psql -U postgres -d postgres -t -c $checkDb 2>&1 | Out-String

    if ($LASTEXITCODE -ne 0) {
        Write-Host "  ERROR: Failed to check if database exists" -ForegroundColor Red
        Write-Host "  Make sure PostgreSQL is running and psql is in PATH" -ForegroundColor Yellow
        continue
    }

    if ([string]::IsNullOrWhiteSpace($dbExists.Trim())) {
        Write-Host "  WARNING: Database $db does not exist. Skipping..." -ForegroundColor Yellow
        continue
    }

    Write-Host "  Applying migration..." -ForegroundColor Cyan

    # Apply migration
    Get-Content $migrationFile | psql -U postgres -d $db

    if ($LASTEXITCODE -eq 0) {
        Write-Host "  [OK] Migration applied successfully to $db" -ForegroundColor Green

        # Verify the migration
        Write-Host "  Verifying migration..." -ForegroundColor Cyan
        $verifyQuery = "SELECT data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'players' AND column_name = 'player_id';"
        $result = psql -U postgres -d $db -t -c $verifyQuery 2>&1 | Out-String

        if ($result -match 'uuid') {
            Write-Host "  [OK] Verified: players.player_id is now UUID type" -ForegroundColor Green
        } else {
            Write-Host "  [WARNING] Verification failed. players.player_id type: $result" -ForegroundColor Yellow
        }
    } else {
        Write-Host "  [ERROR] Migration failed for $db" -ForegroundColor Red
        Write-Host "  Check PostgreSQL logs for details" -ForegroundColor Yellow
    }
}

Write-Host "`nMigration process completed." -ForegroundColor Green
