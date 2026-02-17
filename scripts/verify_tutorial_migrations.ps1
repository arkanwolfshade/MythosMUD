# Verify tutorial migrations (08 and 12) on mythos_dev and mythos_unit databases
# Migration 08: Adds tutorial_instance_id column to players table
# Migration 12: Adds tutorial bedroom room and room link

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
# Suppress PSAvoidUsingConvertToSecureStringWithPlainText: Default parameter value requires plaintext conversion
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingConvertToSecureStringWithPlainText', '', Justification = 'Default parameter value requires plaintext conversion for SecureString parameter')]
param(
    [string]$DbHost = "localhost",
    [int]$Port = 5432,
    [string]$User = "postgres",
    [SecureString]$Password = (ConvertTo-SecureString "Cthulhu1" -AsPlainText -Force)
)

$databases = @("mythos_dev", "mythos_unit")
$psqlPath = "psql"

# Convert SecureString password to plaintext for psql environment variable
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($Password)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
$env:PGPASSWORD = $plainPassword
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

# Colors for output
function Write-ColorOutput($Message, $ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    Write-Output $Message
    $host.UI.RawUI.ForegroundColor = $fc
}

function Test-Migration08($Database) {
    Write-Host "`n[CHECK] Migration 08: tutorial_instance_id column in players table" -ForegroundColor Cyan

    $query = @"
SELECT EXISTS (
    SELECT 1
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'players'
      AND column_name = 'tutorial_instance_id'
) AS column_exists;
"@

    $result = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -t -A -c $query 2>&1

    if ($LASTEXITCODE -ne 0) {
        Write-ColorOutput "[FAIL] Error checking migration 08: $result" "Red"
        return $false
    }

    $exists = $result.Trim()
    if ($exists -eq "t") {
        Write-ColorOutput "[PASS] Migration 08 applied - tutorial_instance_id column exists" "Green"
        return $true
    }
    else {
        Write-ColorOutput "[FAIL] Migration 08 NOT applied - tutorial_instance_id column missing" "Red"
        return $false
    }
}

function Test-Migration12($Database) {
    Write-Host "`n[CHECK] Migration 12: Tutorial bedroom room and room link" -ForegroundColor Cyan

    # Check for room by stable_id
    $roomQuery = @"
SELECT EXISTS (
    SELECT 1
    FROM rooms
    WHERE stable_id = 'earth_arkhamcity_sanitarium_room_tutorial_bedroom_001'
) AS room_exists;
"@

    $roomResult = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -t -A -c $roomQuery 2>&1

    if ($LASTEXITCODE -ne 0) {
        Write-ColorOutput "[FAIL] Error checking tutorial bedroom room: $roomResult" "Red"
        return $false
    }

    $roomExists = $roomResult.Trim()

    # Check for room link
    $linkQuery = @"
SELECT EXISTS (
    SELECT 1
    FROM room_links
    WHERE from_room_id = '0745a816-793c-5717-a8d9-bedb5bbe244d'::uuid
      AND direction = 'out'
) AS link_exists;
"@

    $linkResult = & $psqlPath -h $DbHost -p $Port -U $User -d $Database -t -A -c $linkQuery 2>&1

    if ($LASTEXITCODE -ne 0) {
        Write-ColorOutput "[FAIL] Error checking tutorial bedroom link: $linkResult" "Red"
        return $false
    }

    $linkExists = $linkResult.Trim()

    $allPassed = $true

    if ($roomExists -eq "t") {
        Write-ColorOutput "[PASS] Tutorial bedroom room exists" "Green"
    }
    else {
        Write-ColorOutput "[FAIL] Tutorial bedroom room missing" "Red"
        $allPassed = $false
    }

    if ($linkExists -eq "t") {
        Write-ColorOutput "[PASS] Tutorial bedroom exit link exists" "Green"
    }
    else {
        Write-ColorOutput "[FAIL] Tutorial bedroom exit link missing" "Red"
        $allPassed = $false
    }

    return $allPassed
}

# Main verification
Write-Host "`n========================================" -ForegroundColor Yellow
Write-Host "Verifying Tutorial Migrations" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Yellow

$overallSuccess = $true

foreach ($db in $databases) {
    Write-Host "`n--- Database: $db ---" -ForegroundColor Magenta

    $migration08Ok = Test-Migration08 -Database $db
    $migration12Ok = Test-Migration12 -Database $db

    if ($migration08Ok -and $migration12Ok) {
        Write-ColorOutput "`n[SUMMARY] $db : All migrations verified" "Green"
    }
    else {
        Write-ColorOutput "`n[SUMMARY] $db : Some migrations missing" "Red"
        $overallSuccess = $false
    }
}

Write-Host "`n========================================" -ForegroundColor Yellow
if ($overallSuccess) {
    Write-ColorOutput "All migrations verified successfully on all databases!" "Green"
}
else {
    Write-ColorOutput "Some migrations are missing. Please apply missing migrations." "Red"
    Write-Host "`nTo apply migrations:" -ForegroundColor Yellow
    Write-Host "  Migration 08: Get-Content data/db/migrations/08_add_tutorial_instance_id.sql | psql -h $DbHost -p $Port -U $User -d <database>" -ForegroundColor Cyan
    Write-Host "  Migration 12: Get-Content data/db/migrations/12_add_tutorial_bedroom_room.sql | psql -h $DbHost -p $Port -U $User -d <database>" -ForegroundColor Cyan
}
Write-Host "========================================`n" -ForegroundColor Yellow

# Clean up password from environment
Remove-Item Env:\PGPASSWORD -ErrorAction SilentlyContinue

if ($overallSuccess) {
    exit 0
}
else {
    exit 1
}
