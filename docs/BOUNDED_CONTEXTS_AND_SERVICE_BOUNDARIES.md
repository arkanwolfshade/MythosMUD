# Bounded Contexts and Service Boundaries

**Document Version:** 1.0
**Date:** January 2026
**Status:** Architecture documentation
**Purpose:** Define explicit bounded contexts and service boundaries for MythosMUD per the Architecture Review Plan.

## 1. Overview

This document defines **bounded contexts** (DDD-style) and **service boundaries** for the MythosMUD server. It aligns with:

- **ApplicationContainer** domain bundles: `docs/APPLICATION_CONTAINER_ANALYSIS.md`
- **Event ownership**: `docs/EVENT_OWNERSHIP_MATRIX.md`
- **Architecture Review Plan**: `.cursor/plans/architecture_review_plan_7bcbc812.plan.md`

Bounded contexts are logical boundaries within which a particular model and vocabulary apply. Service boundaries define which services belong to which context, what they own, and how they interact.

## 2. Bounded Contexts

| Context            | Description                                                                 | Container bundle(s) |
| ------------------ | --------------------------------------------------------------------------- | ------------------- |
| **Core**           | Configuration, database, task registry, event bus, persistence facade      | CoreBundle          |
| **Realtime**       | WebSocket connections, NATS, event→message transformation, room presence   | RealtimeBundle      |
| **Game**           | Players, rooms, movement, exploration, containers, user identity, caches    | GameBundle          |
| **Combat**         | Player/NPC combat, death, respawn, lucidity, catatonia                      | CombatBundle        |
| **Magic**          | Spells, MP, spell effects, targeting, learning                              | MagicBundle         |
| **NPC**            | NPC lifecycle, spawning, population control                                 | NPCBundle           |
| **Chat**           | Room/whisper/global chat over NATS                                          | ChatBundle          |
| **Temporal**       | In-game time, holidays, schedule, mythos tick consumer                      | TimeBundle          |
| **Monitoring**     | Performance, exceptions, dashboard, log aggregation                         | MonitoringBundle    |

## 3. Service Boundaries by Context

### 3.1 Core

**Owns:** Application config, database manager, task registry, tracked task manager, EventBus, persistence facade (sync + async).

**Services / components:**

- `config` (configuration)
- `database_manager`
- `task_registry`, `tracked_task_manager`
- `event_bus`
- `persistence`, `async_persistence`

**Inbound:** None (root of dependency graph).

**Outbound:** All other contexts depend on Core for config, persistence, and events.

**Contracts:**

- Persistence: repositories accessed via `async_persistence` (e.g. PlayerRepository, RoomRepository).
- Events: domain events published/subscribed via `event_bus`.

---

### 3.2 Realtime

**Owns:** WebSocket connection lifecycle, room-based subscriptions, presence tracking, NATS client, EventBus→WebSocket transformation, NATS→WebSocket delivery.

**Services / components:**

- `connection_manager`
- `real_time_event_handler`
- `nats_service`
- `nats_message_handler`
- `event_publisher`

**Inbound:** EventBus (domain events), NATS (chat/combat subjects). Depends on Core (config, event_bus, task_registry, async_persistence).

**Outbound:** WebSocket messages to clients. Other contexts use `connection_manager` to send messages or resolve connections.

**Contracts:**

- **EventBus → WebSocket:** RealTimeEventHandler subscribes to domain events and sends typed WebSocket messages (e.g. `player_entered`, `player_left`, `combat_event`). See EVENT_OWNERSHIP_MATRIX.md.
- **NATS → WebSocket:** NATSMessageHandler subscribes to `chat.*`, `combat.{room_id}` and forwards to WebSocket.

---

### 3.3 Game

**Owns:** Player identity and state, room data and movement, exploration, containers/inventory, user lookup, room/profession caches, in-game calendar (holiday/schedule), item prototypes and factory.

**Services / components:**

- `player_service`, `player_position_service`, `player_preferences_service`
- `room_service`, `room_cache_service`, `room_data_cache`, `room_data_fixer`, `room_data_validator`, `room_sync_service`
- `movement_service`, `exploration_service`
- `user_manager`
- `container_service`, `environmental_container_loader`, `wearable_container_service`, `inventory_service`, `inventory_mutation_guard`, `equipment_service`
- `profession_cache_service`
- `holiday_service`, `schedule_service`, `mythos_tick_scheduler`
- `item_prototype_registry`, `item_factory`
- `coordinate_generator`, `coordinate_validator`
- `ascii_map_renderer`

**Inbound:** Depends on Core (persistence, event_bus). May use Realtime (e.g. user_manager / nats_message_handler for presence).

**Outbound:** Publishes domain events (e.g. Room emits PlayerEnteredRoom, PlayerLeftRoom). Other contexts call Game services for player/room/container data.

**Contracts:**

- **Movement:** MovementService updates position and calls Room.player_entered() / player_left(); EventBus notifies Realtime.
- **Containers:** ContainerService owns container CRUD and contents; persistence via ContainerRepository (async).

---

### 3.4 Combat

**Owns:** Combat sessions, turns, attacks, flee, death, respawn, HP sync, lucidity/catatonia, combat–NATS publishing.

**Services / components:**

- `player_combat_service`, `player_death_service`, `player_respawn_service`
- `combat_service`, `combat_service_state`, `combat_event_handler`, `combat_event_publisher`, `combat_attack_handler`, `combat_flee_handler`, `combat_death_handler`, `combat_cleanup_handler`, `combat_initialization`, `combat_turn_processor`, `combat_persistence_handler`, `combat_messaging_service`, `combat_messaging_integration`, `combat_configuration_service`, `combat_monitoring_service`, `combat_hp_sync`
- `catatonia_registry`, `passive_lucidity_flux_service`
- `lucidity_service`, `active_lucidity_service`, `lucidity_event_dispatcher`, `lucidity_command_disruption`, `lucidity_communication_dampening`, `hallucination_frequency_service`, `fake_hallucination_service`
- `target_resolution_service`
- `corpse_lifecycle_service`, `rescue_service`
- `phantom_hostile_service`
- NPC combat: `npc_combat_*` (handlers, integration, lifecycle, rewards, etc.)

