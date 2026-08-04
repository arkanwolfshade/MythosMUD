# message filtering helpers

> 11 nodes

## Key Concepts

- **SecureBaseModel** (10 connections) — `server/schemas/shared/base.py`
- **user.py** (9 connections) — `server/schemas/auth/user.py`
- **invite.py** (8 connections) — `server/schemas/auth/invite.py`
- **base.py** (6 connections) — `server/schemas/shared/base.py`
- **ResponseBaseModel** (6 connections) — `server/schemas/shared/base.py`
- **BaseModel** (2 connections)
- **Pydantic schemas for Invite model.  This module defines Pydantic schemas for inv** (1 connections) — `server/schemas/auth/invite.py`
- **Pydantic schemas for User model.  This module defines Pydantic schemas for user** (1 connections) — `server/schemas/auth/user.py`
- **Base Pydantic model classes for MythosMUD schemas.  This module provides base cl** (1 connections) — `server/schemas/shared/base.py`
- **Base model with standard security configuration.      All models that handle use** (1 connections) — `server/schemas/shared/base.py`
- **Base model for API response schemas.      Response models may need additional co** (1 connections) — `server/schemas/shared/base.py`

## Relationships

- [level curve game](level_curve_game.md) (4 shared connections)
- [command factories moderation](command_factories_moderation.md) (3 shared connections)
- [target resolution service](target_resolution_service.md) (3 shared connections)
- [professions endpoints all](professions_endpoints_all.md) (2 shared connections)
- [spawn npc services](spawn_npc_services.md) (2 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)

## Source Files

- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/shared/base.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*