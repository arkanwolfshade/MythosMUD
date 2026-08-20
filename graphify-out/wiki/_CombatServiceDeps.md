# _CombatServiceDeps

> 12 nodes

## Key Concepts

- **_CombatServiceDeps** (8 connections) — `server/services/combat_death_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_death_handler.py`
- **.get_npc_combat_integration_service()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_player_died_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **.publish_player_mortally_wounded_event_to_nats()** (2 connections) — `server/services/combat_death_handler.py`
- **Minimal CombatService surface required by CombatDeathHandler.** (1 connections) — `server/services/combat_death_handler.py`
- **Return NPC combat integration service when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPCDiedEvent to NATS.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish PlayerDiedEvent to NATS (#634).** (1 connections) — `server/services/combat_death_handler.py`
- **Publish PlayerMortallyWoundedEvent to NATS (#634).** (1 connections) — `server/services/combat_death_handler.py`
- **Initialize the death handler. Args: combat_service: Reference to the parent…** (1 connections) — `server/services/combat_death_handler.py`

## Relationships

- [NATSError](NATSError.md) (3 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*