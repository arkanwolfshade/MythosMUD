#Requires -Version 5.1
<#
.SYNOPSIS
    Project-scoped process identification for MythosMUD PowerShell tooling.

.DESCRIPTION
    Stops accidental termination of unrelated workloads (other repos, global NATS,
    other Python servers). A process is considered owned by THIS MythosMUD worktree
    only when its Win32_Process ExecutablePath or CommandLine contains the canonical
    repository root path for this scripts/ directory.

    Indexers and MCP tooling (jcodemunch, Model Context Protocol servers, Cursor plugin
    hosts) often include the repo path in the command line; those processes are never
    stopped even when they match the repo root (see Test-MythosMudProtectedDevToolProcess).

    Set MYTHOSMUD_REPO_ROOT to override the detected repo root when needed.

.NOTES
    Dot-source from scripts under the repo: . (Join-Path $PSScriptRoot 'MythosMudProcessScope.ps1')
#>

$script:MythosMudRepoRootResolved = $null

function Get-MythosMudProtectedDevToolPattern {
    [CmdletBinding()]
    param()

    # Lowercase; paths normalized to forward slashes before matching.
    # Keep specific enough to avoid matching MythosMUD app code unintentionally.
    return @(
        'jcodemunch'
        'jcodemunch-mcp'
        'modelcontextprotocol'
        'mcp-server'
        'mcp_server'
        '.cursor/plugins'
        '/mcps/'
        'cursor-public'
        'plugin-context7'
        'plugin-slack'
    )
}

function Test-MythosMudProtectedDevToolProcess {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, ParameterSetName = 'ById')]
        [int]$ProcessId,

        [Parameter(Mandatory = $true, ParameterSetName = 'ByProcess')]
        [Microsoft.Management.Infrastructure.CimInstance]$Win32Process
    )

    if ($PSCmdlet.ParameterSetName -eq 'ById') {
        if ($ProcessId -le 0) {
            return $false
        }
        try {
            $p = Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $ProcessId" -ErrorAction Stop
        }
        catch {
            return $false
        }
        if (-not $p) {
            return $false
        }
    }
    else {
        $p = $Win32Process
        if (-not $p) {
            return $false
        }
    }

    $chunks = @()
    foreach ($segment in @($p.ExecutablePath, $p.CommandLine)) {
        if (-not [string]::IsNullOrEmpty($segment)) {
            $chunks += $segment
        }
    }

    if ($chunks.Count -eq 0) {
        return $false
    }

    $hay = ($chunks -join "`0").ToLowerInvariant().Replace('\', '/')
    foreach ($sig in Get-MythosMudProtectedDevToolPattern) {
        if ($hay.Contains($sig)) {
            return $true
        }
    }

    return $false
}

function Get-MythosMudRepoRoot {
    [CmdletBinding()]
    param()

    if ($null -ne $script:MythosMudRepoRootResolved) {
        return $script:MythosMudRepoRootResolved
    }

    if ($env:MYTHOSMUD_REPO_ROOT -and (Test-Path -LiteralPath $env:MYTHOSMUD_REPO_ROOT)) {
        $script:MythosMudRepoRootResolved = (Get-Item -LiteralPath $env:MYTHOSMUD_REPO_ROOT).FullName
        return $script:MythosMudRepoRootResolved
    }

    $script:MythosMudRepoRootResolved = (Get-Item -LiteralPath (Join-Path $PSScriptRoot '..')).FullName
    return $script:MythosMudRepoRootResolved
}

function Test-MythosMudProjectProcess {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [int]$ProcessId
    )

    if ($ProcessId -le 0) {
        return $false
    }

    try {
        $p = Get-CimInstance -ClassName Win32_Process -Filter "ProcessId = $ProcessId" -ErrorAction Stop
    }
    catch {
        return $false
    }

    if (-not $p) {
        return $false
    }

    if (Test-MythosMudProtectedDevToolProcess -Win32Process $p) {
        return $false
    }

    $root = Get-MythosMudRepoRoot
    $rootLower = $root.ToLowerInvariant()

    foreach ($segment in @($p.ExecutablePath, $p.CommandLine)) {
        if ([string]::IsNullOrEmpty($segment)) {
            continue
        }
        if ($segment.ToLowerInvariant().Contains($rootLower)) {
            return $true
        }
    }

    return $false
}

function Stop-MythosMudProjectProcessTree {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [int]$ProcessId,

        [Parameter()]
        [switch]$SkipRootProjectValidation
    )

    if (-not $SkipRootProjectValidation) {
        if (Test-MythosMudProtectedDevToolProcess -ProcessId $ProcessId) {
            Write-Host (
                "Skipping PID ${ProcessId}: protected indexer/MCP/plugin process (never stop)"
            ) -ForegroundColor Yellow
            return
        }
        if (-not (Test-MythosMudProjectProcess -ProcessId $ProcessId)) {
            Write-Host (
                "Skipping PID ${ProcessId}: not owned by this MythosMUD repo ({0})" -f (Get-MythosMudRepoRoot)
            ) -ForegroundColor Yellow
            return
        }
    }

    if (-not $PSCmdlet.ShouldProcess("process tree for PID $ProcessId", "Stop")) {
        return
    }

    $forwardCommon = @{}
    foreach ($k in @(
            'WhatIf', 'Confirm', 'Verbose', 'Debug', 'ErrorAction', 'WarningAction', 'InformationAction'
        )) {
        if ($PSBoundParameters.ContainsKey($k)) {
            $forwardCommon[$k] = $PSBoundParameters[$k]
        }
    }

    try {
        $children = Get-CimInstance -ClassName Win32_Process -Filter "ParentProcessId = $ProcessId"

        foreach ($child in $children) {
            Stop-MythosMudProjectProcessTreeInternal @forwardCommon -ProcessId $child.ProcessId
        }

        Stop-Process -Id $ProcessId -Force
        Write-Host "Terminated process tree for PID: $ProcessId" -ForegroundColor Green
    }
    catch {
        Write-Host "Could not terminate process tree for PID: $ProcessId" -ForegroundColor Yellow
    }
}

function Stop-MythosMudProjectProcessTreeInternal {
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [int]$ProcessId
    )

    if (Test-MythosMudProtectedDevToolProcess -ProcessId $ProcessId) {
        Write-Verbose "Skipping nested PID ${ProcessId}: protected indexer/MCP/plugin process"
        return
    }

    try {
        $children = Get-CimInstance -ClassName Win32_Process -Filter "ParentProcessId = $ProcessId"

        foreach ($child in $children) {
            Stop-MythosMudProjectProcessTreeInternal @PSBoundParameters -ProcessId $child.ProcessId
        }

        if ($PSCmdlet.ShouldProcess("PID $ProcessId", "Stop-Process")) {
            Stop-Process -Id $ProcessId -Force
        }
        Write-Verbose "Terminated nested process PID: $ProcessId"
    }
    catch {
        Write-Verbose "Could not terminate nested PID: $ProcessId"
    }
}
