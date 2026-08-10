# Archive Frd Random

> 96 nodes

## Key Concepts

- **get_config()** (105 connections) — `server/config/__init__.py`
- **AppConfig** (31 connections) — `server/config/models/app.py`
- **__init__.py** (11 connections) — `server/config/__init__.py`
- **reset_config()** (9 connections) — `server/config/__init__.py`
- **test_config.py** (9 connections) — `server/tests/unit/config/test_config.py`
- **test_config_init.py** (9 connections) — `server/tests/unit/config/test_config_init.py`
- **ChatConfig** (8 connections) — `server/config/models/chat_time.py`
- **load_motd()** (8 connections) — `server/utils/motd_loader.py`
- **.to_legacy_dict()** (7 connections) — `server/config/models/app.py`
- **test_motd_loader.py** (7 connections) — `server/tests/unit/utils/test_motd_loader.py`
- **Any** (6 connections)
- **_create_config_instance()** (5 connections) — `server/config/__init__.py`
- **_get_config_cached()** (5 connections) — `server/config/__init__.py`
- **_get_config_test()** (5 connections) — `server/config/__init__.py`
- **.__init__()** (5 connections) — `server/config/models/app.py`
- **._legacy_game_entries()** (5 connections) — `server/config/models/app.py`
- **._legacy_nats_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_chat_dict()** (5 connections) — `server/config/models/app.py`
- **._legacy_cors_dict()** (5 connections) — `server/config/models/app.py`
- **generate_unique_codes()** (5 connections) — `tools/invite_tools/generate_invites.py`
- **_is_test_mode()** (4 connections) — `server/config/__init__.py`
- **._sanitize_environment_for_nested_configs()** (4 connections) — `server/config/models/app.py`
- **test_reset_config_clears_state()** (4 connections) — `server/tests/unit/config/test_config.py`
- **test_reset_config_in_test_mode()** (4 connections) — `server/tests/unit/config/test_config_init.py`
- **generate_invites.py** (4 connections) — `tools/invite_tools/generate_invites.py`
- *... and 71 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (28 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (8 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (5 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (5 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [Message Broadcaster Core](Message_Broadcaster_Core.md) (3 shared connections)
- [Playwright E2E Specs](Playwright_E2E_Specs.md) (2 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (2 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (2 shared connections)

## Source Files

- `server/config/__init__.py`
- `server/config/models/app.py`
- `server/config/models/chat_time.py`
- `server/game/player_service.py`
- `server/tests/conftest.py`
- `server/tests/unit/config/test_config.py`
- `server/tests/unit/config/test_config_init.py`
- `server/tests/unit/test_config_smoke.py`
- `server/tests/unit/utils/test_motd_loader.py`
- `server/utils/motd_loader.py`
- `tools/invite_tools/generate_invites.py`

## Audit Trail

- EXTRACTED: 379 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*