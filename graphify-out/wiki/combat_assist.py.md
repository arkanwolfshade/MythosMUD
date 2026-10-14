# combat_assist.py

> 81 nodes

## Key Concepts

- **combat_assist.py** (38 connections) — `server/commands/combat_assist.py`
- **test_combat_protect.py** (38 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **_protect()** (27 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **AssistCommandHandler** (26 connections) — `server/commands/combat_assist.py`
- **combat_protect.py** (22 connections) — `server/commands/combat_protect.py`
- **asyncio** (18 connections)
- **run_handle_protect_command()** (15 connections) — `server/commands/combat_protect.py`
- **_match()** (15 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **run_handle_assist_command()** (14 connections) — `server/commands/combat_assist.py`
- **_fight()** (13 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **load_assister()** (11 connections) — `server/commands/combat_assist.py`
- **find_ally_fight()** (10 connections) — `server/commands/combat_assist.py`
- **_resolve_assisted()** (8 connections) — `server/commands/combat_assist.py`
- **_join_if_needed()** (8 connections) — `server/commands/combat_protect.py`
- **UUID** (8 connections)
- **_find_assisted_foe()** (7 connections) — `server/commands/combat_assist.py`
- **resolve_named_player()** (7 connections) — `server/commands/combat_assist.py`
- **assisted_name_from_command()** (6 connections) — `server/commands/combat_assist.py`
- **_foe_of()** (6 connections) — `server/commands/combat_assist.py`
- **_resolve_party_leader()** (6 connections) — `server/commands/combat_assist.py`
- **execute_attack_on_npc()** (6 connections) — `server/commands/combat_attack.py`
- **_queue_protect()** (6 connections) — `server/commands/combat_protect.py`
- **test_a_phantom_fight_cannot_be_covered()** (6 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **test_protect_replaces_whatever_you_had_queued_for_the_next_round()** (6 connections) — `server/tests/unit/commands/test_combat_protect.py`
- **_npc_string_id()** (5 connections) — `server/commands/combat_assist.py`
- *... and 56 more nodes in this community*

## Relationships

- [CombatService](CombatService.md) (19 shared connections)
- [CombatParticipant](CombatParticipant.md) (11 shared connections)
- [CombatInstance](CombatInstance.md) (9 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (8 shared connections)
- [TargetType](TargetType.md) (7 shared connections)
- [test_combat_assist.py](test_combat_assist.py.md) (6 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [Player](Player.md) (4 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (4 shared connections)
- [PartyService](PartyService.md) (3 shared connections)
- [NpcDisposition](NpcDisposition.md) (3 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)

## Source Files

- `server/commands/combat_assist.py`
- `server/commands/combat_attack.py`
- `server/commands/combat_protect.py`
- `server/tests/unit/commands/test_combat_protect.py`

## Audit Trail

- EXTRACTED: 252 (92%)
- INFERRED: 23 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*