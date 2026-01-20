# quick_metrics_check.ps1
$metrics = Invoke-RestMethod -Uri "http://localhost:54731/monitoring/memory-leaks"

Write-Host "=== Memory Leak Metrics ===" -ForegroundColor Cyan
Write-Host "Closed WebSockets: $($metrics.connection.closed_websockets_count)" -ForegroundColor $(if ($metrics.connection.closed_websockets_count -gt 5000) { "Red" } else { "Green" })
Write-Host "Active/Player Ratio: $($metrics.connection.active_to_player_ratio)" -ForegroundColor $(if ($metrics.connection.active_to_player_ratio -gt 2.0) { "Red" } else { "Green" })
Write-Host "Orphaned Connections: $($metrics.connection.orphaned_connections)" -ForegroundColor $(if ($metrics.connection.orphaned_connections -gt 10) { "Red" } else { "Green" })
Write-Host "Active Tasks: $($metrics.task.active_task_count)"
Write-Host "Orphaned Tasks: $($metrics.task.orphaned_task_count)" -ForegroundColor $(if ($metrics.task.orphaned_task_count -gt 5) { "Red" } else { "Green" })

if ($metrics.alerts.Count -gt 0) {
    Write-Host "`n⚠️ ALERTS:" -ForegroundColor Red
    $metrics.alerts | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
}
