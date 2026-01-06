#!/usr/bin/env pwsh
# Suppress PSAvoidUsingWriteHost: This script uses Write-Host for status/output messages
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSAvoidUsingWriteHost', '', Justification = 'Status and output messages require Write-Host for proper display')]
<#
.SYNOPSIS
    Run comprehensive bug prevention tests for MythosMUD.

.DESCRIPTION
    This script runs the specific tests designed to catch the bugs we've encountered
    during development, including:
    - Event broadcasting bugs
    - Self-message exclusion issues
    - Chat buffer persistence
    - Event storm prevention
    - Connection timeout handling
    - UUID serialization issues

.PARAMETER TestType
    Type of tests to run: "server", "client", "integration", or "all" (default)

.PARAMETER Verbose
    Enable verbose output

.EXAMPLE
    .\run_bug_prevention_tests.ps1
    .\run_bug_prevention_tests.ps1 -TestType server
    .\run_bug_prevention_tests.ps1 -TestType all -Verbose
#>

# Suppress PSReviewUnusedParameter: Verbose is used in conditional logic for pytest verbosity
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSReviewUnusedParameter', 'Verbose', Justification = 'Parameter is used to control pytest verbosity via conditional logic')]
param(
    [ValidateSet("server", "client", "integration", "all")]
    [string]$TestType = "all",
    [switch]$Verbose
)

# Set error action preference
$ErrorActionPreference = "Stop"

# Colors for output
$Red = "`e[31m"
$Green = "`e[32m"
$Yellow = "`e[33m"
$Blue = "`e[34m"
$Reset = "`e[0m"

function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = $Reset
    )
    Write-Host "$Color$Message$Reset"
}

function Write-Header {
    param([string]$Title)
    Write-ColorOutput "`n$('=' * 60)" $Blue
    Write-ColorOutput "  $Title" $Blue
    Write-ColorOutput "$('=' * 60)" $Blue
}

function Write-Section {
    param([string]$Title)
    Write-ColorOutput "`n--- $Title ---" $Yellow
}

function Test-Command {
    param([string]$Command)
    try {
        Get-Command $Command -ErrorAction Stop | Out-Null
        return $true
    }
    catch {
        return $false
    }
}

function Invoke-ServerTest {
    Write-Section "Running Server-Side Bug Prevention Tests"

    # Check if we're in the right directory
    if (-not (Test-Path "server/tests/test_event_broadcasting_bugs.py")) {
        Write-ColorOutput "ERROR: Server test files not found. Run from project root." $Red
        return $false
    }

    # Activate virtual environment
    if (Test-Path ".venv/Scripts/Activate.ps1") {
        Write-ColorOutput "Activating virtual environment..." $Blue
        & .venv/Scripts/Activate.ps1
    }

    # Run specific bug prevention tests
    $testFiles = @(
        "server/tests/test_event_broadcasting_bugs.py",
        "server/tests/test_unresolved_bugs.py",
        "server/tests/test_integration_bug_prevention.py"
    )

    $allPassed = $true

    foreach ($testFile in $testFiles) {
        if (Test-Path $testFile) {
            Write-ColorOutput "Running $testFile..." $Blue

            $pytestArgs = @(
                "-v",
                "--tb=short",
                $testFile
            )

            if ($Verbose) {
                $pytestArgs += "-s"
            }

            try {
                python -m pytest @pytestArgs | Out-Null
                if ($LASTEXITCODE -eq 0) {
                    Write-ColorOutput "✓ $testFile passed" $Green
                }
                else {
                    Write-ColorOutput "✗ $testFile failed" $Red
                    $allPassed = $false
                }
            }
            catch {
                Write-ColorOutput "✗ Error running $testFile : $_" $Red
                $allPassed = $false
            }
        }
        else {
            Write-ColorOutput "Warning: $testFile not found" $Yellow
        }
    }

    return $allPassed
}

function Invoke-ClientTest {
    Write-Section "Running Client-Side Bug Prevention Tests"

    # Check if we're in the right directory
    if (-not (Test-Path "client/src/components/GameTerminalWithPanels.test.tsx")) {
        Write-ColorOutput "ERROR: Client test files not found. Run from project root." $Red
        return $false
    }

    # Check if Node.js is available
    if (-not (Test-Command "npm")) {
        Write-ColorOutput "ERROR: npm not found. Please install Node.js." $Red
        return $false
    }

    # Navigate to client directory
    Push-Location "client"

    try {
        # Install dependencies if needed
        if (-not (Test-Path "node_modules")) {
            Write-ColorOutput "Installing client dependencies..." $Blue
            npm install
        }

        # Run client tests
        Write-ColorOutput "Running client tests..." $Blue

        $testArgs = @("test")

        if ($Verbose) {
            $testArgs += "--reporter=verbose"
        }

        npm @testArgs | Out-Null
        $success = $LASTEXITCODE -eq 0

        if ($success) {
            Write-ColorOutput "✓ Client tests passed" $Green
        }
        else {
            Write-ColorOutput "✗ Client tests failed" $Red
        }

        return $success
    }
    catch {
        Write-ColorOutput "✗ Error running client tests: $_" $Red
        return $false
    }
    finally {
        Pop-Location
    }
}

