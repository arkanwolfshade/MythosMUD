#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Clean Log Files for MythosMUD

.DESCRIPTION
    This script removes all *.log files from the logs directory and its subdirectories.
    As noted in the restricted archives of Miskatonic University, maintaining clean
    log files is essential for preventing the corruption of temporal signatures
    and ensuring proper system operation.

.PARAMETER DryRun
    Show what would be deleted without actually deleting files

.PARAMETER Confirm
    Skip confirmation prompt and delete files immediately

.EXAMPLE
    .\clean_logs.ps1
    Shows what files would be deleted and asks for confirmation

.EXAMPLE
    .\clean_logs.ps1 -DryRun
    Shows what files would be deleted without making changes

.EXAMPLE
    .\clean_logs.ps1 -Confirm
    Deletes all log files without asking for confirmation

.NOTES
    Author: MythosMUD Development Team
    Version: 1.0
    Requires: PowerShell 5.1 or higher
#>

[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(HelpMessage = "Show what would be deleted without making changes")]
    [switch]$DryRun,

    [Parameter(HelpMessage = "Skip confirmation prompt")]
    [switch]$Confirm
)

# Get the script directory and project root
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
$LogsPath = Join-Path $ProjectRoot "logs"

Write-Host "MythosMUD Log Cleanup Utility" -ForegroundColor Green
Write-Host "=============================" -ForegroundColor Green
Write-Host ""

# Check if logs directory exists
if (-not (Test-Path $LogsPath)) {
    Write-Host "❌ Logs directory not found at: $LogsPath" -ForegroundColor Red
    Write-Host "Please ensure you're running this script from the correct location." -ForegroundColor Yellow
    exit 1
}

Write-Host "📁 Scanning logs directory: $LogsPath" -ForegroundColor Cyan

# Find all .log files recursively
$LogFiles = Get-ChildItem -Path $LogsPath -Filter "*.log" -Recurse -File

if ($LogFiles.Count -eq 0) {
    Write-Host "✅ No .log files found in the logs directory" -ForegroundColor Green
    exit 0
}

Write-Host "📋 Found $($LogFiles.Count) .log files:" -ForegroundColor Yellow
Write-Host ""

# Group files by directory for better display
$FilesByDirectory = $LogFiles | Group-Object DirectoryName | Sort-Object Name

foreach ($DirectoryGroup in $FilesByDirectory) {
    $DirectoryName = $DirectoryGroup.Name
    $RelativePath = $DirectoryName.Replace($LogsPath, "logs")
    Write-Host "  📂 $RelativePath" -ForegroundColor Cyan

    foreach ($File in $DirectoryGroup.Group | Sort-Object Name) {
        $FileSize = [math]::Round($File.Length / 1KB, 2)
        Write-Host "    📄 $($File.Name) ($FileSize KB)" -ForegroundColor White
    }
    Write-Host ""
}

# Calculate total size
$TotalSize = ($LogFiles | Measure-Object -Property Length -Sum).Sum
$TotalSizeKB = [math]::Round($TotalSize / 1KB, 2)
$TotalSizeMB = [math]::Round($TotalSize / 1MB, 2)

Write-Host "📊 Total files: $($LogFiles.Count)" -ForegroundColor Yellow
Write-Host "📊 Total size: $TotalSizeKB KB ($TotalSizeMB MB)" -ForegroundColor Yellow
Write-Host ""

if ($DryRun) {
    Write-Host "🔍 Dry run mode - no files will be deleted" -ForegroundColor Cyan
    Write-Host "Run without -DryRun to actually delete these files" -ForegroundColor Gray
    exit 0
}

# Confirmation prompt
if (-not $Confirm) {
    Write-Host "⚠️  This will permanently delete all .log files in the logs directory!" -ForegroundColor Red
    Write-Host ""
    $Response = Read-Host "Are you sure you want to continue? (y/N)"

    if ($Response -notmatch '^[Yy]') {
        Write-Host "❌ Operation cancelled by user" -ForegroundColor Yellow
        exit 0
    }
}

Write-Host ""
Write-Host "🗑️  Deleting log files..." -ForegroundColor Cyan

$DeletedCount = 0
$ErrorCount = 0

foreach ($File in $LogFiles) {
    try {
        if ($PSCmdlet.ShouldProcess($File.FullName, "Delete")) {
            Remove-Item -Path $File.FullName -Force
            Write-Host "  ✅ Deleted: $($File.Name)" -ForegroundColor Green
            $DeletedCount++
        }
    }
    catch {
        Write-Host "  ❌ Failed to delete: $($File.Name) - $($_.Exception.Message)" -ForegroundColor Red
        $ErrorCount++
    }
}

Write-Host ""
Write-Host "📊 Cleanup Summary:" -ForegroundColor Yellow
Write-Host "  ✅ Files deleted: $DeletedCount" -ForegroundColor Green
if ($ErrorCount -gt 0) {
    Write-Host "  ❌ Errors: $ErrorCount" -ForegroundColor Red
}
Write-Host "  📁 Space freed: $TotalSizeKB KB ($TotalSizeMB MB)" -ForegroundColor Cyan

if ($ErrorCount -eq 0) {
    Write-Host ""
    Write-Host "🎉 Log cleanup completed successfully!" -ForegroundColor Green
    Write-Host "The temporal signatures have been cleansed, Professor Wolfshade." -ForegroundColor Gray
}
else {
    Write-Host ""
    Write-Host "⚠️  Log cleanup completed with errors" -ForegroundColor Yellow
    Write-Host "Some files could not be deleted. Check the error messages above." -ForegroundColor Gray
    exit 1
}
