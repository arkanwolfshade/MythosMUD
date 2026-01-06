# Agent OS Installation Script for Windows PowerShell
# Equivalent to the bash setup script but adapted for PowerShell

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param(
    [switch]$Cursor,
    [switch]$ClaudeCode,
    [switch]$OverwriteInstructions,
    [switch]$OverwriteStandards,
    [switch]$OverwriteConfig
)

Write-Host "Agent OS Base Installation" -ForegroundColor Green
Write-Host "=============================" -ForegroundColor Green
Write-Host ""

# Set installation directory to current directory
$CURRENT_DIR = Get-Location
$INSTALL_DIR = Join-Path $CURRENT_DIR ".agent-os"
$BASE_URL = "https://raw.githubusercontent.com/buildermethods/agent-os/main"

Write-Host "The Agent OS base installation will be installed in the current directory ($CURRENT_DIR)" -ForegroundColor Yellow
Write-Host ""

Write-Host "Creating base directories..." -ForegroundColor Cyan
Write-Host ""

# Create directories
New-Item -ItemType Directory -Path $INSTALL_DIR -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $INSTALL_DIR "setup") -Force | Out-Null

# Function to download file from GitHub
function Save-WebFile {
    param(
        [string]$Url,
        [string]$Destination,
        [bool]$Overwrite = $false,
        [string]$Description = ""
    )

    if ((Test-Path $Destination) -and -not $Overwrite) {
        Write-Host "  [SKIP] $Description already exists - skipping" -ForegroundColor Yellow
        return $true
    }

    try {
        Invoke-WebRequest -Uri $Url -OutFile $Destination -UseBasicParsing
        if ($Overwrite) {
            Write-Host "  [OK] $Description (overwritten)" -ForegroundColor Green
        }
        else {
            Write-Host "  [OK] $Description" -ForegroundColor Green
        }
        return $true
    }
    catch {
        Write-Host "  [ERROR] Failed to download $Description" -ForegroundColor Red
        return $false
    }
}

# Function to copy directory recursively
function Copy-DirectoryRecursive {
    param(
        [string]$Source,
        [string]$Destination,
        [bool]$Overwrite = $false
    )

    if (-not (Test-Path $Source)) {
        return $false
    }

    New-Item -ItemType Directory -Path $Destination -Force | Out-Null

    Get-ChildItem -Path $Source -Recurse -File | ForEach-Object {
        $relativePath = $_.FullName.Substring($Source.Length + 1)
        $destFile = Join-Path $Destination $relativePath
        $destDir = Split-Path $destFile -Parent

        New-Item -ItemType Directory -Path $destDir -Force | Out-Null

        if ((Test-Path $destFile) -and -not $Overwrite) {
            Write-Host "  [SKIP] $relativePath already exists - skipping" -ForegroundColor Yellow
        }
        else {
            Copy-Item $_.FullName $destFile -Force
            if ($Overwrite) {
                Write-Host "  [OK] $relativePath (overwritten)" -ForegroundColor Green
            }
            else {
                Write-Host "  [OK] $relativePath" -ForegroundColor Green
            }
        }
    }
}

