# test room service

> 14 nodes

## Key Concepts

- **test_room_service.py** (56 connections) — `server/tests/unit/game/test_room_service.py`
- **test_validate_room_exists_cache_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_occupants_cache_not_found()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_with_sub_zone()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_list_rooms_exclude_exits()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_get_room_info_success()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **test_describe_lighting_unknown_daypart()** (2 connections) — `server/tests/unit/game/test_room_service.py`
- **Unit tests for room service.  Tests the RoomService class for room-related opera** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test validate_room_exists() returns False when room not in cache.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_occupants() returns empty list when room not found.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() filters by sub_zone.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test list_rooms() excludes exits when include_exits=False.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test get_room_info() returns comprehensive room information.** (1 connections) — `server/tests/unit/game/test_room_service.py`
- **Test describe_lighting() returns default for unknown daypart.** (1 connections) — `server/tests/unit/game/test_room_service.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [Test evaluate boolean condition() handles](Test_evaluate_boolean_condition%28%29_handles.md) (2 shared connections)
- [Test extract chat message fields](Test_extract_chat_message_fields.md) (2 shared connections)
- [Test add rule() returns False](Test_add_rule%28%29_returns_False.md) (1 shared connections)
- [Test execute applicable rules() returns](Test_execute_applicable_rules%28%29_returns.md) (1 shared connections)
- [SafeHtml](SafeHtml.md) (1 shared connections)
- [room_service_with_cache](room_service_with_cache.md) (1 shared connections)
- [Test delete player returns False](Test_delete_player_returns_False.md) (1 shared connections)
- [Test setup connection metadata() creates](Test_setup_connection_metadata%28%29_creates.md) (1 shared connections)
- [test_describe_lighting_night](test_describe_lighting_night.md) (1 shared connections)
- [Test evaluate boolean condition() treats](Test_evaluate_boolean_condition%28%29_treats.md) (1 shared connections)
- [Test add rule() replaces existing](Test_add_rule%28%29_replaces_existing.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_room_service.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*