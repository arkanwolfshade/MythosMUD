# Apply all database migrations to mythos_e2e database
# This script applies all numbered migrations (002-014) in order

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Default parameter value requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Default parameter value requires plaintext conversion for SecureString parameter')]
param(
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [SecureString]$Password = (ConvertTo-SecureString "Cthulhu1" -AsPlainText -Force),
    [string]$Database = "mythos_e2e"
)

$ErrorActionPreference = "Stop"

# PostgreSQL psql executable path
$psqlPath = "E:\Program Files\PostgreSQL\18\bin\psql.exe"

if (-not (Test-Path $psqlPath)) {
    Write-Host "[ERROR] psql not found at: $psqlPath" -ForegroundColor Red
    Write-Host "Please update the psqlPath variable in this script to point to your PostgreSQL installation" -ForegroundColor Yellow
    exit 1
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
$migrationsDir = Join-Path $projectRoot "db\migrations"

# Set PostgreSQL password
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$env:PGPASSWORD = $plainPassword
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

# List of migrations to apply in order
$migrations = @(
    "002_add_hashed_password_column.sql",
    "003_add_used_by_user_id_column.sql",
    "004_rename_invites_columns.sql",
    "005_add_fastapi_users_columns.sql",
    "006_migrate_stats_to_jsonb.sql",
    "007_fix_professions_table_schema.sql",
    "008_increase_current_room_id_length.sql",
    "009_add_password_hash_column.sql",
    "010_migrate_player_id_to_uuid.sql",
    "012_create_containers_table.sql",  # Must be before 011
    "011_add_container_item_instance_id.sql",  # Depends on 012
    "013_add_map_coordinates_to_rooms.sql",
    "014_create_player_exploration_table.sql"
)

Write-Host "=== Applying Migrations to $Database ===" -ForegroundColor Cyan
Write-Host ""

# Check if database exists
Write-Host "[INFO] Checking if database exists..." -ForegroundColor Yellow
$dbExists = & $psqlPath -h $DbHost -p $Port -U $User -lqt | Select-String -Pattern "^\s*$Database\s"
if (-not $dbExists) {
    Write-Host "[ERROR] Database $Database does not exist!" -ForegroundColor Red
    Write-Host "Please create the database first or check the database name." -ForegroundColor Yellow
    exit 1
}
Write-Host "[OK] Database $Database exists" -ForegroundColor Green
Write-Host ""

$successCount = 0
$skipCount = 0
$errorCount = 0

foreach ($migration in $migrations) {
    $migrationFile = Join-Path $migrationsDir $migration

    if (-not (Test-Path $migrationFile)) {
        Write-Host "[WARN] Migration file not found: $migration" -ForegroundColor Yellow
        Write-Host "   Skipping..." -ForegroundColor Yellow
        $skipCount++
        continue
    }

    Write-Host "[INFO] Applying migration: $migration" -ForegroundColor Yellow

    try {
        # Apply migration - capture both stdout and stderr
        # NOTICE messages go to stderr but are not errors
        $process = Start-Process -FilePath $psqlPath -ArgumentList @("-h", $DbHost, "-p", $Port, "-U", $User, "-d", $Database, "-f", $migrationFile) -NoNewWindow -Wait -PassThru -RedirectStandardOutput "temp_stdout.txt" -RedirectStandardError "temp_stderr.txt"

        $exitCode = $process.ExitCode
        $stderrContent = Get-Content "temp_stderr.txt" -ErrorAction SilentlyContinue | Out-String

        # Clean up temp files
        Remove-Item "temp_stdout.txt" -ErrorAction SilentlyContinue
        Remove-Item "temp_stderr.txt" -ErrorAction SilentlyContinue

        if ($exitCode -eq 0) {
            # Check if stderr contains only NOTICE messages (which are not errors)
            $errorLines = $stderrContent -split "`n" | Where-Object { $_ -notmatch "^\s*$" -and $_ -notmatch "NOTICE:" -and $_ -notmatch "WARNING:" }

            if ($errorLines.Count -eq 0) {
                Write-Host "[OK] Migration $migration applied successfully" -ForegroundColor Green
                $successCount++
            }
            else {
                Write-Host "[ERROR] Migration $migration had errors" -ForegroundColor Red
                Write-Host $stderrContent -ForegroundColor Red
                $errorCount++
            }
        }
        else {
            Write-Host "[ERROR] Migration $migration failed with exit code $exitCode" -ForegroundColor Red
            if ($stderrContent) {
                Write-Host $stderrContent -ForegroundColor Red
            }
            $errorCount++
        }
    }
    catch {
        Write-Host "[ERROR] Error applying migration $migration : $_" -ForegroundColor Red
        $errorCount++
    }

    Write-Host ""
}

Write-Host "=== Migration Summary ===" -ForegroundColor Cyan
Write-Host "Successfully applied: $successCount" -ForegroundColor Green
Write-Host "Skipped (already applied): $skipCount" -ForegroundColor Cyan
Write-Host "Errors: $errorCount" -ForegroundColor $(if ($errorCount -eq 0) { "Green" } else { "Red" })

if ($errorCount -eq 0) {
    Write-Host ""
    Write-Host "[SUCCESS] All migrations completed!" -ForegroundColor Green

    # Verify key migrations
    Write-Host ""
    Write-Host "[INFO] Verifying key migrations..." -ForegroundColor Yellow
    $verifyQuery = @"
SELECT
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'containers') AS containers_exists,
    EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'player_exploration') AS player_exploration_exists,
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'rooms' AND column_name = 'map_x') AS map_x_exists,
    EXISTS (SELECT 1 FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'containers' AND column_name = 'container_item_instance_id') AS container_item_instance_id_exists;
"@

    $verifyResult = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -c $verifyQuery 2>&1
    Write-Host $verifyResult
}
else {
    Write-Host ""
    Write-Host "[WARNING] Some migrations failed. Please review the errors above." -ForegroundColor Yellow
    exit 1
}

$env:PGPASSWORD = $null
if ($plainPassword) {
    $plainPassword = $null
}
