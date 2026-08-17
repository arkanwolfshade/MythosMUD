# server services corpse lifecycle service

> 25 nodes

## Key Concepts

- **CorpseLifecycleService** (21 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (9 connections)
- **.cleanup_decayed_corpse()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse_on_death()** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (7 connections)
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._persist_corpse()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **._build_corpse_component()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.can_access_corpse()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **._grace_period_allows_others()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Create a corpse container when a player dies.** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **True if player may access corpse (owner/admin always; others after grace).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Check if a corpse container has decayed. Args: corpse: Corpse container to…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Get all decayed corpse containers in a room. Args: room_id: Room ID to check…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Delete a decayed corpse container (items discarded with the container).** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clean up all decayed corpse containers in a room. Args: room_id: Room ID to…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Get all decayed corpse containers across all rooms. Returns:…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Clean up all decayed corpse containers across all rooms. Returns: int: Number…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Service for managing corpse container lifecycle. Handles creation on death,…** (1 connections) — `server/services/corpse_lifecycle_service.py`
- **Test CorpseLifecycleService initialization fails without persistence.** (1 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Relationships

- [server services corpse lifecycle service](server_services_corpse_lifecycle_service.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (3 shared connections)
- [server tests unit services test](server_tests_unit_services_test.md) (3 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 60 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*