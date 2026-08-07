# System Metrics

> 148 nodes

## Key Concepts

- **Stats** (88 connections) — `server/models/game.py`
- **StatsGenerator** (48 connections) — `server/game/stats_generator.py`
- **test_game_stats_methods.py** (31 connections) — `server/tests/unit/models/test_game_stats_methods.py`
- **test_stats_generator.py** (19 connections) — `server/tests/unit/game/test_stats_generator.py`
- **stats_generator.py** (15 connections) — `server/game/stats_generator.py`
- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **generate_random_stats()** (12 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **.create_character_with_stats()** (7 connections) — `server/game/character_creation_service.py`
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **.validate_character_stats()** (6 connections) — `server/game/character_creation_service.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **Any** (5 connections)
- **.roll_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **.validate_current_vs_max_stats()** (5 connections) — `server/models/game.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- *... and 123 more nodes in this community*

## Relationships

- [npc rationale extract](npc_rationale_extract.md) (10 shared connections)
- [combat npc service](combat_npc_service.md) (10 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (10 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (10 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [add used user](add_used_user.md) (5 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (5 shared connections)
- [command inventory models](command_inventory_models.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [schemas invite user](schemas_invite_user.md) (4 shared connections)
- [combat services turn](combat_services_turn.md) (3 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/game/stats_generator.py`
- `server/models/game.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/game/test_stats_generator.py`
- `server/tests/unit/models/test_game_stats_methods.py`

## Audit Trail

- EXTRACTED: 541 (96%)
- INFERRED: 23 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*