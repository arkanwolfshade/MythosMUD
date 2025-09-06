# MythosMUD Monitoring Stack Deployment Script

param(
    [string]$Environment = "development",
    [switch]$SkipPrometheus,
    [switch]$SkipGrafana,
    [switch]$SkipAlertmanager,
    [switch]$Force
)

Write-Host "Deploying MythosMUD Monitoring Stack for $Environment environment..." -ForegroundColor Green

# Check if Docker is running
try {
    docker version | Out-Null
    Write-Host "Docker is running" -ForegroundColor Green
}
catch {
    Write-Host "Error: Docker is not running. Please start Docker and try again." -ForegroundColor Red
    exit 1
}

# Check if Docker Compose is available
try {
    docker-compose version | Out-Null
    Write-Host "Docker Compose is available" -ForegroundColor Green
}
catch {
    Write-Host "Error: Docker Compose is not available. Please install Docker Compose and try again." -ForegroundColor Red
    exit 1
}

# Create monitoring directory if it doesn't exist
if (-not (Test-Path "monitoring")) {
    Write-Host "Creating monitoring directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Path "monitoring" | Out-Null
}

# Copy configuration files if they don't exist
$configFiles = @(
    "prometheus.yml",
    "mythos_alerts.yml",
    "alertmanager.yml",
    "grafana-dashboard.json",
    "docker-compose.monitoring.yml"
)

foreach ($file in $configFiles) {
    if (-not (Test-Path "monitoring/$file")) {
        Write-Host "Warning: $file not found in monitoring directory" -ForegroundColor Yellow
    }
}

# Stop existing monitoring stack if Force is specified
if ($Force) {
    Write-Host "Stopping existing monitoring stack..." -ForegroundColor Yellow
    Set-Location monitoring
    docker-compose -f docker-compose.monitoring.yml down
    Set-Location ..
}

# Deploy monitoring stack
Write-Host "Starting monitoring stack..." -ForegroundColor Green
Set-Location monitoring

try {
    # Start the monitoring stack
    docker-compose -f docker-compose.monitoring.yml up -d

    Write-Host "Monitoring stack deployed successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Services available at:" -ForegroundColor Cyan
    Write-Host "  Prometheus: http://localhost:9090" -ForegroundColor White
    Write-Host "  Grafana: http://localhost:3000 (admin/admin)" -ForegroundColor White
    Write-Host "  Alertmanager: http://localhost:9093" -ForegroundColor White
    Write-Host "  Node Exporter: http://localhost:9100" -ForegroundColor White
    Write-Host "  Webhook Receiver: http://localhost:5001" -ForegroundColor White
    Write-Host ""
    Write-Host "To view logs:" -ForegroundColor Cyan
    Write-Host "  docker-compose -f docker-compose.monitoring.yml logs -f" -ForegroundColor White
    Write-Host ""
    Write-Host "To stop the stack:" -ForegroundColor Cyan
    Write-Host "  docker-compose -f docker-compose.monitoring.yml down" -ForegroundColor White

}
catch {
    Write-Host "Error deploying monitoring stack: $_" -ForegroundColor Red
    exit 1
}
finally {
    Set-Location ..
}

# Wait for services to be ready
Write-Host "Waiting for services to be ready..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Check service health
$services = @(
    @{Name = "Prometheus"; Url = "http://localhost:9090/-/healthy" },
    @{Name = "Grafana"; Url = "http://localhost:3000/api/health" },
    @{Name = "Alertmanager"; Url = "http://localhost:9093/-/healthy" }
)

foreach ($service in $services) {
    try {
        $response = Invoke-WebRequest -Uri $service.Url -TimeoutSec 10 -UseBasicParsing
        if ($response.StatusCode -eq 200) {
            Write-Host "✓ $($service.Name) is healthy" -ForegroundColor Green
        }
        else {
            Write-Host "✗ $($service.Name) returned status $($response.StatusCode)" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host "✗ $($service.Name) is not responding" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Monitoring stack deployment completed!" -ForegroundColor Green
