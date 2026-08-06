# NPC Combat

> 156 nodes

## Key Concepts

- **subject_controller.py** (27 connections) — `server/api/admin/subject_controller.py`
- **game.py** (25 connections) — `server/api/game.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_subject_controller.py** (21 connections) — `server/tests/unit/api/admin/test_subject_controller.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **MythosTimeResponse** (15 connections) — `server/schemas/game/game.py`
- **get_mythos_time()** (14 connections) — `server/api/game.py`
- **broadcast_message()** (13 connections) — `server/api/game.py`
- **register_pattern()** (12 connections) — `server/api/admin/subject_controller.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **TestGetMythosTime** (12 connections) — `server/tests/unit/api/test_game.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **__init__.py** (10 connections) — `server/api/__init__.py`
- **validate_subject()** (10 connections) — `server/api/admin/subject_controller.py`
- **GameStatusResponse** (9 connections) — `server/schemas/game/game.py`
- **BroadcastMessageResponse** (9 connections) — `server/schemas/game/game.py`
- **get_subject_statistics()** (8 connections) — `server/api/admin/subject_controller.py`
- **get_patterns()** (8 connections) — `server/api/admin/subject_controller.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **ValidateSubjectRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **RegisterPatternRequest** (7 connections) — `server/api/admin/subject_controller.py`
- **require_admin_user()** (7 connections) — `server/api/admin/subject_controller.py`
- **get_game_status()** (7 connections) — `server/api/game.py`
- **__init__.py** (7 connections) — `server/schemas/game/__init__.py`
- *... and 131 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (32 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (22 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (11 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (10 shared connections)
- [combat models rationale](combat_models_rationale.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)
- [manager subject services](manager_subject_services.md) (6 shared connections)
- [subject validation services](subject_validation_services.md) (6 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [Room Broadcast](Room_Broadcast.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/admin/subject_controller.py`
- `server/api/game.py`
- `server/auth/dependencies.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/auth/test_auth_dependencies.py`

## Audit Trail

- EXTRACTED: 592 (94%)
- INFERRED: 37 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*