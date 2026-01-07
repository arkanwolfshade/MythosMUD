# Agent OS Setup Wrapper Script
# Equivalent to: curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/base.sh | bash -s -- --cursor
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for user-facing colored output
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'User-facing help text requires colored output')]

param(
    [switch]$Cursor,
    [switch]$ClaudeCode,
    [switch]$OverwriteInstructions,
    [switch]$OverwriteStandards,
    [switch]$OverwriteConfig,
    [switch]$Help
)

if ($Help) {
    Write-Host "Agent OS Setup Script" -ForegroundColor Green
    Write-Host "====================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor Yellow
    Write-Host "  .\scripts\agent_os_setup.ps1 [options]" -ForegroundColor White
    Write-Host ""
    Write-Host "Options:" -ForegroundColor Yellow
    Write-Host "  -Cursor              Enable Cursor support" -ForegroundColor White
    Write-Host "  -ClaudeCode          Enable Claude Code support" -ForegroundColor White
    Write-Host "  -OverwriteInstructions  Overwrite existing instruction files" -ForegroundColor White
    Write-Host "  -OverwriteStandards     Overwrite existing standards files" -ForegroundColor White
    Write-Host "  -OverwriteConfig        Overwrite existing config file" -ForegroundColor White
    Write-Host "  -Help                 Show this help message" -ForegroundColor White
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor Yellow
    Write-Host "  .\scripts\agent_os_setup.ps1 -Cursor" -ForegroundColor White
    Write-Host "  .\scripts\agent_os_setup.ps1 -Cursor -ClaudeCode" -ForegroundColor White
    Write-Host "  .\scripts\agent_os_setup.ps1 -Cursor -OverwriteInstructions" -ForegroundColor White
    Write-Host ""
    Write-Host "This script is equivalent to the bash command:" -ForegroundColor Cyan
    Write-Host "  curl -sSL https://raw.githubusercontent.com/buildermethods/agent-os/main/setup/base.sh | bash -s -- --cursor" -ForegroundColor White
    exit 0
}

# Default to Cursor if no options specified (matching the original command)
if (-not $Cursor -and -not $ClaudeCode -and -not $OverwriteInstructions -and -not $OverwriteStandards -and -not $OverwriteConfig) {
    $Cursor = $true
}

# Run the base installation script
$scriptPath = Join-Path $PSScriptRoot "install_agent_os.ps1"
& $scriptPath -Cursor:$Cursor -ClaudeCode:$ClaudeCode -OverwriteInstructions:$OverwriteInstructions -OverwriteStandards:$OverwriteStandards -OverwriteConfig:$OverwriteConfig