**Inbound:** Depends on Core (persistence, event_bus), Realtime (connection_manager for broadcasts), Game (movement_service for flee/position).

**Outbound:** Publishes CombatStartedEvent, PlayerAttackedEvent, NPCAttackedEvent, CombatEndedEvent; PlayerDeathService/PlayerRespawnService publish death/respawn events. CombatEventPublisher sends to NATS (`combat.{room_id}`). RealTimeEventHandler and NATSMessageHandler deliver to clients.

**Contracts:**

- **Combat events:** CombatService is the authority for combat state; events flow EventBus → CombatEventPublisher → NATS and/or EventBus → RealTimeEventHandler → WebSocket (see EVENT_OWNERSHIP_MATRIX.md).

---

### 3.5 Magic

**Owns:** Spell registry, targeting, effects, learning, MP regeneration, spell execution.

**Services / components:**

- `magic_service`
- `spell_registry`, `spell_targeting_service`, `spell_effects`, `spell_learning_service`, `mp_regeneration_service`

**Inbound:** Depends on Core (async_persistence), Game (player_service), Combat (combat_service, player_combat_service).

**Outbound:** Affects player state (MP, learned spells); may trigger or interact with combat (e.g. spell damage).

**Contracts:**

- Magic reads/writes player data via persistence; coordinates with Combat for in-combat spell rules.

---

### 3.6 NPC

**Owns:** NPC lifecycle, spawning, population control, NPC definitions/rules.

**Services / components:**

- `npc_lifecycle_manager`, `npc_spawning_service`, `npc_population_controller`
- `npc_service`, `npc_instance_service`, `npc_startup_service`
- NPC combat is owned by Combat context but uses NPC data (see Combat).

**Inbound:** Depends on Core (event_bus, persistence, async_persistence).

**Outbound:** Publishes/consumes room-related events (e.g. NPC enter/leave room). TimeBundle (mythos_time_consumer) may drive NPC lifecycle.

**Contracts:**

- NPC lifecycle and room occupancy; combat logic for NPCs lives in Combat context with clear interfaces to NPC data.

---

### 3.7 Chat

**Owns:** Room say, whisper, (planned) global/local channels; NATS subjects for chat.

**Services / components:**

- `chat_service`
- `chat_logger` (if present)

**Inbound:** Depends on Core (persistence), Game (player_service, user_manager), Realtime (nats_service).

**Outbound:** Publishes to NATS (`chat.say.{room_id}`, `chat.whisper.{player_id}`). NATSMessageHandler delivers to WebSocket.

**Contracts:**

- Chat is the single publisher for chat NATS subjects; Realtime only forwards NATS→WebSocket.

---

### 3.8 Temporal

**Owns:** Consumption of in-game time events; coordinates holiday, schedule, and NPC lifecycle reactions to time.

**Services / components:**

- `mythos_time_consumer`

**Inbound:** Depends on Core (event_bus), Game (holiday_service, schedule_service, room_service), NPC (npc_lifecycle_manager).

**Outbound:** Subscribes to time/tick events; may trigger room or NPC updates.

**Contracts:**

- Single consumer for mythos time events; delegates to Game and NPC services for side effects.

---

### 3.9 Monitoring

**Owns:** Performance metrics, exception tracking, monitoring dashboard, log aggregation.

**Services / components:**

- `performance_monitor`, `exception_tracker`, `monitoring_dashboard`, `log_aggregator`

**Inbound:** Optional; may receive events or metrics from other contexts.

**Outbound:** Observability only; no domain behavior.

**Contracts:**

- Non-invasive; other contexts may report metrics or errors to Monitoring.

---

## 4. Cross-Context Dependencies (Summary)

```
Core
 ├── Realtime (config, event_bus, task_registry, async_persistence)
 ├── Game (persistence, event_bus; optional Realtime for user_manager)
 ├── Combat (persistence, event_bus, Realtime.connection_manager, Game.movement_service)
 ├── Magic (async_persistence, Game.player_service, Combat.*)
 ├── NPC (event_bus, persistence, async_persistence)
 ├── Chat (persistence, Game.player_service, Game.user_manager, Realtime.nats_service)
 ├── Temporal (event_bus, Game.holiday/schedule/room_service, NPC.npc_lifecycle_manager)
 └── Monitoring (standalone)
```

## 5. Service Boundary Rules

1. **Single owner:** Each service belongs to exactly one bounded context.
2. **Cross-context access:** Use published interfaces (e.g. PlayerService, RoomService) rather than reaching into another context’s internals.
3. **Events:** Domain events are the preferred way to notify other contexts; see EVENT_OWNERSHIP_MATRIX.md for canonical ownership.
4. **Persistence:** All persistence goes through Core (async_persistence and repositories); no context bypasses the persistence layer.
5. **Realtime delivery:** Only Realtime context sends WebSocket messages; other contexts publish events or NATS messages, and Realtime (or NATS handler) delivers to clients.

## 6. References

- **ApplicationContainer and bundles:** `docs/APPLICATION_CONTAINER_ANALYSIS.md`
- **Event ownership and duplication:** `docs/EVENT_OWNERSHIP_MATRIX.md`
- **Architecture Review Plan:** `.cursor/plans/architecture_review_plan_7bcbc812.plan.md`
- **Container implementation:** `server/container/` (main.py, utils.py, bundles/)
