# _CombatServiceDeps

> 20 nodes

## Key Concepts

- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (6 connections) — `server/services/combat_death_handler.py`
- **_NPCCombatIntegrationLike** (4 connections) — `server/services/combat_death_handler.py`
- **.get_original_string_id()** (4 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **Protocol** (3 connections)
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_player_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_player_mortally_wounded_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **UUID** (2 connections)
- **Resolve UUID participant id to canonical NPC string id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **UUID mapping surface used to resolve NPC string ids.** (1 connections) — `server/services/combat_death_handler.py`
- **Return original NPC id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **Minimal CombatService surface required by CombatDeathHandler.** (1 connections) — `server/services/combat_death_handler.py`
- **Return NPC combat integration service when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPCDiedEvent to NATS.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish PlayerDiedEvent to NATS (#634).** (1 connections) — `server/services/combat_death_handler.py`
- **Publish PlayerMortallyWoundedEvent to NATS (#634).** (1 connections) — `server/services/combat_death_handler.py`
- **Initialize the death handler. Args: combat_service: Reference to the parent…** (1 connections) — `server/services/combat_death_handler.py`

## Relationships

- [CombatService](CombatService.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*