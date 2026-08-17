# server npc combat integration npccombatintegration

> 8 nodes

## Key Concepts

- **._get_npc_display_name()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_lifecycle_manager()** (5 connections) — `server/npc/combat_integration.py`
- **._get_npc_name_from_lifecycle()** (4 connections) — `server/npc/combat_integration.py`
- **._derive_npc_name_from_id()** (3 connections) — `server/npc/combat_integration.py`
- **Resolve NPC instance display name from lifecycle manager, or derive from npc_id.** (1 connections) — `server/npc/combat_integration.py`
- **Best-effort lookup of NPC name from the lifecycle manager.** (1 connections) — `server/npc/combat_integration.py`
- **Resolve the NPC lifecycle manager from the app state, if available.** (1 connections) — `server/npc/combat_integration.py`
- **Fallback name derivation: first segment of npc_id (e.g. nightgaunt_limbo_... ->…** (1 connections) — `server/npc/combat_integration.py`

## Relationships

- [server npc combat integration npccombatintegration](server_npc_combat_integration_npccombatintegration.md) (5 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)

## Source Files

- `server/npc/combat_integration.py`

## Audit Trail

- EXTRACTED: 13 (93%)
- INFERRED: 1 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*