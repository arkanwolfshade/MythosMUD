# server tests unit realtime test

> 19 nodes

## Key Concepts

- **test_message_builders.py** (15 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **_builder()** (8 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_entered_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_player_left_message()** (4 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_occupants_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_state_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_build_room_update_message()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_create_npc_movement_message_variants()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_non_callable_returns_zero()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **test_get_next_sequence_uses_callable()** (3 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Unit tests for MessageBuilder.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Sequence counter callable is invoked.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Non-callable sequence counter returns 0.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Player entered message includes ids and player name.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Player left message includes ids and player name.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **NPC movement messages cover direction and movement type branches.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Occupants update includes structured and legacy fields.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Room update wraps room data without occupants.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`
- **Room state includes occupants from room_data.** (1 connections) — `server/tests/unit/realtime/test_message_builders.py`

## Relationships

- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_builders.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*