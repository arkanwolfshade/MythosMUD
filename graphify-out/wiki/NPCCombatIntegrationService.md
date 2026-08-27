# NPCCombatIntegrationService

> 220 nodes

## Key Concepts

- **MythosMUDError** (45 connections) — `server/exceptions.py`
- **test_exceptions.py** (44 connections) — `server/tests/unit/test_exceptions.py`
- **RateLimitError** (35 connections) — `server/exceptions.py`
- **test_exceptions_comprehensive.py** (35 connections) — `server/tests/unit/test_exceptions_comprehensive.py`
- **ErrorContext** (34 connections) — `server/exceptions.py`
- **test_error_logging.py** (25 connections) — `server/tests/unit/utils/test_error_logging.py`
- **LoggedException** (20 connections) — `server/exceptions.py`
- **create_error_context()** (20 connections) — `server/exceptions.py`
- **.__init__()** (15 connections) — `server/exceptions.py`
- **CombatMessagingService** (14 connections) — `server/services/combat_messaging_service.py`
- **create_enhanced_error_context()** (13 connections) — `server/utils/enhanced_error_logging.py`
- **Any** (13 connections)
- **ResourceNotFoundError** (12 connections) — `server/exceptions.py`
- **handle_exception()** (11 connections) — `server/exceptions.py`
- **NetworkError** (10 connections) — `server/exceptions.py`
- **create_error_context()** (10 connections) — `server/api/player_helpers.py`
- **create_context_from_request()** (10 connections) — `server/utils/error_logging.py`
- **test_enhanced_logging_config.py** (9 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **ConfigurationError** (8 connections) — `server/exceptions.py`
- **GameLogicError** (8 connections) — `server/exceptions.py`
- **wrap_third_party_exception()** (8 connections) — `server/utils/error_logging.py`
- **_StubBoundLogger** (7 connections) — `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- **.__init__()** (7 connections) — `server/exceptions.py`
- **create_context_from_websocket()** (7 connections) — `server/utils/error_logging.py`
- **create_logged_http_exception()** (7 connections) — `server/utils/error_logging.py`
- *... and 195 more nodes in this community*

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (59 shared connections)
- [ContainerComponent](ContainerComponent.md) (12 shared connections)
- [ChatService](ChatService.md) (9 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (8 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (6 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (6 shared connections)
- [_handle_admin_set_stat_command](_handle_admin_set_stat_command.md) (6 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (6 shared connections)
- [ValidationError](ValidationError.md) (5 shared connections)
- [canonical_room_id_impl](canonical_room_id_impl.md) (4 shared connections)
- [register_user](register_user.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/api/player_helpers.py`
- `server/exceptions.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/api/test_player_helpers.py`
- `server/tests/unit/services/test_combat_messaging_service.py`
- `server/tests/unit/structured_logging/test_enhanced_logging_config.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/utils/test_enhanced_error_logging.py`
- `server/tests/unit/utils/test_error_logging.py`
- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 471 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*