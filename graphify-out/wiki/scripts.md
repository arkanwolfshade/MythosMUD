# scripts

> 25 nodes · cohesion 0.10

## Key Concepts

- **active_lucidity_service.py** (26 connections) — `server/services/active_lucidity_service.py`
- **UnknownEncounterCategoryError** (9 connections) — `server/services/active_lucidity_service.py`
- **.apply_timed_recovery()** (7 connections) — `server/services/active_lucidity_service.py`
- **.perform_recovery_action()** (7 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_loss()** (6 connections) — `server/services/active_lucidity_service.py`
- **LucidityActionError** (6 connections) — `server/services/active_lucidity_service.py`
- **.get_action_cooldown()** (5 connections) — `server/services/active_lucidity_service.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **UUID** (5 connections)
- **Any** (3 connections)
- **EncounterProfile** (2 connections) — `server/services/active_lucidity_service.py`
- **datetime** (2 connections)
- **RuntimeError** (2 connections)
- **RecoveryActionProfile** (2 connections) — `server/services/active_lucidity_service.py`
- **AsyncSession** (1 connections)
- **timedelta** (1 connections)
- **Active LCD adjustment helpers for encounters and recovery rituals.** (1 connections) — `server/services/active_lucidity_service.py`
- **Perform a recovery action and enforce cooldowns.** (1 connections) — `server/services/active_lucidity_service.py`
- **Apply an LCD gain under a named cooldown (shared by recovery actions and…** (1 connections) — `server/services/active_lucidity_service.py`
- **Fetch the cooldown record for a recovery action.** (1 connections) — `server/services/active_lucidity_service.py`
- **Base error for lucidity action operations.** (1 connections) — `server/services/active_lucidity_service.py`
- **Raised when an encounter category is not recognised.** (1 connections) — `server/services/active_lucidity_service.py`
- **Damage profile for a Mythos encounter category.** (1 connections) — `server/services/active_lucidity_service.py`
- **Recovery action configuration.** (1 connections) — `server/services/active_lucidity_service.py`
- **Apply LCD loss for a Mythos encounter.** (1 connections) — `server/services/active_lucidity_service.py`

## Relationships

- [test_look_npc.py](test_look_npc.py.md) (8 shared connections)
- [log_and_raise_enhanced](log_and_raise_enhanced.md) (7 shared connections)
- [PopulationStats](PopulationStats.md) (5 shared connections)
- [TargetMatch](TargetMatch.md) (3 shared connections)
- [gen_arena_migration_sql.py](gen_arena_migration_sql.py.md) (3 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (3 shared connections)
- [test_command_registry_consistency.py](test_command_registry_consistency.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_websocket_handler_commands.py](test_websocket_handler_commands.py.md) (2 shared connections)
- [items/catalog_dml.py](items-catalog_dml.py.md) (2 shared connections)
- [ValidationError](ValidationError.md) (2 shared connections)
- [.get_memory_status_report](get_memory_status_report.md) (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 64 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*