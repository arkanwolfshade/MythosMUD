# models/combat.py

> 152 nodes

## Key Concepts

- **models/combat.py** (60 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **.check_connection_state()** (4 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_instance_clear_queued_actions()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_clear_queued_actions_specific_round()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_alive_participants()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_alive_participants_empty()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_with_valid_turn()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_participants_by_initiative()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_queued_actions()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_is_combat_over_when_active()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **cleanup_handler()** (4 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.cleanup_combat_tracking()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_instance_advance_turn()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_advance_turn_always_increments_round()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_advance_turn_increments_round()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_default_values()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_missing_participant()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_current_turn_participant_no_turn_order()** (3 connections) — `server/tests/unit/models/test_combat.py`
- *... and 127 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (44 shared connections)
- [CombatInstance](CombatInstance.md) (26 shared connections)
- [CombatParticipantType](CombatParticipantType.md) (8 shared connections)
- [CombatService](CombatService.md) (7 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (6 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (5 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (3 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (2 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_cleanup_handler.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`

## Audit Trail

- EXTRACTED: 297 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*