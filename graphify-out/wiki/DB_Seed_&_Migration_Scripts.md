# DB Seed & Migration Scripts

> 181 nodes

## Key Concepts

- **get_async_session()** (70 connections) — `server/database.py`
- **rescue_commands.py** (44 connections) — `server/commands/rescue_commands.py`
- **corruption_service.py** (42 connections) — `server/services/corruption_service.py`
- **cleanse_command.py** (23 connections) — `server/commands/cleanse_command.py`
- **CorruptionRepository** (18 connections) — `server/services/corruption_repository.py`
- **CorruptionService** (16 connections) — `server/services/corruption_service.py`
- **test_corruption_repository.py** (14 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **handle_cleanse_command()** (13 connections) — `server/commands/cleanse_command.py`
- **compute_tier()** (13 connections) — `server/models/corruption.py`
- **.apply_corruption_adjustment()** (13 connections) — `server/services/corruption_service.py`
- **player_state_service.py** (13 connections) — `server/game/player_state_service.py`
- **test_cleanse_command.py** (13 connections) — `server/tests/unit/commands/test_cleanse_command.py`
- **CorruptionPersistencePlayer** (11 connections) — `server/services/corruption_service.py`
- **_MockAsyncSession** (10 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **_finish_ground()** (10 connections) — `server/commands/rescue_commands.py`
- **.perform_recovery_action()** (10 connections) — `server/services/corruption_service.py`
- **corruption_repository.py** (10 connections) — `server/services/corruption_repository.py`
- **PlayerStateService** (9 connections) — `server/game/player_state_service.py`
- **CorruptionPersistenceProtocol** (9 connections) — `server/services/corruption_service.py`
- **CleansePersistence** (8 connections) — `server/commands/cleanse_command.py`
- **CorruptionActionOnCooldownError** (8 connections) — `server/services/corruption_service.py`
- **.get_cooldown_expiry()** (7 connections) — `server/services/corruption_service.py`
- **test_get_cooldown_returns_record()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **test_set_cooldown_updates_existing()** (7 connections) — `server/tests/unit/services/test_corruption_repository.py`
- **Any** (7 connections)
- *... and 156 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (44 shared connections)
- [Community 115](Community_115.md) (14 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (13 shared connections)
- [Schema Validation & Channels](Schema_Validation_&_Channels.md) (13 shared connections)
- [Channel Commands](Channel_Commands.md) (8 shared connections)
- [Community 337](Community_337.md) (8 shared connections)
- [Core Bundle & DB Init](Core_Bundle_&_DB_Init.md) (6 shared connections)
- [Community 207](Community_207.md) (6 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (5 shared connections)
- [Community 245](Community_245.md) (4 shared connections)
- [Community 206](Community_206.md) (4 shared connections)
- [Community 416](Community_416.md) (3 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/commands/cleanse_command.py`
- `server/commands/rescue_commands.py`
- `server/database.py`
- `server/game/player_state_service.py`
- `server/models/corruption.py`
- `server/services/corruption_repository.py`
- `server/services/corruption_service.py`
- `server/tests/unit/commands/test_cleanse_command.py`
- `server/tests/unit/models/test_corruption.py`
- `server/tests/unit/services/test_corruption_repository.py`

## Audit Trail

- EXTRACTED: 476 (97%)
- INFERRED: 17 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*