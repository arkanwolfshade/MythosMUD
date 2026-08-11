# Dual Connection Troubleshooting

> 17 nodes

## Key Concepts

- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **AlertSeverity** (5 connections) — `server/services/combat_monitoring_service.py`
- **AlertType** (5 connections) — `server/services/combat_monitoring_service.py`
- **.record_combat_error()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_error_threshold()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **Enum** (3 connections)
- **.update_resource_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._check_performance_threshold()** (3 connections) — `server/services/combat_monitoring_service.py`
- **Alert severity levels.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Alert types for combat monitoring.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Record a combat error.          Args:             error_type: Type of error (val** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update resource usage metrics.          Args:             memory_mb: Memory usag** (1 connections) — `server/services/combat_monitoring_service.py`
- **Check if error threshold has been exceeded.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Check resource usage thresholds.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Check if performance threshold has been exceeded.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Generate and dispatch an alert.** (1 connections) — `server/services/combat_monitoring_service.py`

## Relationships

- [Combat Monitoring Service](Combat_Monitoring_Service.md) (6 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (4 shared connections)
- [Rate Limiter Service](Rate_Limiter_Service.md) (2 shared connections)
- [Archive Planning Aliases](Archive_Planning_Aliases.md) (2 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*