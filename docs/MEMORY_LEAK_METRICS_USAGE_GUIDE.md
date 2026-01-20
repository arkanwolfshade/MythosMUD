# Memory Leak Metrics Usage Guide

This guide explains how to use the comprehensive memory leak monitoring system implemented for MythosMUD.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Accessing Monitoring Endpoints](#accessing-monitoring-endpoints)
3. [Automatic Logging](#automatic-logging)
4. [Key Metrics to Monitor](#key-metrics-to-monitor)
5. [Client-Side Monitoring](#client-side-monitoring)
6. [Setting Up Monitoring Dashboard](#setting-up-monitoring-dashboard)
7. [Alerting](#alerting)
8. [Troubleshooting](#troubleshooting)
9. [Quick Health Check Script](#quick-health-check-script)

---

## Quick Start

### 1. Start the Server

```powershell
# Start the development environment
./scripts/start_local.ps1

# Or just the server
./scripts/start_server.ps1
```

The server runs on `http://localhost:54731` by default.

### 2. Check Metrics Immediately

```powershell
# Quick health check
./scripts/quick_metrics_check.ps1

# Or manually
Invoke-RestMethod -Uri "http://localhost:54731/monitoring/memory-leaks" | ConvertTo-Json -Depth 10
```

---

## Accessing Monitoring Endpoints

### Comprehensive Memory Leak Metrics (Main Endpoint)

The primary endpoint aggregates all metrics from all sources:

```powershell
# PowerShell
Invoke-RestMethod -Uri "http://localhost:54731/monitoring/memory-leaks" | ConvertTo-Json -Depth 10

# Browser
http://localhost:54731/monitoring/memory-leaks
```

**Response includes:**

- Connection metrics (websockets, metadata, orphaned connections)
- Event system metrics (subscribers, tasks, churn rates)
- Cache metrics (sizes, expiration, utilization)
- Task metrics (counts, lifecycle, orphaned tasks)
- NATS metrics (subscriptions, cleanup status)
- Growth rates (calculated from historical data)
- Automated alerts (based on configured thresholds)

### Individual Component Metrics

#### Connection Metrics

```powershell
Invoke-RestMethod -Uri "http://localhost:54731/monitoring/memory" | ConvertTo-Json
```

Returns connection statistics including active websockets, closed websockets count, and orphaned connections.

#### EventBus Metrics

```powershell
Invoke-RestMethod -Uri "http://localhost:54731/monitoring/eventbus" | ConvertTo-Json
```

Returns subscriber counts by event type, active task count, and subscription churn rate. Useful for detecting event subscription leaks.

#### Cache Metrics

```powershell
Invoke-RestMethod -Uri "http://localhost:54731/monitoring/caches" | ConvertTo-Json
```

Returns cache sizes, hit rates, expired entry counts, expiration rates, and capacity utilization. Helps identify cache-related memory leaks.

#### Task Metrics

```powershell
Invoke-RestMethod -Uri "http://localhost:54731/monitoring/tasks" | ConvertTo-Json
```

Returns active task counts, task lifecycle metrics, and service-level breakdown. Tracks orphaned tasks and task growth rates.

---

## Automatic Logging

The system automatically logs memory leak metrics:

- **Every 5 minutes**: Periodic metrics logged to structured logs
- **On startup**: Initial metrics captured for baseline comparison
- **On shutdown**: Final metrics with delta calculations

### Viewing Logs

```powershell
# View structured logs
Get-Content logs/local/app.log -Tail 50 | Select-String "Memory leak metrics"

# Or check the metrics file
Get-Content logs/local/memory_leak_metrics.json | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

### Metrics File Location

Metrics are persisted to: `logs/local/memory_leak_metrics.json`

This file contains:

- Startup metrics (baseline)
- Shutdown metrics (final state)
- Delta calculations (growth over application lifetime)

---

## Key Metrics to Monitor

### Connection Leaks (Most Critical)

#### `closed_websockets_count`

- **Normal**: < 1000
- **Warning**: > 5000
- **Critical**: > 10000

This indicates WebSocket connections that were closed but their IDs are still being tracked. High values suggest cleanup issues.

#### `active_to_player_ratio`

- **Normal**: 0.8-1.2 (approximately one connection per player)
- **Abnormal**: > 2.0 (multiple connections per player)

High ratios indicate players have multiple active connections, which can lead to memory leaks.

#### `orphaned_connections`

- **Normal**: 0
- **Warning**: > 10

Connections without associated active players indicate cleanup failures.

### Event Subscription Leaks

#### `subscription_churn_rate`

- **Normal**: < 0.1 (10% growth per period)
- **Abnormal**: > 0.2 (20% growth per period)

High churn rates indicate subscriptions are being created faster than they're being cleaned up.

#### `active_task_count`

- **Should remain relatively stable**
- **Growing count indicates leaks**

EventBus tasks that aren't completing or being cleaned up properly.

### Cache Leaks

#### `capacity_utilization`

- **Normal**: < 100%
- **Warning**: > 110% (cache exceeded max_size)

Caches exceeding their configured maximum size indicate potential memory leaks.

#### `expiration_rates`

- **High rates**: TTL working correctly (entries expiring as expected)
- **Low rates with high sizes**: Potential leak (entries not expiring)

### Task Leaks

#### `orphaned_task_count`

- **Normal**: 0
- **Warning**: > 5

Tasks that are done but not cleaned up from the registry.

#### `task_growth_rate`

- **Normal**: < 0.2 (20% per period)
- **Abnormal**: > 0.3 (30% growth)

Tasks being created faster than they complete.

### NATS Subscription Leaks

#### `subscription_count`

- **Should match expected service subscriptions**
- **Growing count indicates leaks**

#### Subscriptions After Cleanup

- **Normal**: 0
- **Warning**: > 0

Subscriptions remaining after service shutdown indicate cleanup failures.

---

## Client-Side Monitoring

### Using Lifecycle Tracking Hooks

In your React components, use the provided hooks to track component lifecycle and store subscriptions:

```typescript
import { useComponentLifecycleTracking } from '@/hooks/useComponentLifecycleTracking';
import { useStoreSubscriptionTracking } from '@/hooks/useStoreSubscriptionTracking';

function MyComponent() {
  // Track component lifecycle
  const { hasCleanup, setCleanup } = useComponentLifecycleTracking({
    componentName: 'MyComponent'
  });

  // Track store subscriptions
  useStoreSubscriptionTracking({ storeName: 'gameStore' });

  useEffect(() => {
    // Your component logic

    // Register cleanup function
    setCleanup(() => {
      // Cleanup logic
    });
  }, [setCleanup]);

  // ... rest of component
}
```

### Resource Manager

The `useResourceCleanup` hook` automatically tracks:

- Timers (`setTimeout`)
- Intervals (`setInterval`)
- WebSocket connections
- Custom resources

In development mode, resource statistics are logged to the console every 5 minutes.

### Viewing Client Metrics

Open browser DevTools console (development mode only):

- Look for `[ResourceManager] Periodic stats:` messages
- Check for warnings about missing cleanup functions
- Monitor store subscription/unsubscription events

---

## Setting Up Monitoring Dashboard

### Prerequisites

- Docker Desktop installed and running
- Docker Compose available
- **MythosMUD server should be running** (or start it after monitoring stack)

### Startup Order

**Recommended Order:**

1. **Start the MythosMUD server first** (`./scripts/start_server.ps1` or `./scripts/start_local.ps1`)
2. **Then start the monitoring stack** (`./scripts/start_monitoring.ps1`)

**Why?**

- The server exposes metrics endpoints that Prometheus scrapes
- Starting the server first ensures metrics are immediately available when Prometheus starts
- Prometheus will show targets as "down" if the server isn't running yet (not a problem, but less ideal)

**Alternative:**

- You can start them in either order - they're independent
- If you start monitoring first, Prometheus will just show the server target as down until the server starts
- Once the server starts, Prometheus will automatically begin collecting metrics

### Step 1: Verify Docker is Running

```powershell
# Check Docker status
docker version

# If Docker is not running, start Docker Desktop:
# 1. Open Docker Desktop from Start Menu
# 2. Wait for it to fully start (whale icon in system tray)
# 3. Verify: docker ps
```

### Step 2: Start Monitoring Stack

```powershell
# Use the helper script (recommended - includes Docker check)
./scripts/start_monitoring.ps1

# Or use the full deployment script
./scripts/deploy_monitoring.ps1

# Or manually (only if Docker is confirmed running)
cd monitoring
docker-compose -f docker-compose.monitoring.yml up -d
```

**Note**: The `start_monitoring.ps1` script will automatically check if Docker Desktop is running and provide clear instructions if it's not.

### Step 3: Access Services

Once started, access the monitoring services:

- **Prometheus**: <http://localhost:9090>
  - View metrics, run queries, check targets
- **Grafana**: <http://localhost:3000>
  - Default credentials: `admin` / `admin`
  - View dashboards with memory leak visualizations
- **Alertmanager**: <http://localhost:9093>
  - View and manage alerts

### Step 4: View Grafana Dashboard

The Grafana dashboard includes panels for:

1. **Closed WebSockets Count** - Memory leak indicator
2. **Active to Player Ratio** - Connection efficiency
3. **EventBus Subscriber Count** - Event subscription tracking
4. **Cache Capacity Utilization** - Cache health
5. **Active Tasks Count** - Task management
6. **Orphaned Resources** - Cleanup verification

### Stopping the Monitoring Stack

```powershell
# Use the helper script (recommended)
./scripts/stop_monitoring.ps1

# Or manually
cd monitoring
docker-compose -f docker-compose.monitoring.yml down
```

---

## Alerting

### Alert Configuration

Alerts are configured in `monitoring/mythos_alerts.yml` and trigger when:

#### Connection Alerts

- **HighClosedWebsocketsCount**: > 5000 (warning), > 10000 (critical)
- **OrphanedConnectionsDetected**: > 10 connections

#### Event System Alerts

- **HighSubscriberGrowthRate**: > 10% growth per period

#### Cache Alerts

- **HighCacheCapacityUtilization**: > 110% of max_size

#### Task Alerts

- **HighTaskGrowthRate**: > 20% growth per period
- **OrphanedTasksDetected**: > 5 orphaned tasks

### Viewing Alerts

1. **In API Response**: Check the `alerts` array in `/monitoring/memory-leaks` response
2. **In Prometheus**: <http://localhost:9090/alerts>
3. **In Alertmanager**: <http://localhost:9093>

### Alert Thresholds

Thresholds are configured in `MemoryLeakMetricsCollector`:

```python
_alert_thresholds = {
    "closed_websockets_max": 5000,
    "subscriber_growth_rate": 0.1,  # 10% growth per period
    "cache_size_limit_factor": 1.1,  # 110% of max_size
    "task_growth_rate": 0.2,  # 20% growth per period
}
```

---

## Troubleshooting

### Server Not Responding

```powershell
# Check if server is running
Invoke-WebRequest -Uri "http://localhost:54731/monitoring/health"

# Check server logs
Get-Content logs/local/app.log -Tail 50
```

### Docker Issues

**Error: "Docker Desktop is not running"**

1. Start Docker Desktop application from Start Menu
2. Wait for full startup (check system tray icon - whale should be steady, not animating)
3. Verify: `docker ps`
4. Use `./scripts/start_monitoring.ps1` which will check Docker status automatically

**Error: "version is obsolete"**

- This has been fixed - the `version: '3.8'` line has been removed from `monitoring/docker-compose.monitoring.yml`
- If you still see this error, ensure you have the latest version of the file

**Error: "unable to get image" or "cannot find the file specified"**

- This means Docker Desktop is not running
- Use `./scripts/start_monitoring.ps1` which provides clear error messages and instructions

### Metrics Not Appearing

1. **Check server is running**: `http://localhost:54731/monitoring/health`
2. **Check endpoint directly**: `http://localhost:54731/monitoring/memory-leaks`
3. **Check server logs** for errors
4. **Verify metrics collector initialized**: Look for "Memory leak metrics collector initialized" in logs

### High Metric Values

If you see high values:

1. **Check the alerts array** in the metrics response
2. **Review specific metric category** (connection/event/cache/task)
3. **Check server logs** for detailed context
4. **Use individual endpoints** to drill down
5. **Review client-side console logs** for client-side leaks

### Comparing Metrics Over Time

The system logs metrics on startup and shutdown. Compare:

```powershell
# Get startup metrics (from logs/local/memory_leak_metrics.json)
$startup = (Get-Content logs/local/memory_leak_metrics.json | ConvertFrom-Json).startup_metrics

# Get current metrics
$current = Invoke-RestMethod -Uri "http://localhost:54731/monitoring/memory-leaks"

# Compare closed websockets
Write-Host "Startup: $($startup.connection.closed_websockets_count)"
Write-Host "Current: $($current.connection.closed_websockets_count)"
Write-Host "Growth: $($current.connection.closed_websockets_count - $startup.connection.closed_websockets_count)"
```

---

## Quick Health Check Script

Use the provided script for quick health checks:

```powershell
./scripts/quick_metrics_check.ps1
```

Or create your own custom check:

```powershell
# Custom metrics check
$metrics = Invoke-RestMethod -Uri "http://localhost:54731/monitoring/memory-leaks"

Write-Host "=== Memory Leak Metrics ===" -ForegroundColor Cyan
Write-Host "Closed WebSockets: $($metrics.connection.closed_websockets_count)" -ForegroundColor $(if ($metrics.connection.closed_websockets_count -gt 5000) { "Red" } else { "Green" })
Write-Host "Active/Player Ratio: $($metrics.connection.active_to_player_ratio)" -ForegroundColor $(if ($metrics.connection.active_to_player_ratio -gt 2.0) { "Red" } else { "Green" })
Write-Host "Orphaned Connections: $($metrics.connection.orphaned_connections)" -ForegroundColor $(if ($metrics.connection.orphaned_connections -gt 10) { "Red" } else { "Green" })
Write-Host "Active Tasks: $($metrics.task.active_task_count)"
Write-Host "Orphaned Tasks: $($metrics.task.orphaned_task_count)" -ForegroundColor $(if ($metrics.task.orphaned_task_count -gt 5) { "Red" } else { "Green" })

if ($metrics.alerts.Count -gt 0) {
    Write-Host "`n⚠️ ALERTS:" -ForegroundColor Red
    $metrics.alerts | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
}
```

---

## Best Practices

1. **Regular Monitoring**: Check metrics periodically during development
2. **Baseline Comparison**: Compare current metrics to startup baseline
3. **Watch Growth Rates**: Monitor growth rates over time, not just absolute values
4. **Client-Side Tracking**: Use lifecycle hooks in all components
5. **Cleanup Verification**: Ensure all resources have cleanup functions
6. **Alert Response**: Investigate alerts promptly
7. **Log Analysis**: Review structured logs for detailed context

---

## Additional Resources

- **API Documentation**: See `server/README.md` for detailed endpoint documentation
- **Memory Leak Audit Report**: `docs/MEMORY_LEAK_AUDIT_REPORT.md`
- **Remediation Plan**: `.cursor/plans/memory_leak_remediation_plan_6321808e.plan.md`
- **Metrics Collection Plan**: `.cursor/plans/memory_leak_metrics_collection_plan_a4707e8b.plan.md`

---

## Summary

The memory leak metrics system provides comprehensive monitoring across:

- ✅ Connection management
- ✅ Event subscriptions
- ✅ Cache utilization
- ✅ Task lifecycle
- ✅ NATS subscriptions
- ✅ Client-side resources

All metrics are:

- Exposed via REST API endpoints
- Logged automatically every 5 minutes
- Tracked with growth rate calculations
- Monitored with automated alerts
- Visualized in Grafana dashboards (optional)

Use this system to proactively detect and address memory leaks before they impact performance.
