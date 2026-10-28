# test_player_combat_service.py

> 248 nodes · cohesion 0.02

## Key Concepts

- **CombatInstance** (271 connections) — `server/models/combat.py`
- **get_config()** (126 connections) — `server/config/__init__.py`
- **combat_turn_participant_actions.py** (49 connections) — `server/services/combat_turn_participant_actions.py`
- **aggro_threat.py** (42 connections) — `server/services/aggro_threat.py`
- **add_damage_threat()** (33 connections) — `server/services/aggro_threat.py`
- **test_aggro_threat.py** (33 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **update_aggro()** (29 connections) — `server/services/aggro_threat.py`
- **combat_protect_action.py** (28 connections) — `server/services/combat_protect_action.py`
- **combat_taunt_action.py** (27 connections) — `server/services/combat_taunt_action.py`
- **get_or_create_hate_list()** (24 connections) — `server/services/aggro_threat.py`
- **_make_combat()** (24 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_aggro_flow.py** (18 connections) — `server/tests/integration/test_aggro_flow.py`
- **add_utility_threat()** (17 connections) — `server/services/aggro_threat.py`
- **_make_participant()** (17 connections) — `server/tests/unit/services/test_aggro_threat.py`
- **test_guarding_threat.py** (16 connections) — `server/tests/unit/services/test_guarding_threat.py`
- **add_heal_threat()** (15 connections) — `server/services/aggro_threat.py`
- **apply_taunt()** (15 connections) — `server/services/aggro_threat.py`
- **UUID** (14 connections)
- **_make_participant()** (12 connections) — `server/tests/integration/test_aggro_flow.py`
- **_resolve_npc_target()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_weapon_damage_from_equipped_player()** (11 connections) — `server/services/combat_turn_participant_actions.py`
- **_make_combat()** (11 connections) — `server/tests/integration/test_aggro_flow.py`
- **_corruption_scale()** (10 connections) — `server/services/aggro_threat.py`
- **process_npc_turn()** (10 connections) — `server/services/combat_turn_participant_actions.py`
- **_fight()** (10 connections) — `server/tests/unit/services/test_guarding_threat.py`
- *... and 223 more nodes in this community*

## Relationships

- [DatabaseManager](DatabaseManager.md) (96 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (77 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (39 shared connections)
- [Reporter](Reporter.md) (36 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (31 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (29 shared connections)
- [Room](Room.md) (21 shared connections)
- [test_windows_safe_rotation.py](test_windows_safe_rotation.py.md) (19 shared connections)
- [test_npc_combat_integration_join.py](test_npc_combat_integration_join.py.md) (18 shared connections)
- [stateUpdateUtils.ts](stateUpdateUtils.ts.md) (15 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (9 shared connections)
- [useThemeContext.ts](useThemeContext.ts.md) (8 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/models/combat.py`
- `server/services/aggro_threat.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_protect_action.py`
- `server/services/combat_taunt_action.py`
- `server/services/combat_turn_participant_actions.py`
- `server/services/combat_turn_processor.py`
- `server/tests/integration/test_aggro_flow.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/services/test_aggro_threat.py`
- `server/tests/unit/services/test_combat_turn_participant_actions.py`
- `server/tests/unit/services/test_guarding_threat.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 1011 (98%)
- INFERRED: 18 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*