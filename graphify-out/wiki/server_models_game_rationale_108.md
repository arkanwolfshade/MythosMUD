# server models game rationale 108

> 10 nodes

## Key Concepts

- **.__init__()** (5 connections) — `server/models/invite.py`
- **.is_alive()** (5 connections) — `server/npc/npc_base.py`
- **.is_active()** (4 connections) — `server/models/game.py`
- **_npc_alive_and_active()** (4 connections) — `server/npc/idle_movement.py`
- **Any** (1 connections)
- **setter** (1 connections)
- **Check if the status effect is still active.** (1 connections) — `server/models/game.py`
- **Initialize Invite with defaults.** (1 connections) — `server/models/invite.py`
- **Return True if NPC is alive (determination_points > 0).** (1 connections) — `server/npc/npc_base.py`
- **Allow backward-compatible assignment (npc.is_alive = False).** (1 connections) — `server/npc/npc_base.py`

## Relationships

- [server game magic spell effects](server_game_magic_spell_effects.md) (1 shared connections)
- [server auth invites](server_auth_invites.md) (1 shared connections)
- [object](object.md) (1 shared connections)
- [server npc idle movement idlemovementhandler](server_npc_idle_movement_idlemovementhandler.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (1 shared connections)

## Source Files

- `server/models/game.py`
- `server/models/invite.py`
- `server/npc/idle_movement.py`
- `server/npc/npc_base.py`

## Audit Trail

- EXTRACTED: 11 (73%)
- INFERRED: 4 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*