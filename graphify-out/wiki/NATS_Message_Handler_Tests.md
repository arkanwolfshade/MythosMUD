# NATS Message Handler Tests

> 14 nodes

## Key Concepts

- **test_command_factories.py** (59 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_command_factory_create_nonexistent_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_pose_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_reply_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_stand_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_cast_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **test_create_spells_command()** (2 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Unit tests for command factories.  Tests the CommandFactory class.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test CommandFactory.create_*() methods exist for all command types.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_pose_command delegates to communication factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_reply_command delegates to communication factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_stand_command delegates to exploration factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_cast_command delegates to utility factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`
- **Test create_spells_command delegates to utility factory.** (1 connections) — `server/tests/unit/utils/test_command_factories.py`

## Relationships

- [Phase 2: Categorize and Prioritize Lint Issues](Phase_2-_Categorize_and_Prioritize_Lint_Issues.md) (2 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (2 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [test_get_alerts_no_alerts](test_get_alerts_no_alerts.md) (1 shared connections)
- [test_validate_room_integrity_room_without_get_players](test_validate_room_integrity_room_without_get_players.md) (1 shared connections)
- [.test_init_with_failover_callback](test_init_with_failover_callback.md) (1 shared connections)
- [.test_is_catatonic_after_cleared](test_is_catatonic_after_cleared.md) (1 shared connections)
- [.test_get_snapshot_empty](test_get_snapshot_empty.md) (1 shared connections)
- [.test_get_attack_message_attacker_perspective](test_get_attack_message_attacker_perspective.md) (1 shared connections)
- [.test_get_attack_message_defender_perspective](test_get_attack_message_defender_perspective.md) (1 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*