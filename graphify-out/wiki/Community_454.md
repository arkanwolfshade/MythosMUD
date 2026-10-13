# Community 454

> 39 nodes

## Key Concepts

- **PlayerDeathService** (26 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (11 connections) — `server/services/player_death_service.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **._publish_death_event()** (6 connections) — `server/services/player_death_service.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (5 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._persist_death_location_stats()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **Player** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Exception** (1 connections)
- **BoundLogger** (1 connections)
- **Get all players who are dead (DP <= -10). Args: session: Async database session…** (1 connections) — `server/services/player_death_service.py`
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (8 shared connections)
- [Community 108](Community_108.md) (5 shared connections)
- [Community 564](Community_564.md) (5 shared connections)
- [Community 130](Community_130.md) (2 shared connections)
- [Community 88](Community_88.md) (2 shared connections)
- [Community 317](Community_317.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (2 shared connections)
- [API Response Models](API_Response_Models.md) (1 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (1 shared connections)
- [Community 92](Community_92.md) (1 shared connections)
- [Community 460](Community_460.md) (1 shared connections)
- [Community 226](Community_226.md) (1 shared connections)

## Source Files

- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 85 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*