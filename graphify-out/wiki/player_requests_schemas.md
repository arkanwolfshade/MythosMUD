# player requests schemas

> 11 nodes

## Key Concepts

- **player_requests.py** (14 connections) — `server/schemas/players/player_requests.py`
- **BaseModel** (11 connections)
- **SelectCharacterRequest** (8 connections) — `server/schemas/players/player_requests.py`
- **OccupationSlot** (3 connections) — `server/schemas/players/player_requests.py`
- **PersonalInterestSlot** (3 connections) — `server/schemas/players/player_requests.py`
- **test_select_character_request()** (3 connections) — `server/tests/unit/schemas/test_player_requests.py`
- **Request models for player API endpoints.  This module defines Pydantic request m** (1 connections) — `server/schemas/players/player_requests.py`
- **One occupation skill slot: skill_id and fixed value (70, 60, 50, or 40).** (1 connections) — `server/schemas/players/player_requests.py`
- **One personal interest skill: skill_id only (server applies base + 20).** (1 connections) — `server/schemas/players/player_requests.py`
- **Request model for character selection.** (1 connections) — `server/schemas/players/player_requests.py`
- **Test SelectCharacterRequest can be instantiated.** (1 connections) — `server/tests/unit/schemas/test_player_requests.py`

## Relationships

- [Player Stats](Player_Stats.md) (4 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [player schemas requests](player_schemas_requests.md) (3 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (2 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [combat messaging service](combat_messaging_service.md) (2 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (2 shared connections)
- [character creation validate](character_creation_validate.md) (2 shared connections)

## Source Files

- `server/schemas/players/player_requests.py`
- `server/tests/unit/schemas/test_player_requests.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*