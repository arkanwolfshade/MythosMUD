#Requires -Version 5.1

<#
.SYNOPSIS
    Tests for clean_logs.ps1 file matching.

.DESCRIPTION
    Regression coverage for the log-cleanup filter. clean_logs.ps1 originally used
    -Filter "*.log", which matches only files ENDING in .log. Both rotation forms produce
    siblings that do not:

      - size rotation (RotatingFileHandler):  server.log.1, server.log.2, server.log.3
      - startup rotation (rotate_log_files):  errors.log.2026_09_17_212459

    Those survived every cleanup run and then appeared in the next run's log directory,
    looking like current-run evidence. These tests pin the corrected matching.
#>

Describe "clean_logs.ps1 log file matching" {

    BeforeAll {
        $script:CleanLogsPath = Join-Path $PSScriptRoot "..\clean_logs.ps1"
        $script:TempLogRoot = Join-Path ([System.IO.Path]::GetTempPath()) "mythos_clean_logs_tests"
    }

    BeforeEach {
        if (Test-Path $script:TempLogRoot) {
            Remove-Item $script:TempLogRoot -Recurse -Force
        }
        $envDir = Join-Path $script:TempLogRoot "e2e_test"
        New-Item -ItemType Directory -Path $envDir -Force | Out-Null

        # One of each shape the real log directory contains.
        'x' | Set-Content (Join-Path $envDir "server.log")
        'x' | Set-Content (Join-Path $envDir "server.log.1")
        'x' | Set-Content (Join-Path $envDir "server.log.3")
        'x' | Set-Content (Join-Path $envDir "errors.log.2026_09_17_212459")
        'x' | Set-Content (Join-Path $envDir "audit_2026-09-17.jsonl")
    }

    AfterEach {
        if (Test-Path $script:TempLogRoot) {
            Remove-Item $script:TempLogRoot -Recurse -Force
        }
    }

    It "matches rotated and timestamp-archived logs, not just *.log" {
        $matched = @(Get-ChildItem -Path $script:TempLogRoot -Filter "*.log*" -Recurse -File |
                Select-Object -ExpandProperty Name)

        ($matched -contains "server.log") | Should Be $true
        ($matched -contains "server.log.1") | Should Be $true
        ($matched -contains "server.log.3") | Should Be $true
        ($matched -contains "errors.log.2026_09_17_212459") | Should Be $true
    }

    It "would have missed the rotated siblings with the old *.log filter" {
        $oldFilter = @(Get-ChildItem -Path $script:TempLogRoot -Filter "*.log" -Recurse -File |
                Select-Object -ExpandProperty Name)

        ($oldFilter -contains "server.log") | Should Be $true
        ($oldFilter -contains "server.log.1") | Should Be $false
        ($oldFilter -contains "errors.log.2026_09_17_212459") | Should Be $false
    }

    It "leaves non-log files alone" {
        $matched = @(Get-ChildItem -Path $script:TempLogRoot -Filter "*.log*" -Recurse -File |
                Select-Object -ExpandProperty Name)

        ($matched -contains "audit_2026-09-17.jsonl") | Should Be $false
    }

    It "uses a filter that covers rotated siblings" {
        # Guards the actual script: reverting to "*.log" silently reintroduces the bug.
        $content = Get-Content $script:CleanLogsPath -Raw
        $content | Should Match '-Filter "\*\.log\*"'
    }
}
