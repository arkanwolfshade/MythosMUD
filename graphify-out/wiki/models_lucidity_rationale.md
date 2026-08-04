# models lucidity rationale

> 96 nodes

## Key Concepts

- **PerformanceMonitor** (32 connections) — `server/monitoring/performance_monitor.py`
- **websocket_integration.py** (22 connections) — `docs/examples/logging/websocket_integration.py`
- **measure_performance()** (22 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (21 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (18 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (15 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (9 connections) — `server/monitoring/performance_monitor.py`
- **handle_websocket_message()** (8 connections) — `docs/examples/logging/websocket_integration.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **WebSocketManager** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_endpoint()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **.send_text()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **reset_performance_metrics()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.disconnect()** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_game_action()** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **chat_service** (6 connections) — `docs/examples/logging/websocket_integration.py`
- **Any** (6 connections)
- **.get_operation_stats()** (6 connections) — `server/monitoring/performance_monitor.py`
- **.connect()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **handle_chat_message()** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **WebSocket** (5 connections) — `docs/examples/logging/websocket_integration.py`
- **.get_all_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- *... and 71 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (8 shared connections)
- [world loader room](world_loader_room.md) (5 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (5 shared connections)
- [examples logging testing](examples_logging_testing.md) (4 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (4 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (3 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (3 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [commands emote rationale](commands_emote_rationale.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 371 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*