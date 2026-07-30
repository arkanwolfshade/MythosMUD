# NPCInstanceService

> 15 nodes

## Key Concepts

- **__init__.py** (12 connections) — `server/schemas/auth/__init__.py`
- **SecureBaseModel** (10 connections) — `server/schemas/shared/base.py`
- **user.py** (9 connections) — `server/schemas/auth/user.py`
- **invite.py** (8 connections) — `server/schemas/auth/invite.py`
- **UserRead** (7 connections) — `server/schemas/auth/user.py`
- **base.py** (6 connections) — `server/schemas/shared/base.py`
- **ResponseBaseModel** (6 connections) — `server/schemas/shared/base.py`
- **BaseModel** (2 connections)
- **Auth domain schemas: user and invite.** (1 connections) — `server/schemas/auth/__init__.py`
- **Pydantic schemas for Invite model.  This module defines Pydantic schemas for inv** (1 connections) — `server/schemas/auth/invite.py`
- **Pydantic schemas for User model.  This module defines Pydantic schemas for user** (1 connections) — `server/schemas/auth/user.py`
- **Schema for reading user data.** (1 connections) — `server/schemas/auth/user.py`
- **Base Pydantic model classes for MythosMUD schemas.  This module provides base cl** (1 connections) — `server/schemas/shared/base.py`
- **Base model with standard security configuration.      All models that handle use** (1 connections) — `server/schemas/shared/base.py`
- **Base model for API response schemas.      Response models may need additional co** (1 connections) — `server/schemas/shared/base.py`

## Relationships

- [. call ()](_call_%28%29.md) (10 shared connections)
- [init](init.md) (8 shared connections)
- [lifespan](lifespan.md) (3 shared connections)
- [test player event handlers state](test_player_event_handlers_state.md) (2 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)

## Source Files

- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/schemas/auth/user.py`
- `server/schemas/shared/base.py`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*