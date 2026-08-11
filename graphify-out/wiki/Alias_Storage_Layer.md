# Alias Storage Layer

> 89 nodes

## Key Concepts

- **NPCCombatLucidity** (34 connections) — `server/services/npc_combat_lucidity.py`
- **debrief_command.py** (25 connections) — `server/commands/debrief_command.py`
- **ActiveLucidityService** (24 connections) — `server/services/active_lucidity_service.py`
- **active_lucidity_service.py** (22 connections) — `server/services/active_lucidity_service.py`
- **TestNPCCombatLucidity** (17 connections) — `server/tests/unit/services/test_npc_combat_lucidity.py`
- **handle_debrief_command()** (16 connections) — `server/commands/debrief_command.py`
- **npc_combat_lucidity.py** (13 connections) — `server/services/npc_combat_lucidity.py`
- **UnknownEncounterCategoryError** (11 connections) — `server/services/active_lucidity_service.py`
- **_EncounterCtx** (9 connections) — `server/services/npc_combat_lucidity.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (8 connections)
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **_generate_narrative_recap()** (6 connections) — `server/commands/debrief_command.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **Any** (6 connections)
- **_check_debrief_availability()** (5 connections) — `server/commands/debrief_command.py`
- **_perform_therapy_if_requested()** (5 connections) — `server/commands/debrief_command.py`
- **_complete_debrief()** (5 connections) — `server/commands/debrief_command.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **_get_persistence_from_app()** (4 connections) — `server/commands/debrief_command.py`
- **_get_catatonia_registry_from_app()** (4 connections) — `server/commands/debrief_command.py`
- **_validate_debrief_context()** (4 connections) — `server/commands/debrief_command.py`
- **UUID** (4 connections)
- *... and 64 more nodes in this community*

## Relationships

- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (14 shared connections)
- [Client Event Store](Client_Event_Store.md) (11 shared connections)
- [WebSocket Message Validator](WebSocket_Message_Validator.md) (8 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (6 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (4 shared connections)
- [Profession Get Mechanical Effects](Profession_Get_Mechanical_Effects.md) (4 shared connections)
- [Container Open Events](Container_Open_Events.md) (4 shared connections)
- [Npc Behavior Engine](Npc_Behavior_Engine.md) (4 shared connections)
- [Calendar NPC Schedule](Calendar_NPC_Schedule.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (3 shared connections)
- [Memory Threshold Monitor](Memory_Threshold_Monitor.md) (3 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (3 shared connections)

## Source Files

- `server/commands/debrief_command.py`
- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 353 (94%)
- INFERRED: 22 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*