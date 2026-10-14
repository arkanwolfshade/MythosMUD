# test_combat_assist.py

> 35 nodes

## Key Concepts

- **test_combat_assist.py** (43 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **_assist()** (29 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **asyncio** (21 connections)
- **_match()** (16 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **_fight()** (15 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **_two_foe_fight()** (8 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **_participant()** (7 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_phantom_fight_cannot_be_joined()** (6 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_you_are_told_when_you_are_already_in_that_fight()** (6 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_bare_assist_follows_the_party_leader()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_dead_tracked_target_falls_back_to_a_living_foe()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_fight_in_another_room_is_not_here()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_fight_with_no_living_foe_is_not_a_fight_to_join()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_assist_a_named_player_attacks_the_foe_they_are_fighting()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_assist_prefers_the_assisted_players_tracked_target()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_the_npc_id_falls_back_to_the_participant_uuid_when_no_string_id_was_mapped()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_without_a_tracked_target_assist_takes_the_first_living_foe()** (5 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **UUID** (5 connections)
- **test_a_bare_assist_from_the_party_leader_asks_for_a_name()** (4 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_bare_assist_without_a_party_asks_for_a_name()** (4 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_an_idle_player_is_not_fighting_anything()** (4 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_assist_needs_a_real_player_and_a_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_only_players_can_be_assisted()** (4 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_you_cannot_assist_yourself()** (4 connections) — `server/tests/unit/commands/test_combat_assist.py`
- **test_a_player_lookup_error_is_passed_through()** (3 connections) — `server/tests/unit/commands/test_combat_assist.py`
- *... and 10 more nodes in this community*

## Relationships

- [combat_assist.py](combat_assist.py.md) (6 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [CombatParticipant](CombatParticipant.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [PartyService](PartyService.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [Player](Player.md) (2 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_combat_assist.py`

## Audit Trail

- EXTRACTED: 133 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*