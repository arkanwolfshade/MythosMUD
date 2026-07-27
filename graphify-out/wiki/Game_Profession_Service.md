# Game Profession Service

> 13 nodes · cohesion 0.21

## Key Concepts

- **ProfessionService** (11 connections) — `server/game/profession_service.py`
- **.profession_to_dict()** (5 connections) — `server/game/profession_service.py`
- **.get_all_professions_dict()** (4 connections) — `server/game/profession_service.py`
- **.get_profession_by_id_dict()** (4 connections) — `server/game/profession_service.py`
- **.validate_and_get_profession()** (3 connections) — `server/game/profession_service.py`
- **Any** (3 connections) — `server/game/profession_service.py`
- **.__init__()** (2 connections) — `server/game/profession_service.py`
- **Service class for profession-related business operations.** (1 connections) — `server/game/profession_service.py`
- **Initialize the profession service with a persistence layer.** (1 connections) — `server/game/profession_service.py`
- **Convert a Profession model to a dictionary for API responses.          Args:** (1 connections) — `server/game/profession_service.py`
- **Get all available professions as dictionaries.          Returns:             lis** (1 connections) — `server/game/profession_service.py`
- **Get a profession by ID as a dictionary.          Args:             profession_id** (1 connections) — `server/game/profession_service.py`
- **Validate that a profession exists and return it.          This method encapsulat** (1 connections) — `server/game/profession_service.py`

## Relationships

- [[NPC Admin API]] (4 shared connections)
- [[Character Creation API]] (1 shared connections)
- [[Dependency Injection Tests]] (1 shared connections)

## Source Files

- `server/game/profession_service.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
