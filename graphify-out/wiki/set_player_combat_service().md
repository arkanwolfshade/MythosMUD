# .set player combat service()

> 151 nodes

## Key Concepts

- **PlayerCombatService** (73 connections) — `server/services/player_combat_service.py`
- **test_player_combat_service.py** (37 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **player_combat_service.py** (34 connections) — `server/services/player_combat_service.py`
- **player_combat_service_support.py** (19 connections) — `server/services/player_combat_service_support.py`
- **UUID** (15 connections)
- **PlayerCombatState** (14 connections) — `server/services/player_combat_service.py`
- **NPCCombatIntegrationReadApi** (10 connections) — `server/services/player_combat_service_support.py`
- **EventBusPublish** (9 connections) — `server/services/player_combat_service_support.py`
- **PlayerXpLike** (9 connections) — `server/services/player_combat_service_support.py`
- **._award_xp_via_persistence_fallback()** (7 connections) — `server/services/player_combat_service.py`
- **.award_xp_on_npc_death()** (6 connections) — `server/services/player_combat_service.py`
- **Protocol** (6 connections)
- **NPCCombatRewardsLike** (6 connections) — `server/services/player_combat_service_support.py`
- **UUIDMappingXP** (6 connections) — `server/services/player_combat_service_support.py`
- **PersistenceWithNpcLifecycleManager** (6 connections) — `server/services/player_combat_service_support.py`
- **.track_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **.clear_player_combat_state()** (5 connections) — `server/services/player_combat_service.py`
- **._get_xp_from_lifecycle_manager()** (5 connections) — `server/services/player_combat_service.py`
- **original_string_id_for_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **lifecycle_lookup_id()** (5 connections) — `server/services/player_combat_service_support.py`
- **async_load_lifecycle_manager()** (5 connections) — `server/services/player_combat_service_support.py`
- **log_missing_lifecycle_npc()** (5 connections) — `server/services/player_combat_service_support.py`
- **player_combat_service()** (5 connections) — `server/tests/unit/services/test_player_combat_service.py`
- **.get_player_combat_state()** (4 connections) — `server/services/player_combat_service.py`
- **.handle_combat_start()** (4 connections) — `server/services/player_combat_service.py`
- *... and 126 more nodes in this community*

## Relationships

- [Any](Any.md) (16 shared connections)
- [. repr ()](_repr_%28%29.md) (11 shared connections)
- [Player Position Service](Player_Position_Service.md) (10 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (7 shared connections)
- [. init ()](_init_%28%29.md) (7 shared connections)
- [main()](main%28%29.md) (6 shared connections)
- [.initialize()](initialize%28%29.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (3 shared connections)
- [UUID](UUID.md) (1 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (1 shared connections)
- [. apply player info()](_apply_player_info%28%29.md) (1 shared connections)
- [.store npc xp mapping for](store_npc_xp_mapping_for.md) (1 shared connections)

## Source Files

- `server/services/combat_service.py`
- `server/services/player_combat_service.py`
- `server/services/player_combat_service_support.py`
- `server/tests/unit/services/test_player_combat_service.py`

## Audit Trail

- EXTRACTED: 498 (93%)
- INFERRED: 37 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*