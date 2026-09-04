#Requires -Version 5.1
<#
.SYNOPSIS
  Sync graphify code-graph artifacts into the MythosMUD Obsidian LLM wiki vault.

.DESCRIPTION
  Regenerates the agent-crawlable community wiki (graphify export wiki) and copies
  it into data/MythosMUD-Obsidian/raw/graphify/ as immutable raw material for the
  Karpathy LLM wiki. Does NOT export one Obsidian note per graph node (too large).

.NOTES
  Human: refresh the vault's code-graph snapshot after graphify update.
  AI: run from repo root; never hand-edit raw/graphify/code-wiki afterward.
#>

[CmdletBinding()]
param(
    [switch]$SkipExport,
    [string]$RepoRoot = ""
)

$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
    $RepoRoot = Split-Path -Parent $PSScriptRoot
}

$vaultRaw = Join-Path $RepoRoot "data\MythosMUD-Obsidian\raw\graphify"
$codeWikiDest = Join-Path $vaultRaw "code-wiki"
$reportSrc = Join-Path $RepoRoot "graphify-out\GRAPH_REPORT.md"
$wikiSrc = Join-Path $RepoRoot "graphify-out\wiki"

if (-not (Test-Path (Join-Path $RepoRoot "graphify-out\graph.json"))) {
    throw "graphify-out/graph.json not found. Run graphify update . from the repo root first."
}

New-Item -ItemType Directory -Force -Path $vaultRaw | Out-Null

if (-not $SkipExport) {
    Write-Host "Exporting graphify community wiki..."
    Push-Location $RepoRoot
    try {
        & graphify export wiki
        if ($LASTEXITCODE -ne 0) {
            throw "graphify export wiki failed with exit code $LASTEXITCODE"
        }
    }
    finally {
        Pop-Location
    }
}

if (-not (Test-Path $wikiSrc)) {
    throw "Missing $wikiSrc after export."
}

Write-Host "Syncing wiki -> $codeWikiDest"
if (Test-Path $codeWikiDest) {
    Remove-Item -LiteralPath $codeWikiDest -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $codeWikiDest | Out-Null

# Robocopy exit codes 0-7 are success; 8+ are failures.
& robocopy $wikiSrc $codeWikiDest /E /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
$rc = $LASTEXITCODE
if ($rc -ge 8) {
    throw "robocopy failed with exit code $rc"
}
$global:LASTEXITCODE = 0

if (Test-Path $reportSrc) {
    Copy-Item -LiteralPath $reportSrc -Destination (Join-Path $vaultRaw "GRAPH_REPORT.md") -Force
    Write-Host "Synced GRAPH_REPORT.md"
}
else {
    Write-Warning "GRAPH_REPORT.md not found; skipped."
}

$stampPath = Join-Path $vaultRaw "SYNC_STAMP.md"
$stamp = @"
---
title: Graphify sync stamp
type: meta
updated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
---

# Graphify sync stamp

Last sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss K')

- Source wiki: ``graphify-out/wiki/``
- Destination: ``raw/graphify/code-wiki/``
- Report: ``raw/graphify/GRAPH_REPORT.md``

Regenerate with ``./scripts/sync_obsidian_graphify.ps1`` from the repo root.
"@
Set-Content -LiteralPath $stampPath -Value $stamp -Encoding utf8

$articleCount = (Get-ChildItem -LiteralPath $codeWikiDest -Filter *.md -File | Measure-Object).Count
Write-Host "Done. Synced $articleCount markdown articles into raw/graphify/code-wiki/."
Write-Host "Append a log entry in data/MythosMUD-Obsidian/log.md if this sync is meaningful."
