# commands communication flows

> 89 nodes

## Key Concepts

- **test_communication_commands_flows.py** (41 connections) — `server/tests/unit/commands/test_communication_commands_flows.py`
- **communication_commands_flows.py** (33 connections) — `server/commands/communication_commands_flows.py`
- **communication_commands.py** (31 connections) — `server/commands/communication_commands.py`
- **ChatCommandsProtocol** (18 connections) — `server/commands/communication_commands_support.py`
- **communication_commands_support.py** (16 connections) — `server/commands/communication_commands_support.py`
- **PlayerResolutionProtocol** (16 connections) — `server/commands/communication_commands_support.py`
- **_chat_send_with_room_bundle()** (14 connections) — `server/commands/communication_commands_flows.py`
- **flow_global_command()** (12 connections) — `server/commands/communication_commands_flows.py`
- **_message_from_command()** (11 connections) — `server/commands/communication_commands_flows.py`
- **_RoomChannelOutcomeConfig** (11 connections) — `server/commands/communication_commands_flows.py`
- **chat_result_map()** (11 connections) — `server/commands/communication_commands_support.py`
- **message_id_from_result()** (11 connections) — `server/commands/communication_commands_support.py`
- **_require_chat_pair()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_say_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **flow_reply_command()** (10 connections) — `server/commands/communication_commands_flows.py`
- **_str_error_from_chat_result()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_room_player_bundle()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_system_send_if_admin()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_system_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **flow_whisper_command()** (9 connections) — `server/commands/communication_commands_flows.py`
- **_global_player_bundle()** (8 connections) — `server/commands/communication_commands_flows.py`
- **flow_local_command()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_whisper_id_pair_or_error()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_whisper_message()** (8 connections) — `server/commands/communication_commands_flows.py`
- **_deliver_reply_to_last_whisper()** (8 connections) — `server/commands/communication_commands_flows.py`
- *... and 64 more nodes in this community*

## Relationships

- [rate limiter services](rate_limiter_services.md) (30 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (7 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [commands whisper command](commands_whisper_command.md) (6 shared connections)
- [message nats handler](message_nats_handler.md) (5 shared connections)
- [commands admin mute](commands_admin_mute.md) (2 shared connections)
- [commands party examples](commands_party_examples.md) (1 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (1 shared connections)
- [player cache rationale](player_cache_rationale.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands.py`
- `server/commands/communication_commands_flows.py`
- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_flows.py`

## Audit Trail

- EXTRACTED: 461 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*