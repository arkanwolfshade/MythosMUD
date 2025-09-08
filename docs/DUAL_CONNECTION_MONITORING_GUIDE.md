# Dual Connection System Monitoring and Logging Guide

## Overview

This guide provides comprehensive documentation for monitoring and logging the dual WebSocket/SSE connection system. It covers system health monitoring, performance metrics, error tracking, and operational insights.

## Table of Contents

1. [Monitoring Architecture](#monitoring-architecture)
2. [Health Monitoring](#health-monitoring)
3. [Performance Metrics](#performance-metrics)
4. [Error Tracking](#error-tracking)
5. [Logging Configuration](#logging-configuration)
6. [Alerting Setup](#alerting-setup)
7. [Dashboard Configuration](#dashboard-configuration)
8. [Troubleshooting](#troubleshooting)

## Monitoring Architecture

### System Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │    │   Monitoring    │    │   Alerting      │
│                 │    │   System        │    │   System        │
│  ┌───────────┐  │    │                 │    │                 │
│  │Connection │  │───▶│  ┌───────────┐  │───▶│  ┌───────────┐  │
│  │Manager    │  │    │  │Prometheus │  │    │  │Alertmanager│ │
│  └───────────┘  │    │  └───────────┘  │    │  └───────────┘  │
│                 │    │                 │    │                 │
│  ┌───────────┐  │    │  ┌───────────┐  │    │  ┌───────────┐  │
│  │Health     │  │───▶│  │Grafana    │  │    │  │Slack/     │  │
│  │Service    │  │    │  │Dashboard  │  │    │  │Email      │  │
│  └───────────┘  │    │  └───────────┘  │    │  └───────────┘  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Monitoring Stack

- **Metrics Collection**: Prometheus
- **Visualization**: Grafana
- **Alerting**: Alertmanager
- **Logging**: Structured logging with JSON format
- **Health Checks**: Custom health endpoints

## Health Monitoring

### Health Check Endpoints

**Basic Health Check:**
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-06T19:55:00Z",
  "version": "1.0.0",
  "uptime": 3600,
  "components": {
    "database": "healthy",
    "connections": "healthy",
    "memory": "healthy"
  }
}
```

**Detailed Health Check:**
```http
GET /health/detailed
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-06T19:55:00Z",
  "components": {
    "database": {
      "status": "healthy",
      "response_time_ms": 5.2,
      "connection_count": 10
    },
    "connections": {
      "status": "healthy",
      "total_connections": 150,
      "healthy_connections": 148,
      "unhealthy_connections": 2,
      "health_percentage": 98.7
    },
    "memory": {
      "status": "healthy",
      "used_mb": 512,
      "total_mb": 2048,
      "usage_percentage": 25.0
    },
    "performance": {
      "status": "healthy",
      "avg_response_time_ms": 45.2,
      "requests_per_second": 125.5
    }
  }
}
```

### Connection Health Monitoring

**Connection Health Statistics:**
```http
GET /monitoring/connection-health
```

**Response:**
```json
{
  "overall_health": {
    "total_connections": 150,
    "healthy_connections": 148,
    "unhealthy_connections": 2,
    "health_percentage": 98.7
  },
  "connection_type_health": {
    "websocket": {
      "total": 75,
      "healthy": 74,
      "unhealthy": 1,
      "health_percentage": 98.7
    },
    "sse": {
      "total": 75,
      "healthy": 74,
      "unhealthy": 1,
      "health_percentage": 98.7
    }
  },
  "health_trends": {
    "last_hour_health_percentage": 98.5,
    "last_24_hours_health_percentage": 98.8
  },
  "connection_age_distribution": {
    "0-5_minutes": 45,
    "5-30_minutes": 78,
    "30_minutes-2_hours": 25,
    "2_hours+": 2
  }
}
```

### Health Check Implementation

```python
# server/services/health_service.py
import asyncio
import time
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class HealthStatus:
    status: str
    response_time_ms: float
    details: Dict[str, Any] = None

class HealthService:
    def __init__(self, connection_manager, database):
        self.connection_manager = connection_manager
        self.database = database
        self.start_time = time.time()

    async def check_database_health(self) -> HealthStatus:
        start_time = time.time()
        try:
            # Test database connectivity
            await self.database.execute("SELECT 1")
            response_time = (time.time() - start_time) * 1000
            return HealthStatus("healthy", response_time)
        except Exception as e:
            response_time = (time.time() - start_time) * 1000
            return HealthStatus("unhealthy", response_time, {"error": str(e)})

    async def check_connection_health(self) -> HealthStatus:
        start_time = time.time()
        try:
            stats = self.connection_manager.get_connection_health_stats()
            response_time = (time.time() - start_time) * 1000

            health_percentage = stats["overall_health"]["health_percentage"]
            status = "healthy" if health_percentage >= 95 else "degraded" if health_percentage >= 80 else "unhealthy"

            return HealthStatus(status, response_time, stats)
        except Exception as e:
            response_time = (time.time() - start_time) * 1000
            return HealthStatus("unhealthy", response_time, {"error": str(e)})

    async def check_memory_health(self) -> HealthStatus:
        start_time = time.time()
        try:
            import psutil
            memory = psutil.virtual_memory()
            response_time = (time.time() - start_time) * 1000

            usage_percentage = memory.percent
            status = "healthy" if usage_percentage < 80 else "degraded" if usage_percentage < 90 else "unhealthy"

            return HealthStatus(status, response_time, {
                "used_mb": memory.used // (1024 * 1024),
                "total_mb": memory.total // (1024 * 1024),
                "usage_percentage": usage_percentage
            })
        except Exception as e:
            response_time = (time.time() - start_time) * 1000
            return HealthStatus("unhealthy", response_time, {"error": str(e)})

    async def get_overall_health(self) -> Dict[str, Any]:
        # Run all health checks concurrently
        db_health, conn_health, mem_health = await asyncio.gather(
            self.check_database_health(),
            self.check_connection_health(),
            self.check_memory_health()
        )

        # Determine overall status
        statuses = [db_health.status, conn_health.status, mem_health.status]
        if "unhealthy" in statuses:
            overall_status = "unhealthy"
        elif "degraded" in statuses:
            overall_status = "degraded"
        else:
            overall_status = "healthy"

        return {
            "status": overall_status,
            "timestamp": time.time(),
            "uptime": time.time() - self.start_time,
            "components": {
                "database": {
                    "status": db_health.status,
                    "response_time_ms": db_health.response_time_ms,
                    "details": db_health.details
                },
                "connections": {
                    "status": conn_health.status,
                    "response_time_ms": conn_health.response_time_ms,
                    "details": conn_health.details
                },
                "memory": {
                    "status": mem_health.status,
                    "response_time_ms": mem_health.response_time_ms,
                    "details": mem_health.details
                }
            }
        }
```

## Performance Metrics

### Prometheus Metrics

**Connection Metrics:**
```python
# server/monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge, start_http_server

# Connection metrics
connections_total = Gauge('mythos_connections_total', 'Total number of connections')
connections_by_type = Gauge('mythos_connections_by_type', 'Connections by type', ['type'])
connection_health_percentage = Gauge('mythos_connection_health_percentage', 'Connection health percentage')
connection_establishment_time = Histogram('mythos_connection_establishment_seconds', 'Connection establishment time', ['type'])

# Message metrics
messages_sent_total = Counter('mythos_messages_sent_total', 'Total messages sent', ['type', 'status'])
message_delivery_time = Histogram('mythos_message_delivery_seconds', 'Message delivery time')
message_delivery_success_rate = Gauge('mythos_message_delivery_success_rate', 'Message delivery success rate')

# Session metrics
sessions_total = Gauge('mythos_sessions_total', 'Total number of sessions')
session_connections = Gauge('mythos_session_connections', 'Connections per session', ['session_id'])

# Performance metrics
request_duration = Histogram('mythos_request_duration_seconds', 'Request duration', ['method', 'endpoint'])
active_connections = Gauge('mythos_active_connections', 'Number of active connections')
memory_usage = Gauge('mythos_memory_usage_bytes', 'Memory usage in bytes')
cpu_usage = Gauge('mythos_cpu_usage_percent', 'CPU usage percentage')
```

**Metrics Collection:**
```python
# server/monitoring/collector.py
import asyncio
import time
from prometheus_client import CollectorRegistry, generate_latest

class MetricsCollector:
    def __init__(self, connection_manager):
        self.connection_manager = connection_manager
        self.registry = CollectorRegistry()
        self._register_metrics()

    def _register_metrics(self):
        # Register all metrics with the registry
        self.registry.register(connections_total)
        self.registry.register(connections_by_type)
        self.registry.register(connection_health_percentage)
        # ... register other metrics

    async def collect_metrics(self):
        """Collect and update all metrics"""
        # Update connection metrics
        stats = self.connection_manager.get_dual_connection_stats()
        connections_total.set(stats["connection_distribution"]["total_players"])

        # Update connection type metrics
        connections_by_type.labels(type='websocket').set(
            stats["connection_distribution"]["websocket_only_players"]
        )
        connections_by_type.labels(type='sse').set(
            stats["connection_distribution"]["sse_only_players"]
        )
        connections_by_type.labels(type='dual').set(
            stats["connection_distribution"]["dual_connection_players"]
        )

        # Update health metrics
        health_stats = self.connection_manager.get_connection_health_stats()
        connection_health_percentage.set(
            health_stats["overall_health"]["health_percentage"]
        )

        # Update performance metrics
        perf_stats = self.connection_manager.get_performance_stats()
        # ... update performance metrics

    def get_metrics(self):
        """Return metrics in Prometheus format"""
        return generate_latest(self.registry)
```

### Performance Monitoring Endpoints

**Performance Statistics:**
```http
GET /monitoring/performance
```

**Response:**
```json
{
  "connection_establishment": {
    "total_connections": 150,
    "websocket_connections": 75,
    "sse_connections": 75,
    "avg_websocket_establishment_ms": 45.2,
    "avg_sse_establishment_ms": 32.1,
    "max_websocket_establishment_ms": 120.5,
    "max_sse_establishment_ms": 89.3,
    "p95_websocket_establishment_ms": 85.2,
    "p95_sse_establishment_ms": 65.1
  },
  "message_delivery": {
    "total_messages_sent": 12500,
    "successful_deliveries": 12450,
    "failed_deliveries": 50,
    "delivery_success_rate": 99.6,
    "avg_delivery_time_ms": 12.5,
    "max_delivery_time_ms": 150.2,
    "p95_delivery_time_ms": 45.8
  },
  "system_performance": {
    "avg_response_time_ms": 45.2,
    "requests_per_second": 125.5,
    "memory_usage_mb": 512,
    "cpu_usage_percent": 25.3,
    "active_connections": 150
  },
  "timestamp": "2025-01-06T19:55:00Z"
}
```

### Performance Tracking Implementation

```python
# server/monitoring/performance_monitor.py
import time
import asyncio
from collections import deque
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class PerformanceMetrics:
    timestamp: float
    connection_establishment_times: List[float]
    message_delivery_times: List[float]
    memory_usage: float
    cpu_usage: float
    active_connections: int

class PerformanceMonitor:
    def __init__(self, max_samples: int = 1000):
        self.max_samples = max_samples
        self.connection_times = deque(maxlen=max_samples)
        self.message_times = deque(maxlen=max_samples)
        self.metrics_history = deque(maxlen=100)  # Keep last 100 samples

    def record_connection_establishment(self, connection_type: str, duration_ms: float):
        """Record connection establishment time"""
        self.connection_times.append({
            'type': connection_type,
            'duration_ms': duration_ms,
            'timestamp': time.time()
        })

    def record_message_delivery(self, duration_ms: float):
        """Record message delivery time"""
        self.message_times.append({
            'duration_ms': duration_ms,
            'timestamp': time.time()
        })

    def get_performance_stats(self) -> Dict[str, any]:
        """Get current performance statistics"""
        current_time = time.time()

        # Connection establishment stats
        ws_times = [t['duration_ms'] for t in self.connection_times if t['type'] == 'websocket']
        sse_times = [t['duration_ms'] for t in self.connection_times if t['type'] == 'sse']

        connection_stats = {
            'total_connections': len(self.connection_times),
            'websocket_connections': len(ws_times),
            'sse_connections': len(sse_times),
            'avg_websocket_establishment_ms': sum(ws_times) / len(ws_times) if ws_times else 0,
            'avg_sse_establishment_ms': sum(sse_times) / len(sse_times) if sse_times else 0,
            'max_websocket_establishment_ms': max(ws_times) if ws_times else 0,
            'max_sse_establishment_ms': max(sse_times) if sse_times else 0,
            'p95_websocket_establishment_ms': self._percentile(ws_times, 95) if ws_times else 0,
            'p95_sse_establishment_ms': self._percentile(sse_times, 95) if sse_times else 0
        }

        # Message delivery stats
        message_times = [t['duration_ms'] for t in self.message_times]
        message_stats = {
            'total_messages_sent': len(message_times),
            'avg_delivery_time_ms': sum(message_times) / len(message_times) if message_times else 0,
            'max_delivery_time_ms': max(message_times) if message_times else 0,
            'p95_delivery_time_ms': self._percentile(message_times, 95) if message_times else 0
        }

        return {
            'connection_establishment': connection_stats,
            'message_delivery': message_stats,
            'timestamp': current_time
        }

    def _percentile(self, data: List[float], percentile: int) -> float:
        """Calculate percentile of data"""
        if not data:
            return 0
        sorted_data = sorted(data)
        index = int(len(sorted_data) * percentile / 100)
        return sorted_data[min(index, len(sorted_data) - 1)]
```

## Error Tracking

### Error Classification

```python
# server/monitoring/error_tracker.py
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional
import time

class ErrorType(Enum):
    CONNECTION_ERROR = "connection_error"
    AUTHENTICATION_ERROR = "authentication_error"
    SESSION_ERROR = "session_error"
    MESSAGE_DELIVERY_ERROR = "message_delivery_error"
    SYSTEM_ERROR = "system_error"
    VALIDATION_ERROR = "validation_error"

class ErrorSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class ErrorEvent:
    error_type: ErrorType
    severity: ErrorSeverity
    message: str
    details: Dict[str, any]
    timestamp: float
    player_id: Optional[str] = None
    session_id: Optional[str] = None
    connection_id: Optional[str] = None

class ErrorTracker:
    def __init__(self, max_errors: int = 1000):
        self.max_errors = max_errors
        self.errors = deque(maxlen=max_errors)
        self.error_counts = {}
        self.error_rates = {}

    def record_error(self, error_event: ErrorEvent):
        """Record an error event"""
        self.errors.append(error_event)

        # Update error counts
        error_key = f"{error_event.error_type.value}_{error_event.severity.value}"
        self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1

        # Update error rates
        current_time = time.time()
        minute_key = int(current_time // 60)
        if minute_key not in self.error_rates:
            self.error_rates[minute_key] = {}
        self.error_rates[minute_key][error_key] = self.error_rates[minute_key].get(error_key, 0) + 1

        # Clean up old error rates (keep last 60 minutes)
        cutoff_time = current_time - 3600
        cutoff_minute = int(cutoff_time // 60)
        self.error_rates = {k: v for k, v in self.error_rates.items() if k > cutoff_minute}

    def get_error_statistics(self) -> Dict[str, any]:
        """Get error statistics"""
        current_time = time.time()
        last_hour = current_time - 3600

        # Filter errors from last hour
        recent_errors = [e for e in self.errors if e.timestamp >= last_hour]

        # Count errors by type and severity
        error_breakdown = {}
        for error in recent_errors:
            key = f"{error.error_type.value}_{error.severity.value}"
            error_breakdown[key] = error_breakdown.get(key, 0) + 1

        # Calculate error rates
        total_errors = len(recent_errors)
        error_rate_per_minute = total_errors / 60 if total_errors > 0 else 0

        return {
            'total_errors_last_hour': total_errors,
            'error_rate_per_minute': error_rate_per_minute,
            'error_breakdown': error_breakdown,
            'recent_errors': [
                {
                    'type': e.error_type.value,
                    'severity': e.severity.value,
                    'message': e.message,
                    'timestamp': e.timestamp,
                    'player_id': e.player_id
                }
                for e in recent_errors[-10:]  # Last 10 errors
            ]
        }
```

### Error Monitoring Endpoints

**Error Statistics:**
```http
GET /monitoring/errors
```

**Response:**
```json
{
  "total_errors_last_hour": 25,
  "error_rate_per_minute": 0.42,
  "error_breakdown": {
    "connection_error_medium": 15,
    "authentication_error_high": 5,
    "message_delivery_error_low": 3,
    "system_error_critical": 2
  },
  "recent_errors": [
    {
      "type": "connection_error",
      "severity": "medium",
      "message": "WebSocket connection failed",
      "timestamp": 1704567300.0,
      "player_id": "test_player_1"
    },
    {
      "type": "authentication_error",
      "severity": "high",
      "message": "Invalid session token",
      "timestamp": 1704567280.0,
      "player_id": "test_player_2"
    }
  ]
}
```

## Logging Configuration

### Structured Logging Setup

```python
# server/logging_config.py
import structlog
import logging
import sys
from typing import Any, Dict

def configure_logging(log_level: str = "INFO", log_format: str = "json"):
    """Configure structured logging"""

    # Configure structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer() if log_format == "json" else structlog.dev.ConsoleRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )

    # Set up loggers for different components
    loggers = {
        'server': logging.getLogger('server'),
        'server.realtime': logging.getLogger('server.realtime'),
        'server.api': logging.getLogger('server.api'),
        'server.monitoring': logging.getLogger('server.monitoring'),
    }

    for logger in loggers.values():
        logger.setLevel(getattr(logging, log_level.upper()))

    return loggers

# Usage in application
loggers = configure_logging()
logger = loggers['server.realtime']
```

### Connection Logging

```python
# server/realtime/connection_manager.py
import structlog

logger = structlog.get_logger('server.realtime.connection_manager')

class ConnectionManager:
    async def connect_websocket(self, websocket, player_id: str, session_id: str = None):
        """Connect WebSocket with comprehensive logging"""
        connection_id = str(uuid.uuid4())
        start_time = time.time()

        try:
            # Log connection attempt
            logger.info(
                "WebSocket connection attempt",
                player_id=player_id,
                session_id=session_id,
                connection_id=connection_id,
                existing_connections=self._get_existing_connection_count(player_id)
            )

            # Establish connection
            await websocket.accept()

            # Log successful connection
            establishment_time = (time.time() - start_time) * 1000
            logger.info(
                "WebSocket connected",
                player_id=player_id,
                session_id=session_id,
                connection_id=connection_id,
                connection_type="websocket",
                establishment_time_ms=establishment_time,
                existing_sse_connections=len(self.active_sse_connections.get(player_id, [])),
                existing_websocket_connections=len(self.player_websockets.get(player_id, [])),
                is_dual_connection=self._is_dual_connection(player_id),
                total_connections=self._get_total_connection_count()
            )

            # Record performance metrics
            self.performance_monitor.record_connection_establishment('websocket', establishment_time)

            return True

        except Exception as e:
            # Log connection failure
            establishment_time = (time.time() - start_time) * 1000
            logger.error(
                "WebSocket connection failed",
                player_id=player_id,
                session_id=session_id,
                connection_id=connection_id,
                error=str(e),
                establishment_time_ms=establishment_time,
                exc_info=True
            )

            # Record error
            self.error_tracker.record_error(ErrorEvent(
                error_type=ErrorType.CONNECTION_ERROR,
                severity=ErrorSeverity.MEDIUM,
                message=f"WebSocket connection failed: {str(e)}",
                details={'player_id': player_id, 'session_id': session_id},
                timestamp=time.time(),
                player_id=player_id,
                session_id=session_id,
                connection_id=connection_id
            ))

            return False
```

### Message Delivery Logging

```python
async def send_personal_message(self, player_id: str, message: Dict[str, Any]) -> Dict[str, Any]:
    """Send message with comprehensive logging"""
    start_time = time.time()

    logger.info(
        "Message delivery attempt",
        player_id=player_id,
        message_type=message.get('type', 'unknown'),
        message_size=len(str(message))
    )

    try:
        # Send message logic...
        delivery_time = (time.time() - start_time) * 1000

        logger.info(
            "Message delivered",
            player_id=player_id,
            message_type=message.get('type', 'unknown'),
            delivery_time_ms=delivery_time,
            websocket_delivered=result['websocket_delivered'],
            sse_delivered=result['sse_delivered'],
            total_connections=result['total_connections'],
            active_connections=result['active_connections']
        )

        # Record performance metrics
        self.performance_monitor.record_message_delivery(delivery_time)

        return result

    except Exception as e:
        delivery_time = (time.time() - start_time) * 1000

        logger.error(
            "Message delivery failed",
            player_id=player_id,
            message_type=message.get('type', 'unknown'),
            error=str(e),
            delivery_time_ms=delivery_time,
            exc_info=True
        )

        # Record error
        self.error_tracker.record_error(ErrorEvent(
            error_type=ErrorType.MESSAGE_DELIVERY_ERROR,
            severity=ErrorSeverity.MEDIUM,
            message=f"Message delivery failed: {str(e)}",
            details={'player_id': player_id, 'message_type': message.get('type')},
            timestamp=time.time(),
            player_id=player_id
        ))

        raise
```

## Alerting Setup

### Prometheus Alert Rules

**mythos_alerts.yml:**
```yaml
groups:
- name: mythos_connection_alerts
  rules:
  - alert: HighConnectionFailureRate
    expr: rate(mythos_connection_failures_total[5m]) > 0.1
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "High connection failure rate detected"
      description: "Connection failure rate is {{ $value }} failures per second"

  - alert: LowConnectionHealth
    expr: mythos_connection_health_percentage < 90
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Connection health is low"
      description: "Connection health is {{ $value }}%"

  - alert: HighMemoryUsage
    expr: mythos_memory_usage_percent > 85
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High memory usage detected"
      description: "Memory usage is {{ $value }}%"

  - alert: HighErrorRate
    expr: rate(mythos_errors_total[5m]) > 0.05
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "High error rate detected"
      description: "Error rate is {{ $value }} errors per second"

- name: mythos_performance_alerts
  rules:
  - alert: SlowConnectionEstablishment
    expr: histogram_quantile(0.95, mythos_connection_establishment_seconds) > 2
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Slow connection establishment"
      description: "95th percentile connection establishment time is {{ $value }}s"

  - alert: SlowMessageDelivery
    expr: histogram_quantile(0.95, mythos_message_delivery_seconds) > 0.5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Slow message delivery"
      description: "95th percentile message delivery time is {{ $value }}s"
```

### Alertmanager Configuration

**alertmanager.yml:**
```yaml
global:
  smtp_smarthost: 'localhost:587'
  smtp_from: 'alerts@yourdomain.com'

route:
  group_by: ['alertname']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'web.hook'
  routes:
  - match:
      severity: critical
    receiver: 'critical-alerts'
  - match:
      severity: warning
    receiver: 'warning-alerts'

receivers:
- name: 'web.hook'
  webhook_configs:
  - url: 'http://localhost:5001/'

- name: 'critical-alerts'
  email_configs:
  - to: 'admin@yourdomain.com'
    subject: 'CRITICAL: {{ .GroupLabels.alertname }}'
    body: |
      {{ range .Alerts }}
      Alert: {{ .Annotations.summary }}
      Description: {{ .Annotations.description }}
      {{ end }}
  slack_configs:
  - api_url: 'YOUR_SLACK_WEBHOOK_URL'
    channel: '#alerts'
    title: 'CRITICAL Alert'
    text: '{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}'

- name: 'warning-alerts'
  email_configs:
  - to: 'dev-team@yourdomain.com'
    subject: 'WARNING: {{ .GroupLabels.alertname }}'
    body: |
      {{ range .Alerts }}
      Alert: {{ .Annotations.summary }}
      Description: {{ .Annotations.description }}
      {{ end }}
```

## Dashboard Configuration

### Grafana Dashboard

**Connection Overview Dashboard:**
```json
{
  "dashboard": {
    "title": "MythosMUD Connection Overview",
    "panels": [
      {
        "title": "Total Connections",
        "type": "stat",
        "targets": [
          {
            "expr": "mythos_connections_total",
            "legendFormat": "Total Connections"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "thresholds": {
              "steps": [
                {"color": "green", "value": null},
                {"color": "yellow", "value": 100},
                {"color": "red", "value": 200}
              ]
            }
          }
        }
      },
      {
        "title": "Connection Health",
        "type": "gauge",
        "targets": [
          {
            "expr": "mythos_connection_health_percentage",
            "legendFormat": "Health %"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "min": 0,
            "max": 100,
            "thresholds": {
              "steps": [
                {"color": "red", "value": 0},
                {"color": "yellow", "value": 80},
                {"color": "green", "value": 95}
              ]
            }
          }
        }
      },
      {
        "title": "Connections by Type",
        "type": "piechart",
        "targets": [
          {
            "expr": "mythos_connections_by_type",
            "legendFormat": "{{type}}"
          }
        ]
      },
      {
        "title": "Connection Establishment Time",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.50, mythos_connection_establishment_seconds)",
            "legendFormat": "50th percentile"
          },
          {
            "expr": "histogram_quantile(0.95, mythos_connection_establishment_seconds)",
            "legendFormat": "95th percentile"
          }
        ]
      }
    ]
  }
}
```

### Custom Monitoring Panel

```typescript
// client/src/components/panels/MonitoringPanel.tsx
import React, { useState, useEffect } from 'react';

interface MonitoringData {
  connections: {
    total: number;
    healthy: number;
    unhealthy: number;
    health_percentage: number;
  };
  performance: {
    avg_response_time_ms: number;
    requests_per_second: number;
  };
  errors: {
    total_errors_last_hour: number;
    error_rate_per_minute: number;
  };
}

function MonitoringPanel() {
  const [data, setData] = useState<MonitoringData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [healthResponse, perfResponse, errorResponse] = await Promise.all([
          fetch('/monitoring/connection-health'),
          fetch('/monitoring/performance'),
          fetch('/monitoring/errors')
        ]);

        const [healthData, perfData, errorData] = await Promise.all([
          healthResponse.json(),
          perfResponse.json(),
          errorResponse.json()
        ]);

        setData({
          connections: healthData.overall_health,
          performance: perfData.system_performance,
          errors: errorData
        });
      } catch (error) {
        console.error('Failed to fetch monitoring data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 30000); // Update every 30 seconds

    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return <div>Loading monitoring data...</div>;
  }

  if (!data) {
    return <div>Failed to load monitoring data</div>;
  }

  return (
    <div className="monitoring-panel">
      <h3>System Monitoring</h3>

      <div className="metrics-grid">
        <div className="metric-card">
          <h4>Connection Health</h4>
          <div className="metric-value">
            {data.connections.health_percentage.toFixed(1)}%
          </div>
          <div className="metric-details">
            {data.connections.healthy} / {data.connections.total} healthy
          </div>
        </div>

        <div className="metric-card">
          <h4>Response Time</h4>
          <div className="metric-value">
            {data.performance.avg_response_time_ms.toFixed(1)}ms
          </div>
          <div className="metric-details">
            {data.performance.requests_per_second.toFixed(1)} req/s
          </div>
        </div>

        <div className="metric-card">
          <h4>Error Rate</h4>
          <div className="metric-value">
            {data.errors.error_rate_per_minute.toFixed(2)}/min
          </div>
          <div className="metric-details">
            {data.errors.total_errors_last_hour} errors (last hour)
          </div>
        </div>
      </div>
    </div>
  );
}

export default MonitoringPanel;
```

## Troubleshooting

### Common Monitoring Issues

**1. Metrics Not Appearing:**
```bash
# Check if metrics endpoint is accessible
curl http://localhost:9090/metrics

# Check Prometheus configuration
curl http://localhost:9090/api/v1/targets

# Check if application is exposing metrics
curl http://localhost:8000/monitoring/performance
```

**2. High Memory Usage:**
```bash
# Check memory usage
ps aux | grep python
htop

# Check for memory leaks
python -m memory_profiler server/main.py

# Monitor memory metrics
curl http://localhost:8000/monitoring/performance | jq '.system_performance.memory_usage_mb'
```

**3. Slow Performance:**
```bash
# Check response times
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:8000/health

# Check connection establishment times
curl http://localhost:8000/monitoring/performance | jq '.connection_establishment'

# Check database performance
psql mythos_prod -c "SELECT * FROM pg_stat_activity WHERE state = 'active';"
```

### Log Analysis

**1. Error Analysis:**
```bash
# Count errors by type
grep "ERROR" logs/mythos.log | jq -r '.error_type' | sort | uniq -c

# Find recent errors
grep "ERROR" logs/mythos.log | tail -50

# Analyze error patterns
grep "connection_error" logs/mythos.log | jq -r '.player_id' | sort | uniq -c
```

**2. Performance Analysis:**
```bash
# Check connection establishment times
grep "WebSocket connected" logs/mythos.log | jq -r '.establishment_time_ms' | sort -n

# Check message delivery times
grep "Message delivered" logs/mythos.log | jq -r '.delivery_time_ms' | sort -n

# Check for slow operations
grep "establishment_time_ms" logs/mythos.log | jq 'select(.establishment_time_ms > 1000)'
```

**3. Connection Analysis:**
```bash
# Count connections by type
grep "connected" logs/mythos.log | jq -r '.connection_type' | sort | uniq -c

# Check dual connection usage
grep "is_dual_connection" logs/mythos.log | jq -r '.is_dual_connection' | sort | uniq -c

# Analyze connection patterns
grep "WebSocket connected" logs/mythos.log | jq -r '.player_id' | sort | uniq -c
```

### Performance Optimization

**1. Connection Pool Tuning:**
```python
# Adjust connection pool settings
CONNECTION_POOL_SIZE = 1000  # Increase for high load
MAX_CONNECTIONS_PER_PLAYER = 2  # Reduce for resource conservation
CONNECTION_TIMEOUT = 180  # Reduce for faster cleanup
```

**2. Database Optimization:**
```sql
-- Add indexes for better performance
CREATE INDEX CONCURRENTLY idx_connections_player_session ON connections(player_id, session_id);
CREATE INDEX CONCURRENTLY idx_connections_created_at ON connections(created_at);

-- Analyze query performance
EXPLAIN ANALYZE SELECT * FROM connections WHERE player_id = 'test_player';
```

**3. Memory Optimization:**
```python
# Adjust metrics collection frequency
METRICS_COLLECTION_INTERVAL = 30  # seconds
MAX_METRICS_SAMPLES = 1000  # Reduce for memory conservation

# Enable garbage collection
import gc
gc.set_threshold(700, 10, 10)
```

---

*This monitoring guide is maintained as part of the MythosMUD dual connection system implementation. Last updated: 2025-01-06*
