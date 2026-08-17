# _validate_taunt_context

> 19 nodes

## Key Concepts

- **_validate_taunt_context()** (12 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_combat_and_participant()** (9 connections) — `server/commands/combat_taunt.py`
- **_resolve_taunt_room_and_player()** (6 connections) — `server/commands/combat_taunt.py`
- **UUID** (5 connections)
- **_RoomWithIdOnly** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **test_resolve_taunt_room_and_player_falls_back_to_id()** (4 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_taunt.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_taunt.py`
- **test_resolve_taunt_room_and_player_uses_room_id_attr()** (3 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **AppWithState** (3 connections)
- **.__init__()** (1 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **Validate taunt preconditions and resolve combat/NPC. Returns error dict or…** (1 connections) — `server/commands/combat_taunt.py`
- **Load player and room from the request context, or return an error dict.** (1 connections) — `server/commands/combat_taunt.py`
- **Return a blocking error dict (e.g. rest), or None if the player may act.** (1 connections) — `server/commands/combat_taunt.py`
- **Resolve room_id and player_id. Returns error dict or (room_id, player_id).** (1 connections) — `server/commands/combat_taunt.py`
- **Resolve combat and NPC participant. Returns error dict or (combat,…** (1 connections) — `server/commands/combat_taunt.py`
- **room_id from room.room_id when present.** (1 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **Room-like object with only ``id`` (no ``room_id``).** (1 connections) — `server/tests/unit/commands/test_combat_taunt.py`
- **Falls back to room.id when room_id missing.** (1 connections) — `server/tests/unit/commands/test_combat_taunt.py`

## Relationships

- [AliasStorage](AliasStorage.md) (13 shared connections)
- [CombatInstance](CombatInstance.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [combat_service_npc.py](combat_service_npc.py.md) (1 shared connections)
- [TargetMatch](TargetMatch.md) (1 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (1 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (1 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/tests/unit/commands/test_combat_taunt.py`

## Audit Trail

- EXTRACTED: 39 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*