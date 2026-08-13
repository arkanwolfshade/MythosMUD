# Apply player_id UUID migration to mythos_dev and mythos_unit databases
# This script applies the migration to convert players.player_id from VARCHAR to UUID

param(
    [string]$DatabaseUrl = "postgresql://postgres:Cthulhu1@localhost:5432",
    [switch]$DryRun
)

Write-Output "Applying player_id UUID migration to databases..."

$databases = @("mythos_dev", "mythos_unit")
$migrationFile = "db/migrations/010_migrate_player_id_to_uuid.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Output "ERROR: Migration file not found: $migrationFile"
    exit 1
}

# Set PostgreSQL password for all psql commands
$env:PGPASSWORD = "Cthulhu1"

foreach ($db in $databases) {
    Write-Output "`nProcessing database: $db"

    if ($DryRun) {
        Write-Output "  [DRY RUN] Would apply migration to $db"
        continue
    }

    # Check if database exists
    $checkDb = "SELECT 1 FROM pg_database WHERE datname = '$db';"
    $dbExists = psql -U postgres -d postgres -t -c $checkDb 2>&1 | Out-String

    if ($LASTEXITCODE -ne 0) {
        Write-Output "  ERROR: Failed to check if database exists"
        Write-Output "  Make sure PostgreSQL is running and psql is in PATH"
        continue
    }

    if ([string]::IsNullOrWhiteSpace($dbExists.Trim())) {
        Write-Output "  WARNING: Database $db does not exist. Skipping..."
        continue
    }

    Write-Output "  Applying migration..."

    # Apply migration
    Get-Content $migrationFile | psql -U postgres -d $db

    if ($LASTEXITCODE -eq 0) {
        Write-Output "  [OK] Migration applied successfully to $db"

        # Verify the migration
        Write-Output "  Verifying migration..."
        $verifyQuery = "SELECT data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'players' AND column_name = 'player_id';"
        $result = psql -U postgres -d $db -t -c $verifyQuery 2>&1 | Out-String

        if ($result -match 'uuid') {
            Write-Output "  [OK] Verified: players.player_id is now UUID type"
        } else {
            Write-Output "  [WARNING] Verification failed. players.player_id type: $result"
        }
    } else {
        Write-Output "  [ERROR] Migration failed for $db"
        Write-Output "  Check PostgreSQL logs for details"
    }
}

Write-Output "`nMigration process completed."
