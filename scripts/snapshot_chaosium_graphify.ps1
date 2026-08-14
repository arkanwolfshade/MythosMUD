#Requires -Version 5.1
<#
.SYNOPSIS
  Snapshot Chaosium CoC pack graphify reports into the Obsidian LLM wiki vault.

.DESCRIPTION
  Copies agent-generated GRAPH_REPORT.md (plus a thin MANIFEST.md) from each
  Chaosium pack's graphify-out/ into data/MythosMUD-Obsidian/raw/chaosium/<slug>/.
  Does NOT copy PDFs, graph.html, chunks, or text_extracts/. Does NOT touch wiki/.

.NOTES
  Human: run after /graphify on Chaosium packs; content commits live in data/.
  AI: parent-repo tooling only; durable content lands under the data submodule.
#>

[CmdletBinding()]
param(
    [string]$ChaosiumRoot = "",
    [string]$PackPath = "",
    [string]$RepoRoot = ""
)

$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
    $RepoRoot = Split-Path -Parent $PSScriptRoot
}

if (-not $ChaosiumRoot) {
    $ChaosiumRoot = Join-Path $env:USERPROFILE "Proton Drive\arkanwolfshade\My files\Chaosium"
}

$destRoot = Join-Path $RepoRoot "data\MythosMUD-Obsidian\raw\chaosium"
New-Item -ItemType Directory -Force -Path $destRoot | Out-Null

function Get-ChaosiumSlug {
    param([string]$Name)
    $slug = $Name.ToLowerInvariant()
    $slug = $slug -replace "[^\p{L}\p{Nd}]+", "-"
    $slug = $slug.Trim("-")
    if (-not $slug) { $slug = "pack" }
    return $slug
}

function Get-GraphCount {
    param([string]$GraphJsonPath)
    $nodes = 0
    $edges = 0
    if (-not (Test-Path -LiteralPath $GraphJsonPath)) {
        return @{ Nodes = $nodes; Edges = $edges }
    }
    try {
        $json = Get-Content -LiteralPath $GraphJsonPath -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($null -ne $json.nodes) { $nodes = @($json.nodes).Count }
        # NetworkX node-link JSON uses "links", not "edges"
        if ($null -ne $json.links) { $edges = @($json.links).Count }
        elseif ($null -ne $json.edges) { $edges = @($json.edges).Count }
    }
    catch {
        Write-Warning "Could not parse graph.json at $GraphJsonPath"
    }
    return @{ Nodes = $nodes; Edges = $edges }
}

function Get-HonestyNote {
    param([string]$ReportPath)
    if (-not (Test-Path -LiteralPath $ReportPath)) { return @() }
    $lines = Get-Content -LiteralPath $ReportPath -Encoding UTF8
    $notes = @()
    $head = $lines | Select-Object -First 60
    foreach ($line in $head) {
        $t = $line.Trim()
        if (-not $t) { continue }
        if ($t -match "(?i)(FINAL:|size.?cap|words?\s*=\s*0|partial extract|health warning|WARNING|fully scanned|not need a graph)") {
            $notes += $t
            if ($notes.Count -ge 6) { break }
        }
    }
    return $notes
}

function Export-PackSnapshot {
    param([System.IO.DirectoryInfo]$PackDir)

    $gout = Join-Path $PackDir.FullName "graphify-out"
    $graphJson = Join-Path $gout "graph.json"
    $reportSrc = Join-Path $gout "GRAPH_REPORT.md"

    if (-not (Test-Path -LiteralPath $graphJson)) {
        Write-Host "SKIP (no graph.json): $($PackDir.Name)"
        return $false
    }

    $slug = Get-ChaosiumSlug -Name $PackDir.Name
    $destDir = Join-Path $destRoot $slug
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null

    $counts = Get-GraphCount -GraphJsonPath $graphJson
    $honesty = @()
    if (Test-Path -LiteralPath $reportSrc) {
        Copy-Item -LiteralPath $reportSrc -Destination (Join-Path $destDir "GRAPH_REPORT.md") -Force
        $honesty = Get-HonestyNote -ReportPath $reportSrc
    }
    else {
        Write-Warning "Missing GRAPH_REPORT.md for $($PackDir.Name); writing MANIFEST only."
    }

    $stamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $honestyBlock = if ($honesty.Count -gt 0) {
        ($honesty | ForEach-Object { "- $_" }) -join "`n"
    }
    else {
        "- (none detected in report scan)"
    }

    $manifest = @"
# Chaosium graphify snapshot - $($PackDir.Name)

- pack_title: $($PackDir.Name)
- slug: $slug
- source_path: $($PackDir.FullName)
- nodes: $($counts.Nodes)
- edges: $($counts.Edges)
- snapshot_utc: $stamp
- artifacts: GRAPH_REPORT.md only (no PDFs / text_extracts / graph.html)

## Honesty notes

$honestyBlock
"@

    [System.IO.File]::WriteAllText(
        (Join-Path $destDir "MANIFEST.md"),
        $manifest,
        [System.Text.UTF8Encoding]::new($false)
    )
    Write-Host "OK $slug nodes=$($counts.Nodes) edges=$($counts.Edges)"
    return $true
}

$packs = @()
if ($PackPath) {
    if (-not (Test-Path -LiteralPath $PackPath)) {
        throw "PackPath not found: $PackPath"
    }
    $packs = @(Get-Item -LiteralPath $PackPath)
}
else {
    if (-not (Test-Path -LiteralPath $ChaosiumRoot)) {
        throw "ChaosiumRoot not found: $ChaosiumRoot"
    }
    $packs = @(Get-ChildItem -LiteralPath $ChaosiumRoot -Directory)
}

$ok = 0
foreach ($pack in $packs) {
    if (Export-PackSnapshot -PackDir $pack) { $ok++ }
}

Write-Host "Snapshotted $ok pack(s) into $destRoot"
