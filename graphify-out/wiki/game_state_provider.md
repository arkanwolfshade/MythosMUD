# game state provider

> 10 nodes

## Key Concepts

- **test_game_state_provider.py** (41 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **mock_get_async_persistence()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_to_names()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_get_fallback_player_data_json_stats()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **test_convert_room_uuids_with_npcs()** (2 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Unit tests for game state provider.  Tests the GameStateProvider class.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Create a mock get_async_persistence callback.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() converts UUIDs to names.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test _get_fallback_player_data() parses JSON stats string.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`
- **Test convert_room_uuids_to_names() converts NPC IDs to display names.** (1 connections) — `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Relationships

- [npc aggressive mob](npc_aggressive_mob.md) (3 shared connections)
- [realtime player event](realtime_player_event.md) (3 shared connections)
- [room toolkit validator](room_toolkit_validator.md) (3 shared connections)
- [command factories create](command_factories_create.md) (2 shared connections)
- [command player state](command_player_state.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [persistence damage player()](persistence_damage_player%28%29.md) (1 shared connections)
- [persistence heal player()](persistence_heal_player%28%29.md) (1 shared connections)
- [archive 2025 REMEDIATION](archive_2025_REMEDIATION.md) (1 shared connections)
- [models profession available](models_profession_available.md) (1 shared connections)
- [player realtime event](player_realtime_event.md) (1 shared connections)
- [infrastructure security rationale](infrastructure_security_rationale.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*