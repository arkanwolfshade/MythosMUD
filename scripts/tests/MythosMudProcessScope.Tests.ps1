#Requires -Version 5.1

<#
.SYNOPSIS
    Tests for MythosMudProcessScope.ps1 repository root resolution.
#>

Describe "MythosMudProcessScope" {

    $scopePath = Join-Path $PSScriptRoot "..\MythosMudProcessScope.ps1"
    . $scopePath

    It "Get-MythosMudRepoRoot returns the repo root (parent of scripts/)" {
        # This test file lives in scripts/tests/; MythosMudProcessScope.ps1 resolves from scripts/.
        $expected = (Get-Item -LiteralPath (Join-Path $PSScriptRoot "..\..")).FullName
        $result = Get-MythosMudRepoRoot
        $result | Should Be $expected
    }

    It "Test-MythosMudProjectProcess returns false for the current shell when path is unrelated" {
        $current = $PID
        Test-MythosMudProjectProcess -ProcessId $current | Should Be $false
    }

    It "Get-MythosMudProtectedDevToolPattern includes jcodemunch and modelcontextprotocol" {
        $s = Get-MythosMudProtectedDevToolPattern
        ($s -contains 'jcodemunch') | Should Be $true
        ($s -contains 'modelcontextprotocol') | Should Be $true
    }

    It "Get-MythosMudChildProcess skips a process whose parent PID was reused by a newer process" {
        $born = Get-Date '2026-11-20T13:00:00'
        Mock Get-CimInstance -ParameterFilter { $Filter -eq 'ProcessId = 42' } {
            [pscustomobject]@{ ProcessId = 42; CreationDate = $born }
        }
        Mock Get-CimInstance -ParameterFilter { $Filter -eq 'ParentProcessId = 42' } {
            [pscustomobject]@{ ProcessId = 7600; CreationDate = $born.AddHours(-1) }  # started before PID 42 existed
            [pscustomobject]@{ ProcessId = 43; CreationDate = $born.AddSeconds(1) }
        }
        $children = @(Get-MythosMudChildProcess -ProcessId 42)
        $children.Count | Should Be 1
        $children[0].ProcessId | Should Be 43
    }
}
