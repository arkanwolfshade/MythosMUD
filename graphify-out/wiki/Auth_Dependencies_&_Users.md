# Auth Dependencies & Users

> 464 nodes

## Key Concepts

- **User** (215 connections) — `server/models/user.py`
- **models/user.py** (75 connections) — `server/models/user.py`
- **factory.py** (51 connections) — `server/app/factory.py`
- **endpoints.py** (51 connections) — `server/auth/endpoints.py`
- **users.py** (50 connections) — `server/auth/users.py`
- **login_user()** (34 connections) — `server/auth/endpoints.py`
- **UserCreate** (31 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **subject_controller.py** (31 connections) — `server/api/admin/subject_controller.py`
- **test_endpoints_register.py** (30 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **system_monitoring.py** (24 connections) — `server/api/system_monitoring.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **api/game.py** (22 connections) — `server/api/game.py`
- **invites.py** (21 connections) — `server/auth/invites.py`
- **professions.py** (20 connections) — `server/api/professions.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **server/main.py** (19 connections) — `server/main.py`
- **api/item_catalog.py** (18 connections) — `server/api/item_catalog.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **asyncio** (18 connections)
- **get_system_metrics()** (15 connections) — `server/api/system_monitoring.py`
- *... and 439 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (74 shared connections)
- [Container API Models](Container_API_Models.md) (73 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (39 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (28 shared connections)
- [API Response Models](API_Response_Models.md) (25 shared connections)
- [Map & Admin Responses](Map_&_Admin_Responses.md) (22 shared connections)
- [Community 147](Community_147.md) (18 shared connections)
- [Community 193](Community_193.md) (15 shared connections)
- [Community 467](Community_467.md) (13 shared connections)
- [Community 291](Community_291.md) (13 shared connections)
- [Community 476](Community_476.md) (13 shared connections)
- [Community 411](Community_411.md) (13 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/admin/subject_controller.py`
- `server/api/containers.py`
- `server/api/game.py`
- `server/api/help.py`
- `server/api/item_catalog.py`
- `server/api/monitoring_models.py`
- `server/api/player_helpers.py`
- `server/api/player_router.py`
- `server/api/professions.py`
- `server/api/skills.py`
- `server/api/system_monitoring.py`
- `server/app/factory.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/command_handler_unified.py`

## Audit Trail

- EXTRACTED: 1321 (89%)
- INFERRED: 161 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*