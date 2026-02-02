# ApplicationContainer Structure Analysis and Domain-Specific Split Proposal

**Document Version:** 1.1
**Date:** January 2026
**Status:** Implemented (Phase 1 and Phase 2 complete)
**Purpose:** Analyze `server/container.py` (ApplicationContainer) and propose a domain-specific container split per the Architecture Review Plan.

## 1. Executive Summary

`ApplicationContainer` in `server/container.py` is a ~1,251-line dependency injection container that manages 50+ service attributes and 15 initialization phases. The architecture review plan recommends splitting it into domain-specific containers to improve maintainability, testability, and clarity. This document analyzes the current structure and proposes a split that preserves the existing public API and singleton behavior while organizing initialization and ownership by domain.

## 2. Current Structure Analysis

### 2.1 Attribute Inventory by Domain

Attributes in `ApplicationContainer.__init__` (lines 104-205) and their logical domains:

| Domain               | Attributes                                                                                                                                         | Count |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **Configuration**    | `config`                                                                                                                                           | 1     |
| **Infrastructure**   | `database_manager`, `task_registry`, `tracked_task_manager`                                                                                        | 3     |
| **Event system**     | `event_bus`                                                                                                                                        | 1     |
| **Persistence**      | `persistence`, `async_persistence`                                                                                                                 | 2     |
| **Real-time**        | `connection_manager`, `real_time_event_handler`, `nats_service`, `nats_message_handler`, `event_publisher`                                         | 5     |
| **Game**             | `player_service`, `room_service`, `movement_service`, `exploration_service`, `user_manager`, `container_service`                                   | 6     |
| **Caching**          | `room_cache_service`, `profession_cache_service`                                                                                                   | 2     |
| **Monitoring**       | `performance_monitor`, `exception_tracker`, `monitoring_dashboard`, `log_aggregator`                                                               | 4     |
| **Temporal**         | `holiday_service`, `schedule_service`, `mythos_tick_scheduler`                                                                                     | 3     |
| **Item system**      | `item_prototype_registry`, `item_factory`                                                                                                          | 2     |
| **Combat**           | `player_combat_service`, `player_death_service`, `player_respawn_service`, `combat_service`, `catatonia_registry`, `passive_lucidity_flux_service` | 6     |
| **Magic**            | `magic_service`, `spell_registry`, `spell_targeting_service`, `spell_effects`, `spell_learning_service`, `mp_regeneration_service`                 | 6     |
| **NPC**              | `npc_lifecycle_manager`, `npc_spawning_service`, `npc_population_controller`                                                                       | 3     |
| **Chat**             | `chat_service`                                                                                                                                     | 1     |
| **Time consumer**    | `mythos_time_consumer`                                                                                                                             | 1     |
| **State / internal** | `server_shutdown_pending`, `shutdown_data`, `tick_task`, `_initialized`, `_initialization_lock`, `_project_root`                                   | 6     |

**Total:** ~49 service/configuration attributes plus 6 state/internal attributes.

### 2.2 Initialization Order and Dependencies

Current `initialize()` phases (lines 258-568):

| Phase    | Description                                                                                | Depends on                                                                        |
| -------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| 1        | Configuration                                                                              | —                                                                                 |
| 2        | Database infrastructure                                                                    | config                                                                            |
| 3        | Task management                                                                            | config                                                                            |
| 4        | Event system                                                                               | task_registry                                                                     |
| 5        | Persistence (async)                                                                        | database, event_bus                                                               |
| 5.1      | Room cache warmup                                                                          | async_persistence                                                                 |
| 5.2      | Gameplay (movement, exploration)                                                           | event_bus, async_persistence                                                      |
| 5.5      | Temporal (holiday, schedule, mythos tick)                                                  | async_persistence, config                                                         |
| 6        | Real-time (NATS, connection_manager, event_handler, event_publisher, nats_message_handler) | config, event_bus, task_registry, async_persistence                               |
| 7        | Game (player, room, user_manager, container_service)                                       | persistence                                                                       |
| 7 (item) | Item services                                                                              | database_manager                                                                  |
| 8        | Caching                                                                                    | persistence                                                                       |
| 9        | Monitoring                                                                                 | —                                                                                 |
| 10       | Combat                                                                                     | persistence, event_bus, connection_manager, movement_service                      |
| 11       | NPC                                                                                        | event_bus, persistence, async_persistence                                         |
| 12       | NATS + combat (CombatService, NATS message handler start)                                  | nats_service, combat-related, player_service                                      |
| 13       | Magic                                                                                      | async_persistence, player_service, combat_service, player_combat_service          |
| 14       | Chat                                                                                       | config, persistence, player_service, user_manager, nats_service                   |
| 15       | Mythos time consumer                                                                       | event_bus, holiday_service, schedule_service, room_service, npc_lifecycle_manager |

