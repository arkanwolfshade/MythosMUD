# Async Persistence Migration

> 24 nodes

## Key Concepts

- **NPCCombatLucidity** (34 connections) — `server/services/npc_combat_lucidity.py`
- **ActiveLucidityService** (24 connections) — `server/services/active_lucidity_service.py`
- **_EncounterCtx** (9 connections) — `server/services/npc_combat_lucidity.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (6 connections)
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **.get_lucidity_service()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **test_perform_recovery_action_naive_datetime_cooldown()** (3 connections) — `server/tests/unit/services/test_active_lucidity_service.py`
- **Handle active lucidity adjustments such as encounters and recovery actions.** (1 connections) — `server/services/active_lucidity_service.py`
- **Return lucidity dependency for integration collaborators.** (1 connections) — `server/services/npc_combat_integration_service.py`
- **NamedTuple** (1 connections)
- **Context for applying encounter lucidity loss.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Manages lucidity effects for NPC encounters.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Resolve encounter archetype name from NPC definition or id.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply and commit one encounter lucidity loss for the given category.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Retry encounter loss with the disturbing category after unknown-category failure** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply encounter lucidity loss, falling back to disturbing on unknown category.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply lucidity loss when a player engages an eldritch entity.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Determine encounter category based on NPC definition metadata.          Args:** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Test perform_recovery_action() handles naive datetime in cooldown.** (1 connections) — `server/tests/unit/services/test_active_lucidity_service.py`

## Relationships

- [Alias Storage Layer](Alias_Storage_Layer.md) (16 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (11 shared connections)
- [Archive Optimization Summary](Archive_Optimization_Summary.md) (4 shared connections)
- [WebSocket Message Validator](WebSocket_Message_Validator.md) (4 shared connections)
- [Character Creation API](Character_Creation_API.md) (3 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Mythos Calendar Time Service](Mythos_Calendar_Time_Service.md) (2 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (1 shared connections)
- [Realtime Visual Indicator](Realtime_Visual_Indicator.md) (1 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_integration_service.py`
- `server/services/npc_combat_lucidity.py`
- `server/tests/unit/services/test_active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 119 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*