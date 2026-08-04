# config models game

> 17 nodes

## Key Concepts

- **_StubPlayerRepo** (18 connections) — `server/tests/unit/persistence/test_protocols.py`
- **test_player_repository_protocol_stub()** (17 connections) — `server/tests/unit/persistence/test_protocols.py`
- **UUID** (6 connections)
- **.get_player_by_id()** (4 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_batch()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.soft_delete_player()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.delete_player()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.update_player_last_active()** (3 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_player_by_user_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_by_user_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_active_players_by_user_id()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_player_by_name()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.save_player()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.save_players()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.list_players()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.get_players_in_room()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`
- **.validate_and_fix_player_room()** (2 connections) — `server/tests/unit/persistence/test_protocols.py`

## Relationships

- [realtime circuit breaker](realtime_circuit_breaker.md) (4 shared connections)
- [persistence protocols rationale](persistence_protocols_rationale.md) (2 shared connections)
- [useDraggablePanelInteractions draggableP](useDraggablePanelInteractions_draggableP.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/test_protocols.py`

## Audit Trail

- EXTRACTED: 71 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*