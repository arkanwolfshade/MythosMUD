# NATSMessageSubscriptionMixin

> 49 nodes

## Key Concepts

- **.get_instance()** (34 connections) — `server/container/main.py`
- **test_combat_cleanup_handler.py** (18 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.connection_manager()** (15 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (14 connections) — `server/services/combat_service.py`
- **CombatCleanupHandler** (12 connections) — `server/services/combat_cleanup_handler.py`
- **.check_player_connection_state()** (6 connections) — `server/services/npc_combat_rewards.py`
- **.check_connection_state()** (5 connections) — `server/services/combat_cleanup_handler.py`
- **._resolve_connection_manager_from_container()** (5 connections) — `server/services/combat_messaging/base.py`
- **.__init__()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **.cleanup_combat_tracking()** (3 connections) — `server/services/combat_cleanup_handler.py`
- **Any** (3 connections)
- **cleanup_handler()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **mock_combat()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_end_combat_method()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_stale_combats_no_stale_combats()** (3 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **.cleanup_stale_combats()** (2 connections) — `server/services/combat_cleanup_handler.py`
- **mock_combat_service()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_handler_init()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_cleanup_combat_tracking()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_error()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_no_connection_manager()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **test_check_connection_state_no_room_subscriptions()** (2 connections) — `server/tests/unit/services/test_combat_cleanup_handler.py`
- **Get the singleton container instance.** (1 connections) — `server/container/main.py`
- *... and 24 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (18 shared connections)
- [Any](Any.md) (11 shared connections)
- [.get instance()](get_instance%28%29.md) (3 shared connections)
- [.shutdown()](shutdown%28%29.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [look container](look_container.md) (3 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (2 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (2 shared connections)
- [test combat persistence handler persistence](test_combat_persistence_handler_persistence.md) (2 shared connections)
- [SafeHtml](SafeHtml.md) (2 shared connections)
- [src/**/*.spec](src-__-_.spec.md) (2 shared connections)

## Source Files

- `server/container/main.py`
- `server/services/combat_cleanup_handler.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_service.py`
- `server/services/npc_combat_rewards.py`
- `server/tests/unit/services/test_combat_cleanup_handler.py`

## Audit Trail

- EXTRACTED: 153 (88%)
- INFERRED: 21 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*