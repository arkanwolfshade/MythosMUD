# docs examples logging websocket integration

> 94 nodes

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **websocket_integration.py** (23 connections) — `docs/examples/logging/websocket_integration.py`
- **exception_tracker.py** (21 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (13 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **ExceptionStats** (10 connections) — `server/monitoring/exception_tracker.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **handle_websocket_message()** (7 connections) — `docs/examples/logging/websocket_integration.py`
- **Exception** (7 connections)
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (6 connections) — `server/monitoring/exception_tracker.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **ExceptionContextTrackInput** (4 connections) — `server/monitoring/exception_tracker.py`
- **handle_game_action()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **websocket_endpoint()** (4 connections) — `docs/examples/logging/websocket_integration.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._parse_track_options()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- **handle_chat_message()** (3 connections) — `docs/examples/logging/websocket_integration.py`
- *... and 69 more nodes in this community*

## Relationships

- [server monitoring init getattr](server_monitoring_init_getattr.md) (9 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (6 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [performancestats](performancestats.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server app lifespan](server_app_lifespan.md) (3 shared connections)
- [docs examples logging testing examples](docs_examples_logging_testing_examples.md) (3 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (2 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (2 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)

## Source Files

- `docs/examples/logging/websocket_integration.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 185 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*