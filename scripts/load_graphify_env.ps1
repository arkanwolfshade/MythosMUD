#Requires -Version 5.1
<#
.SYNOPSIS
  Load Graphify Gemini credentials from .env.graphify.local into this process.

.DESCRIPTION
  Dot-source before graphify extract/label when GEMINI_API_KEY is not already set.
  Does not print secret values.
#>
[CmdletBinding()]
param(
    [string]$RepoRoot = ""
)

$ErrorActionPreference = "Stop"

if (-not $RepoRoot) {
    $RepoRoot = Split-Path -Parent $PSScriptRoot
}

$envFile = Join-Path $RepoRoot ".env.graphify.local"
if (-not (Test-Path -LiteralPath $envFile)) {
    throw @"
Missing $envFile
Copy env.graphify.example to .env.graphify.local and set GEMINI_API_KEY.
"@
}

Get-Content -LiteralPath $envFile | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) {
        return
    }
    $eq = $line.IndexOf("=")
    if ($eq -lt 1) {
        return
    }
    $name = $line.Substring(0, $eq).Trim()
    $value = $line.Substring($eq + 1).Trim().Trim('"').Trim("'")
    if ($name -match '^(GEMINI_API_KEY|GOOGLE_API_KEY)$' -and $value) {
        Set-Item -Path "Env:$name" -Value $value
    }
}

if (-not $env:GEMINI_API_KEY -and -not $env:GOOGLE_API_KEY) {
    throw "No GEMINI_API_KEY or GOOGLE_API_KEY found in $envFile"
}

Write-Host "Graphify env loaded (GEMINI_API_KEY set=$([bool]$env:GEMINI_API_KEY))."