**Key cross-domain dependencies:**

- **Realtime** depends on: config, event_bus, task_registry, async_persistence.
- **Game** depends on: persistence, nats_message_handler (for user_manager).
- **Combat** depends on: persistence, event_bus, connection_manager, movement_service.
- **Magic** depends on: async_persistence, player_service, combat_service, player_combat_service.
- **Chat** depends on: persistence, player_service, user_manager, nats_service.
- **Mythos time** depends on: event_bus, holiday_service, schedule_service, room_service, npc_lifecycle_manager.

### 2.3 Private Initializers and Helpers

| Method                               | Purpose                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `_initialize_item_services()`        | Load item prototypes from PostgreSQL, create PrototypeRegistry and ItemFactory                                |
| `_initialize_combat_services()`      | PlayerCombatService, PlayerDeathService, PlayerRespawnService, CatatoniaRegistry, PassiveLucidityFluxService  |
| `_initialize_npc_services()`         | NPCSpawningService, NPCLifecycleManager, NPCPopulationController, NPC definitions/rules                       |
| `_initialize_nats_combat_service()`  | CombatService, NATS message handler start, wire player_service                                                |
| `_initialize_magic_services()`       | SpellRegistry, SpellTargetingService, SpellEffects, SpellLearningService, MPRegenerationService, MagicService |
| `_initialize_chat_service()`         | ChatService                                                                                                   |
| `_initialize_mythos_time_consumer()` | MythosTimeEventConsumer                                                                                       |
| `_sanitarium_failover_callback()`    | Catatonia failover (uses database_manager, player_respawn_service)                                            |
| `_decode_json_column()`              | JSON column decoding (item prototypes)                                                                        |
| `_normalize_path_from_url_or_path()` | Deprecated item DB path normalization                                                                         |
| `_get_project_root()`                | Project root path                                                                                             |
| `_shutdown_*`                        | Log aggregator, NATS, event bus, database                                                                     |

### 2.4 Public API and Consumers

- **Singleton:** `ApplicationContainer.get_instance()`, `set_instance()`, `reset_instance()`.
- **Factory:** `get_container()`, `reset_container()` (backward compatibility).
- **Access:** Direct attributes (e.g. `container.player_service`), `get_service(name)`.
- **Lifecycle:** `initialize()`, `shutdown()`, `is_initialized`.

Consumers use `app.state.container` or `ApplicationContainer.get_instance()` and then attribute access. No consumer should need to know about sub-containers if we preserve the same attributes on the root container.

## 3. Proposed Domain-Specific Split

### 3.1 Option A: Internal Bundles (Recommended)

Keep a single **ApplicationContainer** as the public facade and singleton. Split implementation into internal **domain bundles** (plain classes or modules) that own initialization and hold references. The container delegates initialization to bundles and then **flattens** their attributes onto itself so existing code (`container.player_service`, etc.) continues to work.

**Bundle layout:**

| Bundle               | Module path                              | Owns                                                                                                                                                                                                                                                |
| -------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CoreBundle**       | `server/container/bundles/core.py`       | config, database_manager, task_registry, tracked_task_manager, event_bus, persistence, async_persistence                                                                                                                                            |
| **RealtimeBundle**   | `server/container/bundles/realtime.py`   | connection_manager, real_time_event_handler, nats_service, nats_message_handler, event_publisher                                                                                                                                                    |
| **GameBundle**       | `server/container/bundles/game.py`       | movement_service, exploration_service, player_service, room_service, user_manager, container_service, room_cache_service, profession_cache_service, holiday_service, schedule_service, mythos_tick_scheduler, item_prototype_registry, item_factory |
| **MonitoringBundle** | `server/container/bundles/monitoring.py` | performance_monitor, exception_tracker, monitoring_dashboard, log_aggregator                                                                                                                                                                        |
| **CombatBundle**     | `server/container/bundles/combat.py`     | player_combat_service, player_death_service, player_respawn_service, combat_service, catatonia_registry, passive_lucidity_flux_service                                                                                                              |
| **NPCBundle**        | `server/container/bundles/npc.py`        | npc_lifecycle_manager, npc_spawning_service, npc_population_controller                                                                                                                                                                              |
| **MagicBundle**      | `server/container/bundles/magic.py`      | spell_registry, spell_targeting_service, spell_effects, spell_learning_service, mp_regeneration_service, magic_service                                                                                                                              |
| **ChatBundle**       | `server/container/bundles/chat.py`       | chat_service                                                                                                                                                                                                                                        |
| **TimeBundle**       | `server/container/bundles/time.py`       | mythos_time_consumer                                                                                                                                                                                                                                |

**ApplicationContainer** (slimmed `server/container.py`):

