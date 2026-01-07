# Agent OS Project Installation Script for Windows PowerShell
# Equivalent to the bash project.sh script but adapted for PowerShell

# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
param(
    [switch]$Cursor,
    [switch]$ClaudeCode,
    [switch]$OverwriteInstructions,
    [switch]$OverwriteStandards,
    [switch]$NoBase,
    [string]$ProjectType = "default"
)

Write-Host "Agent OS Project Installation" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""

# Get project directory info
$CURRENT_DIR = Get-Location
$PROJECT_NAME = Split-Path $CURRENT_DIR -Leaf
$INSTALL_DIR = ".\.agent-os"

Write-Host "Installing Agent OS to this project's root directory ($PROJECT_NAME)" -ForegroundColor Yellow
Write-Host ""

# Determine if running from base installation or GitHub
if ($NoBase) {
    $IS_FROM_BASE = $false
    Write-Host "Installing directly from GitHub (no base installation)" -ForegroundColor Cyan
    # Set BASE_URL for GitHub downloads
    $BASE_URL = "https://raw.githubusercontent.com/buildermethods/agent-os/main"
} else {
    $IS_FROM_BASE = $true
    # Get the base Agent OS directory - it should be in the current directory
    $BASE_AGENT_OS = Join-Path (Get-Location) ".agent-os"
    Write-Host "Using Agent OS base installation at $BASE_AGENT_OS" -ForegroundColor Green
}

Write-Host ""
Write-Host "Creating project directories..." -ForegroundColor Cyan
Write-Host ""
New-Item -ItemType Directory -Path $INSTALL_DIR -Force | Out-Null

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
        } else {
            Write-Host "  [OK] $Description" -ForegroundColor Green
        }
        return $true
    }
    catch {
        Write-Host "  [ERROR] Failed to download $Description" -ForegroundColor Red
        return $false
    }
}

# Function to copy file
function Copy-File {
    param(
        [string]$Source,
        [string]$Destination,
        [bool]$Overwrite = $false,
        [string]$Description = ""
    )

    if ((Test-Path $Destination) -and -not $Overwrite) {
        Write-Host "  [SKIP] $Description already exists - skipping" -ForegroundColor Yellow
        return $true
    }

    if (Test-Path $Source) {
        Copy-Item $Source $Destination -Force
        if ($Overwrite) {
            Write-Host "  [OK] $Description (overwritten)" -ForegroundColor Green
        } else {
            Write-Host "  [OK] $Description" -ForegroundColor Green
        }
        return $true
    } else {
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
        } else {
            Copy-Item $_.FullName $destFile -Force
            if ($Overwrite) {
                Write-Host "  [OK] $relativePath (overwritten)" -ForegroundColor Green
            } else {
                Write-Host "  [OK] $relativePath" -ForegroundColor Green
            }
        }
    }
}

# Function to convert command file to Cursor .mdc format
function Convert-ToCursorRule {
    param(
        [string]$Source,
        [string]$Destination
    )

    if (Test-Path $Destination) {
        Write-Host "  [SKIP] $(Split-Path $Destination -Leaf) already exists - skipping" -ForegroundColor Yellow
        return
    }

    # Create the front-matter and append original content
    $frontMatter = @"
---
alwaysApply: false
---

"@

    $content = Get-Content $Source -Raw
    $frontMatter + $content | Set-Content $Destination
    Write-Host "  [OK] $(Split-Path $Destination -Leaf)" -ForegroundColor Green
}

