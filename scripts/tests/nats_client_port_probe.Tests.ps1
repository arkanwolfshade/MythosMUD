#Requires -Version 5.1

<#
.SYNOPSIS
    Regression tests for the NATS client-port health check.

.DESCRIPTION
    The client port (4222) requires TLS whenever certs exist in certs/nats. Probing it with
    Test-NetConnection opens a raw TCP socket and drops it without a TLS ClientHello, which NATS
    logs as:

        [ERR] [::1]:... - TLS handshake error: ... forcibly closed by the remote host

    Every status call appended one of those, filling logs/nats/nats-server.log with lines that
    look like real client failures. Get-NatsServerStatus now asks NATS's own monitoring endpoint
    instead. These are source-level guards: exercising the real behaviour needs a live TLS NATS
    server, so the point here is that a revert to the raw probe fails loudly.
#>

Describe "NATS client port probe" {

    BeforeAll {
        $script:NatsManagerPath = Join-Path $PSScriptRoot "..\nats_manager.ps1"
        $script:Source = Get-Content $script:NatsManagerPath -Raw
    }

    It "defines the side-effect-free client port check" {
        $script:Source | Should Match 'function Test-NatsClientPortOpen'
    }

    It "checks the client port via the NATS monitoring endpoint" {
        $script:Source | Should Match 'healthz'
    }

    It "does not raw-TCP probe the TLS client port in the status function" {
        # Isolate Get-NatsServerStatus and assert it never probes $NatsPort directly.
        $statusStart = $script:Source.IndexOf('function Get-NatsServerStatus')
        $statusStart | Should Not Be -1
        $statusBody = $script:Source.Substring($statusStart)

        ($statusBody -match 'Test-NetConnection[^\r\n]*-Port\s+\$NatsPort\b') | Should Be $false
    }

    It "still reports the HTTP monitoring port with a plain TCP check" {
        # 8222 is plaintext HTTP, so a TCP probe there creates no TLS noise.
        $script:Source | Should Match 'Test-NetConnection[^\r\n]*-Port \$NatsHttpPort'
    }

    It "keeps the ClientPortOpen result key for existing callers" {
        $script:Source | Should Match 'ClientPortOpen\s*='
    }
}
