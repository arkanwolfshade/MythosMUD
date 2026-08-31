# get_pose_persistence

> 8 nodes

## Key Concepts

- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **test_get_pose_persistence_from_container()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_pose_persistence_state_fallback()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **.get_player_by_name()** (1 connections) — `server/commands/communication_commands_support.py`
- **.save_player()** (1 connections) — `server/commands/communication_commands_support.py`
- **Resolve async persistence from app state or container for pose commands.** (1 connections) — `server/commands/communication_commands_support.py`
- **Minimal persistence for pose read/write in emote/pose flows.** (1 connections) — `server/commands/communication_commands_support.py`

## Relationships

- [test_communication_commands_flows.py](test_communication_commands_flows.py.md) (6 shared connections)
- [talk_command.py](talk_command.py.md) (2 shared connections)
- [request_with_app_container](request_with_app_container.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 17 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*