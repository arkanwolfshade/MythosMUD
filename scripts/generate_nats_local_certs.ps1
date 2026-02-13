#Requires -Version 5.1
<#
.SYNOPSIS
    Generate local NATS TLS certificates for development.

.DESCRIPTION
    Creates a self-signed CA and signs server and client certificates for use
    with NATS over TLS in the local development environment. Output is written
    to certs/nats/ (relative to repository root). Private keys and the CA key
    are for local use only and must not be committed.

.PARAMETER OutDir
    Directory for certificate output. Default: certs/nats under repo root.

.EXAMPLE
    .\scripts\generate_nats_local_certs.ps1
    .\scripts\generate_nats_local_certs.ps1 -OutDir E:\dev\mythos-certs

.NOTES
    Requires OpenSSL on PATH (e.g. from Git for Windows or chocolatey).
    After generation, set in .env.local:
      NATS_TLS_ENABLED=true
      NATS_TLS_CERT_FILE=<path>/client.crt
      NATS_TLS_KEY_FILE=<path>/client.key
      NATS_TLS_CA_FILE=<path>/ca.crt
      NATS_TLS_VERIFY=false
    For nats-server with TLS, use server.crt and server.key; point clients to
    tls://localhost:4222 and use ca.crt for verification if desired.
#>

[CmdletBinding()]
param(
    [Parameter()]
    [string] $OutDir = "",
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $Remaining = @()
)

$ErrorActionPreference = "Stop"

# Resolve repo root (directory containing .git or scripts/)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Get-Item $scriptDir).Parent.FullName
if ($OutDir -eq "") {
    $OutDir = Join-Path $repoRoot "certs" "nats"
}

$OutPath = [System.IO.Path]::GetFullPath($OutDir)
if (-not (Test-Path $OutPath)) {
    New-Item -ItemType Directory -Path $OutPath -Force | Out-Null
    Write-Host "Created directory: $OutPath" -ForegroundColor Gray
}

# Check for OpenSSL
$openssl = $null
try {
    $openssl = Get-Command openssl -ErrorAction Stop
}
catch {
    Write-Error @"
OpenSSL not found on PATH. Install one of:
  - Git for Windows (includes OpenSSL in Git\usr\bin)
  - Chocolatey: choco install openssl
  - Add your OpenSSL bin directory to PATH, then re-run this script.
"@
}

Push-Location $OutPath
try {
    $days = 825  # ~2.25 years for local dev

    # 1. CA key and certificate (run via cmd so OpenSSL stderr does not trigger PowerShell error)
    Write-Host "Generating CA (ca.key, ca.crt)..." -ForegroundColor Cyan
    $caArgs = "req", "-x509", "-newkey", "rsa:2048", "-keyout", "ca.key", "-out", "ca.crt",
    "-days", $days, "-nodes", "-subj", "/CN=MythosMUD-NATS-Local-CA"
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList $caArgs -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "CA generation failed" }

    # 2. Server key and CSR; need SAN for localhost
    $sanConfig = Join-Path $OutPath "openssl_san_server.cnf"
    @"
[req]
distinguished_name = req_dn
req_extensions = v3_req
[req_dn]
CN = localhost
[v3_req]
subjectAltName = @alt
[alt]
DNS.1 = localhost
IP.1 = 127.0.0.1
"@ | Set-Content -Path $sanConfig -Encoding ASCII

    Write-Host "Generating server key and certificate (server.key, server.crt)..." -ForegroundColor Cyan
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList "genrsa", "-out", "server.key", "2048" -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "Server key generation failed" }
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList "req", "-new", "-key", "server.key", "-out", "server.csr", "-subj", "/CN=localhost", "-config", $sanConfig, "-extensions", "v3_req" -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "Server CSR failed" }
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList "x509", "-req", "-in", "server.csr", "-CA", "ca.crt", "-CAkey", "ca.key", "-CAcreateserial", "-out", "server.crt", "-days", $days, "-extfile", $sanConfig, "-extensions", "v3_req" -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "Server cert signing failed" }
    Remove-Item server.csr -Force -ErrorAction SilentlyContinue
    Remove-Item $sanConfig -Force -ErrorAction SilentlyContinue
    if (Test-Path "ca.srl") { Remove-Item "ca.srl" -Force -ErrorAction SilentlyContinue }

    # 3. Client key and certificate
    Write-Host "Generating client key and certificate (client.key, client.crt)..." -ForegroundColor Cyan
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList "genrsa", "-out", "client.key", "2048" -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "Client key generation failed" }
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList "req", "-new", "-key", "client.key", "-out", "client.csr", "-subj", "/CN=mythosmud-client" -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "Client CSR failed" }
    $proc = Start-Process -FilePath $openssl.Source -ArgumentList "x509", "-req", "-in", "client.csr", "-CA", "ca.crt", "-CAkey", "ca.key", "-CAcreateserial", "-out", "client.crt", "-days", $days -WorkingDirectory $OutPath -PassThru -Wait -NoNewWindow -RedirectStandardError "NUL"
    if ($proc.ExitCode -ne 0) { throw "Client cert signing failed" }
    Remove-Item client.csr -Force -ErrorAction SilentlyContinue
    if (Test-Path "ca.srl") { Remove-Item "ca.srl" -Force -ErrorAction SilentlyContinue }

    Write-Host "Done. Certificates written to: $OutPath" -ForegroundColor Green
    Write-Host ""
    Write-Host "Files created:" -ForegroundColor Gray
    Get-ChildItem -Path $OutPath -File | ForEach-Object { Write-Host "  $($_.Name)" -ForegroundColor Gray }
    Write-Host ""
    Write-Host "For MythosMUD app (.env.local), use client cert and CA:" -ForegroundColor Yellow
    $clientCrt = Join-Path $OutPath "client.crt"
    $clientKey = Join-Path $OutPath "client.key"
    $caCrt = Join-Path $OutPath "ca.crt"
    Write-Host "  NATS_TLS_ENABLED=true"
    Write-Host "  NATS_TLS_CERT_FILE=$clientCrt"
    Write-Host "  NATS_TLS_KEY_FILE=$clientKey"
    Write-Host "  NATS_TLS_CA_FILE=$caCrt"
    Write-Host "  NATS_TLS_VERIFY=false"
    Write-Host ""
    Write-Host "For nats-server, configure TLS with server.crt and server.key; use tls://localhost:4222." -ForegroundColor Yellow
}
finally {
    Pop-Location
}
