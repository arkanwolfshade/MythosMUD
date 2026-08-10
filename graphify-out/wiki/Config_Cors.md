# Config Cors

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

- [Design Cursor Skills](Design_Cursor_Skills.md) (4 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (3 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (3 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (3 shared connections)
- [Cursor Plans Github](Cursor_Plans_Github.md) (2 shared connections)
- [Cursor Plans App](Cursor_Plans_App.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

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