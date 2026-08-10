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

- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (2 shared connections)
- [Migration Verification](Migration_Verification.md) (2 shared connections)
- [Mythosmud Obsidian Raw](Mythosmud_Obsidian_Raw.md) (2 shared connections)
- [Commands Go Command](Commands_Go_Command.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (2 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (1 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (1 shared connections)
- [Services Player Respawn](Services_Player_Respawn.md) (1 shared connections)
- [test_should_idle_move_true_when_not_in_combat_and_probability_succeeds](test_should_idle_move_true_when_not_in_combat_and_probability_succeeds.md) (1 shared connections)
- [test_get_valid_exits_empty_room](test_get_valid_exits_empty_room.md) (1 shared connections)
- [Nats Subject Patterns](Nats_Subject_Patterns_2.md) (1 shared connections)
- [Archive Migration Completion](Archive_Migration_Completion.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_factories.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*