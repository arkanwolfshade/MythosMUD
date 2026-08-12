# Enhanced Logging Exceptions

> 209 nodes

## Key Concepts

- **LucidityService** (77 connections) — `server/services/lucidity_service.py`
- **lucidity_service.py** (50 connections) — `server/services/lucidity_service.py`
- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **PlayerRespawnService** (40 connections) — `server/services/player_respawn_service.py`
- **combat_flee_handler.py** (23 connections) — `server/services/combat_flee_handler.py`
- **lucidity_helpers.py** (23 connections) — `server/services/lucidity_helpers.py`
- **active_lucidity_service.py** (22 connections) — `server/services/active_lucidity_service.py`
- **test_combat_flee_handler.py** (17 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **UUID** (16 connections)
- **._prepare_sanitarium_respawn()** (16 connections) — `server/services/player_respawn_service.py`
- **execute_voluntary_flee()** (15 connections) — `server/services/combat_flee_handler.py`
- **UUID** (14 connections)
- **._apply_sanitarium_liability_update()** (12 connections) — `server/services/player_respawn_service.py`
- **try_voluntary_flee_roll()** (11 connections) — `server/services/combat_flee_handler.py`
- **decode_liabilities()** (11 connections) — `server/services/lucidity_helpers.py`
- **.respawn_player()** (11 connections) — `server/services/player_respawn_service.py`
- **_make_participant()** (11 connections) — `server/tests/unit/services/test_combat_flee_handler.py`
- **test_lucidity_service.py** (11 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **._send_lucidity_change_event_if_needed()** (10 connections) — `server/services/lucidity_service.py`
- **._finalize_lucidity_adjustment()** (10 connections) — `server/services/lucidity_service.py`
- **.respawn_player_from_delirium()** (10 connections) — `server/services/player_respawn_service.py`
- **.respawn_player_from_sanitarium()** (10 connections) — `server/services/player_respawn_service.py`
- **hallucination_frequency_service.py** (9 connections) — `server/services/hallucination_frequency_service.py`
- **LucidityUpdateResult** (9 connections) — `server/services/lucidity_helpers.py`
- **.apply_lucidity_adjustment()** (9 connections) — `server/services/lucidity_service.py`
- *... and 184 more nodes in this community*

## Relationships

- [Rest Command Flow](Rest_Command_Flow.md) (28 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (23 shared connections)
- [Client Event Store](Client_Event_Store.md) (21 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (19 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (19 shared connections)
- [Redis to NATS Migration](Redis_to_NATS_Migration.md) (16 shared connections)
- [Character Creation API](Character_Creation_API.md) (8 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (8 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (8 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (7 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (7 shared connections)
- [Services Combat Persistence](Services_Combat_Persistence.md) (6 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/services/active_lucidity_service.py`
- `server/services/combat_flee_handler.py`
- `server/services/hallucination_frequency_service.py`
- `server/services/lucidity_command_disruption.py`
- `server/services/lucidity_helpers.py`
- `server/services/lucidity_service.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_combat_flee_handler.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/test_lucidity_service_smoke.py`
- `server/utils/liability_types.py`

## Audit Trail

- EXTRACTED: 935 (93%)
- INFERRED: 73 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*