# Alertmanager Monitoring Stack

> 31 nodes · cohesion 0.09

## Key Concepts

- **Prometheus Configuration** (9 connections) — `monitoring/prometheus.yml`
- **Alertmanager Configuration** (8 connections) — `monitoring/alertmanager.yml`
- **MythosMUD Prometheus Alert Rules** (8 connections) — `monitoring/mythos_alerts.yml`
- **MythosMUD Monitoring Stack** (7 connections) — `monitoring/docker-compose.monitoring.yml`
- **mythos_connection_alerts group** (4 connections) — `monitoring/mythos_alerts.yml`
- **connection-alerts receiver** (3 connections) — `monitoring/alertmanager.yml`
- **Alertmanager service** (3 connections) — `monitoring/docker-compose.monitoring.yml`
- **Prometheus service** (3 connections) — `monitoring/docker-compose.monitoring.yml`
- **ServiceDown alert** (3 connections) — `monitoring/mythos_alerts.yml`
- **mythos_system_alerts group** (3 connections) — `monitoring/mythos_alerts.yml`
- **performance-alerts receiver** (2 connections) — `monitoring/alertmanager.yml`
- **system-alerts receiver** (2 connections) — `monitoring/alertmanager.yml`
- **Node Exporter** (2 connections) — `monitoring/docker-compose.monitoring.yml`
- **mythos_memory_leak_alerts group** (2 connections) — `monitoring/mythos_alerts.yml`
- **mythos_performance_alerts group** (2 connections) — `monitoring/mythos_alerts.yml`
- **/monitoring/dual-connections endpoint** (2 connections) — `monitoring/prometheus.yml`
- **/monitoring/memory-leaks endpoint** (2 connections) — `monitoring/prometheus.yml`
- **mythos-server scrape job** (2 connections) — `monitoring/prometheus.yml`
- **critical-alerts receiver** (1 connections) — `monitoring/alertmanager.yml`
- **Critical inhibits warning alerts** (1 connections) — `monitoring/alertmanager.yml`
- **maintenance-window time interval** (1 connections) — `monitoring/alertmanager.yml`
- **warning-alerts receiver** (1 connections) — `monitoring/alertmanager.yml`
- **Grafana service** (1 connections) — `monitoring/docker-compose.monitoring.yml`
- **PostgreSQL Exporter** (1 connections) — `monitoring/docker-compose.monitoring.yml`
- **Redis Exporter** (1 connections) — `monitoring/docker-compose.monitoring.yml`
- *... and 6 more nodes in this community*

## Relationships

- No strong cross-community connections detected

## Source Files

- `monitoring/alertmanager.yml`
- `monitoring/docker-compose.monitoring.yml`
- `monitoring/mythos_alerts.yml`
- `monitoring/prometheus.yml`

## Audit Trail

- EXTRACTED: 64 (80%)
- INFERRED: 16 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