# Function to install from GitHub
function Install-FromGitHub {
    param(
        [string]$TargetDir,
        [bool]$OverwriteInst,
        [bool]$OverwriteStd,
        [bool]$IncludeCommands = $true
    )

    # Create directories
    New-Item -ItemType Directory -Path (Join-Path $TargetDir "standards") -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $TargetDir "standards\code-style") -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $TargetDir "instructions") -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $TargetDir "instructions\core") -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $TargetDir "instructions\meta") -Force | Out-Null

    # Download instructions
    Write-Host ""
    Write-Host "Downloading instruction files to $TargetDir\instructions\" -ForegroundColor Cyan

    # Core instructions
    Write-Host "  Core instructions:" -ForegroundColor Yellow
    $coreFiles = @("plan-product", "post-execution-tasks", "create-spec", "create-tasks", "execute-tasks", "execute-task", "analyze-product")
    foreach ($file in $coreFiles) {
        $url = "$BASE_URL/instructions/core/$file.md"
        $dest = Join-Path $TargetDir "instructions\core\$file.md"
        Save-WebFile -Url $url -Destination $dest -Overwrite $OverwriteInst -Description "instructions/core/$file.md"
    }

    # Meta instructions
    Write-Host ""
    Write-Host "  Meta instructions:" -ForegroundColor Yellow
    $metaFiles = @("pre-flight", "post-flight")
    foreach ($file in $metaFiles) {
        $url = "$BASE_URL/instructions/meta/$file.md"
        $dest = Join-Path $TargetDir "instructions\meta\$file.md"
        Save-WebFile -Url $url -Destination $dest -Overwrite $OverwriteInst -Description "instructions/meta/$file.md"
    }

    # Download standards
    Write-Host ""
    Write-Host "Downloading standards files to $TargetDir\standards\" -ForegroundColor Cyan

    $standardsFiles = @{
        "tech-stack.md"     = "standards/tech-stack.md"
        "code-style.md"     = "standards/code-style.md"
        "best-practices.md" = "standards/best-practices.md"
    }

    foreach ($file in $standardsFiles.Keys) {
        $url = "$BASE_URL/standards/$file"
        $dest = Join-Path $TargetDir "standards\$file"
        Save-WebFile -Url $url -Destination $dest -Overwrite $OverwriteStd -Description $standardsFiles[$file]
    }

    # Download code-style subdirectory
    Write-Host ""
    Write-Host "Downloading code style files to $TargetDir\standards\code-style\" -ForegroundColor Cyan

    $codeStyleFiles = @("css-style", "html-style", "javascript-style")
    foreach ($file in $codeStyleFiles) {
        $url = "$BASE_URL/standards/code-style/$file.md"
        $dest = Join-Path $TargetDir "standards\code-style\$file.md"
        Save-WebFile -Url $url -Destination $dest -Overwrite $OverwriteStd -Description "standards/code-style/$file.md"
    }

    # Download commands (only if requested)
    if ($IncludeCommands) {
        Write-Host ""
        Write-Host "Downloading command files to $TargetDir\commands\" -ForegroundColor Cyan
        New-Item -ItemType Directory -Path (Join-Path $TargetDir "commands") -Force | Out-Null

        $commandFiles = @("plan-product", "create-spec", "create-tasks", "execute-tasks", "analyze-product")
        foreach ($cmd in $commandFiles) {
            $url = "$BASE_URL/commands/$cmd.md"
            $dest = Join-Path $TargetDir "commands\$cmd.md"
            Save-WebFile -Url $url -Destination $dest -Overwrite $OverwriteStd -Description "commands/$cmd.md"
        }
    }
}

# Download functions.sh to its permanent location
Write-Host "Downloading setup functions..." -ForegroundColor Cyan
Save-WebFile -Url "$BASE_URL/setup/functions.sh" -Destination (Join-Path $INSTALL_DIR "setup\functions.sh") -Overwrite $true -Description "setup/functions.sh"

Write-Host ""
Write-Host "Installing the latest version of Agent OS from the Agent OS GitHub repository..." -ForegroundColor Cyan

# Install /instructions, /standards, and /commands folders and files from GitHub
Install-FromGitHub -TargetDir $INSTALL_DIR -OverwriteInst $OverwriteInstructions -OverwriteStd $OverwriteStandards

# Download config.yml
Write-Host ""
Write-Host "Downloading configuration..." -ForegroundColor Cyan
Save-WebFile -Url "$BASE_URL/config.yml" -Destination (Join-Path $INSTALL_DIR "config.yml") -Overwrite $OverwriteConfig -Description "config.yml"

# Download setup/project.sh
Write-Host ""
Write-Host "Downloading project setup script..." -ForegroundColor Cyan
Save-WebFile -Url "$BASE_URL/setup/project.sh" -Destination (Join-Path $INSTALL_DIR "setup\project.sh") -Overwrite $true -Description "setup/project.sh"

