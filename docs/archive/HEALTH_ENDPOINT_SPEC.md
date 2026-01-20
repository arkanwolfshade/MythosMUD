# Health Endpoint Specification and Verification

## Overview

This document provides a comprehensive specification for the MythosMUD health endpoint, including its implementation, usage, and integration with the multiplayer scenarios playbook.

## Health Endpoint Details

### Endpoint Information

**URL**: `http://localhost:54731/monitoring/health`

**Method**: `GET`

**Content-Type**: `application/json`
- **Authentication**: None required
- **Response Format**: JSON

### Response Structure

The health endpoint returns a comprehensive JSON response with the following structure:

```json
{
    "status": "healthy|degraded|unhealthy",
    "timestamp": "2025-09-06T17:07:49.737786+00:00",
    "uptime_seconds": 3.9536983966827393,
    "version": "0.1.0",
    "components": {
        "server": {
            "status": "healthy|degraded|unhealthy",
            "uptime_seconds": 3.852517604827881,
            "memory_usage_mb": 107.125,
            "cpu_usage_percent": 41.8
        },
        "database": {
            "status": "healthy|degraded|unhealthy",
            "connection_count": 114,
            "last_query_time_ms": 0.0
        },
        "connections": {
            "status": "healthy|degraded|unhealthy",
            "active_connections": 0,
            "max_connections": 100,
            "connection_rate_per_minute": 0.0
        }
    },
    "alerts": []
}
```

### Status Values

**`healthy`**: All systems operating normally

**`degraded`**: Some systems experiencing issues but still functional

**`unhealthy`**: Critical systems failing

### HTTP Status Codes

**200 OK**: System is healthy or degraded (status in response body)

**503 Service Unavailable**: System is unhealthy

## Implementation Details

### Server-Side Implementation

The health endpoint is implemented in `server/api/monitoring.py`:

```python
@router.get("/health", response_model=HealthResponse)
async def get_health_status():
    """Get comprehensive system health status."""
    try:
        health_service = get_health_service()
        health_response = health_service.get_health_status()

        # Return appropriate HTTP status code based on health status

        if health_response.status == HealthStatus.HEALTHY:
            return health_response
        elif health_response.status == HealthStatus.DEGRADED:
            # Return 200 with degraded status in response body

            return health_response
        else:  # UNHEALTHY
            # Return 503 with unhealthy status in response body

            return JSONResponse(
                status_code=503,
                content=health_response.model_dump()
            )
    except Exception as e:
        logger.error("Health check failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=500, detail="Health check failed") from e
```

### Router Configuration

The health endpoint is registered under the `/monitoring` prefix:

```python
router = APIRouter(prefix="/monitoring", tags=["monitoring"])
```

This results in the full endpoint path: `/monitoring/health`

## Testing and Verification

### Manual Testing

#### PowerShell (Windows)

```powershell
# Basic health check

$response = Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing
$response.StatusCode  # Should be 200
$healthData = $response.Content | ConvertFrom-Json
$healthData.status  # Should be "healthy"

# Pretty-printed response

(Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing).Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

#### cURL (Cross-platform)

```bash
# Basic health check

curl -s http://localhost:54731/monitoring/health

# With status code

curl -s -w "HTTP Status: %{http_code}\n" http://localhost:54731/monitoring/health

# Pretty-printed JSON

curl -s http://localhost:54731/monitoring/health | jq .
```

### Automated Testing

The health endpoint is covered by comprehensive unit tests in `server/tests/test_health_endpoint.py`:

```python
def test_health_endpoint_returns_200_when_healthy(self, client):
    """Test that health endpoint returns 200 when system is healthy."""
    response = client.get("/monitoring/health")

    assert response.status_code == 200
    data = response.json()

    # Verify response structure

    assert "status" in data
    assert "timestamp" in data
    assert "uptime_seconds" in data
    assert "version" in data
    assert "components" in data
    assert "alerts" in data
```

## Integration with Multiplayer Scenarios

### Current Issue

The `MULTIPLAYER_SCENARIOS_PLAYBOOK.md` contains an incorrect health endpoint URL:

**❌ Incorrect (Current)**:

```powershell
curl http://localhost:54731/health
```

**✅ Correct (Should be)**:

```powershell
curl http://localhost:54731/monitoring/health
```

### Required Fix

The playbook needs to be updated to use the correct endpoint path. This affects:

1. **Pre-Scenario Setup** (Step 4: Verify Server Accessibility)
2. **Error Handling and Troubleshooting** section
3. **Debugging Commands** section

### Updated Playbook Commands

#### PowerShell Commands

```powershell
# Test server health

