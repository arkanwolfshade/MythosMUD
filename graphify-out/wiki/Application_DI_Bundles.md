# Application DI Bundles

> 96 nodes · cohesion 0.03

## Key Concepts

- **ApplicationContainer** (107 connections) — `server/container/main.py`
- **test_application_container.py** (26 connections) — `server/tests/unit/test_application_container.py`
- **__init__.py** (19 connections) — `server/container/bundles/__init__.py`
- **.initialize()** (13 connections) — `server/container/main.py`
- **TimeBundle** (8 connections) — `server/container/bundles/time.py`
- **reset_container()** (8 connections) — `server/container/main.py`
- **__init__.py** (8 connections) — `server/tests/fixtures/unit/__init__.py`
- **ChatBundle** (7 connections) — `server/container/bundles/chat.py`
- **time.py** (7 connections) — `server/container/bundles/time.py`
- **chat.py** (6 connections) — `server/container/bundles/chat.py`
- **__init__.py** (6 connections) — `server/container/__init__.py`
- **Test ApplicationContainer._decode_json_column() decodes JSON.** (6 connections) — `server/tests/unit/test_application_container.py`
- **.shutdown()** (5 connections) — `server/container/main.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **strict_mocker()** (5 connections) — `server/tests/fixtures/unit/mock_helpers.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **.get_service()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **_flatten_bundle()** (4 connections) — `server/container/main.py`
- **utils.py** (4 connections) — `server/container/utils.py`
- **mock_helpers.py** (4 connections) — `server/tests/fixtures/unit/mock_helpers.py`
- **strict_patch()** (4 connections) — `server/tests/fixtures/unit/mock_helpers.py`
- **Test ApplicationContainer._normalize_path_from_url_or_path() normalizes path.** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_get_container_singleton()** (4 connections) — `server/tests/unit/test_application_container.py`
- *... and 71 more nodes in this community*

## Relationships

- [[Game Service Bundle]] (19 shared connections)
- [[NPC Admin API]] (18 shared connections)
- [[Combat Aggro Threat]] (9 shared connections)
- [[Magic Service Bundle]] (8 shared connections)
- [[Realtime Service Bundle]] (8 shared connections)
- [[WebSocket Message Handlers]] (8 shared connections)
- [[Monitoring Bundle Services]] (7 shared connections)
- [[NPC Services Bundle]] (7 shared connections)
- [[Combat Service Bundle]] (6 shared connections)
- [[Chat Service Whispers]] (4 shared connections)
- [[Time Event Consumer]] (4 shared connections)
- [[Game Tick Processing]] (2 shared connections)

## Source Files

- `server/container/__init__.py`
- `server/container/bundles/__init__.py`
- `server/container/bundles/chat.py`
- `server/container/bundles/time.py`
- `server/container/main.py`
- `server/container/utils.py`
- `server/tests/fixtures/unit/__init__.py`
- `server/tests/fixtures/unit/mock_helpers.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 371 (91%)
- INFERRED: 38 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
