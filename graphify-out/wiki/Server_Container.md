# Server Container

> 26 nodes

## Key Concepts

- **GameBundle** (15 connections) — `server/container/bundles/game.py`
- **.initialize()** (11 connections) — `server/container/bundles/game.py`
- **game.py** (9 connections) — `server/container/bundles/game.py`
- **._initialize_item_services()** (6 connections) — `server/container/bundles/game.py`
- **._require_core_services()** (5 connections) — `server/container/bundles/game.py`
- **._wire_user_manager_after_init()** (4 connections) — `server/container/bundles/game.py`
- **._initialize_caching_services()** (4 connections) — `server/container/bundles/game.py`
- **._handle_item_prototypes_db_error()** (4 connections) — `server/container/bundles/game.py`
- **._build_prototype_payload()** (4 connections) — `server/container/bundles/game.py`
- **Any** (3 connections)
- **ApplicationContainer** (3 connections)
- **._resolve_hourly_holidays()** (3 connections) — `server/container/bundles/game.py`
- **._wire_item_registry_to_player_service()** (3 connections) — `server/container/bundles/game.py`
- **datetime** (2 connections)
- **Exception** (1 connections)
- **Game bundle: player, room, movement, exploration, user_manager, container_servic** (1 connections) — `server/container/bundles/game.py`
- **Game services: movement, player, room, user, container, caches, temporal, items.** (1 connections) — `server/container/bundles/game.py`
- **Raise if core services are missing (required before GameBundle init).** (1 connections) — `server/container/bundles/game.py`
- **Resolve active holiday names for tick scheduler; return empty list on error or n** (1 connections) — `server/container/bundles/game.py`
- **Wire user_manager into follow_service and nats_message_handler when present.** (1 connections) — `server/container/bundles/game.py`
- **Set item prototype registry on player service when both are available.** (1 connections) — `server/container/bundles/game.py`
- **Create room and profession cache services; set to None on RuntimeError.** (1 connections) — `server/container/bundles/game.py`
- **Initialize game services. Requires Core and Realtime.** (1 connections) — `server/container/bundles/game.py`
- **On SQLAlchemyError: log, optionally warn about schema/DDL, and clear item regist** (1 connections) — `server/container/bundles/game.py`
- **Build a single item prototype payload from a DB row for validation.** (1 connections) — `server/container/bundles/game.py`
- *... and 1 more nodes in this community*

## Relationships

- [Server App (2)](Server_App_%282%29.md) (5 shared connections)
- [Server Game (26)](Server_Game_%2826%29.md) (3 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Utils (14)](Server_Utils_%2814%29.md) (1 shared connections)
- [Server Realtime (82)](Server_Realtime_%2882%29.md) (1 shared connections)
- [Server Quest](Server_Quest.md) (1 shared connections)
- [Server (11)](Server_%2811%29.md) (1 shared connections)

## Source Files

- `server/container/bundles/game.py`

## Audit Trail

- EXTRACTED: 84 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*