- Holds state flags: `server_shutdown_pending`, `shutdown_data`, `tick_task`, `_initialized`, `_initialization_lock`, `_project_root`.
- Creates bundles, calls `await bundle.initialize(container)` (or similar) in dependency order, then copies bundle attributes onto `self` so `container.player_service` etc. remain valid.
- `shutdown()` calls bundle shutdowns in reverse order (or each bundle registers shutdown steps).
- Singleton and `get_container()`/`reset_container()` unchanged.

**Benefits:**

- No change to public API or consumer code.
- Clear domain boundaries and smaller files (~150-250 lines per bundle).
- Easier to test bundles in isolation (pass mocks for dependencies).
- Same initialization order and dependency graph, just organized by domain.

### 3.2 Option B: Composed Sub-Containers (Alternative)

Introduce first-class **sub-containers** (e.g. `RealtimeContainer`, `GameContainer`) that are exposed as attributes: `container.realtime`, `container.game`. Consumers would use `container.game.player_service` instead of `container.player_service`.

**Pros:** Stronger encapsulation, explicit domain boundaries.
**Cons:** Breaking change for all consumers; requires updates to lifespan, dependencies, tests, and any code that uses `get_container()` or `app.state.container`.

**Recommendation:** Option A (internal bundles with flattened attributes) unless the team explicitly wants a breaking API change and is prepared to update all call sites.

### 3.3 Dependency Flow Between Bundles

```
CoreBundle (config, db, tasks, event_bus, persistence)
    │
    ├── RealtimeBundle (nats, connection_manager, event_handler, event_publisher, nats_message_handler)
    │       └── depends on: Core
    │
    ├── GameBundle (movement, exploration, player, room, user_manager, container_service, caches, temporal, items)
    │       └── depends on: Core, Realtime (for user_manager / nats_message_handler)
    │
    ├── MonitoringBundle
    │       └── depends on: (none for init)
    │
    ├── CombatBundle
    │       └── depends on: Core, Realtime (connection_manager), Game (movement_service)
    │
    ├── NPCBundle
    │       └── depends on: Core
    │
    ├── MagicBundle
    │       └── depends on: Core (async_persistence), Game (player_service), CombatBundle (combat_service, player_combat_service)
    │
    ├── ChatBundle
    │       └── depends on: Core, Game (player_service, user_manager), Realtime (nats_service)
    │
    └── TimeBundle (mythos_time_consumer)
            └── depends on: Core (event_bus), Game (holiday_service, schedule_service, room_service), NPCBundle (npc_lifecycle_manager)
```

Initialization order: Core → Realtime → Game → Monitoring → Combat → NPC → (NATS/combat wiring) → Magic → Chat → Time. Shutdown: reverse order.

## 4. Migration Path

### Phase 1: Extract bundles without changing behavior [COMPLETE]

1. Add `server/container/bundles/` package. **Done**
2. Implement each bundle with `async def initialize(self, container)` and optional `async def shutdown(self)`. **Done** - 9 bundles.
3. In `ApplicationContainer.initialize()`: Instantiate bundles, call init, copy attributes via `_flatten_bundle()`. **Done**
4. In `ApplicationContainer.shutdown()`, call bundle’s shutdowns in reverse order. **Done**
5. All tests pass. **Done**

### Phase 2: Reduce ApplicationContainer to orchestrator [COMPLETE]

1. Helper methods moved to `server/container/utils.py` (`decode_json_column`, `normalize_path_from_url_or_path`). ApplicationContainer delegates. **Done**
2. Keep `get_instance()`, `set_instance()`, `reset_instance()`, `get_service()`, `is_initialized`, and state flags in ApplicationContainer. **Done**
3. ApplicationContainer ~219 lines (target 200-300). **Done**

### Phase 3: (Optional) Extract service factories

- For the largest initializers (e.g. magic, combat), consider dedicated factory functions or small factory classes to reduce bundle size and improve testability.

## 5. Backward Compatibility

- **Public API:** No change. `container.player_service`, `get_container()`, `ApplicationContainer.get_instance()` remain as today.
- **Tests:** No change to tests that rely on `container.player_service` or `get_container()`; only internal structure of `server/container.py` and new bundle modules change.
- **Lifespan:** `app/lifespan.py` and `app/lifespan_startup.py` continue to use the same ApplicationContainer; no changes required if Phase 1 is done correctly.

## 6. Success Criteria

- ApplicationContainer file size reduced from ~1,251 lines to ~200-350 lines (orchestration only).
- Each domain bundle in a single file of ~100-250 lines with a clear, documented responsibility.
- Initialization order and dependency graph documented and enforced by bundle init order.
- All existing tests pass without modification.
- No change to consumer-facing API or lifespan wiring.

## 7. References

- Architecture Review Plan: `.cursor/plans/architecture_review_plan_7bcbc812.plan.md`
- ApplicationContainer implementation: `server/container.py`
- Dependency injection and lifespan: `server/app/lifespan.py`, `server/app/lifespan_startup.py`
