# Active Lucidity Service

> 32 nodes · cohesion 0.11

## Key Concepts

- **CatatoniaObserverProtocol** (23 connections) — `server/services/lucidity_service.py`
- **ActiveLucidityService** (22 connections) — `server/services/active_lucidity_service.py`
- **active_lucidity_service.py** (21 connections) — `server/services/active_lucidity_service.py`
- **UnknownLucidityActionError** (12 connections) — `server/services/active_lucidity_service.py`
- **UnknownEncounterCategoryError** (11 connections) — `server/services/active_lucidity_service.py`
- **LucidityActionError** (8 connections) — `server/services/active_lucidity_service.py`
- **UUID** (6 connections) — `server/services/active_lucidity_service.py`
- **.perform_recovery_action()** (6 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_effect()** (6 connections) — `server/services/npc_combat_lucidity.py`
- **Any** (5 connections) — `server/services/active_lucidity_service.py`
- **.apply_encounter_lucidity_loss()** (5 connections) — `server/services/active_lucidity_service.py`
- **.__init__()** (5 connections) — `server/services/active_lucidity_service.py`
- **CatatoniaObserverProtocol** (4 connections) — `server/services/active_lucidity_service.py`
- **datetime** (4 connections) — `server/services/active_lucidity_service.py`
- **Any** (4 connections) — `server/services/npc_combat_lucidity.py`
- **.get_action_cooldown()** (4 connections) — `server/services/active_lucidity_service.py`
- **EncounterProfile** (4 connections) — `server/services/active_lucidity_service.py`
- **RecoveryActionProfile** (4 connections) — `server/services/active_lucidity_service.py`
- **._resolve_lucidity_category()** (4 connections) — `server/services/npc_combat_lucidity.py`
- **AsyncSession** (3 connections) — `server/services/active_lucidity_service.py`
- **Active LCD adjustment helpers for encounters and recovery rituals.** (1 connections) — `server/services/active_lucidity_service.py`
- **Perform a recovery action and enforce cooldowns.** (1 connections) — `server/services/active_lucidity_service.py`
- **Fetch the cooldown record for a recovery action.** (1 connections) — `server/services/active_lucidity_service.py`
- **Base error for lucidity action operations.** (1 connections) — `server/services/active_lucidity_service.py`
- **Raised when an unrecognised recovery action is requested.** (1 connections) — `server/services/active_lucidity_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [[Lucidity State Models]] (20 shared connections)
- [[Lucidity Recovery Commands]] (11 shared connections)
- [[NPC Combat Lifecycle]] (7 shared connections)
- [[Active Lucidity Service]] (7 shared connections)
- [[Inventory Service Helpers]] (5 shared connections)
- [[Catatonia Registry Service]] (3 shared connections)
- [[Alias Expansion Logic]] (3 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Lucidity Database Models]] (2 shared connections)
- [[Database Manager Tests]] (2 shared connections)
- [[Lucidity Event Dispatcher]] (1 shared connections)
- [[Lucidity Rescue Helpers]] (1 shared connections)

## Source Files

- `server/services/active_lucidity_service.py`
- `server/services/lucidity_service.py`
- `server/services/npc_combat_lucidity.py`

## Audit Trail

- EXTRACTED: 123 (71%)
- INFERRED: 50 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
