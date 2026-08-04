# level curve game

> 6 nodes

## Key Concepts

- **__init__.py** (12 connections) — `server/schemas/auth/__init__.py`
- **UserRead** (7 connections) — `server/schemas/auth/user.py`
- **test_user_read()** (3 connections) — `server/tests/unit/schemas/test_user_schemas.py`
- **Auth domain schemas: user and invite.** (1 connections) — `server/schemas/auth/__init__.py`
- **Schema for reading user data.** (1 connections) — `server/schemas/auth/user.py`
- **Test UserRead can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_user_schemas.py`

## Relationships

- [message filtering helpers](message_filtering_helpers.md) (4 shared connections)
- [command factories moderation](command_factories_moderation.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [professions endpoints all](professions_endpoints_all.md) (1 shared connections)
- [combat models rationale](combat_models_rationale.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [spawn npc services](spawn_npc_services.md) (1 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (1 shared connections)

## Source Files

- `server/schemas/auth/__init__.py`
- `server/schemas/auth/user.py`
- `server/tests/unit/schemas/test_user_schemas.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*