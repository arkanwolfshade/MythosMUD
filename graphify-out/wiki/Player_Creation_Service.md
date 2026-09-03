# Player Creation Service

> 15 nodes

## Key Concepts

- **player_creation_service.py** (16 connections) — `server/game/player_creation_service.py`
- **PlayerCreationService** (9 connections) — `server/game/player_creation_service.py`
- **.create_player_with_stats()** (8 connections) — `server/game/player_creation_service.py`
- **.create_player()** (7 connections) — `server/game/player_creation_service.py`
- **._resolve_tutorial_start_room()** (5 connections) — `server/game/player_creation_service.py`
- **UUID** (4 connections)
- **.__init__()** (3 connections) — `server/game/player_creation_service.py`
- **Any** (1 connections)
- **Stats** (1 connections)
- **Player creation service. This module handles player character creation…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character with specific stats. Args: name: The player's…** (1 connections) — `server/game/player_creation_service.py`
- **Service for player creation operations.** (1 connections) — `server/game/player_creation_service.py`
- **Initialize with persistence layer, schema converter, and optional instance…** (1 connections) — `server/game/player_creation_service.py`
- **Resolve starting room and tutorial instance ID. For tutorial players, returns…** (1 connections) — `server/game/player_creation_service.py`
- **Create a new player character. Args: name: The player's name profession_id: The…** (1 connections) — `server/game/player_creation_service.py`

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (5 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (4 shared connections)
- [Test Command Factories Utility](Test_Command_Factories_Utility.md) (3 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (2 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (1 shared connections)
- [Stats Generator](Stats_Generator.md) (1 shared connections)
- [Character Creation API](Character_Creation_API.md) (1 shared connections)

## Source Files

- `server/game/player_creation_service.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*