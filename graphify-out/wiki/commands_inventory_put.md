# commands inventory put

> 22 nodes

## Key Concepts

- **character_creation_service.py** (13 connections) — `server/game/character_creation_service.py`
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
- **Character creation service for MythosMUD server.  This module handles all charac** (1 connections) — `server/game/character_creation_service.py`
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

- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (5 shared connections)
- [event connection helpers](event_connection_helpers.md) (4 shared connections)
- [npc rationale extract](npc_rationale_extract.md) (4 shared connections)
- [player service game](player_service_game.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)

## Source Files

- `server/game/character_creation_service.py`
- `server/tests/unit/game/test_character_creation_service.py`

## Audit Trail

- EXTRACTED: 73 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*