# argon2 auth rationale

> 5 nodes

## Key Concepts

- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (2 connections)
- **Apply lucidity loss when a player engages an eldritch entity.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Determine encounter category based on NPC definition metadata.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`

## Relationships

- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*