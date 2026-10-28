# game_tick_processing.py

> 59 nodes · cohesion 0.04

## Key Concepts

- **UUID** (14 connections)
- **PlayerCreationService** (12 connections) — `server/game/player_creation_service.py`
- **Any** (11 connections)
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.__init__()** (8 connections) — `server/game/player_service.py`
- **._build_new_player()** (7 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **UUID** (6 connections)
- **._check_character_limit()** (5 connections) — `server/game/player_creation_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (5 connections) — `server/game/player_service.py`
- **.delete_player()** (5 connections) — `server/game/player_service.py`
- **.get_player_by_id()** (5 connections) — `server/game/player_service.py`
- **.soft_delete_character()** (5 connections) — `server/game/player_service.py`
- **.validate_character_access()** (5 connections) — `server/game/player_service.py`
- **._check_name_available()** (4 connections) — `server/game/player_creation_service.py`
- **.apply_corruption()** (4 connections) — `server/game/player_service.py`
- **.apply_fear()** (4 connections) — `server/game/player_service.py`
- **.apply_lucidity_loss()** (4 connections) — `server/game/player_service.py`
- **.convert_player_to_schema()** (4 connections) — `server/game/player_service.py`
- **.create_player()** (4 connections) — `server/game/player_service.py`
- **.damage_player()** (4 connections) — `server/game/player_service.py`
- **.gain_occult_knowledge()** (4 connections) — `server/game/player_service.py`
- **.get_user_characters()** (4 connections) — `server/game/player_service.py`
- **.heal_player()** (4 connections) — `server/game/player_service.py`
- *... and 34 more nodes in this community*

## Relationships

- [test_security_validator.py](test_security_validator.py.md) (19 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (13 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)
- [Communities (11 total, 0 thin omitted)](Communities_11_total,_0_thin_omitted.md) (1 shared connections)
- [_ScalarResult](_ScalarResult.md) (1 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`
- `server/game/player_service.py`

## Audit Trail

- EXTRACTED: 116 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*