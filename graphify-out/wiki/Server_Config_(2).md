# Server Config (2)

> 96 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **combat_monitoring_service.py** (21 connections) — `server/services/combat_monitoring_service.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **CombatMetrics** (11 connections) — `server/services/combat_monitoring_service.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **.delete_player()** (9 connections) — `server/game/player_service.py`
- **get_feature_flags()** (9 connections) — `server/services/feature_flag_service.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **.__init__()** (8 connections) — `server/services/combat_monitoring_service.py`
- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **test_motd_loader.py** (7 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **get_combat_metrics()** (6 connections) — `server/services/combat_monitoring_service.py`
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **get_combat_config()** (5 connections) — `server/services/combat_configuration_service.py`
- **AlertSeverity** (5 connections) — `server/services/combat_monitoring_service.py`
- **AlertType** (5 connections) — `server/services/combat_monitoring_service.py`
- **.__init__()** (5 connections) — `server/time/time_service.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **.__init__()** (4 connections) — `server/services/combat_configuration_service.py`
- **.get_current_metrics()** (4 connections) — `server/services/combat_monitoring_service.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- *... and 71 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (21 shared connections)
- [Server Config](Server_Config.md) (7 shared connections)
- [Server Services (7)](Server_Services_%287%29.md) (6 shared connections)
- [Server Services (39)](Server_Services_%2839%29.md) (6 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (5 shared connections)
- [Server Services (56)](Server_Services_%2856%29.md) (5 shared connections)
- [Server Npc (8)](Server_Npc_%288%29.md) (4 shared connections)
- [Server Services (93)](Server_Services_%2893%29.md) (4 shared connections)
- [Server Npc](Server_Npc.md) (3 shared connections)
- [Server Services (36)](Server_Services_%2836%29.md) (3 shared connections)
- [Server Services (102)](Server_Services_%28102%29.md) (2 shared connections)
- [Server Admin](Server_Admin.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/game/player_service.py`
- `server/services/combat_configuration_service.py`
- `server/services/combat_monitoring_service.py`
- `server/services/feature_flag_service.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`
- `server/tests/unit/test_config_smoke.py`
- `server/tests/unit/utils/test_motd_loader.py`
- `server/time/time_service.py`
- `server/utils/motd_loader.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 390 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*