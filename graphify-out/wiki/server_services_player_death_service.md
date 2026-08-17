# server services player death service

> 37 nodes

## Key Concepts

- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **_as_bound_logger()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **test_log_exception_once_logged_exception_uses_mark_logged()** (6 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **test_log_exception_once_plain_exception_sets_flag_and_skips_repeat()** (5 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **AsyncSession** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **Any** (3 connections)
- **Player** (3 connections)
- **.__init__()** (1 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **Exception** (1 connections)
- **BoundLogger** (1 connections)
- **Process DP decay for a single mortally wounded player. Decreases player DP by…** (1 connections) — `server/services/player_death_service.py`
- **Ensure player posture is set to lying when dead. Args: player: Player object to…** (1 connections) — `server/services/player_death_service.py`
- **Clear player combat state when they die. BUGFIX #244: As documented in…** (1 connections) — `server/services/player_death_service.py`
- *... and 12 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server events event types playerdiedevent](server_events_event_types_playerdiedevent.md) (7 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (2 shared connections)
- [server app lifespan](server_app_lifespan.md) (2 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (2 shared connections)
- [leveluphook](leveluphook.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (1 shared connections)
- [server container main applicationcontainer get](server_container_main_applicationcontainer_get.md) (1 shared connections)

## Source Files

- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 81 (91%)
- INFERRED: 8 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*