function Invoke-IntegrationTest {
    Write-Section "Running Integration Tests"

    # Run the integration tests that simulate real scenarios
    $integrationTestFile = "server/tests/test_integration_bug_prevention.py"

    if (Test-Path $integrationTestFile) {
        Write-ColorOutput "Running integration tests..." $Blue

        # Activate virtual environment
        if (Test-Path ".venv/Scripts/Activate.ps1") {
            & .venv/Scripts/Activate.ps1
        }

        $pytestArgs = @(
            "-v",
            "--tb=short",
            "--timeout=30",
            $integrationTestFile
        )

        if ($Verbose) {
            $pytestArgs += "-s"
        }

        try {
            python -m pytest @pytestArgs | Out-Null
            $success = $LASTEXITCODE -eq 0

            if ($success) {
                Write-ColorOutput "✓ Integration tests passed" $Green
            }
            else {
                Write-ColorOutput "✗ Integration tests failed" $Red
            }

            return $success
        }
        catch {
            Write-ColorOutput "✗ Error running integration tests: $_" $Red
            return $false
        }
    }
    else {
        Write-ColorOutput "Warning: Integration test file not found" $Yellow
        return $true
    }
}

function Show-TestSummary {
    param(
        [bool]$ServerTestsPassed,
        [bool]$ClientTestsPassed,
        [bool]$IntegrationTestsPassed
    )

    Write-Header "Test Summary"

    $totalTests = 0
    $passedTests = 0

    if ($TestType -eq "all" -or $TestType -eq "server") {
        $totalTests++
        if ($ServerTestsPassed) { $passedTests++ }
        $status = if ($ServerTestsPassed) { "✓ PASSED" } else { "✗ FAILED" }
        $color = if ($ServerTestsPassed) { $Green } else { $Red }
        Write-ColorOutput "Server Tests: $status" $color
    }

    if ($TestType -eq "all" -or $TestType -eq "client") {
        $totalTests++
        if ($ClientTestsPassed) { $passedTests++ }
        $status = if ($ClientTestsPassed) { "✓ PASSED" } else { "✗ FAILED" }
        $color = if ($ClientTestsPassed) { $Green } else { $Red }
        Write-ColorOutput "Client Tests: $status" $color
    }

    if ($TestType -eq "all" -or $TestType -eq "integration") {
        $totalTests++
        if ($IntegrationTestsPassed) { $passedTests++ }
        $status = if ($IntegrationTestsPassed) { "✓ PASSED" } else { "✗ FAILED" }
        $color = if ($IntegrationTestsPassed) { $Green } else { $Red }
        Write-ColorOutput "Integration Tests: $status" $color
    }

    Write-ColorOutput "`nOverall: $passedTests/$totalTests test suites passed" $(if ($passedTests -eq $totalTests) { $Green } else { $Red })

    if ($passedTests -eq $totalTests) {
        Write-ColorOutput "`n🎉 All bug prevention tests passed! The fixes are working correctly." $Green
    }
    else {
        Write-ColorOutput "`n⚠️  Some tests failed. Review the output above for details." $Yellow
    }
}

# Main execution
Write-Header "MythosMUD Bug Prevention Test Suite"
Write-ColorOutput "Running tests to verify our bug fixes are working correctly..." $Blue

$serverTestsPassed = $true
$clientTestsPassed = $true
$integrationTestsPassed = $true

try {
    # Run tests based on type
    if ($TestType -eq "all" -or $TestType -eq "server") {
        $serverTestsPassed = Invoke-ServerTest
    }

    if ($TestType -eq "all" -or $TestType -eq "client") {
        $clientTestsPassed = Invoke-ClientTest
    }

    if ($TestType -eq "all" -or $TestType -eq "integration") {
        $integrationTestsPassed = Invoke-IntegrationTest
    }

    # Show summary
    Show-TestSummary -ServerTestsPassed $serverTestsPassed -ClientTestsPassed $clientTestsPassed -IntegrationTestsPassed $integrationTestsPassed

    # Exit with appropriate code
    $allPassed = $serverTestsPassed -and $clientTestsPassed -and $integrationTestsPassed
    exit $(if ($allPassed) { 0 } else { 1 })
}
catch {
    Write-ColorOutput "`n❌ Unexpected error during test execution: $_" $Red
    exit 1
}
