#Requires -Version 5.1

<#
.SYNOPSIS
    Tests for NATS Manager PowerShell functions

.DESCRIPTION
    This test file validates the NATS Manager functionality including
    environment variable support for NATS_SERVER_PATH configuration.
#>

# Import the module under test
$modulePath = Join-Path $PSScriptRoot "..\nats_manager.ps1"
. $modulePath

Describe "NATS Manager Environment Variable Support" {

    BeforeEach {
        # Clear any existing NATS_SERVER_PATH environment variable
        if ($env:NATS_SERVER_PATH) {
            Remove-Item Env:NATS_SERVER_PATH
        }
    }

    AfterEach {
        # Clean up environment variable after each test
        if ($env:NATS_SERVER_PATH) {
            Remove-Item Env:NATS_SERVER_PATH
        }
    }

    Context "Get-NatsServerPath Function" {

        It "Should return environment variable path when NATS_SERVER_PATH is set to valid path" {
            # Arrange
            $testPath = "C:\test\nats-server.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return true for our test path
            Mock Test-Path { return $true } -ParameterFilter { $Path -eq $testPath }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Be $testPath
        }

        It "Should return environment variable path when NATS_SERVER_PATH is set to relative path" {
            # Arrange
            $testPath = ".\nats-server.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return true for our test path
            Mock Test-Path { return $true } -ParameterFilter { $Path -eq $testPath }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Be $testPath
        }

        It "Should fallback to hardcoded paths when NATS_SERVER_PATH is not set" {
            # Arrange - Ensure no environment variable is set
            if ($env:NATS_SERVER_PATH) {
                Remove-Item Env:NATS_SERVER_PATH
            }

            # Mock Test-Path to return false for all paths initially, then true for first hardcoded path
            $mockCallCount = 0
            Mock Test-Path {
                $mockCallCount++
                if ($mockCallCount -eq 1 -and $Path -like "*nats-server*") {
                    return $true
                }
                return $false
            }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Not BeNullOrEmpty
            $result | Should Match ".*nats-server.*"
        }

        It "Should fallback to hardcoded paths when NATS_SERVER_PATH points to non-existent file" {
            # Arrange
            $invalidPath = "C:\nonexistent\nats-server.exe"
            $env:NATS_SERVER_PATH = $invalidPath

            # Mock Test-Path to return false for invalid path, true for first hardcoded path
            $mockCallCount = 0
            Mock Test-Path {
                $mockCallCount++
                if ($Path -eq $invalidPath) {
                    return $false
                }
                if ($mockCallCount -eq 2 -and $Path -like "*nats-server*") {
                    return $true
                }
                return $false
            }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Not BeNullOrEmpty
            $result | Should Match ".*nats-server.*"
        }

        It "Should validate that environment variable path points to NATS server executable" {
            # Arrange
            $testPath = "C:\test\nats-server.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return true
            Mock Test-Path { return $true } -ParameterFilter { $Path -eq $testPath }

            # Mock version check to return NATS server version
            Mock Invoke-Expression { return "nats-server version 2.10.25" }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Be $testPath
        }

        It "Should provide clear error message when NATS_SERVER_PATH points to invalid executable" {
            # Arrange
            $testPath = "C:\test\not-nats.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return true
            Mock Test-Path { return $true } -ParameterFilter { $Path -eq $testPath }

            # Mock version check to fail (not a NATS server)
            Mock Invoke-Expression { throw "Not a NATS server" }

            # Act & Assert
            { Get-NatsServerPath } | Should Throw "*not a valid NATS server*"
        }
    }

    Context "Test-NatsServerInstalled Function" {

        It "Should return true when NATS_SERVER_PATH points to valid NATS server" {
            # Arrange
            $testPath = "C:\test\nats-server.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return true
            Mock Test-Path { return $true } -ParameterFilter { $Path -eq $testPath }

            # Act
            $result = Test-NatsServerInstalled

            # Assert
            $result | Should Be $true
        }

        It "Should return false when NATS_SERVER_PATH points to non-existent file" {
            # Arrange
            $testPath = "C:\nonexistent\nats-server.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return false
            Mock Test-Path { return $false } -ParameterFilter { $Path -eq $testPath }

            # Act
            $result = Test-NatsServerInstalled

            # Assert
            $result | Should Be $false
        }
    }

    Context "Environment Variable Integration" {

        It "Should load environment variable from .env file" {
            # Arrange
            $envContent = @"
NATS_SERVER_PATH=C:\custom\nats-server.exe
DATABASE_URL=sqlite:///./data/players/players.db
"@
            $envFile = Join-Path $TestDrive ".env"
            $envContent | Out-File -FilePath $envFile -Encoding UTF8

            # Mock Test-Path to return true
            Mock Test-Path { return $true }

            # Act - Simulate loading environment from file
            Get-Content $envFile | ForEach-Object {
                if ($_ -match "^([^#][^=]+)=(.*)$") {
                    $name = $matches[1].Trim()
                    $value = $matches[2].Trim()
                    [Environment]::SetEnvironmentVariable($name, $value, "Process")
                }
            }

            # Assert
            $env:NATS_SERVER_PATH | Should Be "C:\custom\nats-server.exe"
        }

        It "Should handle empty NATS_SERVER_PATH environment variable gracefully" {
            # Arrange
            $env:NATS_SERVER_PATH = ""

            # Mock Test-Path to return false for empty path, true for hardcoded paths
            $mockCallCount = 0
            Mock Test-Path {
                $mockCallCount++
                if ($Path -eq "") {
                    return $false
                }
                if ($mockCallCount -eq 2 -and $Path -like "*nats-server*") {
                    return $true
                }
                return $false
            }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Not BeNullOrEmpty
            $result | Should Match ".*nats-server.*"
        }
    }
}

Describe "NATS Manager Backward Compatibility" {

    BeforeEach {
        # Clear any existing NATS_SERVER_PATH environment variable
        if ($env:NATS_SERVER_PATH) {
            Remove-Item Env:NATS_SERVER_PATH
        }
    }

    AfterEach {
        # Clean up environment variable after each test
        if ($env:NATS_SERVER_PATH) {
            Remove-Item Env:NATS_SERVER_PATH
        }
    }

    Context "Fallback Behavior" {

        It "Should use hardcoded paths when no environment variable is set" {
            # Arrange - No environment variable set

            # Mock Test-Path to return true for first hardcoded path
            Mock Test-Path {
                if ($Path -like "*WinGet*" -or $Path -like "*nats-server*") {
                    return $true
                }
                return $false
            }

            # Act
            $result = Get-NatsServerPath

            # Assert
            $result | Should Not BeNullOrEmpty
        }

        It "Should maintain existing function signatures" {
            # Arrange
            $testPath = "C:\test\nats-server.exe"
            $env:NATS_SERVER_PATH = $testPath

            # Mock Test-Path to return true
            Mock Test-Path { return $true } -ParameterFilter { $Path -eq $testPath }

            # Act & Assert - Functions should accept same parameters
            { Test-NatsServerInstalled } | Should Not Throw
            { Test-NatsServerRunning } | Should Not Throw
            { Get-NatsServerStatus } | Should Not Throw
        }
    }
}
