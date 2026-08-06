# Player Stats

> 189 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **players.py** (66 connections) — `server/api/players.py`
- **test_players_api_coverage.py** (54 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **PlayerRead** (48 connections) — `server/schemas/players/player.py`
- **_user()** (27 connections) — `server/tests/unit/api/test_players_api_coverage.py`
- **player.py** (20 connections) — `server/schemas/players/player.py`
- **get_player_quests()** (17 connections) — `server/api/players.py`
- **FastAPIRequest** (16 connections)
- **start_login_grace_period_endpoint()** (16 connections) — `server/api/players.py`
- **ClassDefinition** (15 connections) — `server/schemas/players/class_definition.py`
- **select_character()** (14 connections) — `server/api/players.py`
- **UUID** (14 connections)
- **UUID** (13 connections)
- **_validate_character_access()** (13 connections) — `server/api/players.py`
- **test_players_quests.py** (13 connections) — `server/tests/unit/api/test_players_quests.py`
- **get_player_skills()** (12 connections) — `server/api/players.py`
- **delete_player()** (12 connections) — `server/api/players.py`
- **_disconnect_other_characters()** (12 connections) — `server/api/players.py`
- **get_player()** (11 connections) — `server/api/players.py`
- **delete_character()** (11 connections) — `server/api/players.py`
- **_validate_player_for_grace_period()** (11 connections) — `server/api/players.py`
- **Any** (11 connections)
- **PlayerBase** (11 connections) — `server/schemas/players/player.py`
- **create_player()** (10 connections) — `server/api/players.py`
- **list_players()** (10 connections) — `server/api/players.py`
- *... and 164 more nodes in this community*

## Relationships

- [NPC Definitions Admin](NPC_Definitions_Admin.md) (30 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (30 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (22 shared connections)
- [player requests schemas](player_requests_schemas.md) (22 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (16 shared connections)
- [combat npc service](combat_npc_service.md) (11 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (10 shared connections)
- [command inventory models](command_inventory_models.md) (9 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (9 shared connections)
- [spell game magic](spell_game_magic.md) (9 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (8 shared connections)
- [rate limiter realtime](rate_limiter_realtime.md) (8 shared connections)

## Source Files

- `server/api/players.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/player_service.py`
- `server/schemas/players/class_definition.py`
- `server/schemas/players/player.py`
- `server/schemas/players/skill.py`
- `server/schemas/quest/quest.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/api/test_players_api_coverage.py`
- `server/tests/unit/api/test_players_quests.py`
- `server/tests/unit/game/test_player_service_mutations.py`

## Audit Trail

- EXTRACTED: 967 (90%)
- INFERRED: 102 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*