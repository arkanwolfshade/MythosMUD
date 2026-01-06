# Redis Configuration for MythosMUD
# This script provides Redis connection information and utilities

# Redis connection details
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
$WSL_IP = "172.28.79.204"
$Port = 6379
$Localhost = "localhost"

Write-Host "=== Redis Configuration for MythosMUD ===" -ForegroundColor Cyan
Write-Host "WSL Redis Server IP: $WSL_IP" -ForegroundColor Green
Write-Host "Redis Port: $Port" -ForegroundColor Green
Write-Host "Localhost Access: $Localhost" -ForegroundColor Green
Write-Host ""

# Test connections
Write-Host "Testing Redis connections..." -ForegroundColor Yellow

# Test WSL connection
$wslConnectionString = "$WSL_IP`:$Port"
Write-Host "Testing WSL connection ($wslConnectionString)..." -ForegroundColor White
$wslTest = Test-NetConnection -ComputerName $WSL_IP -Port $Port -WarningAction SilentlyContinue
if ($wslTest.TcpTestSucceeded) {
    Write-Host "✓ WSL connection successful" -ForegroundColor Green
} else {
    Write-Host "✗ WSL connection failed" -ForegroundColor Red
}

# Test localhost connection
$localhostConnectionString = "$Localhost`:$Port"
Write-Host "Testing localhost connection ($localhostConnectionString)..." -ForegroundColor White
$localhostTest = Test-NetConnection -ComputerName $Localhost -Port $Port -WarningAction SilentlyContinue
if ($localhostTest.TcpTestSucceeded) {
    Write-Host "✓ Localhost connection successful" -ForegroundColor Green
} else {
    Write-Host "✗ Localhost connection failed" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Connection Strings ===" -ForegroundColor Cyan
Write-Host "For Python (redis-py):" -ForegroundColor Yellow
$wslRedisUrl = "redis://$WSL_IP`:$Port"
$localhostRedisUrl = "redis://$Localhost`:$Port"
Write-Host "  $wslRedisUrl" -ForegroundColor White
Write-Host "  $localhostRedisUrl" -ForegroundColor White
Write-Host ""
Write-Host "For Node.js (ioredis):" -ForegroundColor Yellow
Write-Host "  $wslRedisUrl" -ForegroundColor White
Write-Host "  $localhostRedisUrl" -ForegroundColor White
Write-Host ""

# Function to get WSL IP (in case it changes)
function Get-WSLIP {
    $wslIP = wsl hostname -I
    return $wslIP.Trim()
}

Write-Host "=== Management Commands ===" -ForegroundColor Cyan
Write-Host "Start Redis in WSL: wsl sudo service redis-server start" -ForegroundColor White
Write-Host "Stop Redis in WSL: wsl sudo service redis-server stop" -ForegroundColor White
Write-Host "Restart Redis in WSL: wsl sudo service redis-server restart" -ForegroundColor White
Write-Host "Check Redis status: wsl sudo service redis-server status" -ForegroundColor White
Write-Host "Access Redis CLI: wsl redis-cli" -ForegroundColor White
Write-Host ""

Write-Host "=== Current WSL IP ===" -ForegroundColor Cyan
$currentWSLIP = Get-WSLIP
Write-Host "Current WSL IP: $currentWSLIP" -ForegroundColor Green
if ($currentWSLIP -ne $WSL_IP) {
    Write-Host "Note: WSL IP has changed from configured value!" -ForegroundColor Yellow
    Write-Host "Update the WSL_IP variable in this script if needed." -ForegroundColor Yellow
}
