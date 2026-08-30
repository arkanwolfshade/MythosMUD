# Services Package Design

**Version 1.0.0** · MythosMUD · 2026-08-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`server/services/` is the largest server package — 121 files, ~31,000 lines — and holds nearly
all game-mechanics business logic: combat, NPC behavior, lucidity/sanity, containers, NATS
messaging infrastructure, room/world data, player lifecycle, chat logging, inventory, and a
cluster of cross-cutting infrastructure services. Where `docs/subsystems/` describes *what
happens* when a player does something, this document describes *what lives here and how the
files relate* — the two are complementary, not competing (§8 cross-references the subsystem doc
for each cluster that has one). Reverse-engineered from code; code is the source of truth. Written
to close [`#736`](https://github.com/arkanwolfshade/MythosMUD/issues/736).

## 2. Members

**[SPEC]**

Thirteen clusters account for all 121 files (`__init__.py` + 120 implementation files across the
top level and four subpackages: `combat_messaging/`, `nats_subject_manager/`, `npc_service/`,
`passive_lucidity_flux/`). Verified by enumeration against the actual file tree, not by eye.

| Cluster | Files | Purpose |
| --- | --- | --- |
| Combat core | 13 | `combat_service.py` and its `combat_service_{attack,end,events,npc,start,state,types}.py` split, `combat_types.py`, `combat_configuration_service.py`, `combat_initialization.py`, `combat_turn_processor.py`, `combat_turn_participant_actions.py`. The combat state machine and turn engine. |
| Combat handlers | 9 | `combat_attack_handler.py`, `combat_cleanup_handler.py`, `combat_death_handler.py`, `combat_event_handler.py`, `combat_event_publisher.py`, `combat_flee_handler.py`, `combat_hp_sync.py`, `combat_monitoring_service.py`, `combat_persistence_handler.py`. Event-driven reactions to combat-core state changes. |
| Combat messaging | 6 | Top-level `combat_messaging_integration.py`/`combat_messaging_service.py` plus the `combat_messaging/` subpackage (`base.py`, `combat_broadcasts.py`, `integration.py`, `player_broadcasts.py`) — combat-specific chat/broadcast formatting, kept separate from `server/services/chat_*` (below) because it's combat-triggered, not player-initiated. |
| NPC combat integration | 11 | `npc_combat_{data_provider,grace,handlers,integration_combat_mixin,integration_service,integration_validation_mixin,lifecycle,lucidity,memory,rewards,uuid_mapping}.py`. The largest single-prefix cluster — bridges NPC state into the combat-core state machine. |
| NPC lifecycle | 6 | `npc_instance_service.py`, `npc_service_models.py`, `npc_startup_service.py`, plus the `npc_service/` subpackage (`definition_crud.py`, `queries.py`, `spawn_rule_crud.py`) — NPC definition/spawn-rule persistence and instance creation, distinct from the combat-integration cluster above. |
| Container system | 8 | `container_service.py` and its `_access`/`_helpers`/`_lock`/`_session`/`_transfer_from`/`_transfer_to` split, `container_websocket_events.py`. |
| Lucidity & sanity effects | 19 | `lucidity_{command_disruption,communication_dampening,event_dispatcher,helpers,repository,service,trigger_handlers}.py`, `active_lucidity_service.py`, `catatonia_registry.py`, `hallucination_frequency_service.py`, `fake_hallucination_service.py`, `phantom_hostile_service.py`, `rescue_service.py`, `passive_lucidity_flux_service.py` (thin re-export shim) plus the `passive_lucidity_flux/` subpackage (`config.py`, `hallucinations.py`, `models.py`, `rate_overrides.py`, `service.py`). The second-largest cluster — the full sanity/lucidity mechanic and everything downstream of it (hallucinations, catatonia, rescue). |
| NATS messaging infrastructure | 11 | `nats_{exceptions,metrics,service,service_connect,service_pool}.py` plus the `nats_subject_manager/` subpackage (`exceptions.py`, `manager.py`, `metrics.py`, `pattern_matcher.py`, `patterns.py`, `subscription_patterns.py`, `validation.py`). The connection/subject-routing layer underneath `server/realtime/`'s NATS usage — see [`DISTRIBUTED_EVENTBUS_NATS.md`](../architecture/DISTRIBUTED_EVENTBUS_NATS.md). |
| Room / world / map | 8 | `room_data_{cache,fixer,validator}.py`, `room_sync_service.py`, `coordinate_{generator,validator}.py`, `ascii_map_renderer.py`, `environmental_container_loader.py`. |
| Player lifecycle | 6 | `player_combat_service.py` + `_support`, `player_death_service.py`, `player_position_service.py`, `player_preferences_service.py`, `player_respawn_service.py`. |
| Chat logging | 2 | `chat_channel_logger.py`, `chat_logger.py` — persistence-side logging, not chat delivery (that's `server/services/combat_messaging/` for combat and elsewhere in `server/` for general chat — see [`EVENT_OWNERSHIP_MATRIX.md`](../EVENT_OWNERSHIP_MATRIX.md)). |
| Inventory & equipment | 4 | `inventory_mutation_guard.py`, `inventory_service.py`, `equipment_service.py`, `wearable_container_service.py`. |
| Cross-cutting infrastructure | 12 | `admin_auth_service.py`, `aggro_threat.py`, `corpse_lifecycle_service.py`, `exploration_service.py`, `feature_flag_service.py`, `game_tick_service.py`, `health_service.py`, `holiday_service.py`, `rate_limiter.py`, `schedule_service.py`, `target_resolution_service.py`, `user_manager.py`. No shared theme beyond "doesn't belong to a bigger cluster" — the catch-all is honest about that rather than forcing a false grouping. |

## 3. Boundary contract

**[SPEC]**

**Exports.** `__init__.py` re-exports a large but not exhaustive surface — most clusters' primary
service class is re-exported at package level (`from server.services import CombatService`,
etc.); internal helper/handler classes generally are not and are imported from their own module.

**Dependents:** `server/commands/` and `server/command_handler/` (route command dispatch into
services), `server/api/` (REST/WebSocket handlers call services directly), `server/app/`'s
game-tick files (`process_combat_tick` etc. call into combat-core and NPC-combat-integration),
`server/realtime/` (NATS service cluster).

**Invariants a caller must not violate:**

- **Combat core vs. combat handlers is a state-machine/reaction split, not a naming accident.**
  Combat-core files own the turn state machine; combat-handler files react to state transitions
  (death, flee, cleanup) without themselves owning state. A new combat feature that mutates
  combat state belongs in combat-core; one that only observes and reacts belongs in
  combat-handlers.
- **NPC combat integration is deliberately separate from combat core** — it is the adapter layer
  translating NPC-specific state (memory, lucidity-interaction, reward calculation) into the
  combat-core state machine's vocabulary, not a parallel combat implementation.
- **`passive_lucidity_flux_service.py` is a re-export shim (5 lines), not a real implementation**
  — the actual logic lives in the `passive_lucidity_flux/` subpackage; a caller should be able to
  import from either and get the same objects, but new logic belongs in the subpackage.

## 4. Key design decisions

**[SPEC]**

- **Four clusters graduated into subpackages** (`combat_messaging/`, `nats_subject_manager/`,
  `npc_service/`, `passive_lucidity_flux/`) while the rest stayed flat files at the package
  root with prefix-based naming (`combat_*`, `npc_combat_*`, `container_*`, `lucidity_*`,
  `nats_*`, `player_*`, `room_*`). The prefix convention is what makes this package navigable
  at 121 files without further subdirectory structure — the four graduated clusters are ones
  that outgrew a flat file split (multiple concerns needing their own `exceptions.py`/`models.py`
  alongside the main logic).
- **Combat is split into three clusters (core/handlers/messaging), not one.** At 28 files
  combined, combat is nearly a quarter of the entire package — the three-way split keeps state
  ownership (core), reaction (handlers), and presentation (messaging) from tangling into a single
  undifferentiable mass of `combat_*.py` files.
- **Lucidity absorbed several thematically-adjacent-but-differently-named services**
  (`catatonia_registry.py`, `hallucination_frequency_service.py`, `fake_hallucination_service.py`,
  `phantom_hostile_service.py`, `rescue_service.py`) rather than each living as its own top-level
  concept — these are all downstream consequences of the lucidity mechanic (low lucidity causes
  hallucinations/phantom hostiles/catatonia; rescue reverses catatonia), so clustering them
  together here, despite the naming not sharing a `lucidity_` prefix, better reflects the actual
  dependency structure than the file names alone suggest.

## 5. Constraints

**[SPEC]**

- New combat logic must respect the core/handlers/messaging split (§3) — do not add
  state-mutating logic to a `combat_*_handler.py` file, and do not add presentation/broadcast
  logic to combat-core files.
- New NATS-adjacent logic belongs in the NATS cluster or `server/realtime/`, not scattered —
  check [`DISTRIBUTED_EVENTBUS_NATS.md`](../architecture/DISTRIBUTED_EVENTBUS_NATS.md) for which
  layer owns what before adding a new NATS-touching file here.

## 6. Developer guide

**[NOTE]**

- **Adding a new service**: place it in the matching cluster by naming convention (prefix-match
  the cluster table in §2); if it doesn't fit an existing cluster, it likely belongs in
  cross-cutting infrastructure — but check whether a new named cluster is actually warranted
  first, per this package's own graduation pattern (§4).
- **Finding where a game mechanic lives**: cross-reference [`docs/subsystems/`](../subsystems/)
  first — the subsystem doc for a behavior usually names the specific service file(s), which is
  faster than searching this package's 121 files cold.
- **Tests**: `server/tests/unit/services/` mirrors this package's module layout, including the
  four subpackages.

## 7. Troubleshooting

**[NOTE]**

- **Can't find where a feature's logic lives**: check the cluster table in §2 by keyword/prefix
  first, then the relevant `docs/subsystems/*.md` doc if one exists for that behavior.
- **A change to NPC behavior doesn't affect combat as expected**: confirm you edited the NPC
  combat *integration* cluster (adapter layer) and not accidentally duplicated logic that
  actually needs to change in combat-core.

## 8. Related docs

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the behavioral counterpart to this
  structural document; consult both together — e.g.
  [`SUBSYSTEM_COMBAT_DESIGN.md`](../subsystems/SUBSYSTEM_COMBAT_DESIGN.md),
  [`SUBSYSTEM_LUCIDITY_DESIGN.md`](../subsystems/SUBSYSTEM_LUCIDITY_DESIGN.md),
  [`SUBSYSTEM_NPC_DESIGN.md`](../subsystems/SUBSYSTEM_NPC_DESIGN.md),
  [`SUBSYSTEM_RESCUE_DESIGN.md`](../subsystems/SUBSYSTEM_RESCUE_DESIGN.md).
- [`DISTRIBUTED_EVENTBUS_NATS.md`](../architecture/DISTRIBUTED_EVENTBUS_NATS.md) — the NATS
  architecture this package's NATS cluster implements against.
- [`EVENT_OWNERSHIP_MATRIX.md`](../EVENT_OWNERSHIP_MATRIX.md) — which events which services own.
- [`PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md) — the persisted entities these services
  operate on.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version, closes #736 |
