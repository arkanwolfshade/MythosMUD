# Client Memory Leak Detector

> 44 nodes

## Key Concepts

- **PlayerLucidity** (74 connections) — `server/models/lucidity.py`
- **rescue_service.py** (19 connections) — `server/services/rescue_service.py`
- **RescueService** (12 connections) — `server/services/rescue_service.py`
- **.rescue()** (9 connections) — `server/services/rescue_service.py`
- **Any** (7 connections)
- **_load_rescue_participants()** (6 connections) — `server/services/rescue_service.py`
- **.__init__()** (6 connections) — `server/services/rescue_service.py`
- **_ensure_uuid()** (5 connections) — `server/services/rescue_service.py`
- **._apply_rescue_adjustment()** (5 connections) — `server/services/rescue_service.py`
- **_maybe_await()** (4 connections) — `server/services/rescue_service.py`
- **_dispatch_rescue_events()** (4 connections) — `server/services/rescue_service.py`
- **test_respawn_player_from_delirium_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **UUID** (3 connections)
- **_rescue_success_payload()** (3 connections) — `server/services/rescue_service.py`
- **test_player_lucidity_creation()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_player_lucidity_defaults()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_player_lucidity_with_catatonia()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_player_lucidity_repr()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **test_player_lucidity_tiers()** (3 connections) — `server/tests/unit/models/test_lucidity_models.py`
- **mock_lucidity_record()** (3 connections) — `server/tests/unit/services/test_lucidity_service.py`
- **test_respawn_player_from_delirium_clears_combat_state()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_no_combat_service()** (3 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **EventDispatcher** (2 connections)
- **Authoritative lucidity state for a single investigator.** (1 connections) — `server/models/lucidity.py`
- *... and 19 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (19 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (13 shared connections)
- [Game Client Container](Game_Client_Container.md) (11 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (6 shared connections)
- [Message Queue Cleanup](Message_Queue_Cleanup.md) (6 shared connections)
- [Catatonia Check Logic](Catatonia_Check_Logic.md) (4 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (4 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (4 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Health Endpoint Spec](Health_Endpoint_Spec.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (2 shared connections)

## Source Files

- `server/models/lucidity.py`
- `server/services/rescue_service.py`
- `server/tests/unit/models/test_lucidity_models.py`
- `server/tests/unit/services/test_lucidity_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 178 (84%)
- INFERRED: 33 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*