# services user manager

> 9 nodes

## Key Concepts

- **user_manager.py** (20 connections) — `server/services/user_manager.py`
- **chat_logger()** (7 connections) — `server/tests/unit/services/test_chat_logger.py`
- **.__init__()** (4 connections) — `server/services/user_manager.py`
- **_get_proper_data_dir()** (4 connections) — `server/services/user_manager.py`
- **Path** (3 connections)
- **User management service for MythosMUD chat system.  This module provides compr** (1 connections) — `server/services/user_manager.py`
- **Initialize the user manager.          Args:             data_dir: Directory f** (1 connections) — `server/services/user_manager.py`
- **Get the proper environment-aware data directory for user management.      Uses** (1 connections) — `server/services/user_manager.py`
- **Create a ChatLogger instance with temp directory.** (1 connections) — `server/tests/unit/services/test_chat_logger.py`

## Relationships

- [services user manager](services_user_manager.md) (5 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (2 shared connections)
- [chat game message](chat_game_message.md) (2 shared connections)
- [chat services logger](chat_services_logger.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [follow game service](follow_game_service.md) (1 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (1 shared connections)
- [user manager services](user_manager_services.md) (1 shared connections)

## Source Files

- `server/services/user_manager.py`
- `server/tests/unit/services/test_chat_logger.py`

## Audit Trail

- EXTRACTED: 37 (88%)
- INFERRED: 5 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*