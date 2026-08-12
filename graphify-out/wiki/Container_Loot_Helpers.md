# Container Loot Helpers

> 20 nodes

## Key Concepts

- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_character_with_stats()** (7 connections) — `server/game/character_creation_service.py`
- **.validate_character_stats()** (6 connections) — `server/game/character_creation_service.py`
- **Any** (5 connections)
- **.roll_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **._get_class_description()** (3 connections) — `server/game/character_creation_service.py`
- **character_creation_service()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **test_character_creation_service_init()** (3 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **UUID** (2 connections)
- **Service class for character creation and stats generation business operations.** (1 connections) — `server/game/character_creation_service.py`
- **Initialize the character creation service with a player service.** (1 connections) — `server/game/character_creation_service.py`
- **Roll random stats for character creation.          Args:             method: The** (1 connections) — `server/game/character_creation_service.py`
- **Validate character stats against class prerequisites.          Args:** (1 connections) — `server/game/character_creation_service.py`
- **Create a new character with specific stats.          Args:             name: The** (1 connections) — `server/game/character_creation_service.py`
- **Get information about all available character classes and their prerequisites.** (1 connections) — `server/game/character_creation_service.py`
- **Get a description for a character class.** (1 connections) — `server/game/character_creation_service.py`
- **Create a CharacterCreationService instance.** (1 connections) — `server/tests/unit/game/test_character_creation_service.py`
- **Test CharacterCreationService initialization.** (1 connections) — `server/tests/unit/game/test_character_creation_service.py`

## Relationships

- [React Node Upgrade Summary](React_Node_Upgrade_Summary.md) (6 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [WebSocket Command Handler](WebSocket_Command_Handler.md) (2 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (2 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 59 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*