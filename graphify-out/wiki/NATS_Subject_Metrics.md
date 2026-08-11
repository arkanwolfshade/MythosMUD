# NATS Subject Metrics

> 27 nodes

## Key Concepts

- **Any** (10 connections)
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect all metrics from all sources.          Returns:             Dictionary c** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect connection metrics from ConnectionManager.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect event metrics from EventBus.          Returns:             Dictionary wi** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager.          Returns:             Dictionar** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect task metrics from TaskRegistry.          Returns:             Dictionary** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect NATS subscription metrics from NATSService.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rate for a single metric.          Args:             current: C** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Calculate growth rates for metrics over time.          Returns:             Dict** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check connection-related alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check subscriber growth rate alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Check cache-related alerts and append to alerts list.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 2 more nodes in this community*

## Relationships

- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (13 shared connections)
- [NPC Occupant Verification](NPC_Occupant_Verification.md) (2 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (1 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (1 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 87 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*