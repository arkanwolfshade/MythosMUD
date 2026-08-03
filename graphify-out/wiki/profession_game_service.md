# profession game service

> 13 nodes

## Key Concepts

- **ProfessionService** (17 connections) — `server/game/profession_service.py`
- **.profession_to_dict()** (5 connections) — `server/game/profession_service.py`
- **.get_all_professions_dict()** (4 connections) — `server/game/profession_service.py`
- **.get_profession_by_id_dict()** (4 connections) — `server/game/profession_service.py`
- **Any** (3 connections)
- **.validate_and_get_profession()** (3 connections) — `server/game/profession_service.py`
- **.__init__()** (2 connections) — `server/game/profession_service.py`
- **Service class for profession-related business operations.** (1 connections) — `server/game/profession_service.py`
- **Initialize the profession service with a persistence layer.** (1 connections) — `server/game/profession_service.py`
- **Convert a Profession model to a dictionary for API responses.          Args:** (1 connections) — `server/game/profession_service.py`
- **Get all available professions as dictionaries.          Returns:             lis** (1 connections) — `server/game/profession_service.py`
- **Get a profession by ID as a dictionary.          Args:             profession_id** (1 connections) — `server/game/profession_service.py`
- **Validate that a profession exists and return it.          This method encapsulat** (1 connections) — `server/game/profession_service.py`

## Relationships

- [character creation validate](character_creation_validate.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (3 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/game/profession_service.py`

## Audit Trail

- EXTRACTED: 44 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*