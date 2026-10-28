# NPCPopulationController

> 124 nodes · cohesion 0.02

## Key Concepts

- **test_nats_message_handler.py** (72 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **asyncio** (55 connections)
- **test_handle_nats_message_attribute_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_circuit_breaker_open()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_connection_manager_resolution_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_dlq_on_final_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_unknown_message_id_defaults()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_validation_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_message_with_retry_exhaustion()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_process_single_message_uuid_conversion_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_start_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_stop_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_event_subjects_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_nats_subscribe_error_handled()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_standardized_chat_subjects_partial_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_failure()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_subscribe_to_subject_nats_error_returns_false()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_error()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_unsubscribe_from_subject_not_found()** (4 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_property_injected_returns_none()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_connection_manager_setter_updates_helpers()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_event_data_detection()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_event_type_detection()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- **test_handle_nats_message_retry_on_failure()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler.py`
- *... and 99 more nodes in this community*

## Relationships

- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (9 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (3 shared connections)
- [test_rate_overrides.py](test_rate_overrides.py.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [security.ts](security.ts.md) (2 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_nats_message_handler.py`

## Audit Trail

- EXTRACTED: 190 (91%)
- INFERRED: 19 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*