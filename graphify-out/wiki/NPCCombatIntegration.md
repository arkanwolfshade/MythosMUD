# NPCCombatIntegration

> 73 nodes

## Key Concepts

- **build_event()** (85 connections) — `server/realtime/envelope.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **rest_countdown_task.py** (13 connections) — `server/commands/rest_countdown_task.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **create_rest_countdown_task()** (7 connections) — `server/commands/rest_countdown_task.py`
- **_handle_countdown_loop()** (6 connections) — `server/commands/rest_countdown_task.py`
- **_send_countdown_message()** (6 connections) — `server/commands/rest_countdown_task.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **UUID** (6 connections)
- **_disconnect_player_after_rest()** (5 connections) — `server/commands/rest_countdown_task.py`
- **_is_rest_interrupted()** (5 connections) — `server/commands/rest_countdown_task.py`
- **Any** (5 connections)
- **_SupportsEventSequence** (4 connections) — `server/realtime/envelope.py`
- **.handle_player_dp_decay()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **test_build_event_json_serializable()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_sequence_priority()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_with_connection_manager()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_uuid_encoder_handles_other_types()** (4 connections) — `server/tests/unit/realtime/test_envelope.py`
- **_get_next_global_sequence()** (3 connections) — `server/realtime/envelope.py`
- **test_build_event_all_parameters()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_basic()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_empty_data()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_no_data_parameter()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_build_event_optional_parameters_none()** (3 connections) — `server/tests/unit/realtime/test_envelope.py`
- *... and 48 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (18 shared connections)
- [NPCDefinition](NPCDefinition.md) (10 shared connections)
- [npc_database.py](npc_database.py.md) (6 shared connections)
- [pytest.md](pytest.md.md) (5 shared connections)
- [chat_channel_message_senders.py](chat_channel_message_senders.py.md) (4 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (3 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (3 shared connections)
- [test_websocket_handler_validation_errors.py](test_websocket_handler_validation_errors.py.md) (3 shared connections)
- [utils/layout.ts](utils-layout.ts.md) (3 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (3 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (3 shared connections)
- [PopulationStats](PopulationStats.md) (3 shared connections)

## Source Files

- `server/commands/rest_countdown_task.py`
- `server/realtime/envelope.py`
- `server/realtime/player_event_handlers_state.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 204 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*