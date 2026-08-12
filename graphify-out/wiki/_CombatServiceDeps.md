# _CombatServiceDeps

> 16 nodes

## Key Concepts

- **_CombatServiceDeps** (10 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (9 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (8 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.canonical_room_id()** (2 connections) — `server/services/combat_death_handler.py`
- **UUID** (2 connections)
- **Connection manager surface used for room subscriber diagnostics.** (1 connections) — `server/services/combat_death_handler.py`
- **Return canonical room id when available.** (1 connections) — `server/services/combat_death_handler.py`
- **UUID mapping surface used to resolve NPC string ids.** (1 connections) — `server/services/combat_death_handler.py`
- **Return original NPC id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **Minimal CombatService surface required by CombatDeathHandler.** (1 connections) — `server/services/combat_death_handler.py`
- **Return NPC combat integration service when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPCDiedEvent to NATS.** (1 connections) — `server/services/combat_death_handler.py`

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (3 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 36 (73%)
- INFERRED: 13 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*