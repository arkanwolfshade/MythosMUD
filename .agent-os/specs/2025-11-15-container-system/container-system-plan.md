## Container System Design Plan

Documented: 2025-11-15
Author: GPT-5.1 Codex (Occult Studies Dept.)

### 1. Requirements & Constraints

**Container Types**

- Environmental props (room objects flagged as containers; metadata includes capacity, locking, decay, ownership scope).
- Wearable containers (backpacks, bandoliers) that occupy equipment slots but expose nested storage.
- Player/NPC corpses treated as temporary containers with decay windows and owner-only grace period.
- **Cross-Cutting Rules**
  - Reuse `InventoryService` semantics (`max_slots = 20`, stack merging, mutation guard serialization).
  - COPPA/privacy: no personal data in container metadata; audit all interactions with enhanced logging.
  - Rate-limit looting commands; enforce secure path validation for persistence writes.

### 2. Comparative Research

**Diku/CircleMUD**: containers are item prototypes with flags; straightforward but persistence-heavy. Corpses reuse same structure.

**LP/Evennia**: component mixins (`Container` scripts) with ACL locks and event hooks. Highlights value of attachable container component.

**LambdaMOO**: every object/player/room can act as container; permission verbs guard all moves. Inspires unified command verbs for Mythos.

### 3. Server-Side Architecture

**ContainerComponent**

- Fields: `container_id`, `source_type` (`environment`, `equipment`, `corpse`), `owner_id`, `capacity_slots`, `weight_limit`, `lock_state`, `decay_at`, `allowed_roles`, `items: list[InventoryStack]`.
- Compose onto room objects, inventory items, and spawned corpse entities.
- **Corpse Flow**
  - Death event spawns `ContainerComponent` with loot snapshot, owner grace timer, decay schedule (auto cleanup).
- **Wearable Containers**
  - Extend `InventoryItem` model with optional `inner_container`.
  - Equip/unequip enforces inventory spill rules and persists nested contents.
- **Persistence & Schema**
  - Augment `InventoryPayload` + JSON schema to allow nested containers.
  - Add `containers` persistence table keyed by `container_instance_id` referencing `room_id` / `entity_id`.
  - Include migration + validation scripts.
- **Services & Lifecycle**
  - New `ContainerService` orchestrates open/insert/remove using `InventoryService`.
  - Mutation guard keyed by container to serialize multi-looter access.
  - Logging via `get_logger` with structured context (container_id, actor_id, action, success).

### 4. Client/UI Integration

**Events**

- Server emits `ContainerOpened`, `ContainerUpdated`, `ContainerClosed` events over existing websocket channel.
- **UX Patterns**
  - Split-pane UI for environmental containers (left = container contents, right = personal inventory).
  - Backpack tab/pill inside inventory UI, honoring overall slot budgets.
  - Corpse overlay shows owner-only countdown and loot-all button once timer expires.
- **Accessibility & Compliance**
  - Keyboard focus cycles between panes; screen readers announce container state.
  - Corpses display anonymized descriptors when privacy flag enabled.

### 5. Testing & Rollout

**Server Tests**: unit tests for `ContainerService`, corpse grace logic, wearable container transitions; integration tests for persistence + concurrent looting.

**Client Tests**: Vitest component tests for panes and countdown UI; Playwright MCP scenarios for multi-user looting and lockouts.

**Telemetry**: assert structured logs in CI; metrics for loot attempts, lock violations.
- **Rollout Plan**: feature flag `containers.v1`; phased enabling—QA rooms → limited production zones → corpse looting after monitoring grief metrics.
