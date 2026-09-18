# Player Effects (Corruption/Fear/Lucidity)

> 203 nodes

## Key Concepts

- **SecureBaseModel** (82 connections) — `server/schemas/shared/base.py`
- **test_player_requests.py** (36 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **api/player_effects.py** (35 connections) — `server/api/player_effects.py`
- **test_player_effects_endpoints.py** (31 connections) — `server/tests/unit/api/test_player_effects_endpoints.py`
- **shared/base.py** (26 connections) — `server/schemas/shared/base.py`
- **player_requests.py** (19 connections) — `server/schemas/players/player_requests.py`
- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **apply_lucidity_loss()** (14 connections) — `server/api/player_effects.py`
- **DialogueTree** (13 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **EffectResponse** (13 connections) — `server/schemas/players/player_effects.py`
- **apply_corruption()** (13 connections) — `server/api/player_effects.py`
- **apply_fear()** (13 connections) — `server/api/player_effects.py`
- **damage_player()** (13 connections) — `server/api/player_effects.py`
- **gain_occult_knowledge()** (13 connections) — `server/api/player_effects.py`
- **heal_player()** (13 connections) — `server/api/player_effects.py`
- **schemas/auth/__init__.py** (13 connections) — `server/schemas/auth/__init__.py`
- **test_user_schemas.py** (13 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **DamageRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **LucidityLossRequest** (12 connections) — `server/schemas/players/player_requests.py`
- **CorruptionRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **FearRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **HealRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **OccultKnowledgeRequest** (11 connections) — `server/schemas/players/player_requests.py`
- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **test_container_models.py** (10 connections) — `server/tests/unit/api/test_container_models.py`
- *... and 178 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (37 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (30 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (15 shared connections)
- [Realtime Message Handlers](Realtime_Message_Handlers.md) (14 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (14 shared connections)
- [Community 100](Community_100.md) (10 shared connections)
- [Community 28](Community_28.md) (7 shared connections)
- [Community 179](Community_179.md) (7 shared connections)
- [Community 424](Community_424.md) (6 shared connections)
- [Community 111](Community_111.md) (5 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (5 shared connections)
- [Community 64](Community_64.md) (3 shared connections)

## Source Files

- `server/api/player_effects.py`
- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/shared/base.py`
- `server/tests/unit/api/test_container_models.py`
- `server/tests/unit/api/test_npc_definitions_api.py`
- `server/tests/unit/api/test_npc_instances_api.py`
- `server/tests/unit/api/test_player_effects_endpoints.py`
- `server/tests/unit/schemas/test_dialogue_tree.py`
- `server/tests/unit/schemas/test_invite_schemas.py`
- `server/tests/unit/schemas/test_player_requests.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 535 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*