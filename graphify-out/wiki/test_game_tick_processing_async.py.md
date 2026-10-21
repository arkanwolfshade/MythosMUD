# test_game_tick_processing_async.py

> 43 nodes · cohesion 0.07

## Key Concepts

- **EmoteService** (18 connections) — `server/game/emote_service.py`
- **test_emote_service.py** (17 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteRepository** (13 connections) — `server/persistence/repositories/emote_repository.py`
- **_service_with_emotes()** (10 connections) — `server/tests/unit/game/test_emote_service.py`
- **EmoteDefinition** (6 connections) — `server/game/emote_service.py`
- **._init_emote_service()** (5 connections) — `server/container/bundles/game.py`
- **.format_emote_messages()** (4 connections) — `server/game/emote_service.py`
- **.get_emote_definition()** (4 connections) — `server/game/emote_service.py`
- **test_load_emotes_handles_missing_table_gracefully()** (4 connections) — `server/tests/unit/game/test_emote_service.py`
- **.__init__()** (3 connections) — `server/game/emote_service.py`
- **.load_emotes()** (3 connections) — `server/game/emote_service.py`
- **.reload_emotes()** (3 connections) — `server/game/emote_service.py`
- **._validate_emote_payload()** (3 connections) — `server/game/emote_service.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/emote_repository.py`
- **asyncio** (3 connections)
- **test_emote_service_init_does_not_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_format_emote_messages_unknown_raises()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_load_emotes_populates_from_repository()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_reload_emotes_calls_load()** (3 connections) — `server/tests/unit/game/test_emote_service.py`
- **.is_emote_alias()** (2 connections) — `server/game/emote_service.py`
- **.list_available_emotes()** (2 connections) — `server/game/emote_service.py`
- **test_format_emote_messages()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_is_emote_alias_and_get_definition()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_list_available_emotes()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- **test_validate_emote_payload_no_validator()** (2 connections) — `server/tests/unit/game/test_emote_service.py`
- *... and 18 more nodes in this community*

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (6 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (5 shared connections)
- [endpoints.py](endpoints.py.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (2 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/game/emote_service.py`
- `server/persistence/repositories/emote_repository.py`
- `server/tests/unit/game/test_emote_service.py`

## Audit Trail

- EXTRACTED: 76 (93%)
- INFERRED: 6 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*