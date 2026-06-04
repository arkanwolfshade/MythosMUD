# Run E2E runtime suite with parallel workers (opt-in isolation from serial default).
# Requires: server already running (e.g. ./scripts/start_local.ps1) and client dev on 127.0.0.1:5173
# Does NOT start webServer from playwright config in parallel mode.

$ErrorActionPreference = "Stop"
$env:E2E_RUNTIME_PARALLEL = "1"
if (-not $env:E2E_WORKERS) {
  $env:E2E_WORKERS = "2"
}

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location (Join-Path $repoRoot "client")

Write-Host "E2E_RUNTIME_PARALLEL=1, workers=$env:E2E_WORKERS"
Write-Host "Ensure server at http://127.0.0.1:54768 and Vite at http://127.0.0.1:5173 before running."

npx playwright test --config=tests/e2e/playwright.runtime.config.ts
