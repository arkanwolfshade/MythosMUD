# WebSocket Command Handler

> 46 nodes

## Key Concepts

- **StatsGenerator** (36 connections) — `server/game/stats_generator.py`
- **Stats** (11 connections)
- **.roll_stats_with_profession()** (7 connections) — `server/game/stats_generator.py`
- **TestGetPlayerService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetRoomService** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **TestGetStatsGenerator** (7 connections) — `server/tests/unit/test_dependency_injection.py`
- **.roll_stats()** (6 connections) — `server/game/stats_generator.py`
- **._roll_size()** (5 connections) — `server/game/stats_generator.py`
- **._roll_3d6()** (5 connections) — `server/game/stats_generator.py`
- **.get_available_classes()** (5 connections) — `server/game/stats_generator.py`
- **.roll_stats_with_validation()** (5 connections) — `server/game/stats_generator.py`
- **._roll_4d6_drop_lowest()** (4 connections) — `server/game/stats_generator.py`
- **._roll_point_buy()** (4 connections) — `server/game/stats_generator.py`
- **.validate_class_prerequisites()** (4 connections) — `server/game/stats_generator.py`
- **._check_profession_requirements()** (4 connections) — `server/game/stats_generator.py`
- **.get_stat_summary()** (4 connections) — `server/game/stats_generator.py`
- **.test_get_player_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_success()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_stats_generator_stateless()** (4 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_player_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.test_get_room_service_not_initialized()** (3 connections) — `server/tests/unit/test_dependency_injection.py`
- **.__init__()** (2 connections) — `server/game/stats_generator.py`
- **Any** (2 connections)
- **Service for generating random character statistics.** (1 connections) — `server/game/stats_generator.py`
- *... and 21 more nodes in this community*

## Relationships

- [Player Domain Model](Player_Domain_Model.md) (14 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Inventory Service Helpers](Inventory_Service_Helpers.md) (4 shared connections)
- [Container Loot Helpers](Container_Loot_Helpers.md) (3 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (1 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (1 shared connections)
- [System Monitoring API](System_Monitoring_API.md) (1 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/game/stats_generator.py`
- `server/tests/unit/test_dependency_injection.py`

## Audit Trail

- EXTRACTED: 148 (88%)
- INFERRED: 21 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*