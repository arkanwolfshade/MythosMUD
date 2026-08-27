# models/combat.py

> 200 nodes

## Key Concepts

- **models/combat.py** (60 connections) — `server/models/combat.py`
- **test_combat.py** (60 connections) — `server/tests/unit/models/test_combat.py`
- **CombatParticipantType** (45 connections) — `server/models/combat.py`
- **test_combat_attack_handler.py** (38 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **combat_death_handler.py** (25 connections) — `server/services/combat_death_handler.py`
- **test_combat_cleanup_handler.py** (19 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **combat_attack_handler.py** (17 connections) — `server/services/combat_attack_handler.py`
- **CombatStatus** (13 connections) — `server/models/combat.py`
- **test_combat_turn_participant_actions.py** (13 connections) — `server/tests/unit/services/test_combat_turn_participant_actions.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **combat_cleanup_handler.py** (11 connections) — `server/services/combat_cleanup_handler.py`
- **combat_types.py** (11 connections) — `server/services/combat_types.py`
- **asyncio** (7 connections)
- **_get_default_damage()** (6 connections) — `server/models/combat.py`
- **fixture** (6 connections)
- **test_combat_types.py** (6 connections) — `server/tests/unit/services/test_combat_types.py`
- **test_combat_instance_clear_queued_actions_specific_round()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_get_alive_participants()** (4 connections) — `server/tests/unit/models/test_combat.py`
- **attack_handler()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_npc()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **mock_target_player()** (4 connections) — `server/tests/unit/services/test_combat_attack_handler.py`
- **cleanup_handler()** (4 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.__init__()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **test_combat_instance_advance_turn()** (3 connections) — `server/tests/unit/models/test_combat.py`
- **test_combat_instance_advance_turn_increments_round()** (3 connections) — `server/tests/unit/models/test_combat.py`
- *... and 175 more nodes in this community*

## Relationships

- [CombatParticipant](CombatParticipant.md) (46 shared connections)
- [CombatInstance](CombatInstance.md) (31 shared connections)
- [combat_service.py](combat_service.py.md) (21 shared connections)
- [CombatDeathHandler](CombatDeathHandler.md) (11 shared connections)
- [combat_turn_participant_actions.py](combat_turn_participant_actions.py.md) (9 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_aggro_threat.py](test_aggro_threat.py.md) (8 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (8 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (6 shared connections)
- [test_combat_event_publisher.py](test_combat_event_publisher.py.md) (5 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [NATSError](NATSError.md) (5 shared connections)

## Source Files

- `server/models/combat.py`
- `server/services/combat_attack_handler.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_death_handler.py`
- `server/services/combat_types.py`
- `server/tests/unit/models/test_combat.py`
- `server/tests/unit/services/test_combat_attack_handler.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_combat_types.py`

## Audit Trail

- EXTRACTED: 445 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*