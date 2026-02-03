# Domain Model Anemic Anti-Pattern Audit

**Date:** 2026-02-02
**Scope:** Full audit of `server/services/` for domain logic that could be moved to domain
models
**Related:** Architecture Review Plan – review-domain-models (Phase 2)

## Executive Summary

This audit identifies services containing business logic that belongs in domain models
(Player, CombatParticipant, ContainerComponent, etc.) per Domain-Driven Design and the
anemic domain model anti-pattern remediation. Services should orchestrate and
coordinate; domain models should encapsulate invariants and behavior.

**Findings:** 15 services contain domain logic that could be enriched into models.
Priority is divided into High (clear-cut moves), Medium (partially in models), and Low
(acceptable service coordination).

---

## 1. Already Addressed (Prior Work)

| Service               | Model             | Change                                                                                     |
| --------------------- | ----------------- | ------------------------------------------------------------------------------------------ |
| PlayerDeathService    | Player            | Uses `is_mortally_wounded()`, `is_dead()`; delegates DP decay to `Player.apply_dp_decay()` |
| CombatAttackHandler   | CombatParticipant | Delegates damage to `target.apply_damage()`; grace period in service                       |
| NPCCombatDataProvider | Player, NPCBase   | Uses `Player.get_combat_stats()` and `NPCBase.get_combat_stats()` for combat participant   |

---

## 2. High Priority – Domain Logic in Services

### 2.1 Player Death Service – DP Decay

**File:** `server/services/player_death_service.py` (lines 143–173)

**Current:** Service applies DP decay and posture updates directly:

```python
stats = player.get_stats()
current_dp = stats.get("current_dp", 0)
new_dp = max(current_dp - 1, -10)
stats["current_dp"] = new_dp
if new_dp <= 0 < old_dp:
    stats["position"] = PositionState.LYING
# ...
player.set_stats(stats)
```

**Recommendation:** Add to `Player`:

- `apply_dp_decay(amount: int = 1) -> tuple[int, int, bool]`
  Returns `(old_dp, new_dp, posture_changed)`, applies cap at -10, updates posture when
  crossing 0.

**Benefit:** Single place for DP decay rules; service orchestrates persistence/events.

---

### 2.2 Combat Turn Processor – “Can Act” Checks

**File:** `server/services/combat_turn_processor.py` (lines 307–319, 373–385)

**Current:** Service checks raw DP:

```python
# NPC
if npc.current_dp <= 0:
    # Skip turn - dead

# Player
if player.current_dp <= 0:
    # Skip turn - unconscious
```

**Recommendation:** Add to `CombatParticipant`:

- `can_act_in_combat() -> bool`
  - Player: `current_dp > 0`
  - NPC: `current_dp > 0` (equivalent to `is_alive()` for NPCs)

**Benefit:** Aligns with `is_alive()`, `is_dead()`; clarifies “can perform voluntary action.”

---

### 2.3 Combat HP Sync – Death Threshold Logic

**File:** `server/services/combat_hp_sync.py` (lines 172–182, 212–239, 261–273)

**Current:** Service contains:

- `current_dp <= 0 < old_dp` (mortally wounded)
- `current_dp <= -10 and old_dp > -10` (death)
- `stats["position"] = PositionState.LYING` when DP <= 0

**Recommendation:**

- Use `Player.is_dead()`, `Player.is_mortally_wounded()` for checks.
- Add `Player.apply_dp_change(new_dp: int) -> tuple[bool, bool]` (or similar) that
  updates DP and posture, returns (became_mortally_wounded, became_dead). Sync logic
  stays in service but delegates state changes to Player.

**Benefit:** Death/posture rules centralized in Player; persistence/sync stays in service.

---

### 2.4 Combat Persistence Handler – Same Patterns

**File:** `server/services/combat_persistence_handler.py` (lines 57–106, 134–173, 200–217)

**Current:** Same death-threshold and posture logic as Combat HP Sync.

**Recommendation:** Same as 2.3 – use Player methods for DP and posture transitions.

---

### 2.5 Player Respawn Service – Stats Restoration

**File:** `server/services/player_respawn_service.py` (lines 178–192, 289–294)

**Current:** Service restores DP and posture:

```python
stats = player.get_stats()
stats["current_dp"] = max_dp
stats["position"] = PositionState.STANDING
player.set_stats(stats)
```

**Recommendation:** Add to `Player`:

- `restore_to_full_health() -> int`
  Sets DP to max, posture to STANDING, returns old DP.

**Benefit:** Respawn semantics live in the model; service handles room, combat, events.

---

## 3. Medium Priority – Partial Enrichment

### 3.1 Wearable Container Service – Capacity Checks

**File:** `server/services/wearable_container_service.py` (lines 125–138, 330–345, 424–436)

**Current:** Inline capacity logic:

```python
if len(current_items) + len(items) > container.capacity_slots:
if len(items) > container.capacity_slots:
```

**Recommendation:** Add to `ContainerComponent`:

- `has_room_for(item_count: int) -> bool` → `len(self.items) + item_count <=
  self.capacity_slots`
- `would_exceed_capacity(items: list) -> bool` for bulk checks

**Benefit:** `ContainerComponent` already has `has_capacity()`; this extends it for "room for N more items."

**Implemented:** All three methods added. WearableContainerService uses `would_exceed_capacity(items)` in add_items.

---

### 3.2 Inventory Service – Slot Capacity

**File:** `server/services/inventory_service.py` (lines 79–135)

**Current:** Generic inventory (lists of stacks) with `max_slots`; not tied to a single model.

**Recommendation:** Keep as service. It operates on generic sequences. If a
`PlayerInventory` or `ContainerInventory` value object emerges, capacity rules could
move there.

