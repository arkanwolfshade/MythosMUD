# server game profession service professionservice

> 7 nodes

## Key Concepts

- **.profession_to_dict()** (5 connections) — `server/game/profession_service.py`
- **.get_all_professions_dict()** (4 connections) — `server/game/profession_service.py`
- **.get_profession_by_id_dict()** (4 connections) — `server/game/profession_service.py`
- **Any** (3 connections)
- **Convert a Profession model to a dictionary for API responses. Args: profession:…** (1 connections) — `server/game/profession_service.py`
- **Get all available professions as dictionaries. Returns: list[dict[str, Any]]:…** (1 connections) — `server/game/profession_service.py`
- **Get a profession by ID as a dictionary. Args: profession_id: Profession ID…** (1 connections) — `server/game/profession_service.py`

## Relationships

- [server api character creation](server_api_character_creation.md) (3 shared connections)

## Source Files

- `server/game/profession_service.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*