# TargetMatch

> 110 nodes

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **TargetResolutionResult** (37 connections) — `server/schemas/shared/target_resolution.py`
- **test_combat_handler.py** (37 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **_handler_with_persistence()** (20 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **AppWithState** (17 connections) — `server/commands/combat_app_protocols.py`
- **test_target_resolution.py** (16 connections) — `server/tests/unit/schemas/test_target_resolution.py`
- **asyncio** (12 connections)
- **TargetMetadata** (11 connections) — `server/schemas/shared/target_metadata.py`
- **target_resolution.py** (11 connections) — `server/schemas/shared/target_resolution.py`
- **_AppStatePersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_AppWithPersistence** (10 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_CmdType** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **_as_app_with_state()** (8 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **._match_npcs_by_name()** (7 connections) — `server/services/target_resolution_service.py`
- **test_get_player_and_room_no_current_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_success()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_player()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_get_player_and_room_unknown_room()** (7 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_dead_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **test_resolve_combat_target_rejects_non_npc()** (6 connections) — `server/tests/unit/commands/test_combat_handler.py`
- **combat_app_protocols.py** (6 connections) — `server/commands/combat_app_protocols.py`
- **.resolve_combat_target()** (5 connections) — `server/commands/combat_handler.py`
- **._validate_combat_target_match()** (5 connections) — `server/commands/combat_handler.py`
- *... and 85 more nodes in this community*

## Relationships

- [PlayerCombatService](PlayerCombatService.md) (30 shared connections)
- [Spell](Spell.md) (21 shared connections)
- [CombatService](CombatService.md) (19 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (18 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (16 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (14 shared connections)
- [spell_effects.py](spell_effects.py.md) (13 shared connections)
- [get_username_from_user](get_username_from_user.md) (12 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (5 shared connections)
- [.resolve_spell_target](resolve_spell_target.md) (5 shared connections)
- [test_damage_grace_period.py](test_damage_grace_period.py.md) (4 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (4 shared connections)

## Source Files

- `server/commands/combat_app_protocols.py`
- `server/commands/combat_handler.py`
- `server/schemas/shared/target_metadata.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_combat_handler.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 362 (92%)
- INFERRED: 33 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*