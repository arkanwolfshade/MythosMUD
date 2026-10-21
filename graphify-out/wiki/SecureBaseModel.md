# SecureBaseModel

> 175 nodes · cohesion 0.02

## Key Concepts

- **log_and_raise_enhanced()** (113 connections) — `server/utils/enhanced_error_logging.py`
- **PlayerStateCommandFactory** (46 connections) — `server/utils/command_factories_player_state.py`
- **ModerationCommandFactory** (37 connections) — `server/utils/command_factories_moderation.py`
- **test_command_factories_player_state.py** (31 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **test_command_factories_moderation.py** (29 connections) — `server/tests/unit/utils/test_command_factories_moderation.py`
- **command_factories.py** (21 connections) — `server/utils/command_factories.py`
- **PlayerStateService** (12 connections) — `server/game/player_state_service.py`
- **command_factories_moderation.py** (11 connections) — `server/utils/command_factories_moderation.py`
- **command_factories_player_state.py** (11 connections) — `server/utils/command_factories_player_state.py`
- **.create_mute_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **.create_mute_global_command()** (9 connections) — `server/utils/command_factories_moderation.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **.create_add_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_admin_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.create_unmute_global_command()** (7 connections) — `server/utils/command_factories_moderation.py`
- **.apply_corruption()** (6 connections) — `server/game/player_state_service.py`
- **.create_mutes_command()** (6 connections) — `server/utils/command_factories_moderation.py`
- **.create_cleanse_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_journal_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_quests_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_quit_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_rest_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- **.create_skills_command()** (6 connections) — `server/utils/command_factories_player_state.py`
- *... and 150 more nodes in this community*

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (44 shared connections)
- [AttributeError](AttributeError.md) (25 shared connections)
- [ContainerComponent](ContainerComponent.md) (23 shared connections)
- [command_service.py](command_service.py.md) (12 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (12 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (10 shared connections)
- [Room](Room.md) (7 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (6 shared connections)
- [CommandFactory](CommandFactory.md) (5 shared connections)
- [_ScalarResult](_ScalarResult.md) (5 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [HeaderBar.tsx](HeaderBar.tsx.md) (3 shared connections)

## Source Files

- `server/game/player_state_service.py`
- `server/tests/unit/utils/test_command_factories_moderation.py`
- `server/tests/unit/utils/test_command_factories_player_state.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories.py`
- `server/utils/command_factories_moderation.py`
- `server/utils/command_factories_player_state.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 411 (84%)
- INFERRED: 76 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*