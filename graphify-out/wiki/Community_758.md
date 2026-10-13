# Community 758

> 22 nodes

## Key Concepts

- **test_combat_turn_player_turn.py** (18 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **process_player_turn()** (15 connections) — `server/services/combat_turn_participant_actions.py`
- **_p()** (10 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **_combat()** (9 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **_service()** (8 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **test_automatic_attack_lands_on_the_npc_not_the_ally()** (8 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **_result()** (7 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **test_a_casting_player_skips_the_automatic_attack()** (7 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **test_a_failed_automatic_attack_still_spends_the_turn()** (7 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **test_an_error_during_the_player_turn_is_contained()** (7 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **test_automatic_attack_follows_the_tracked_target()** (7 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **test_no_automatic_attack_when_no_foe_is_left()** (7 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **_should_skip_for_casting()** (6 connections) — `server/services/combat_turn_participant_actions.py`
- **asyncio** (6 connections)
- **test_casting_check_failure_does_not_block_the_attack()** (4 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **Return True if player is casting (and we should skip autoattack); sets…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Process player turn with automatic basic attack. Args: combat_service: Parent…** (1 connections) — `server/services/combat_turn_participant_actions.py`
- **Unit tests for the automatic player turn (#833): who a player's default attack…** (1 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **A failing attack must not escape and break the whole combat round.** (1 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **If the casting state cannot be read, the player is treated as not casting.** (1 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **A CombatService stand-in whose magic service reports ``casting`` for every…** (1 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`
- **#833: with two players and a ghoul, each player's default attack goes to the…** (1 connections) — `server/tests/unit/services/test_combat_turn_player_turn.py`

## Relationships

- [Combat Attack Execution](Combat_Attack_Execution.md) (9 shared connections)
- [Combat Participants](Combat_Participants.md) (5 shared connections)
- [Combat Instance Turns](Combat_Instance_Turns.md) (4 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (2 shared connections)
- [Community 398](Community_398.md) (1 shared connections)

## Source Files

- `server/services/combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_turn_player_turn.py`

## Audit Trail

- EXTRACTED: 75 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*