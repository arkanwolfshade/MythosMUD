# .perform_recovery_action

> 8 nodes

## Key Concepts

- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **UUID** (4 connections)
- **Any** (3 connections)
- **Perform a recovery action and enforce cooldowns.** (1 connections) — `server/services/active_lucidity_service.py`
- **Fetch the cooldown record for a recovery action.** (1 connections) — `server/services/active_lucidity_service.py`
- **Apply LCD loss for a Mythos encounter.** (1 connections) — `server/services/active_lucidity_service.py`

## Relationships

- [NPCCombatLucidity](NPCCombatLucidity.md) (5 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (2 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*