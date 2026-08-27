# RoomInfoPanel.tsx

> 31 nodes

## Key Concepts

- **game_tick_processing.py** (45 connections) — `server/app/game_tick_processing.py`
- **game_tick_status_effects.py** (26 connections) — `server/app/game_tick_status_effects.py`
- **_TickContainer** (23 connections) — `server/app/game_tick_protocols.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **_process_single_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (10 connections) — `server/app/game_tick_status_effects.py`
- **_process_all_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **_validate_and_get_player()** (9 connections) — `server/app/game_tick_status_effects.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_status_effects.py`
- **_process_player_status_effects()** (8 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (8 connections)
- **Player** (6 connections)
- **_handle_login_warded_expirations()** (4 connections) — `server/app/game_tick_status_effects.py`
- **FastAPI** (2 connections)
- **UUID** (2 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Return the DI container from app.state, or None if missing.** (1 connections) — `server/app/game_tick_protocols.py`
- **Status-effect processing for the game tick loop.** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process a single status effect. Returns: Tuple of (updated_effect_dict or None…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Update and save player status effects if changes occurred. Returns: True if…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_status_effects.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_status_effects.py`
- *... and 6 more nodes in this community*

## Relationships

- [FakeHallucinationService](FakeHallucinationService.md) (32 shared connections)
- [Memory Leak Prevention System - Implementation Summary](Memory_Leak_Prevention_System_-_Implementation_Summary.md) (21 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (16 shared connections)
- [test_room_occupant_manager.py](test_room_occupant_manager.py.md) (11 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (2 shared connections)
- [NPCEnteredRoom](NPCEnteredRoom.md) (2 shared connections)
- [NPCSpawningService](NPCSpawningService.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [NPCCombatIntegration](NPCCombatIntegration.md) (1 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`

## Audit Trail

- EXTRACTED: 142 (86%)
- INFERRED: 23 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*