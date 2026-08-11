# Commands Time

> 13 nodes

## Key Concepts

- **user_manager.py** (18 connections) — `server/services/user_manager.py`
- **.__init__()** (9 connections) — `server/realtime/event_handler.py`
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/rate_limiter.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **Initialize the real-time event handler.          Args:             event_bus: Op** (1 connections) — `server/realtime/event_handler.py`
- **Initialize the rate limiter with configuration-based limits.** (1 connections) — `server/services/rate_limiter.py`
- **User management service for MythosMUD chat system.  This module provides compr** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [Player Mute Persistence](Player_Mute_Persistence.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Command Parser](Command_Parser.md) (3 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (2 shared connections)
- [Performance Optimization Summary](Performance_Optimization_Summary.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (1 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (1 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (1 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (1 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (1 shared connections)

## Source Files

- `server/realtime/event_handler.py`
- `server/services/rate_limiter.py`
- `server/services/user_manager.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 48 (87%)
- INFERRED: 7 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*