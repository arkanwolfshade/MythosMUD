# test_player_death_service.py

> 117 nodes

## Key Concepts

- **test_player_death_service.py** (53 connections) — `server/tests/unit/services/test_player_death_service.py`
- **asyncio** (26 connections)
- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **.initialize()** (8 connections) — `server/container/bundles/combat.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **fixture** (7 connections)
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **._get_room_name_for_death()** (4 connections) — `server/services/player_death_service.py`
- **mock_player()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **AsyncSession** (4 connections)
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player_combat_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 92 more nodes in this community*

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (13 shared connections)
- [ConnectionManager](ConnectionManager.md) (9 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (2 shared connections)
- [PlayerRespawnService](PlayerRespawnService.md) (1 shared connections)
- [CatatoniaRegistry](CatatoniaRegistry.md) (1 shared connections)
- [test_passive_lucidity_flux_service.py](test_passive_lucidity_flux_service.py.md) (1 shared connections)
- [NPCStartupService](NPCStartupService.md) (1 shared connections)
- [test_lifespan_helpers.py](test_lifespan_helpers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 198 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*