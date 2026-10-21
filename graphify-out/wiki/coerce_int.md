# coerce_int

> 43 nodes · cohesion 0.09

## Key Concepts

- **PersonalMessageSender** (24 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (17 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **personal_message_sender.py** (16 connections) — `server/realtime/messaging/personal_message_sender.py`
- **asyncio** (10 connections)
- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (8 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **server/realtime/messaging/__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **_coerce_player_uuid()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **sender()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_prepare_payload_too_large()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_when_player_id_is_a_string()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_fans_out_to_all_listed_sockets()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_outer_exception()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_reports_failure_for_non_uuid_player_id()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_empty_runtime_error_is_debug()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_get_delivery_stats()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_via_websocket()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_queues_when_offline()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- *... and 18 more nodes in this community*

## Relationships

- [test_quest_service.py](test_quest_service.py.md) (4 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [authenticated.ts](authenticated.ts.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (2 shared connections)
- [processing.py](processing.py.md) (2 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (2 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)
- [test_game.py](test_game.py.md) (1 shared connections)
- [_find_item_in_inventory](_find_item_in_inventory.md) (1 shared connections)
- [look_container.py](look_container.py.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 89 (84%)
- INFERRED: 17 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*