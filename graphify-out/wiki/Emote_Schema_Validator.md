# Emote Schema Validator

> 10 nodes · cohesion 0.05

## Key Concepts

- **validate_room_data()** (15 connections) — `server/world_loader.py`
- **world_loader.py** (14 connections) — `server/world_loader.py`
- **get_room_environment()** (13 connections) — `server/world_loader.py`
- **generate_room_id()** (9 connections) — `server/world_loader.py`
- **Any** (4 connections) — `server/world_loader.py`
- **SchemaValidator** (3 connections) — `server/world_loader.py`
- **World loader utilities for room ID generation and schema validation.  This modul** (1 connections) — `server/world_loader.py`
- **Validate room data against schema if validation is available.      Args:** (1 connections) — `server/world_loader.py`
- **Generate hierarchical room ID from components.      Args:         plane: Plane i** (1 connections) — `server/world_loader.py`
- **Determine room environment using inheritance chain.      Priority order:     1.** (1 connections) — `server/world_loader.py`

## Relationships

- [Server Config Loading](Server_Config_Loading.md) (6 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Room Subscription Helpers](Room_Subscription_Helpers.md) (1 shared connections)
- [Async Persistence Types](Async_Persistence_Types.md) (1 shared connections)

## Source Files

- `server/world_loader.py`

## Audit Trail

- EXTRACTED: 58 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*