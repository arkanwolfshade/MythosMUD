# Apply Migration 019: PostgreSQL Anti-Patterns Fixes
# This script applies the migration to test/development databases
#
# Usage:
#   .\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_dev"
#   .\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_unit"
#   .\scripts\apply_019_postgresql_anti_patterns_fixes.ps1 -Database "mythos_e2e"

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Default parameter value requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Default parameter value requires plaintext conversion for SecureString parameter')]
param(
    [string]$DbHost = "localhost",
    [string]$Port = "5432",
    [string]$User = "postgres",
    [SecureString]$Password = (ConvertTo-SecureString "Cthulhu1" -AsPlainText -Force),
    [string]$Database = "mythos_dev",
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

Write-Host "=== Migration 019: PostgreSQL Anti-Patterns Fixes ===" -ForegroundColor Cyan
Write-Host ""

# Find psql executable
$psqlPath = Get-Command psql -ErrorAction SilentlyContinue
if (-not $psqlPath) {
    $commonPaths = @(
        "E:\Program Files\PostgreSQL\18\bin\psql.exe",
        "C:\Program Files\PostgreSQL\*\bin\psql.exe",
        "C:\Program Files (x86)\PostgreSQL\*\bin\psql.exe"
    )

    foreach ($path in $commonPaths) {
        $psqlFiles = Get-ChildItem -Path $path -ErrorAction SilentlyContinue
        if ($psqlFiles) {
            $psqlPath = $psqlFiles[0].FullName
            break
        }
    }

    if (-not $psqlPath) {
        Write-Host "[ERROR] psql not found. Please install PostgreSQL or specify the path." -ForegroundColor Red
        exit 1
    }
}
else {
    $psqlPath = $psqlPath.Path
}

Write-Host "[INFO] Using psql: $psqlPath" -ForegroundColor Cyan

# Set PostgreSQL password
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$env:PGPASSWORD = $plainPassword
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

# Get migration file path
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
$migrationFile = Join-Path $projectRoot "db\migrations\019_postgresql_anti_patterns_fixes.sql"

if (-not (Test-Path $migrationFile)) {
    Write-Host "[ERROR] Migration file not found: $migrationFile" -ForegroundColor Red
    exit 1
}

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

if ($DryRun) {
    Write-Host "[DRY RUN] Would apply migration to $Database" -ForegroundColor Yellow
    Write-Host "[DRY RUN] Migration file: $migrationFile" -ForegroundColor Yellow
    Write-Host "[DRY RUN] No changes will be made" -ForegroundColor Yellow
    exit 0
}

# Verify migration hasn't already been applied
Write-Host "[INFO] Checking if migration already applied..." -ForegroundColor Yellow
$checkQuery = @"
select
    case
        when exists (
            select 1
            from information_schema.columns
            where table_schema = 'public'
            and table_name = 'professions'
            and column_name = 'id'
            and is_identity = 'YES'
            and data_type = 'bigint'
        ) then 'applied'
        else 'not_applied'
    end as migration_status;
"@

$statusResult = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -t -c $checkQuery 2>&1 | Where-Object { $_ -match '\S' }
$statusResult = $statusResult.Trim()

if ($statusResult -eq "applied") {
    Write-Host "[INFO] Migration appears to already be applied (professions.id is already bigint identity)" -ForegroundColor Yellow
    Write-Host "[INFO] Migration script is idempotent - running again to verify..." -ForegroundColor Yellow
    Write-Host ""
}

# Apply migration
Write-Host "[INFO] Applying migration: 019_postgresql_anti_patterns_fixes.sql" -ForegroundColor Yellow
Write-Host ""

try {
    # Apply migration - capture both stdout and stderr
    $process = Start-Process -FilePath $psqlPath -ArgumentList @(
        "-h", $DbHost,
        "-p", $Port,
        "-U", $User,
        "-d", $Database,
        "-f", $migrationFile,
        "-v", "ON_ERROR_STOP=1"
    ) -NoNewWindow -Wait -PassThru -RedirectStandardOutput "temp_stdout_019.txt" -RedirectStandardError "temp_stderr_019.txt"

    $exitCode = $process.ExitCode
    $stdoutContent = Get-Content "temp_stdout_019.txt" -ErrorAction SilentlyContinue | Out-String
    $stderrContent = Get-Content "temp_stderr_019.txt" -ErrorAction SilentlyContinue | Out-String

    # Clean up temp files
    Remove-Item "temp_stdout_019.txt" -ErrorAction SilentlyContinue
    Remove-Item "temp_stderr_019.txt" -ErrorAction SilentlyContinue

    if ($exitCode -eq 0) {
        # Check stderr for warnings (NOTICE messages are normal)
        if ($stderrContent -and $stderrContent -notmatch '^NOTICE:') {
            Write-Host "[WARNING] Migration completed but had warnings:" -ForegroundColor Yellow
            Write-Host $stderrContent -ForegroundColor Yellow
        }
        Write-Host "[OK] Migration 019 applied successfully" -ForegroundColor Green
        Write-Host ""

        # Verify migration
        Write-Host "[INFO] Verifying migration..." -ForegroundColor Yellow
        $verifyQuery = @"
select
    table_name,
    column_name,
    data_type,
    is_identity
from information_schema.columns
where table_schema = 'public'
and table_name in (
    'professions',
    'lucidity_adjustment_log',
    'lucidity_exposure_state',
    'lucidity_cooldowns',
    'item_component_states',
    'npc_definitions',
    'npc_spawn_rules',
    'npc_relationships',
    'player_spells'
)
and column_name = 'id'
order by table_name;
"@

        $verifyResult = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -c $verifyQuery 2>&1
        Write-Host $verifyResult

        Write-Host ""
        Write-Host "[SUCCESS] Migration 019 completed and verified!" -ForegroundColor Green
    }
    else {
        Write-Host "[ERROR] Migration failed with exit code $exitCode" -ForegroundColor Red
        if ($stderrContent) {
            Write-Host "Error output:" -ForegroundColor Red
            Write-Host $stderrContent -ForegroundColor Red
        }
        if ($stdoutContent) {
            Write-Host "Standard output:" -ForegroundColor Yellow
            Write-Host $stdoutContent -ForegroundColor Yellow
        }
        exit 1
    }
}
catch {
    Write-Host "[ERROR] Error applying migration: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "=== Migration Complete ===" -ForegroundColor Cyan
