# services passive lucidity

> 15 nodes

## Key Concepts

- **._log_room_subscribers_before_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **._resolve_original_npc_id()** (8 connections) — `server/services/combat_death_handler.py`
- **._publish_npc_death_event()** (8 connections) — `server/services/combat_death_handler.py`
- **._handle_npc_death()** (8 connections) — `server/services/combat_death_handler.py`
- **.canonical_room_id()** (3 connections) — `server/services/combat_death_handler.py`
- **.get_npc_combat_integration_service()** (3 connections) — `server/services/combat_death_handler.py`
- **.publish_npc_died_event_to_nats()** (3 connections) — `server/services/combat_death_handler.py`
- **Return canonical room id when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Return NPC combat integration service when available.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPCDiedEvent to NATS.** (1 connections) — `server/services/combat_death_handler.py`
- **Best-effort connection diagnostics before publishing NPC death event.** (1 connections) — `server/services/combat_death_handler.py`
- **Resolve UUID participant id to canonical NPC string id when mapping exists.** (1 connections) — `server/services/combat_death_handler.py`
- **Publish NPC death event to NATS when combat publisher is available.** (1 connections) — `server/services/combat_death_handler.py`
- **Handle NPC death event publishing and ID resolution.** (1 connections) — `server/services/combat_death_handler.py`
- **Handle NPC death event publishing and ID resolution.          Args:** (1 connections) — `server/services/combat_death_handler.py`

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (6 shared connections)
- [command factories exploration](command_factories_exploration.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [message filtering realtime](message_filtering_realtime.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/services/combat_death_handler.py`

## Audit Trail

- EXTRACTED: 44 (90%)
- INFERRED: 5 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*