$healthResponse = Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health" -UseBasicParsing
if ($healthResponse.StatusCode -eq 200) {
    $healthData = $healthResponse.Content | ConvertFrom-Json
    Write-Host "Server Status: $($healthData.status)"
    Write-Host "Uptime: $([math]::Round($healthData.uptime_seconds, 2)) seconds"
} else {
    Write-Host "Server health check failed with status: $($healthResponse.StatusCode)"
}

# Test client accessibility

$clientResponse = Invoke-WebRequest -Uri "http://localhost:5173" -UseBasicParsing
Write-Host "Client Status: $($clientResponse.StatusCode)"
```

#### cURL Commands

```bash
# Test server health

curl -s -w "HTTP Status: %{http_code}\n" http://localhost:54731/monitoring/health

# Test client accessibility

curl -s -w "HTTP Status: %{http_code}\n" http://localhost:5173
```

## Monitoring and Alerting

### Health Check Integration

The health endpoint can be integrated with monitoring systems:

1. **Load Balancers**: Use for health checks
2. **Container Orchestration**: Kubernetes liveness/readiness probes
3. **Monitoring Systems**: Prometheus, Grafana, etc.
4. **CI/CD Pipelines**: Pre-deployment health verification

### Example Monitoring Script

```powershell
# Health check script for automation

function Test-MythosMUDHealth {
    param(
        [string]$ServerUrl = "http://localhost:54731/monitoring/health",
        [int]$TimeoutSeconds = 10
    )

    try {
        $response = Invoke-WebRequest -Uri $ServerUrl -UseBasicParsing -TimeoutSec $TimeoutSeconds

        if ($response.StatusCode -eq 200) {
            $healthData = $response.Content | ConvertFrom-Json

            if ($healthData.status -eq "healthy") {
                Write-Host "✅ MythosMUD Server is healthy"
                return $true
            } elseif ($healthData.status -eq "degraded") {
                Write-Host "⚠️ MythosMUD Server is degraded"
                return $false
            } else {
                Write-Host "❌ MythosMUD Server is unhealthy"
                return $false
            }
        } else {
            Write-Host "❌ Health check failed with status: $($response.StatusCode)"
            return $false
        }
    } catch {
        Write-Host "❌ Health check failed with error: $($_.Exception.Message)"
        return $false
    }
}

# Usage

Test-MythosMUDHealth
```

## Security Considerations

### Public Access

The health endpoint is currently publicly accessible without authentication. This is appropriate for:

- Load balancer health checks
- Monitoring system integration
- Basic server status verification

### Information Disclosure

The endpoint exposes:

- Server uptime
- Memory usage
- CPU usage
- Database connection count
- Active connection count

This information is generally safe to expose but should be considered in security-sensitive environments.

## Performance Impact

### Response Time

The health endpoint is designed to be lightweight:

- No database queries for basic health checks
- Minimal CPU usage
- Fast response times (< 100ms typically)

### Caching

Consider implementing caching for high-frequency health checks:

- Cache response for 5-10 seconds
- Return cached data for rapid successive requests
- Update cache asynchronously

## Troubleshooting

### Common Issues

1. **404 Not Found**: Check that the server is running and the endpoint path is correct
2. **Connection Refused**: Server is not running or port is blocked
3. **Timeout**: Server is overloaded or unresponsive
4. **503 Service Unavailable**: Server is unhealthy (check logs)

### Debug Commands

```powershell
# Check if server is running

netstat -an | findstr :54731

# Test basic connectivity

Test-NetConnection -ComputerName localhost -Port 54731

# Check server logs

Get-Content logs/development/server.log -Tail 50
```

## Future Enhancements

### Planned Improvements

1. **Health Check History**: Track health status over time
2. **Detailed Metrics**: More granular performance data
3. **Custom Health Checks**: Plugin system for custom health validations
4. **Health Check Dependencies**: Check external service dependencies
5. **Health Check Scheduling**: Automated health check scheduling

### Configuration Options

Future configuration options may include:

- Health check intervals
- Custom thresholds for degraded/unhealthy status
- Selective component health checks
- Custom alert conditions

## Conclusion

The health endpoint provides comprehensive system health monitoring for MythosMUD. The current implementation is robust and well-tested, but the multiplayer scenarios playbook needs to be updated to use the correct endpoint path (`/monitoring/health` instead of `/health`).

This specification ensures proper integration with monitoring systems and provides clear guidance for troubleshooting and maintenance.

---

**Document Version**: 1.0
**Last Updated**: 2025-09-06
**Next Review**: After playbook updates
**Primary Audience**: Developers and System Administrators
**Update Frequency**: As needed for endpoint changes
