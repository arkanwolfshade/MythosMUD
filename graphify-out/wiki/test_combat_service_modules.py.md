# test_combat_service_modules.py

> 90 nodes

## Key Concepts

- **endpoints.py** (48 connections) — `server/auth/endpoints.py`
- **register_user()** (32 connections) — `server/auth/endpoints.py`
- **UserCreate** (24 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (21 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **asyncio** (14 connections)
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **User** (9 connections)
- **Request** (8 connections)
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **IntegrityError** (7 connections)
- **_check_shutdown_status()** (6 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (6 connections) — `server/auth/endpoints.py`
- **_create_user_object()** (6 connections) — `server/auth/endpoints.py`
- **_generate_jwt_token()** (6 connections) — `server/auth/endpoints.py`
- **_mark_invite_as_used()** (6 connections) — `server/auth/endpoints.py`
- **test_register_user_email_constraint_violation()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginResponse** (5 connections) — `server/auth/endpoints.py`
- *... and 65 more nodes in this community*

## Relationships

- [CombatEventHandler](CombatEventHandler.md) (17 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (10 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [useRespawnHandlers.ts](useRespawnHandlers.ts.md) (4 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (4 shared connections)
- [maps.py](maps.py.md) (2 shared connections)
- [models/container.py](models-container.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [Hierarchical Test Structure](Hierarchical_Test_Structure.md) (1 shared connections)
- [container_persistence.py](container_persistence.py.md) (1 shared connections)
- [EldritchIcon.tsx](EldritchIcon.tsx.md) (1 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_register.py`

## Audit Trail

- EXTRACTED: 223 (92%)
- INFERRED: 20 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*