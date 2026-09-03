# Test Player Death Service

> 117 nodes

## Key Concepts

- **test_player_death_service.py** (53 connections) — `server/tests/unit/services/test_player_death_service.py`
- **asyncio** (26 connections)
- **PlayerDeathService** (25 connections) — `server/services/player_death_service.py`
- **log_exception_once()** (15 connections) — `server/structured_logging/enhanced_logging_config.py`
- **.handle_player_death()** (9 connections) — `server/services/player_death_service.py`
- **._publish_death_event()** (7 connections) — `server/services/player_death_service.py`
- **combat_service_types.py** (7 connections) — `server/services/combat_service_types.py`
- **fixture** (7 connections)
- **.process_mortally_wounded_tick()** (6 connections) — `server/services/player_death_service.py`
- **UUID** (6 connections)
- **._clear_player_combat_state()** (5 connections) — `server/services/player_death_service.py`
- **._ensure_player_posture_lying()** (5 connections) — `server/services/player_death_service.py`
- **.get_dead_players()** (5 connections) — `server/services/player_death_service.py`
- **.get_mortally_wounded_players()** (4 connections) — `server/services/player_death_service.py`
- **mock_player()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **player_death_service_no_dependencies()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **test_process_mortally_wounded_tick_publishes_event()** (4 connections) — `server/tests/unit/services/test_player_death_service.py`
- **AsyncSession** (4 connections)
- **._get_room_name_for_death()** (3 connections) — `server/services/player_death_service.py`
- **.__init__()** (3 connections) — `server/services/player_death_service.py`
- **mock_event_bus()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_player_combat_service()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **mock_session()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- **sample_player_id()** (3 connections) — `server/tests/unit/services/test_player_death_service.py`
- *... and 92 more nodes in this community*

## Relationships

- [Combat Events](Combat_Events.md) (10 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (10 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (4 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (4 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Catatonia Registry](Test_Catatonia_Registry.md) (1 shared connections)
- [Application Container Bundles](Application_Container_Bundles.md) (1 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (1 shared connections)
- [Test Container Bundles](Test_Container_Bundles.md) (1 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (1 shared connections)
- [Test Player Respawn Service](Test_Player_Respawn_Service.md) (1 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (1 shared connections)

## Source Files

- `server/services/combat_service_types.py`
- `server/services/player_death_service.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/services/test_player_death_service.py`

## Audit Trail

- EXTRACTED: 197 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*