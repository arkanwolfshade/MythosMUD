#!/usr/bin/env pwsh
# Monitors the extended idle memory soak (30m warmup + 2h measurement) and writes a report.

param(
    [int]$WarmupMinutes = 30,
    [int]$MeasureMinutes = 120,
    [int]$PollSeconds = 300,
    [string]$SamplePath = "",
    [string]$ReportPath = "",
    [string]$MonitorLog = ""
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path $PSScriptRoot -Parent
if (-not $SamplePath) {
    $SamplePath = Join-Path $repoRoot "logs/idle_memory_samples.post-queue-bound.jsonl"
}
if (-not $ReportPath) {
    $ReportPath = Join-Path $repoRoot "logs/idle_memory_post_queue_bound_report.txt"
}
if (-not $MonitorLog) {
    $MonitorLog = Join-Path $repoRoot "logs/idle_memory_post_queue_bound_monitor.log"
}
$analyzeScript = Join-Path $repoRoot "scripts/analyze_idle_memory_samples.py"

function Write-MonitorLog {
    param([string]$Message)
    $line = "$(Get-Date -Format o) $Message"
    Add-Content -Path $MonitorLog -Value $line
    Write-Host $line
}

$warmupSeconds = $WarmupMinutes * 60
$measureSeconds = $MeasureMinutes * 60
$totalSeconds = $warmupSeconds + $measureSeconds

Write-MonitorLog "Extended soak monitor started."
Write-MonitorLog "Warmup=${WarmupMinutes}m Measure=${MeasureMinutes}m Total=$([math]::Round($totalSeconds / 60))m"
Write-MonitorLog "Sample path: $SamplePath"

while (-not (Test-Path $SamplePath)) {
    Write-MonitorLog "Waiting for first sample..."
    Start-Sleep -Seconds 5
}

$firstSample = Get-Content $SamplePath -Head 1 | ConvertFrom-Json
$startedAt = [DateTimeOffset]::FromUnixTimeSeconds([int64][math]::Floor($firstSample.ts)).LocalDateTime
$endsAt = $startedAt.AddSeconds($totalSeconds)
Write-MonitorLog "Soak anchored to first sample at $($startedAt.ToString('o'))"
Write-MonitorLog "Expected completion: $($endsAt.ToString('o'))"

while ($true) {
    $elapsed = (Get-Date) - $startedAt
    $remaining = $endsAt - (Get-Date)
    $sampleCount = 0
    if (Test-Path $SamplePath) {
        $sampleCount = (Get-Content $SamplePath | Measure-Object -Line).Lines
    }

    $phase = if ($elapsed.TotalSeconds -lt $warmupSeconds) { "warmup" } else { "measure" }
    $elapsedMin = [math]::Floor($elapsed.TotalMinutes)
    $remainingMin = [math]::Ceiling($remaining.TotalMinutes)
    Write-MonitorLog "phase=$phase elapsed_min=$elapsedMin remaining_min=$remainingMin samples=$sampleCount"

    if ($remaining.TotalSeconds -le 0) {
        break
    }

    Start-Sleep -Seconds $PollSeconds
}

Write-MonitorLog "Soak complete. Running analysis..."
$analysis = & uv run python $analyzeScript $SamplePath 2>&1 | Out-String
$header = @(
    "Extended idle memory soak report (post-queue-bound)",
    "started_at=$($startedAt.ToString('o'))",
    "completed_at=$((Get-Date).ToString('o'))",
    "branch=$(git -C $repoRoot branch --show-current 2>$null)",
    ""
)
($header + $analysis.Trim()) | Set-Content -Path $ReportPath -Encoding utf8
Write-MonitorLog "Report written: $ReportPath"
