# utils.py

> 25 nodes

## Key Concepts

- **utils.py** (8 connections) — `server/container/utils.py`
- **decode_json_column()** (7 connections) — `server/container/utils.py`
- **._initialize_caching_services()** (6 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (5 connections) — `server/container/bundles/game.py`
- **normalize_path_from_url_or_path()** (5 connections) — `server/container/utils.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._decode_json_column()** (4 connections) — `server/container/main.py`
- **._get_project_root()** (4 connections) — `server/container/main.py`
- **._normalize_path_from_url_or_path()** (4 connections) — `server/container/main.py`
- **.get_service()** (3 connections) — `server/container/main.py`
- **Any** (3 connections)
- **Any** (3 connections)
- **Path** (2 connections)
- **Any** (1 connections)
- **Path** (1 connections)
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- **Return and cache the repository root directory.** (1 connections) — `server/container/main.py`
- **Delegate to shared util. Kept for backward compatibility.** (1 connections) — `server/container/main.py`
- **Delegate to shared util. Kept for backward compatibility.** (1 connections) — `server/container/main.py`
- **Get a service by name.** (1 connections) — `server/container/main.py`
- **Shared utilities for container and bundles. Holds helpers extracted from…** (1 connections) — `server/container/utils.py`
- **Decode a JSON column value, returning the type's default on failure. Used by…** (1 connections) — `server/container/utils.py`
- **Normalize an item database override into a filesystem path. DEPRECATED: Items…** (1 connections) — `server/container/utils.py`

## Relationships

- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)
- [bundles/game.py](bundles-game.py.md) (5 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [._initialize_item_services](_initialize_item_services.md) (1 shared connections)
- [RoomCacheService](RoomCacheService.md) (1 shared connections)
- [ProfessionCacheService](ProfessionCacheService.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`
- `server/container/main.py`
- `server/container/utils.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*