---

### 3.3 NPC Combat Data Provider – Stats Extraction

**File:** `server/services/npc_combat_data_provider.py` (lines 157–209)

**Current:** Pulls `current_dp`, `max_dp` from `player.get_stats()` and `npc_instance.get_stats()`.

**Recommendation:** Prefer model methods (e.g. `Player.get_combat_stats()`, or
equivalent on NPC) that return `{current_dp, max_dp, ...}` for combat. Reduces
duplication and keeps stat semantics in the model.

---

### 3.4 Combat Event Handler / Publisher – DP in Events

**Files:** `combat_event_handler.py`, `combat_event_publisher.py`

**Current:** Read `target.current_dp` (CombatParticipant) for events; no logic.

**Recommendation:** No change. Reading DP for events is fine. Ensure consistency with
`CombatParticipant` health methods where applicable.

---

## 4. Low Priority – Acceptable Service Logic

### 4.1 Container Service

**File:** `server/services/container_service.py` (lines 432–446)

**Current:** Uses `container.has_capacity()` and `container.get_used_slots()`.

**Recommendation:** No change. Container model already has the right methods.

---

### 4.2 Combat Initialization

**File:** `server/services/combat_initialization.py`

**Current:** Reads `attacker.current_dp`, `target.current_dp` for snapshot creation.

**Recommendation:** No change. Snapshot creation is orchestration.

---

### 4.3 Combat Service, Combat Messaging Integration

**Files:** `combat_service.py`, `combat_messaging_integration.py`

**Current:** Pass through DP values, format messages.

**Recommendation:** No change. Orchestration and presentation only.

---

### 4.4 NPC Instance Service, NPC Combat Integration Service (Done)

**Current:** Use `getattr(npc_instance, "is_alive", True)` and similar.

**Recommendation:** Prefer explicit `is_alive()` (or equivalent) on NPC model if it
exists; otherwise keep defensive checks.

**Implemented:** NPCBase now has `is_alive` property (getter/setter) for explicit
interface. Services updated to use `npc_instance.is_alive` where appropriate.

---

## 5. Models Already Rich (No Action)

| Model              | Domain Behavior                                                    |
| ------------------ | ------------------------------------------------------------------ |
| Room               | `player_entered()`, `object_added()`, etc.                         |
| ContainerComponent | `has_capacity()`, `is_locked()`, `get_used_slots()`, `is_decayed()` |
| CombatParticipant  | `is_alive()`, `is_dead()`, `is_mortally_wounded()`, `apply_damage()` |
| Player             | `is_alive()`, `is_dead()`, `is_mortally_wounded()`, `get_health_*()` |

---

## 6. Recommended Implementation Order

1. **Player.apply_dp_decay()** – unblocks PlayerDeathService and centralizes decay.
2. **CombatParticipant.can_act_in_combat()** – unblocks CombatTurnProcessor.
3. **Player.restore_to_full_health()** – unblocks PlayerRespawnService.
4. **Player DP/posture helper** – shared by CombatHpSync and CombatPersistenceHandler.
5. **ContainerComponent.has_room_for()** – unblocks WearableContainerService.

---

## 7. Services Reviewed (No Domain Logic to Move)

- `admin_auth_service.py` – auth/authorization
- `ascii_map_renderer.py` – rendering
- `chat_logger.py` – logging (thread `is_alive` is threading, not game)
- `combat_cleanup_handler.py` – coordination
- `combat_configuration_service.py` – config
- `combat_death_handler.py` – event handling
- `combat_flee_handler.py` – coordination
- `combat_messaging_service.py` – messaging
- `combat_monitoring_service.py` – monitoring
- `combat_types.py` – data types
- `coordinate_generator.py`, `coordinate_validator.py` – utilities
- `corpse_lifecycle_service.py` – lifecycle coordination
- `environmental_container_loader.py` – loading
- `equipment_service.py` – uses inventory; capacity checks delegated
- `exploration_service.py` – exploration
- `feature_flag_service.py` – feature flags
- `game_tick_service.py` – tick coordination
- `health_service.py` – DB connection health, not game health
- `holiday_service.py` – calendar
- `inventory_mutation_guard.py` – concurrency
- `lucidity_*` services – lucidity domain (separate audit)
- `nats_*` – messaging
- `npc_*` (handlers, memory, rewards, etc.) – mostly coordination
- `phantom_hostile_service.py` – test/phantom data
- `player_combat_service.py` – combat coordination
- `player_position_service.py` – position updates
- `player_preferences_service.py` – preferences
- `rate_limiter.py` – rate limiting
- `rescue_service.py` – rescue flow
- `room_data_*` – room data
- `schedule_service.py` – scheduling
- `target_resolution_service.py` – target resolution
- `user_manager.py` – user management
- `room_data_cache.py` – caching

---

## 8. Summary Table

| Priority | Service                    | Model              | Action                                   |
| -------- | -------------------------- | ------------------ | ---------------------------------------- |
| High     | player_death_service       | Player             | Add `apply_dp_decay()`                   |
| High     | combat_turn_processor      | CombatParticipant  | Add `can_act_in_combat()`                |
| High     | combat_hp_sync             | Player             | Use model methods, add DP/posture helper |
| High     | combat_persistence_handler | Player             | Same as combat_hp_sync                   |
| High     | player_respawn_service     | Player             | Add `restore_to_full_health()`           |
| Medium   | wearable_container_service | ContainerComponent | Add `has_room_for()`                     |
| Medium   | npc_combat_data_provider   | Player, NPCBase    | Add `get_combat_stats()` (done)          |
| Low      | container_service          | —                  | Already uses model                       |
| Low      | combat\_\* (others)        | —                  | Orchestration only                       |