# Function to install from GitHub
function Install-FromGitHub {
    param(
        [string]$TargetDir,
        [bool]$OverwriteInst,
        [bool]$OverwriteStd,
        [bool]$IncludeCommands = $false
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
        "tech-stack.md" = "standards/tech-stack.md"
        "code-style.md" = "standards/code-style.md"
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

# Configure tools and project type based on installation type
if ($IS_FROM_BASE) {
    # Auto-enable tools based on base config if no flags provided
    if (-not $ClaudeCode) {
        # Check if claude_code is enabled in base config
        $configPath = Join-Path $BASE_AGENT_OS "config.yml"
        if (Test-Path $configPath) {
            $content = Get-Content $configPath -Raw
            if ($content -match "claude_code:" -and $content -match "enabled: true") {
                $ClaudeCode = $true
                Write-Host "  [OK] Auto-enabling Claude Code support (from Agent OS config)" -ForegroundColor Green
            }
        }
    }

    if (-not $Cursor) {
        # Check if cursor is enabled in base config
        $configPath = Join-Path $BASE_AGENT_OS "config.yml"
        if (Test-Path $configPath) {
            $content = Get-Content $configPath -Raw
            if ($content -match "cursor:" -and $content -match "enabled: true") {
                $Cursor = $true
                Write-Host "  [OK] Auto-enabling Cursor support (from Agent OS config)" -ForegroundColor Green
            }
        }
    }

    # Read project type from config or use flag
    if ([string]::IsNullOrEmpty($ProjectType) -and (Test-Path (Join-Path $BASE_AGENT_OS "config.yml"))) {
        $configPath = Join-Path $BASE_AGENT_OS "config.yml"
        $content = Get-Content $configPath
        $defaultLine = $content | Where-Object { $_ -match "^default_project_type:" }
        if ($defaultLine) {
            $ProjectType = ($defaultLine -split ":", 2)[1].Trim()
        } else {
            $ProjectType = "default"
        }
    } elseif ([string]::IsNullOrEmpty($ProjectType)) {
        $ProjectType = "default"
    }

    Write-Host ""
    Write-Host "Using project type: $ProjectType" -ForegroundColor Cyan

    # Determine source paths based on project type
    $INSTRUCTIONS_SOURCE = ""
    $STANDARDS_SOURCE = ""

    if ($ProjectType -eq "default") {
        $INSTRUCTIONS_SOURCE = Join-Path $BASE_AGENT_OS "instructions"
        $STANDARDS_SOURCE = Join-Path $BASE_AGENT_OS "standards"
    } else {
        # Look up project type in config
        $configPath = Join-Path $BASE_AGENT_OS "config.yml"
        if (Test-Path $configPath) {
            $content = Get-Content $configPath
            $projectTypeSection = $false
            $instructionsPath = ""
            $standardsPath = ""

            foreach ($line in $content) {
                if ($line -match "^  $ProjectType`:") {
                    $projectTypeSection = $true
                } elseif ($projectTypeSection -and $line -match "instructions:") {
                    $instructionsPath = ($line -split ":", 2)[1].Trim()
                } elseif ($projectTypeSection -and $line -match "standards:") {
                    $standardsPath = ($line -split ":", 2)[1].Trim()
                    break
                } elseif ($projectTypeSection -and $line -match "^  [a-zA-Z]") {
                    break
                }
            }

            # Expand tilde in paths
            $INSTRUCTIONS_SOURCE = $instructionsPath -replace "~", $env:USERPROFILE
            $STANDARDS_SOURCE = $standardsPath -replace "~", $env:USERPROFILE

            # Check if paths exist
            if (-not (Test-Path $INSTRUCTIONS_SOURCE) -or -not (Test-Path $STANDARDS_SOURCE)) {
                Write-Host "  [WARNING] Project type '$ProjectType' paths not found, falling back to default instructions and standards" -ForegroundColor Yellow
                $INSTRUCTIONS_SOURCE = Join-Path $BASE_AGENT_OS "instructions"
                $STANDARDS_SOURCE = Join-Path $BASE_AGENT_OS "standards"
            }
        } else {
            Write-Host "  [WARNING] Project type '$ProjectType' not found in config, using default instructions and standards" -ForegroundColor Yellow
            $INSTRUCTIONS_SOURCE = Join-Path $BASE_AGENT_OS "instructions"
            $STANDARDS_SOURCE = Join-Path $BASE_AGENT_OS "standards"
        }
    }

    # Copy instructions and standards from determined sources
    Write-Host ""
    Write-Host "Installing instruction files to $INSTALL_DIR\instructions\" -ForegroundColor Cyan
    Copy-DirectoryRecursive -Source $INSTRUCTIONS_SOURCE -Destination (Join-Path $INSTALL_DIR "instructions") -Overwrite $OverwriteInstructions

    Write-Host ""
    Write-Host "Installing standards files to $INSTALL_DIR\standards\" -ForegroundColor Cyan
    Copy-DirectoryRecursive -Source $STANDARDS_SOURCE -Destination (Join-Path $INSTALL_DIR "standards") -Overwrite $OverwriteStandards
} else {
    # Running directly from GitHub - download from GitHub
    if ([string]::IsNullOrEmpty($ProjectType)) {
        $ProjectType = "default"
    }

    Write-Host "Using project type: $ProjectType (default when installing from GitHub)" -ForegroundColor Cyan

    # Install instructions and standards from GitHub (no commands folder needed)
    Install-FromGitHub -TargetDir $INSTALL_DIR -OverwriteInst $OverwriteInstructions -OverwriteStd $OverwriteStandards -IncludeCommands $false
}

# Handle Claude Code installation for project
if ($ClaudeCode) {
    Write-Host ""
    Write-Host "Installing Claude Code support..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Path ".\.claude\commands" -Force | Out-Null
    New-Item -ItemType Directory -Path ".\.claude\agents" -Force | Out-Null

    if ($IS_FROM_BASE) {
        # Copy from base installation
        Write-Host "  Commands:" -ForegroundColor Yellow
        $commands = @("plan-product", "create-spec", "create-tasks", "execute-tasks", "analyze-product")
        foreach ($cmd in $commands) {
            $source = Join-Path $BASE_AGENT_OS "commands\$cmd.md"
            $dest = ".\.claude\commands\$cmd.md"
            if (Test-Path $source) {
                Copy-File -Source $source -Destination $dest -Overwrite $false -Description "commands/$cmd.md"
            } else {
                Write-Host "  [WARNING] ${cmd}.md not found in base installation" -ForegroundColor Yellow
            }
        }

        Write-Host ""
        Write-Host "  Agents:" -ForegroundColor Yellow
        $agents = @("context-fetcher", "date-checker", "file-creator", "git-workflow", "project-manager", "test-runner")
        foreach ($agent in $agents) {
            $source = Join-Path $BASE_AGENT_OS "claude-code\agents\$agent.md"
            $dest = ".\.claude\agents\$agent.md"
            if (Test-Path $source) {
                Copy-File -Source $source -Destination $dest -Overwrite $false -Description "agents/$agent.md"
            } else {
                Write-Host "  [WARNING] ${agent}.md not found in base installation" -ForegroundColor Yellow
            }
        }
    } else {
        # Download from GitHub when using --no-base
        Write-Host "  Downloading Claude Code files from GitHub..." -ForegroundColor Cyan
        Write-Host ""
        Write-Host "  Commands:" -ForegroundColor Yellow
        $commands = @("plan-product", "create-spec", "create-tasks", "execute-tasks", "analyze-product")
        foreach ($cmd in $commands) {
            $url = "$BASE_URL/commands/$cmd.md"
            $dest = ".\.claude\commands\$cmd.md"
            Save-WebFile -Url $url -Destination $dest -Overwrite $false -Description "commands/$cmd.md"
        }

        Write-Host ""
        Write-Host "  Agents:" -ForegroundColor Yellow
        $agents = @("context-fetcher", "date-checker", "file-creator", "git-workflow", "project-manager", "test-runner")
        foreach ($agent in $agents) {
            $url = "$BASE_URL/claude-code/agents/$agent.md"
            $dest = ".\.claude\agents\$agent.md"
            Save-WebFile -Url $url -Destination $dest -Overwrite $false -Description "agents/$agent.md"
        }
    }
}

# Handle Cursor installation for project
if ($Cursor) {
    Write-Host ""
    Write-Host "Installing Cursor support..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Path ".\.cursor\rules" -Force | Out-Null

    Write-Host "  Rules:" -ForegroundColor Yellow

    if ($IS_FROM_BASE) {
        # Convert commands from base installation to Cursor rules
        $commands = @("plan-product", "create-spec", "create-tasks", "execute-tasks", "analyze-product")
        foreach ($cmd in $commands) {
            $source = Join-Path $BASE_AGENT_OS "commands\$cmd.md"
            $dest = ".\.cursor\rules\$cmd.mdc"
            if (Test-Path $source) {
                Convert-ToCursorRule -Source $source -Destination $dest
            } else {
                Write-Host "  [WARNING] ${cmd}.md not found in base installation" -ForegroundColor Yellow
            }
        }
    } else {
        # Download from GitHub and convert when using --no-base
        Write-Host "  Downloading and converting from GitHub..." -ForegroundColor Cyan
        $commands = @("plan-product", "create-spec", "create-tasks", "execute-tasks", "analyze-product")
        foreach ($cmd in $commands) {
            $tempFile = Join-Path $env:TEMP "$cmd.md"
            $url = "$BASE_URL/commands/$cmd.md"
            $dest = ".\.cursor\rules\$cmd.mdc"

            try {
                Invoke-WebRequest -Uri $url -OutFile $tempFile -UseBasicParsing
                if (Test-Path $tempFile) {
                    Convert-ToCursorRule -Source $tempFile -Destination $dest
                    Remove-Item $tempFile -Force
                }
            }
            catch {
                Write-Host "  [ERROR] Failed to download $cmd.md" -ForegroundColor Red
            }
        }
    }
}

# Success message
Write-Host ""
Write-Host "[SUCCESS] Agent OS has been installed in your project ($PROJECT_NAME)!" -ForegroundColor Green
Write-Host ""
Write-Host "Project-level files installed to:" -ForegroundColor Yellow
Write-Host "   .agent-os\instructions\    - Agent OS instructions" -ForegroundColor White
Write-Host "   .agent-os\standards\       - Development standards" -ForegroundColor White

if ($ClaudeCode) {
    Write-Host "   .claude\commands\          - Claude Code commands" -ForegroundColor White
    Write-Host "   .claude\agents\            - Claude Code specialized agents" -ForegroundColor White
}

if ($Cursor) {
    Write-Host "   .cursor\rules\             - Cursor command rules" -ForegroundColor White
}

Write-Host ""
Write-Host "--------------------------------" -ForegroundColor Gray
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host ""

if ($ClaudeCode) {
    Write-Host "Claude Code usage:" -ForegroundColor Cyan
    Write-Host "  /plan-product    - Set the mission & roadmap for a new product" -ForegroundColor White
    Write-Host "  /analyze-product - Set up the mission and roadmap for an existing product" -ForegroundColor White
    Write-Host "  /create-spec     - Create a spec for a new feature" -ForegroundColor White
    Write-Host "  /execute-tasks   - Build and ship code for a new feature" -ForegroundColor White
    Write-Host ""
}

if ($Cursor) {
    Write-Host "Cursor usage:" -ForegroundColor Cyan
    Write-Host "  @plan-product    - Set the mission & roadmap for a new product" -ForegroundColor White
    Write-Host "  @analyze-product - Set up the mission and roadmap for an existing product" -ForegroundColor White
    Write-Host "  @create-spec     - Create a spec for a new feature" -ForegroundColor White
    Write-Host "  @execute-tasks   - Build and ship code for a new feature" -ForegroundColor White
    Write-Host ""
}

Write-Host "--------------------------------" -ForegroundColor Gray
Write-Host ""
Write-Host "Refer to the official Agent OS docs at:" -ForegroundColor Yellow
Write-Host "https://buildermethods.com/agent-os" -ForegroundColor White
Write-Host ""
Write-Host "Keep building!" -ForegroundColor Green
Write-Host ""
