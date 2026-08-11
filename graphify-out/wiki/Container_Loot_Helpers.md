# Container Loot Helpers

> 16 nodes

## Key Concepts

- **CharacterCreationService** (12 connections) — `server/game/character_creation_service.py`
- **.create_character_with_stats()** (7 connections) — `server/game/character_creation_service.py`
- **.validate_character_stats()** (6 connections) — `server/game/character_creation_service.py`
- **Any** (5 connections)
- **.roll_character_stats()** (5 connections) — `server/game/character_creation_service.py`
- **.__init__()** (4 connections) — `server/game/character_creation_service.py`
- **.get_available_classes_info()** (4 connections) — `server/game/character_creation_service.py`
- **._get_class_description()** (3 connections) — `server/game/character_creation_service.py`
- **UUID** (2 connections)
- **Service class for character creation and stats generation business operations.** (1 connections) — `server/game/character_creation_service.py`
- **Initialize the character creation service with a player service.** (1 connections) — `server/game/character_creation_service.py`
- **Roll random stats for character creation.          Args:             method: The** (1 connections) — `server/game/character_creation_service.py`
- **Validate character stats against class prerequisites.          Args:** (1 connections) — `server/game/character_creation_service.py`
- **Create a new character with specific stats.          Args:             name: The** (1 connections) — `server/game/character_creation_service.py`
- **Get information about all available character classes and their prerequisites.** (1 connections) — `server/game/character_creation_service.py`
- **Get a description for a character class.** (1 connections) — `server/game/character_creation_service.py`

## Relationships

- [NPC Database Sessions](NPC_Database_Sessions.md) (5 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)

## Source Files

- `server/game/character_creation_service.py`

## Audit Trail

- EXTRACTED: 51 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*