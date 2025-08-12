# MythosMUD Database Verification Script
# PowerShell script to verify both databases have the correct schema

Write-Host "Verifying MythosMUD databases..." -ForegroundColor Green

# Database paths
$prodDb = "../../data/players/players.db"
$testDb = "./tests/data/players/test_players.db"

# Required tables
$requiredTables = @("users", "players", "invites")

function Test-Database {
    param(
        [string]$dbPath,
        [string]$dbName
    )

    if (!(Test-Path $dbPath)) {
        Write-Host "❌ $dbName`: Database file does not exist at $dbPath" -ForegroundColor Red
        return $false
    }

    try {
        $tables = sqlite3 $dbPath ".tables" 2>$null
        if ($LASTEXITCODE -eq 0) {
            $tableList = $tables.Trim() -split '\s+'
            Write-Host "✅ $dbName`: $tableList" -ForegroundColor Green

            # Check for required tables
            $missing = @()
            foreach ($table in $requiredTables) {
                if ($table -notin $tableList) {
                    $missing += $table
                }
            }

            if ($missing.Count -gt 0) {
                Write-Host "❌ $dbName` missing tables: $missing" -ForegroundColor Red
                return $false
            } else {
                Write-Host "✅ $dbName` has all required tables" -ForegroundColor Green
                return $true
            }
        } else {
            Write-Host "❌ $dbName`: Error reading database" -ForegroundColor Red
            return $false
        }
    } catch {
        Write-Host "❌ $dbName`: Error - $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Test both databases
$prodOk = Test-Database $prodDb "Production Database"
$testOk = Test-Database $testDb "Test Database"

Write-Host "`n" + "="*50 -ForegroundColor Cyan
Write-Host "VERIFICATION SUMMARY" -ForegroundColor Cyan
Write-Host "="*50 -ForegroundColor Cyan

if ($prodOk -and $testOk) {
    Write-Host "🎉 All databases verified successfully!" -ForegroundColor Green
    Write-Host "Both databases contain: users, players, invites tables" -ForegroundColor Green
    exit 0
} else {
    Write-Host "❌ Database verification failed!" -ForegroundColor Red
    if (!$prodOk) {
        Write-Host "Production database needs attention" -ForegroundColor Yellow
    }
    if (!$testOk) {
        Write-Host "Test database needs attention" -ForegroundColor Yellow
    }
    exit 1
}
