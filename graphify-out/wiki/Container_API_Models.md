# Container API Models

> 567 nodes

## Key Concepts

- **LoggedHTTPException** (379 connections) — `server/exceptions.py`
- **container_endpoints_basic.py** (57 connections) — `server/api/container_endpoints_basic.py`
- **RateLimitError** (44 connections) — `server/exceptions.py`
- **LootAllRequest** (41 connections) — `server/api/container_models.py`
- **api/container_helpers.py** (40 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (40 connections) — `server/tests/unit/api/test_container_helpers.py`
- **loot_all_items()** (34 connections) — `server/api/container_endpoints_loot.py`
- **handle_transfer_items_exceptions()** (29 connections) — `server/api/container_exception_handlers.py`
- **container_endpoints_loot.py** (29 connections) — `server/api/container_endpoints_loot.py`
- **transfer_items()** (28 connections) — `server/api/container_endpoints_basic.py`
- **open_container()** (27 connections) — `server/api/container_endpoints_basic.py`
- **get_container_service()** (26 connections) — `server/api/container_helpers.py`
- **test_container_exception_handlers.py** (26 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_containers.py** (26 connections) — `server/tests/unit/api/test_containers.py`
- **handle_open_container_exceptions()** (24 connections) — `server/api/container_exception_handlers.py`
- **close_container()** (23 connections) — `server/api/container_endpoints_basic.py`
- **test_player_schema_converter_weapon.py** (23 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **test_container_helpers_loot.py** (22 connections) — `server/tests/unit/api/test_container_helpers_loot.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **container_exception_handlers.py** (21 connections) — `server/api/container_exception_handlers.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **handle_container_service_error()** (20 connections) — `server/api/container_helpers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **TransferContainerRequest** (17 connections) — `server/api/container_models.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- *... and 542 more nodes in this community*

## Relationships

- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (73 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (73 shared connections)
- [API Response Models](API_Response_Models.md) (66 shared connections)
- [Map & Admin Responses](Map_&_Admin_Responses.md) (34 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (28 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (28 shared connections)
- [Community 694](Community_694.md) (24 shared connections)
- [Community 424](Community_424.md) (20 shared connections)
- [Community 180](Community_180.md) (18 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (18 shared connections)
- [Community 147](Community_147.md) (15 shared connections)
- [Community 67](Community_67.md) (14 shared connections)

## Source Files

- `server/api/admin/subject_controller.py`
- `server/api/container_endpoints_basic.py`
- `server/api/container_endpoints_loot.py`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/api/real_time.py`
- `server/dependencies.py`
- `server/exceptions.py`
- `server/game/player_schema_converter.py`
- `server/schemas/containers/__init__.py`
- `server/schemas/containers/container.py`
- `server/schemas/containers/container_data.py`
- `server/schemas/game/weapon.py`
- `server/services/container_service.py`
- `server/tests/fixtures/shared/weapon_metadata.py`
- `server/tests/unit/api/admin/test_subject_controller.py`
- `server/tests/unit/api/test_container_endpoints_basic_weapon.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`

## Audit Trail

- EXTRACTED: 1467 (86%)
- INFERRED: 245 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*