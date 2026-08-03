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

- [room infrastructure persistence](room_infrastructure_persistence.md) (16 shared connections)
- [infrastructure persistence room](infrastructure_persistence_room.md) (9 shared connections)
- [skill game service](skill_game_service.md) (4 shared connections)
- [command utility models](command_utility_models.md) (2 shared connections)
- [game skill service](game_skill_service.md) (2 shared connections)
- [infrastructure persistence core](infrastructure_persistence_core.md) (1 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/integration/test_game_state_provider.py`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*