# Handle Claude Code installation
if ($ClaudeCode) {
    Write-Host ""
    Write-Host "Downloading Claude Code agent templates..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Path (Join-Path $INSTALL_DIR "claude-code\agents") -Force | Out-Null

    # Download agents to base installation for project use
    Write-Host "  Agent templates:" -ForegroundColor Yellow
    $agents = @("context-fetcher", "date-checker", "file-creator", "git-workflow", "project-manager", "test-runner")
    foreach ($agent in $agents) {
        $url = "$BASE_URL/claude-code/agents/$agent.md"
        $dest = Join-Path $INSTALL_DIR "claude-code\agents\$agent.md"
        Save-WebFile -Url $url -Destination $dest -Overwrite $false -Description "claude-code/agents/$agent.md"
    }

    # Update config to enable claude_code
    $configPath = Join-Path $INSTALL_DIR "config.yml"
    if (Test-Path $configPath) {
        $content = Get-Content $configPath -Raw
        $content = $content -replace "enabled: false", "enabled: true"
        Set-Content $configPath $content
        Write-Host "  [OK] Claude Code enabled in configuration" -ForegroundColor Green
    }
}

# Handle Cursor installation
if ($Cursor) {
    Write-Host ""
    Write-Host "Enabling Cursor support..." -ForegroundColor Cyan

    # Only update config to enable cursor
    $configPath = Join-Path $INSTALL_DIR "config.yml"
    if (Test-Path $configPath) {
        $content = Get-Content $configPath -Raw
        $content = $content -replace "enabled: false", "enabled: true"
        Set-Content $configPath $content
        Write-Host "  [OK] Cursor enabled in configuration" -ForegroundColor Green
    }
}

# Success message
Write-Host ""
Write-Host "[SUCCESS] Agent OS base installation has been completed." -ForegroundColor Green
Write-Host ""

# Dynamic project installation command
$PROJECT_SCRIPT = Join-Path $INSTALL_DIR "setup\project.sh"
Write-Host "--------------------------------" -ForegroundColor Gray
Write-Host ""
Write-Host "To install Agent OS in a project, run:" -ForegroundColor Yellow
Write-Host ""
Write-Host "   cd <project-directory>" -ForegroundColor White
Write-Host "   $PROJECT_SCRIPT" -ForegroundColor White
Write-Host ""
Write-Host "--------------------------------" -ForegroundColor Gray
Write-Host ""
Write-Host "Base installation files installed to:" -ForegroundColor Yellow
Write-Host "   $INSTALL_DIR\instructions\      - Agent OS instructions" -ForegroundColor White
Write-Host "   $INSTALL_DIR\standards\         - Development standards" -ForegroundColor White
Write-Host "   $INSTALL_DIR\commands\          - Command templates" -ForegroundColor White
Write-Host "   $INSTALL_DIR\config.yml         - Configuration" -ForegroundColor White
Write-Host "   $INSTALL_DIR\setup\project.sh   - Project installation script" -ForegroundColor White

if ($ClaudeCode) {
    Write-Host "   $INSTALL_DIR\claude-code\agents\ - Claude Code agent templates" -ForegroundColor White
}

Write-Host ""
Write-Host "--------------------------------" -ForegroundColor Gray
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Customize your standards in $INSTALL_DIR\standards\" -ForegroundColor White
Write-Host ""
Write-Host "2. Configure project types in $INSTALL_DIR\config.yml" -ForegroundColor White
Write-Host ""
Write-Host "3. Navigate to a project directory and run: $PROJECT_SCRIPT" -ForegroundColor White
Write-Host ""
Write-Host "--------------------------------" -ForegroundColor Gray
Write-Host ""
Write-Host "Refer to the official Agent OS docs at:" -ForegroundColor Yellow
Write-Host "https://buildermethods.com/agent-os" -ForegroundColor White
Write-Host ""
Write-Host "Keep building!" -ForegroundColor Green
Write-Host ""
