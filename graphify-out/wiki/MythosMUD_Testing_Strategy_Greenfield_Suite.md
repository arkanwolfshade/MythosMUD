# MythosMUD Testing Strategy (Greenfield Suite)

> 12 nodes

## Key Concepts

- **test_message_filtering.py** (36 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_collect_room_targets_empty()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver_not_muted()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_message_filtering_helper_init()** (2 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_by_receiver_exception()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **test_is_player_muted_global_mute_and_admin()** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Unit tests for message filtering. Tests the MessageFilteringHelper class.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test is_player_muted_by_receiver() checks mute status.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test is_player_muted_by_receiver() returns False when not muted.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test MessageFilteringHelper initialization.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`
- **Test collect_room_targets() returns empty set when no subscribers.** (1 connections) — `server/tests/unit/realtime/test_message_filtering.py`

## Relationships

- [](unnamed.md) (11 shared connections)
- [Hardening Dimensions](Hardening_Dimensions.md) (10 shared connections)
- [Three-Column Panel Wireframe Layout](Three-Column_Panel_Wireframe_Layout.md) (2 shared connections)
- [apply_migration](apply_migration.md) (2 shared connections)
- [test_admin_summon_command.py](test_admin_summon_command.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)
- [Test _get_user_manager() falls](Test__get_user_manager_falls.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_filtering.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*