# combat services rationale

> 41 nodes

## Key Concepts

- **combat_flee_handler.py** (22 connections) — `server/services/combat_flee_handler.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **_check_involuntary_flee_with_session()** (8 connections) — `server/services/combat_flee_handler.py`
- **lucidity_command_disruption.py** (8 connections) — `server/services/lucidity_command_disruption.py`
- **_involuntary_flee_on_cooldown()** (5 connections) — `server/services/combat_flee_handler.py`
- **test_try_voluntary_flee_roll_zero_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_above_chance_fails()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_roll_below_chance_succeeds()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_opponents_reduce_chance()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_try_voluntary_flee_roll_dead_opponent_not_counted()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_room_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_execute_voluntary_flee_no_exits_returns_false()** (5 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (4 connections)
- **should_involuntary_flee()** (4 connections) — `server/services/lucidity_command_disruption.py`
- **Any** (2 connections)
- **should_misfire_command()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **get_misfire_message()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **can_perform_action()** (2 connections) — `server/services/lucidity_command_disruption.py`
- **UUID** (2 connections)
- **Combat flee handler for involuntary and voluntary flee logic.  Handles checking** (1 connections) — `server/services/combat_flee_handler.py`
- **Roll for voluntary flee success (no side effects).      Formula: base + (bonus *** (1 connections) — `server/services/combat_flee_handler.py`
- **Execute voluntary flee for a combat participant (shared by /flee command and fle** (1 connections) — `server/services/combat_flee_handler.py`
- *... and 16 more nodes in this community*

## Relationships

- [Item Instances](Item_Instances.md) (23 shared connections)
- [lucidity services helpers](lucidity_services_helpers.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [spell game magic](spell_game_magic.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [combat flee commands](combat_flee_commands.md) (2 shared connections)
- [target resolution service](target_resolution_service.md) (1 shared connections)

## Source Files

- `server/services/combat_flee_handler.py`
- `server/services/lucidity_command_disruption.py`
- `server/tests/unit/services/test_combat_flee_handler.py`

## Audit Trail

- EXTRACTED: 168 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*