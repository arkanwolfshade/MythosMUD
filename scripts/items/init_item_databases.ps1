Param(
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$schemaPath = Join-Path $root "server\sql\items_schema.sql"
$seedPath = Join-Path $root "server\sql\items_seed_data.sql"

if (-not (Test-Path $schemaPath)) {
    Write-Error "Schema file not found at $schemaPath"
}

if (-not (Test-Path $seedPath)) {
    Write-Error "Seed file not found at $seedPath"
}

$targets = @(
    @{ Path = Join-Path $root "data\local\items\local_items.db"; ApplySeed = $true },
    @{ Path = Join-Path $root "data\e2e_test\items\e2e_items.db"; ApplySeed = $true },
    @{ Path = Join-Path $root "data\unit_test_test\items\unit_test_items.db"; ApplySeed = $true }
)

foreach ($target in $targets) {
    $dbPath = $target.Path
    $directory = Split-Path $dbPath -Parent

    if (-not (Test-Path $directory)) {
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
    }

    if (Test-Path $dbPath) {
        if ($Force) {
            Remove-Item $dbPath -Force
        }
        else {
            Write-Host "Skipping existing database: $dbPath (use -Force to recreate)"
            continue
        }
    }

    Write-Host "Creating item database at $dbPath"
    sqlite3 $dbPath ".read `"$schemaPath`""

    if ($target.ApplySeed) {
        sqlite3 $dbPath ".read `"$seedPath`""
    }
}

Write-Host "Item database initialization complete."
