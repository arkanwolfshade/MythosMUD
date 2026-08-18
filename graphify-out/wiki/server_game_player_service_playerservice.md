# server game player service playerservice

> 134 nodes

## Key Concepts

- **log_and_raise_enhanced()** (97 connections) — `server/utils/enhanced_error_logging.py`
- **ExplorationCommandFactory** (59 connections) — `server/utils/command_factories_exploration.py`
- **test_command_factories_exploration.py** (49 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **.create_look_command()** (18 connections) — `server/utils/command_factories_exploration.py`
- **.create_party_command()** (12 connections) — `server/utils/command_factories_exploration.py`
- **command_factories_exploration.py** (11 connections) — `server/utils/command_factories_exploration.py`
- **.create_lie_command()** (8 connections) — `server/utils/command_factories_exploration.py`
- **.create_follow_command()** (7 connections) — `server/utils/command_factories_exploration.py`
- **.create_go_command()** (7 connections) — `server/utils/command_factories_exploration.py`
- **.create_ground_command()** (7 connections) — `server/utils/command_factories_exploration.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **.create_following_command()** (6 connections) — `server/utils/command_factories_exploration.py`
- **.create_sit_command()** (6 connections) — `server/utils/command_factories_exploration.py`
- **.create_stand_command()** (6 connections) — `server/utils/command_factories_exploration.py`
- **.create_unfollow_command()** (6 connections) — `server/utils/command_factories_exploration.py`
- **.apply_corruption()** (5 connections) — `server/game/player_state_service.py`
- **.apply_fear()** (5 connections) — `server/game/player_state_service.py`
- **.apply_lucidity_loss()** (5 connections) — `server/game/player_state_service.py`
- **.damage_player()** (5 connections) — `server/game/player_state_service.py`
- **.gain_occult_knowledge()** (5 connections) — `server/game/player_state_service.py`
- **.heal_player()** (5 connections) — `server/game/player_state_service.py`
- **test_create_follow_command_empty_target()** (5 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_follow_command_no_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- **test_create_following_command_with_args()** (5 connections) — `server/tests/unit/utils/test_command_factories_exploration.py`
- *... and 109 more nodes in this community*

## Relationships

- [mythosvalidationerror](mythosvalidationerror.md) (28 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (23 shared connections)
- [server tests unit structured logging](server_tests_unit_structured_logging.md) (11 shared connections)
- [server api character creation](server_api_character_creation.md) (10 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (10 shared connections)
- [server models command moderation mutecommand](server_models_command_moderation_mutecommand.md) (8 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (7 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (4 shared connections)
- [server models command base basecommand](server_models_command_base_basecommand.md) (3 shared connections)
- [server api players](server_api_players.md) (3 shared connections)
- [server models command base direction](server_models_command_base_direction.md) (3 shared connections)

## Source Files

- `server/game/player_service.py`
- `server/game/player_state_service.py`
- `server/tests/unit/utils/test_command_factories_exploration.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/utils/command_factories_exploration.py`
- `server/utils/enhanced_error_logging.py`

## Audit Trail

- EXTRACTED: 308 (84%)
- INFERRED: 60 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*