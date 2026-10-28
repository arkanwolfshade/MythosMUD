# Codebase Explorer Subagent

> 17 nodes · cohesion 0.17

## Key Concepts

- **send_system_message()** (17 connections) — `server/realtime/websocket_handler.py`
- **test_websocket_handler_system_message.py** (8 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **WebSocket** (4 connections)
- **asyncio** (4 connections)
- **test_send_system_message_disconnected()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_error()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_success()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **test_send_system_message_warning()** (4 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **mock_websocket()** (3 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Send a system message to a player. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/websocket_handler.py`
- **fixture** (1 connections)
- **Unit tests for websocket handler system message functions. Tests the system…** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Create a mock WebSocket.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() successfully sends message.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() with warning type.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() with error type.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **Test send_system_message() handles WebSocket disconnection.** (1 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Relationships

- [Alias](Alias.md) (3 shared connections)
- [NATSService](NATSService.md) (3 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (2 shared connections)
- [resolve_weapon_attack_from_equipped](resolve_weapon_attack_from_equipped.md) (2 shared connections)
- [test_corpse_lifecycle_decay.py](test_corpse_lifecycle_decay.py.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)
- [test_command_admin.py](test_command_admin.py.md) (1 shared connections)
- [look_container.py](look_container.py.md) (1 shared connections)

## Source Files

- `server/realtime/websocket_handler.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*