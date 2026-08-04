# rate limiter services

> 27 nodes

## Key Concepts

- **test_communication_commands_support.py** (21 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **get_services_from_container()** (15 connections) — `server/commands/communication_commands_support.py`
- **primary_id()** (13 connections) — `server/commands/communication_commands_support.py`
- **app_from_request()** (12 connections) — `server/commands/communication_commands_support.py`
- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **.get_player_by_name()** (2 connections) — `server/commands/communication_commands_support.py`
- **.save_player()** (2 connections) — `server/commands/communication_commands_support.py`
- **test_app_from_request_none()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_app_from_request_with_app()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_primary_id_prefers_id()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_primary_id_falls_back_to_player_id()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_services_from_container_no_app()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_services_from_container_via_container()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_services_from_container_state_fallback()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_pose_persistence_from_container()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_pose_persistence_state_fallback()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_chat_result_map_dict()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_chat_result_map_non_dict()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_message_id_from_result_nested()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_message_id_from_result_no_id()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **Minimal persistence for pose read/write in emote/pose flows.** (1 connections) — `server/commands/communication_commands_support.py`
- **Return ``request.app`` if present, else None.** (1 connections) — `server/commands/communication_commands_support.py`
- **Resolve id or player_id from a player-like object without propagating Any.** (1 connections) — `server/commands/communication_commands_support.py`
- **Get services from container with backward compatibility fallback.      Args:** (1 connections) — `server/commands/communication_commands_support.py`
- *... and 2 more nodes in this community*

## Relationships

- [commands communication flows](commands_communication_flows.md) (30 shared connections)
- [player cache rationale](player_cache_rationale.md) (6 shared connections)
- [inventory commands command](inventory_commands_command.md) (2 shared connections)
- [message nats handler](message_nats_handler.md) (2 shared connections)
- [nats services metrics](nats_services_metrics.md) (2 shared connections)
- [models player related](models_player_related.md) (1 shared connections)
- [add hashed password](add_hashed_password.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 108 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*