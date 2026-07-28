# Server Commands (8)

> 104 nodes

## Key Concepts

- **CombatCommandHandler** (54 connections) — `server/commands/combat_handler.py`
- **TargetResolutionResult** (39 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **CombatCommandHandlerExtras** (25 connections) — `server/commands/combat_handler.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **_NpcWithLife** (17 connections) — `server/commands/combat_handler.py`
- **.__init__()** (11 connections) — `server/commands/combat_handler.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **Any** (6 connections)
- **._validate_combat_target_match()** (6 connections) — `server/commands/combat_handler.py`
- **test_get_player_and_room_unknown_player()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_no_current_room()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_attack_command()** (5 connections) — `server/commands/combat_handler.py`
- **.handle_taunt_command()** (5 connections) — `server/commands/combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (5 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **handler()** (5 connections) — `server/tests/unit/commands/test_flee_command.py`
- **.extract_combat_command_data()** (4 connections) — `server/commands/combat_handler.py`
- *... and 79 more nodes in this community*

## Relationships

- [Server Game (2)](Server_Game_%282%29.md) (23 shared connections)
- [Server Commands (24)](Server_Commands_%2824%29.md) (13 shared connections)
- [Server Services (12)](Server_Services_%2812%29.md) (10 shared connections)
- [Server Commands (29)](Server_Commands_%2829%29.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (8 shared connections)
- [Server Commands (37)](Server_Commands_%2837%29.md) (7 shared connections)
- [Server Services (6)](Server_Services_%286%29.md) (6 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (5 shared connections)
- [Server Commands (38)](Server_Commands_%2838%29.md) (5 shared connections)
- [Server Commands (20)](Server_Commands_%2820%29.md) (4 shared connections)
- [Server Events](Server_Events.md) (4 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (4 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/commands/test_flee_command.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 368 (81%)
- INFERRED: 89 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*