# Community 783

> 21 nodes

## Key Concepts

- **_resolve_summon_context()** (14 connections) — `server/commands/admin_summon_command.py`
- **asyncio** (13 connections)
- **handle_summon_command()** (12 connections) — `server/commands/admin_summon_command.py`
- **_complete_summon()** (10 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **test_complete_summon_factory_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_swallows_db_error()** (4 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_no_instance_without_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_complete_summon_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_context_none()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_parse_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_handle_summon_command_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_persist_summoned_item_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_permission_denied()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_player_error()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **test_resolve_summon_context_success()** (3 connections) — `server/tests/unit/commands/test_admin_summon_command.py`
- **Persist item instance to DB. Logs and continues on failure (room drop still…** (1 connections) — `server/commands/admin_summon_command.py`
- **Resolve state, player, admin permission, and summon prerequisites. Returns…** (1 connections) — `server/commands/admin_summon_command.py`
- **Create item, persist, add to room, broadcast event, log; return success message.** (1 connections) — `server/commands/admin_summon_command.py`
- **Handle the `/summon` administrative command.** (1 connections) — `server/commands/admin_summon_command.py`

## Relationships

- [Community 567](Community_567.md) (21 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 42](Community_42.md) (1 shared connections)
- [Community 752](Community_752.md) (1 shared connections)
- [Community 131](Community_131.md) (1 shared connections)
- [Community 937](Community_937.md) (1 shared connections)
- [Community 673](Community_673.md) (1 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (1 shared connections)
- [Community 343](Community_343.md) (1 shared connections)
- [Community 253](Community_253.md) (1 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/tests/unit/commands/test_admin_summon_command.py`

## Audit Trail

- EXTRACTED: 63 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*