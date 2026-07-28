# Dependency Injection Tests

> 234 nodes · cohesion 0.01

## Key Concepts

- **dependencies.py** (104 connections) — `server/dependencies.py`
- **test_dependencies.py** (60 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **get_container()** (41 connections) — `server/dependencies.py`
- **RuntimeError** (37 connections)
- **Request** (29 connections)
- **MythosTimeEventConsumer** (21 connections) — `server/time/time_event_consumer.py`
- **get_player_service()** (12 connections) — `server/dependencies.py`
- **get_room_service()** (12 connections) — `server/dependencies.py`
- **MythosHourTickEvent** (12 connections) — `server/events/event_types.py`
- **get_chat_service()** (10 connections) — `server/dependencies.py`
- **get_combat_service()** (10 connections) — `server/dependencies.py`
- **get_magic_service()** (10 connections) — `server/dependencies.py`
- **get_player_death_service()** (10 connections) — `server/dependencies.py`
- **get_spell_learning_service()** (10 connections) — `server/dependencies.py`
- **get_async_persistence()** (9 connections) — `server/dependencies.py`
- **get_catatonia_registry()** (9 connections) — `server/dependencies.py`
- **get_connection_manager()** (9 connections) — `server/dependencies.py`
- **get_mp_regeneration_service()** (9 connections) — `server/dependencies.py`
- **get_mythos_time_consumer()** (9 connections) — `server/dependencies.py`
- **get_npc_lifecycle_manager()** (9 connections) — `server/dependencies.py`
- **get_npc_population_controller()** (9 connections) — `server/dependencies.py`
- **get_npc_spawning_service()** (9 connections) — `server/dependencies.py`
- **get_passive_lucidity_flux_service()** (9 connections) — `server/dependencies.py`
- **get_player_combat_service()** (9 connections) — `server/dependencies.py`
- **get_player_respawn_service()** (9 connections) — `server/dependencies.py`
- *... and 209 more nodes in this community*

## Relationships

- [Players API Endpoints](Players_API_Endpoints.md) (35 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (30 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (16 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (11 shared connections)
- [ASCII Map API](ASCII_Map_API.md) (9 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (8 shared connections)
- [Application DI Bundles](Application_DI_Bundles.md) (6 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (6 shared connections)
- [Player Effects API](Player_Effects_API.md) (5 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (5 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (4 shared connections)

## Source Files

- `server/dependencies.py`
- `server/events/event_types.py`
- `server/tests/unit/infrastructure/test_dependencies.py`
- `server/time/time_event_consumer.py`

## Audit Trail

- EXTRACTED: 863 (87%)
- INFERRED: 125 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*