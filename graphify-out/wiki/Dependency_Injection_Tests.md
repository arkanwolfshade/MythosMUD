# Dependency Injection Tests

> 60 nodes · cohesion 0.01

## Key Concepts

- **RuntimeError** (208 connections) — `server/realtime/websocket_handler_message_loop.py`
- **dependencies.py** (104 connections) — `server/dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **Request** (29 connections) — `server/dependencies.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **get_player_service_for_testing()** (10 connections) — `server/dependencies.py`
- **Any** (10 connections) — `server/time/time_event_consumer.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_combat_service()** (9 connections) — `server/dependencies.py`
- **get_catatonia_registry()** (8 connections) — `server/dependencies.py`
- **get_chat_service()** (8 connections) — `server/dependencies.py`
- **get_connection_manager()** (8 connections) — `server/dependencies.py`
- **get_exploration_service()** (8 connections) — `server/dependencies.py`
- **get_magic_service()** (8 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (8 connections) — `server/dependencies.py`
- **get_mythos_time_consumer()** (8 connections) — `server/dependencies.py`
- **get_nats_message_handler()** (8 connections) — `server/dependencies.py`
- **get_npc_lifecycle_manager()** (8 connections) — `server/dependencies.py`
- **get_npc_population_controller()** (8 connections) — `server/dependencies.py`
- **get_npc_spawning_service()** (8 connections) — `server/dependencies.py`
- **get_passive_lucidity_flux_service()** (8 connections) — `server/dependencies.py`
- **get_player_combat_service()** (8 connections) — `server/dependencies.py`
- **get_player_death_service()** (8 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (8 connections) — `server/dependencies.py`
- *... and 35 more nodes in this community*

## Relationships

- [NPC Admin API](NPC_Admin_API.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Dependency Risk Analyzer](Dependency_Risk_Analyzer.md) (2 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (2 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (1 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (1 shared connections)
- [World Seed Loader](World_Seed_Loader.md) (1 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/realtime/websocket_handler_message_loop.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 413 (63%)
- INFERRED: 241 (37%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*