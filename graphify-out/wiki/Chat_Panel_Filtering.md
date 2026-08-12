# Chat Panel Filtering

> 84 nodes

## Key Concepts

- **test_player_death_service.py** (52 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_publish_death_event_with_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_event_bus()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player_combat_service()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_session()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **sample_player_id()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_player_death_service_init_no_dependencies()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_empty()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_finds_mortally_wounded()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_healthy()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_excludes_dead()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_mortally_wounded_players_handles_error()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_empty()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_finds_dead()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_excludes_alive()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_get_dead_players_handles_error()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_player_not_found()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_already_dead()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_applies_decay()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_caps_at_negative_10()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_changes_posture_to_lying()** (2 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 59 more nodes in this community*

## Relationships

- [Character Creation E2E](Character_Creation_E2E.md) (4 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Commands Look Item](Commands_Look_Item.md) (1 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 178 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*