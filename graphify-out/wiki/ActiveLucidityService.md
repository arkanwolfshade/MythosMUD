# ActiveLucidityService

> 21 nodes

## Key Concepts

- **ActiveLucidityService** (24 connections) — `server/services/active_lucidity_service.py`
- **_EncounterCtx** (9 connections) — `server/services/npc_combat_lucidity.py`
- **.apply_encounter_lucidity_effect()** (9 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_loss_with_fallback()** (8 connections) — `server/services/npc_combat_lucidity.py`
- **._apply_disturbing_fallback()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **._commit_loss()** (7 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (6 connections)
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **._archetype_from_definition()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **datetime** (2 connections)
- **AsyncSession** (1 connections)
- **NamedTuple** (1 connections)
- **Handle active lucidity adjustments such as encounters and recovery actions.** (1 connections) — `server/services/active_lucidity_service.py`
- **Apply lucidity loss when a player engages an eldritch entity. Args: player_id:…** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Determine encounter category based on NPC definition metadata. Args:…** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Context for applying encounter lucidity loss.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Resolve encounter archetype name from NPC definition or id.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply and commit one encounter lucidity loss for the given category.** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Retry encounter loss with the disturbing category after unknown-category…** (1 connections) — `server/services/npc_combat_lucidity.py`
- **Apply encounter lucidity loss, falling back to disturbing on unknown category.** (1 connections) — `server/services/npc_combat_lucidity.py`

## Relationships

- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (9 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (8 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (5 shared connections)
- [LucidityService](LucidityService.md) (3 shared connections)
- [debrief_command.py](debrief_command.py.md) (2 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (1 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 58 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*