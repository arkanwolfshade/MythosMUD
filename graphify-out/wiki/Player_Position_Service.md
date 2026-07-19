# Player Position Service

> 68 nodes · cohesion 0.05

## Key Concepts

- **PlayerPositionService** (60 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (26 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.change_position()** (10 connections) — `server/services/player_position_service.py`
- **Any** (7 connections) — `server/services/player_position_service.py`
- **._extract_player_info()** (4 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (4 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (4 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (4 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (4 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **.__init__()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **test_change_position_all_positions()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_already_in_position()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_get_stats_error()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_invalid_position()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_get_stats()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_no_persistence()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_player_not_found()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_success()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_connection_manager()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_updates_existing_connection_info()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_creates_missing()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [[Distributed Event Bus]] (14 shared connections)
- [[Game Service Bundle]] (7 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Rest Command Flow]] (2 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 219 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
