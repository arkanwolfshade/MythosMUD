# ActiveLucidityService

> 26 nodes

## Key Concepts

- **ActiveLucidityService** (23 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **_EncounterCtx** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **Any** (6 connections)
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **UUID** (4 connections)
- **Any** (3 connections)
- **NamedTuple** (1 connections)
- **Perform a recovery action and enforce cooldowns.** (1 connections) — `server/services/active_lucidity_service.py`
- **Fetch the cooldown record for a recovery action.** (1 connections) — `server/services/active_lucidity_service.py`
- **Handle active lucidity adjustments such as encounters and recovery actions.** (1 connections) — `server/services/active_lucidity_service.py`
- **Apply LCD loss for a Mythos encounter.** (1 connections) — `server/services/active_lucidity_service.py`
- **Apply lucidity loss when a player engages an eldritch entity. Args: player_id:…** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Determine encounter category based on NPC definition metadata. Args:…** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Context for applying encounter lucidity loss.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Resolve encounter archetype name from NPC definition or id.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply and commit one encounter lucidity loss for the given category.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Retry encounter loss with the disturbing category after unknown-category…** (1 connections) — `server/services/npc_combat_lucidity.py`
- *... and 1 more nodes in this community*

## Relationships

- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (9 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (5 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)
- [debrief_command.py](debrief_command.py.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)
- [LucidityService](LucidityService.md) (1 shared connections)
- [active_lucidity_service](active_lucidity_service.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 62 (91%)
- INFERRED: 6 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*