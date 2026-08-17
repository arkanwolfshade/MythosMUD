# CombatDeathHandler

> 24 nodes

## Key Concepts

- **CombatDeathHandler** (20 connections) — `server/services/combat_death_handler.py`
- **_CombatServiceDeps** (6 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (6 connections) — `server/services/combat_death_handler.py`
- **_ConnectionManagerLike** (5 connections) — `server/services/combat_death_handler.py`
- **._resolve_connection_manager_for_corpse_creation()** (5 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.canonical_room_id()** (2 connections) — `server/services/combat_death_handler.py`
- **UUID** (2 connections)
- **Publish NPC death event to NATS when combat publisher is available.** (1 connections) — `server/services/combat_death_handler.py`
- **Connection manager surface used for room subscriber diagnostics.** (1 connections) — `server/services/combat_death_handler.py`
- **Return canonical room id when available.** (1 connections) — `server/services/combat_death_handler.py`
- **UUID mapping surface used to resolve NPC string ids.** (1 connections) — `server/services/combat_death_handler.py`
- **Return original NPC id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **Minimal CombatService surface required by CombatDeathHandler.** (1 connections) — `server/services/combat_death_handler.py`
- **Return NPC combat integration service when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPCDiedEvent to NATS.** (1 connections) — `server/services/combat_death_handler.py`
- **Handles combat death events and state changes.** (1 connections) — `server/services/combat_death_handler.py`
- **Initialize the death handler. Args: combat_service: Reference to the parent…** (1 connections) — `server/services/combat_death_handler.py`
- **Return connection manager from CombatService getter when exposed.** (1 connections) — `server/services/combat_death_handler.py`

## Relationships

- [CombatInstance](CombatInstance.md) (10 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [test_combat_death_handler.py](test_combat_death_handler.py.md) (2 shared connections)
- [NATSError](NATSError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (1 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 43 (84%)
- INFERRED: 8 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*