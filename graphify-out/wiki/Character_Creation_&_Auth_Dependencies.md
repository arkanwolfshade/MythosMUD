# Character Creation & Auth Dependencies

> 522 nodes

## Key Concepts

- **User** (287 connections) — `server/models/user.py`
- **models/user.py** (67 connections) — `server/models/user.py`
- **api/character_creation.py** (66 connections) — `server/api/character_creation.py`
- **command_handler_unified.py** (55 connections) — `server/command_handler_unified.py`
- **lifespan.py** (45 connections) — `server/app/lifespan.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **factory.py** (44 connections) — `server/app/factory.py`
- **users.py** (42 connections) — `server/auth/users.py`
- **SkillService** (33 connections) — `server/game/skill_service.py`
- **api/game.py** (28 connections) — `server/api/game.py`
- **time_service.py** (27 connections) — `server/time/time_service.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **CreateCharacterRequest** (25 connections) — `server/schemas/players/player_requests.py`
- **RollStatsRequest** (23 connections) — `server/schemas/players/player_requests.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **test_character_creation.py** (22 connections) — `server/tests/unit/api/test_character_creation.py`
- **invites.py** (21 connections) — `server/auth/invites.py`
- **get_mythos_chronicle()** (20 connections) — `server/time/time_service.py`
- **professions.py** (20 connections) — `server/api/professions.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **ProfessionService** (19 connections) — `server/game/profession_service.py`
- **server/main.py** (19 connections) — `server/main.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- *... and 497 more nodes in this community*

## Relationships

- [User Manager & Character Info](User_Manager_&_Character_Info.md) (113 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (106 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (81 shared connections)
- [Community 31](Community_31.md) (74 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (37 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (34 shared connections)
- [Community 79](Community_79.md) (28 shared connections)
- [Invite Codes & Session Maker (E2E)](Invite_Codes_&_Session_Maker_E2E.md) (23 shared connections)
- [Community 140](Community_140.md) (18 shared connections)
- [FastAPI Dependency Providers](FastAPI_Dependency_Providers.md) (18 shared connections)
- [Community 256](Community_256.md) (17 shared connections)
- [Community 145](Community_145.md) (16 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/api/container_models.py`
- `server/api/game.py`
- `server/api/player_helpers.py`
- `server/api/professions.py`
- `server/api/skills.py`
- `server/app/factory.py`
- `server/app/lifespan.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/command_handler_unified.py`
- `server/commands/admin_shutdown_command.py`
- `server/commands/time_commands.py`
- `server/container/__init__.py`
- `server/dependencies.py`
- `server/exceptions.py`

## Audit Trail

- EXTRACTED: 1678 (93%)
- INFERRED: 132 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*