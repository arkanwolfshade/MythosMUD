# npc combat service

> 8 nodes

## Key Concepts

- **get_pose_persistence()** (11 connections) — `server/commands/communication_commands_support.py`
- **AsyncPersistenceForPose** (6 connections) — `server/commands/communication_commands_support.py`
- **.get_player_by_name()** (2 connections) — `server/commands/communication_commands_support.py`
- **.save_player()** (2 connections) — `server/commands/communication_commands_support.py`
- **test_get_pose_persistence_from_container()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **test_get_pose_persistence_state_fallback()** (2 connections) — `server/tests/unit/commands/test_communication_commands_support.py`
- **Minimal persistence for pose read/write in emote/pose flows.** (1 connections) — `server/commands/communication_commands_support.py`
- **Resolve async persistence from app state or container for pose commands.** (1 connections) — `server/commands/communication_commands_support.py`

## Relationships

- [commands communication flows](commands_communication_flows.md) (7 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (2 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (2 shared connections)
- [character creation service](character_creation_service.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)

## Source Files

- `server/commands/communication_commands_support.py`
- `server/tests/unit/commands/test_communication_commands_support.py`

## Audit Trail

- EXTRACTED: 24 (89%)
- INFERRED: 3 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*