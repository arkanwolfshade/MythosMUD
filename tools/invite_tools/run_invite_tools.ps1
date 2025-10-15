#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Run MythosMUD invite management tools with proper environment setup.

.DESCRIPTION
    This script sets up the required environment variables and runs the invite tools.
    It should be run from the project root directory.

.PARAMETER Command
    The command to run: 'generate', 'generate_db', 'check', 'list', or 'count'

.PARAMETER InviteCode
    The invite code to check (only used with 'check' command)

.EXAMPLE
    .\tools\invite_tools\run_invite_tools.ps1 generate
    .\tools\invite_tools\run_invite_tools.ps1 check "Cthulhu"
    .\tools\invite_tools\run_invite_tools.ps1 list
#>

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('generate', 'generate_db', 'check', 'list', 'count')]
    [string]$Command,

    [Parameter(Mandatory = $false)]
    [string]$InviteCode
)

# Set required environment variables
$env:DATABASE_URL = "sqlite+aiosqlite:///./data/local/players/local_players.db"
$env:MYTHOSMUD_SECRET_KEY = "dev-secret-key-for-invite-generation"

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Run the appropriate command
switch ($Command) {
    'generate' {
        Write-Host "Generating invite codes using generate_invites.py..." -ForegroundColor Green
        python "$scriptDir\generate_invites.py"
    }
    'generate_db' {
        Write-Host "Generating invite codes using generate_invites_db.py..." -ForegroundColor Green
        python "$scriptDir\generate_invites_db.py"
    }
    'check' {
        if (-not $InviteCode) {
            Write-Host "Error: Invite code is required for 'check' command" -ForegroundColor Red
            Write-Host "Usage: .\run_invite_tools.ps1 check <invite_code>" -ForegroundColor Yellow
            exit 1
        }
        Write-Host "Checking invite code: $InviteCode" -ForegroundColor Green
        python "$scriptDir\check_invites.py" check $InviteCode
    }
    'list' {
        Write-Host "Listing all invite codes..." -ForegroundColor Green
        python "$scriptDir\check_invites.py" list
    }
    'count' {
        Write-Host "Counting invite codes..." -ForegroundColor Green
        python "$scriptDir\check_invites.py" count
    }
}

Write-Host "Command completed." -ForegroundColor Green
