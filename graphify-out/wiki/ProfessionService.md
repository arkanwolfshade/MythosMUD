# ProfessionService

> 13 nodes

## Key Concepts

- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **.profession_to_dict()** (5 connections) — `server/game/profession_service.py`
- **.get_all_professions_dict()** (4 connections) — `server/game/profession_service.py`
- **.get_profession_by_id_dict()** (4 connections) — `server/game/profession_service.py`
- **.validate_and_get_profession()** (3 connections) — `server/game/profession_service.py`
- **Any** (3 connections)
- **.__init__()** (2 connections) — `server/game/profession_service.py`
- **Service class for profession-related business operations.** (1 connections) — `server/game/profession_service.py`
- **Initialize the profession service with a persistence layer.** (1 connections) — `server/game/profession_service.py`
- **Convert a Profession model to a dictionary for API responses. Args: profession:…** (1 connections) — `server/game/profession_service.py`
- **Get all available professions as dictionaries. Returns: list[dict[str, Any]]:…** (1 connections) — `server/game/profession_service.py`
- **Get a profession by ID as a dictionary. Args: profession_id: Profession ID…** (1 connections) — `server/game/profession_service.py`
- **Validate that a profession exists and return it. This method encapsulates the…** (1 connections) — `server/game/profession_service.py`

## Relationships

- [api/character_creation.py](api-character_creation.py.md) (4 shared connections)
- [roll_character_stats](roll_character_stats.md) (3 shared connections)
- [factory.py](factory.py.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [test_profession_service.py](test_profession_service.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)

## Source Files

- `server/game/profession_service.py`

## Audit Trail

- EXTRACTED: 31 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*