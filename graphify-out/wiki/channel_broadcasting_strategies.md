# channel broadcasting strategies

> 17 nodes

## Key Concepts

- **CombatIntegrationProtocol** (7 connections) — `server/npc/npc_protocols.py`
- **._handle_npc_death()** (6 connections) — `server/npc/npc_base.py`
- **.take_damage()** (5 connections) — `server/npc/npc_base.py`
- **._publish_damage_event()** (4 connections) — `server/npc/npc_base.py`
- **._schedule_end_combat_if_npc_died()** (4 connections) — `server/npc/npc_base.py`
- **npc_protocols.py** (4 connections) — `server/npc/npc_protocols.py`
- **._update_determination_points()** (3 connections) — `server/npc/npc_base.py`
- **Protocol** (2 connections)
- **.handle_npc_death()** (2 connections) — `server/npc/npc_protocols.py`
- **Update determination points after taking damage; return new DP.** (1 connections) — `server/npc/npc_base.py`
- **Publish damage event to event bus.** (1 connections) — `server/npc/npc_base.py`
- **Handle NPC death after taking fatal damage.** (1 connections) — `server/npc/npc_base.py`
- **Schedule end_combat_if_npc_died so the slain NPC no longer gets combat turns (be** (1 connections) — `server/npc/npc_base.py`
- **Take damage and update determination points (DP).** (1 connections) — `server/npc/npc_base.py`
- **Protocols for NPC combat and communication integration (used by NPCBase).** (1 connections) — `server/npc/npc_protocols.py`
- **Protocol for combat integration handle_npc_death.** (1 connections) — `server/npc/npc_protocols.py`
- **Handle NPC death in the combat integration layer.** (1 connections) — `server/npc/npc_protocols.py`

## Relationships

- [Realtime Subscribers](Realtime_Subscribers.md) (11 shared connections)
- [command parser rationale](command_parser_rationale.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/npc/npc_base.py`
- `server/npc/npc_protocols.py`

## Audit Trail

- EXTRACTED: 42 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*