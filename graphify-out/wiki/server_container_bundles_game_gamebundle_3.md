# server container bundles game gamebundle

> 27 nodes

## Key Concepts

- **._initialize_item_services()** (8 connections) — `server/container/bundles/game.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **.get_service()** (3 connections) — `server/container/main.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **Path** (2 connections)
- **Delegate to shared util. Kept for backward compatibility.** (2 connections) — `server/container/main.py`
- **Exception** (1 connections)
- **Any** (1 connections)
- **Path** (1 connections)
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item…** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- **Load item prototypes from PostgreSQL and create item factory.** (1 connections) — `server/container/bundles/game.py`
- **Return and cache the repository root directory.** (1 connections) — `server/container/main.py`
- **Get a service by name.** (1 connections) — `server/container/main.py`
- *... and 2 more nodes in this community*

## Relationships

- [server container bundles chat](server_container_bundles_chat.md) (13 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (4 shared connections)
- [server caching cache service](server_caching_cache_service.md) (2 shared connections)
- [iteminstance](iteminstance.md) (2 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*