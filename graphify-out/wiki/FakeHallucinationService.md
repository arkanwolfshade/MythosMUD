# FakeHallucinationService

> 57 nodes

## Key Concepts

- **game_tick_death.py** (29 connections) — `server/app/game_tick_death.py`
- **test_game_tick_death.py** (25 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_loop()** (15 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_death.py`
- **asyncio** (12 connections)
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **_process_session_dp_decay_and_death()** (9 connections) — `server/app/game_tick_death.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **_tick_online_players()** (9 connections) — `server/app/game_tick_protocols.py`
- **_process_dead_players()** (7 connections) — `server/app/game_tick_death.py`
- **_process_passive_lucidity_flux()** (7 connections) — `server/app/game_tick_death.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (7 connections)
- **_handle_player_death_threshold()** (6 connections) — `server/app/game_tick_death.py`
- **_process_mortally_wounded_players()** (6 connections) — `server/app/game_tick_death.py`
- **_process_single_player_mp_regeneration()** (6 connections) — `server/app/game_tick_death.py`
- **_validate_mp_regeneration_services()** (6 connections) — `server/app/game_tick_death.py`
- **FastAPI** (6 connections)
- **_player_in_active_combat()** (5 connections) — `server/app/game_tick_death.py`
- **test_process_mortally_wounded_publishes_dp_decay_to_nats()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_tick_broadcast_payload()** (3 connections) — `server/app/game_tick_processing.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event_skips_when_no_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 32 more nodes in this community*

## Relationships

- [RoomInfoPanel.tsx](RoomInfoPanel.tsx.md) (32 shared connections)
- [Memory Leak Prevention System - Implementation Summary](Memory_Leak_Prevention_System_-_Implementation_Summary.md) (9 shared connections)
- [test_room_occupant_manager.py](test_room_occupant_manager.py.md) (8 shared connections)
- [NATSService](NATSService.md) (4 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (4 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (2 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (1 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 159 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*