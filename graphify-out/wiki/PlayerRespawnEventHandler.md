# PlayerRespawnEventHandler

> 39 nodes

## Key Concepts

- **CorpseLifecycleService** (23 connections) — `server/services/corpse_lifecycle_service.py`
- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (9 connections) — `server/services/combat_death_handler.py`
- **.get_decayed_corpses_in_room()** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **ContainerComponent** (5 connections)
- **.get_all_decayed_corpses()** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.can_access_corpse()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.is_corpse_decayed()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_decayed_corpses_in_room()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **.cleanup_all_decayed_corpses()** (4 connections) — `server/services/corpse_lifecycle_service.py`
- **Protocol** (3 connections)
- **.canonical_room_id()** (3 connections) — `server/services/combat_death_handler.py`
- **UUID** (3 connections)
- **.get_npc_combat_integration_service()** (3 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (3 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/corpse_lifecycle_service.py`
- **corpse_service()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **Connection manager surface used for room subscriber diagnostics.** (1 connections) — `server/services/combat_death_handler.py`
- **Return canonical room id when available.** (1 connections) — `server/services/combat_death_handler.py`
- **UUID mapping surface used to resolve NPC string ids.** (1 connections) — `server/services/combat_death_handler.py`
- **Return original NPC id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- *... and 14 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (14 shared connections)
- [Room](Room.md) (13 shared connections)
- [Any](Any.md) (6 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (4 shared connections)
- [Protocol](Protocol.md) (2 shared connections)
- [test container persistence sql injection](test_container_persistence_sql_injection.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`
- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 112 (85%)
- INFERRED: 20 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*