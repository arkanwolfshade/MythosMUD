# MythosMUD Worktree Manager
# A script to help manage our Git worktree setup

param(
    [Parameter(Mandatory = $false)]
    [ValidateSet("main", "client", "server", "docs", "testing", "list", "status", "cleanup")]
    [string]$Action = "list"
)

# Configuration
$ProjectRoot = "E:/projects/GitHub/MythosMUD"
$Worktrees = @{
    "main"    = "E:/projects/GitHub/MythosMUD"
    "client"  = "E:/projects/GitHub/MythosMUD-client"
    "server"  = "E:/projects/GitHub/MythosMUD-server"
    "docs"    = "E:/projects/GitHub/MythosMUD-docs"
    "testing" = "E:/projects/GitHub/MythosMUD-testing"
}

function Show-WorktreeStatus {
    Write-Host "`n=== MythosMUD Worktree Status ===" -ForegroundColor Cyan
    git worktree list
    Write-Host "`n=== Current Branch Status ===" -ForegroundColor Cyan
    git branch -v
}

function Switch-ToWorktree {
    param([string]$WorktreeName)

    if ($Worktrees.ContainsKey($WorktreeName)) {
        $Path = $Worktrees[$WorktreeName]
        if (Test-Path $Path) {
            Set-Location $Path
            Write-Host "Switched to $WorktreeName worktree: $Path" -ForegroundColor Green
            Write-Host "Current branch: $(git branch --show-current)" -ForegroundColor Yellow
        }
        else {
            Write-Host "Worktree path not found: $Path" -ForegroundColor Red
        }
    }
    else {
        Write-Host "Unknown worktree: $WorktreeName" -ForegroundColor Red
        Write-Host "Available worktrees: $($Worktrees.Keys -join ', ')" -ForegroundColor Yellow
    }
}

function Show-WorktreeInfo {
    param([string]$WorktreeName)

    if ($Worktrees.ContainsKey($WorktreeName)) {
        $Path = $Worktrees[$WorktreeName]
        if (Test-Path $Path) {
            Push-Location $Path
            Write-Host "`n=== $WorktreeName Worktree Information ===" -ForegroundColor Cyan
            Write-Host "Path: $Path" -ForegroundColor White
            Write-Host "Branch: $(git branch --show-current)" -ForegroundColor Yellow
            Write-Host "Status:" -ForegroundColor White
            git status --short
            Pop-Location
        }
        else {
            Write-Host "Worktree path not found: $Path" -ForegroundColor Red
        }
    }
    else {
        Write-Host "Unknown worktree: $WorktreeName" -ForegroundColor Red
    }
}

function Cleanup-LegacyBranches {
    Write-Host "`n=== Cleaning up legacy branches ===" -ForegroundColor Cyan

    # List branches to be cleaned up
    $LegacyBranches = @(
        "overall_cleanup",
        "arkhamcity_generation",
        "auth_tests",
        "feature/issue-62-configurable-game-tick-rate",
        "feature/room-pathing-validator",
        "realtime"
    )

    Write-Host "Legacy branches to consider for cleanup:" -ForegroundColor Yellow
    foreach ($branch in $LegacyBranches) {
        if (git branch --list $branch) {
            Write-Host "  - $branch" -ForegroundColor White
        }
    }

    Write-Host "`nNote: Use 'git branch -d <branch-name>' to delete merged branches" -ForegroundColor Cyan
    Write-Host "Use 'git branch -D <branch-name>' to force delete unmerged branches" -ForegroundColor Red
}

# Main execution
switch ($Action) {
    "list" {
        Show-WorktreeStatus
    }
    "status" {
        Show-WorktreeStatus
    }
    "main" {
        Switch-ToWorktree "main"
    }
    "client" {
        Switch-ToWorktree "client"
    }
    "server" {
        Switch-ToWorktree "server"
    }
    "docs" {
        Switch-ToWorktree "docs"
    }
    "testing" {
        Switch-ToWorktree "testing"
    }
    "cleanup" {
        Cleanup-LegacyBranches
    }
    default {
        Write-Host "`n=== MythosMUD Worktree Manager ===" -ForegroundColor Cyan
        Write-Host "Usage: .\worktree-manager.ps1 [-Action <action>]" -ForegroundColor White
        Write-Host "`nAvailable actions:" -ForegroundColor Yellow
        Write-Host "  list     - Show all worktrees and their status" -ForegroundColor White
        Write-Host "  status   - Show detailed status of all worktrees" -ForegroundColor White
        Write-Host "  main     - Switch to main worktree" -ForegroundColor White
        Write-Host "  client   - Switch to client worktree" -ForegroundColor White
        Write-Host "  server   - Switch to server worktree" -ForegroundColor White
        Write-Host "  docs     - Switch to docs worktree" -ForegroundColor White
        Write-Host "  testing  - Switch to testing worktree" -ForegroundColor White
        Write-Host "  cleanup  - Show legacy branches for cleanup" -ForegroundColor White
        Write-Host "`nExamples:" -ForegroundColor Yellow
        Write-Host "  .\worktree-manager.ps1 -Action client" -ForegroundColor White
        Write-Host "  .\worktree-manager.ps1 -Action status" -ForegroundColor White
    }
}

Write-Host "`n*'The proper organization of our eldritch knowledge allows for more efficient research.'*" -ForegroundColor Magenta
