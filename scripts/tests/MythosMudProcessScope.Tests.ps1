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
}
