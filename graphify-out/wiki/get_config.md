# get_config

> 74 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **AppConfig** (31 connections) — `server/config/models/app.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- **._first_cors_origins_env()** (3 connections) — `server/config/models/app.py`
- **.set_legacy_environment_variables()** (3 connections) — `server/config/models/app.py`
- **test_get_config_fresh_instances_in_test_mode()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- **test_get_config_has_database_config()** (3 connections) — `server/tests/unit/config/test_config_init.py`
- *... and 49 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (18 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (9 shared connections)
- [models/combat.py](models-combat.py.md) (9 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (3 shared connections)
- [CombatParticipant](CombatParticipant.md) (3 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (3 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [NATSService](NATSService.md) (2 shared connections)
- [GameConfig](GameConfig.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 207 (95%)
- INFERRED: 11 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*