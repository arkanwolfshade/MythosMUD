# NPC Sample Data Population Script (PowerShell)
# This script populates both production and test NPC databases with sample data

param(
    [switch]$TestOnly,
    [switch]$ProdOnly,
    [switch]$Help
)

if ($Help) {
    Write-Host "NPC Sample Data Population Script" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage:"
    Write-Host "  .\scripts\populate_npc_sample_data.ps1                 # Populate both databases"
    Write-Host "  .\scripts\populate_npc_sample_data.ps1 -TestOnly       # Only populate test database"
    Write-Host "  .\scripts\populate_npc_sample_data.ps1 -ProdOnly       # Only populate production database"
    Write-Host "  .\scripts\populate_npc_sample_data.ps1 -Help           # Show this help"
    Write-Host ""
    Write-Host "This script will populate the NPC databases with sample data including:"
    Write-Host "  - 10 NPC definitions (shopkeepers, quest givers, passive/aggressive mobs)"
    Write-Host "  - Spawn rules for different sub-zones and conditions"
    Write-Host "  - NPC relationships (allies, enemies, followers)"
    exit 0
}

Write-Host "🧙‍♂️ Populating NPC Sample Data..." -ForegroundColor Cyan
Write-Host ""

# Build the Python command
$pythonCmd = "python scripts/populate_npc_sample_data.py"

if ($TestOnly) {
    $pythonCmd += " --test-only"
    Write-Host "📝 Populating test database only" -ForegroundColor Yellow
}
elseif ($ProdOnly) {
    $pythonCmd += " --prod-only"
    Write-Host "🏭 Populating production database only" -ForegroundColor Yellow
}
else {
    Write-Host "📝 Populating both test and production databases" -ForegroundColor Yellow
}

Write-Host ""

# Execute the Python script
try {
    Invoke-Expression $pythonCmd

    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ NPC sample data population completed successfully!" -ForegroundColor Green
        Write-Host ""
        Write-Host "Sample data includes:" -ForegroundColor Cyan
        Write-Host "  • 2 Shopkeepers (Ezekiel Whateley, Madame Lavinia)" -ForegroundColor White
        Write-Host "  • 2 Quest Givers (Professor Armitage, Dr. Morgan)" -ForegroundColor White
        Write-Host "  • 3 Passive Mobs (Wandering Scholar, Sanitarium patient, Street Vendor)" -ForegroundColor White
        Write-Host "  • 3 Aggressive Mobs (Cultist, Deep One Hybrid, Nightgaunt)" -ForegroundColor White
        Write-Host "  • Spawn rules for different conditions and sub-zones" -ForegroundColor White
        Write-Host "  • NPC relationships (allies, enemies, followers)" -ForegroundColor White
    }
    else {
        Write-Host ""
        Write-Host "❌ NPC sample data population failed!" -ForegroundColor Red
        Write-Host "Check the error messages above for details." -ForegroundColor Yellow
        exit 1
    }
}
catch {
    Write-Host ""
    Write-Host "❌ Error running NPC sample data population script:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
    exit 1
}
