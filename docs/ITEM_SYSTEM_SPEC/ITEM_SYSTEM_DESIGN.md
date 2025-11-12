# MythosMUD Item System Blueprint

## Document Purpose

- Provide Prof. Wolfshade and design stakeholders with a lore-conscious overview of the forthcoming item system.
- Supply the engineering faculty with a concrete blueprint for data models, services, and integration surfaces.
- Establish implementation phases that respect existing inventory mechanics and monitoring tooling.

## Audience & Scope

- **Stakeholders**: Senior designers, lore archivists, narrative writers; focus on pillars, gameplay goals, extensibility.
- **Engineering Faculty**: Backend and client developers, test automation specialists, observability engineers; focus on schema,
  service boundaries, concurrency, and validation pathways. UI presentation details.
- **Out of Scope**: Drop-rate balancing, economy tuning, procedural generation rules.

## Lore Alignment

As cited in _The Annotated Pnakotic Manuscripts_ (Armitage & Wilmarth, 1933), artifacts must feel ancient yet systematic. Every
item—mundane or eldritch—derives from a curated prototype in the Restricted Archive. This document preserves that hierarchy while
granting modern extensibility akin to Evennia-style component stacks.

## Foundational Design Principles

- **Prototype & Instance Split**: Immutable prototypes define canonical attributes; lightweight instances carry mutable runtime
  state (condition, attunement, binding).
- **Component-Based Augmentation**: Behaviors (e.g., sanity effects, light emission) attach via reusable components inspired by
  Diku/ROM affects and Evennia mixins.
- **Bitvector Flag Encoding**: Performance-oriented representation of wear locations, usage permissions, and effect toggles.
- **Data-Driven Extensibility**: Prototypes stored in structured data (JSON or YAML) with schema validation before promotion to
  production catalogs.
- **Inventory Mutation Guard Compatibility**: All mutations must pass through the existing guard for idempotency and monitoring.

## Item Lifecycle Overview

1. **Prototype Registration**: Lore scribes define or update prototype definitions; validation scripts enforce schema compliance.
2. **Catalog Publication**: Approved prototypes load into the Prototype Registry service at startup (hot reload optional in Phase 2).
3. **Instance Creation**: Instances spawn from prototypes during loot drops, crafting, or administrative commands.
4. **Inventory Integration**: Inventory service associates item instance IDs with player containers, using mutation guards.
5. **Persistence**: Item instances persist via SQLAlchemy ORM models (player inventory linkage, world containers, ground cache).
6. **Observation & Alerts**: Structured logging and monitoring dashboard provide visibility into item mutations and anomalies.

## Item Taxonomy (Stakeholder View)

- **Consumables**: Potions, scrolls, ritual reagents; typically single-use with scripted effects.
- **Equipment**: Weapons, armor, talismans; support wear locations, durability, attribute modifiers.
- **Artifacts & Relics**: Unique lore-bound items with sanity effects or progression gating.
- **Containers**: Bags, chests, cosmic reliquaries; may modify inventory capacity or apply dimensional effects.
- **Quest Items**: Progression-critical objects, often soulbound and tracked via journal metadata.
- **Environmental Objects**: Placeable or interactive props (torches, glyphs, wards) with scripted world hooks.
- **Currency & Trade Goods**: Aggregated stackable items with economic metadata.

## Core Attribute Matrix

| Attribute            | Description                                                                                  | Type           | Notes                             |
| -------------------- | -------------------------------------------------------------------------------------------- | -------------- | --------------------------------- |
| `prototype_id`       | Canonical identifier, e.g., `artifact.miskatonic.codex`                                      | str            | Primary key in prototype registry |
| `name`               | Display name respecting locale and lore                                                      | str            | Supports localization keys        |
| `short_description`  | Concise descriptor for lists                                                                 | str            | 120 char max                      |
| `long_description`   | Rich description for inspection                                                              | str            | Markdown subset allowed           |
| `item_type`          | Enum: `consumable`, `equipment`, `artifact`, `container`, `quest`, `environment`, `currency` | str            | Mirrors taxonomy                  |
| `weight`             | Encumbrance value                                                                            | float          | Supports fractional weights       |
| `base_value`         | Economic valuation                                                                           | int            | Subject to faction modifiers      |
| `durability`         | Max structural integrity                                                                     | int            | `None` when not applicable        |
| `current_condition`  | Runtime condition (instances only)                                                           | int            | 0..durability                     |
| `stat_modifiers`     | Mapping of stat → delta                                                                      | dict[str, int] | Includes sanity modifiers         |
| `effect_components`  | List of component IDs                                                                        | list[str]      | e.g., `component.fear_aura`       |
| `flags`              | Bitvector encoding for properties                                                            | int            | Defined in central registry       |
| `wear_locations`     | Bitvector or list referencing allowed slots                                                  | int            | Mask for compatibility checks     |
| `usage_restrictions` | Structured rules (class, faction, sanity thresholds)                                         | dict           | Evaluated server-side             |
| `stacking_rules`     | Max stack size, merge policy                                                                 | dict           | Instances track `quantity`        |
| `binding`            | Binding type: `unbind`, `pickup`, `equip`, `quest`                                           | str            | Instances store bound player      |
| `lifecycle_hooks`    | Script references executed on events                                                         | dict[str, str] | e.g., `on_use`, `on_tick`         |
| `metadata`           | Arbitrary namespaced key/value payload                                                       | dict[str, Any] | For future expansions             |

## Component Library (Initial Set)

| Component                 | Purpose                            | Notes                                       |
| ------------------------- | ---------------------------------- | ------------------------------------------- |
| `DurabilityComponent`     | Applies wear and break mechanics   | Integrates with crafting repairs            |
| `SanityComponent`         | Adjusts sanity on use/equip        | Pulls tables from Arkham Psychiatry ledger  |
| `LightEmitterComponent`   | Provides illumination radius       | Coordinates with room lighting system       |
| `AuraComponent`           | Broadcasts passive effects         | Reuses monitoring hooks for anomalies       |
| `ChargeComponent`         | Tracks limited charges             | Works with `Rechargeable` trait             |
| `CooldownComponent`       | Enforces usage cooldowns           | Syncs with player action scheduler          |
| `AttunementComponent`     | Requires rituals before unlock     | Stores attunement progress                  |
| `ContainerComponent`      | Defines slot capacity and filters  | Supports nested inventories with safeguards |
| `ScriptedEffectComponent` | Binds to scripting engine triggers | Allows dynamic quest behaviors              |

## Flag & Enumeration Strategy

- Central registry `server/game/items/item_flags.py` (to be created) enumerates:
  - Wear slots (`HEAD`, `TORSO`, `OFF_HAND`, etc.) using bit positions.
  - Property flags (`MAGICAL`, `CURSED`, `NO_DROP`, `NO_SALE`, `SOULBOUND`).
- Provide helper utilities for:
  - `has_flag(flags, ItemFlag.NO_DROP)`
  - `combine_flags([ItemFlag.MAGICAL, ItemFlag.GLOW])`
- Maintain JSON → bitvector mapping in prototype loader for readability.

## Service Responsibilities (Technical Blueprint)

### Prototype Registry Service

- Loads validated prototype definitions from `data/prototypes/items/*.json`.
- Offers lookup by `prototype_id` and supports tag-based queries.
- Exposes API for administrative hot-reload (Phase 2).
- Validates against Pydantic model ensuring 120 char limits, required attributes, flag resolution.

### Item Factory & Instance Service

- `ItemFactory.create_instance(prototype_id, *, quantity=1, overrides=None, source=None)` returns `ItemInstance`.
- Generates unique `item_instance_id` (UUID v7 preferred).
- Applies overrides for dynamic attributes (e.g., randomized damage rolls).
- Integrates with `InventoryMutationGuard` by emitting tokens for multi-step transactions.

### Persistence Layer

- SQLAlchemy models:
  - `ItemPrototype` (optional, if storing in DB) or rely on JSON.
  - `ItemInstance` with fields: `id`, `prototype_id`, `owner_type`, `owner_id`, `location_context`, `quantity`, `condition`,
    `flags`, `metadata`, timestamps.
  - `ItemComponentState` for components requiring persistence (e.g., charges).
- Migration strategy: create new tables under `/data/players/` schema; ensure test fixtures isolate to `/server/tests/data/...`.

### Inventory Integration

- Extend existing inventory services to reference `item_instance_id` rather than raw payload dicts.
- Provide facade methods: `inventory_service.add_item(player_id, item_instance, *, token=None)`.
- Equip/unequip pipelines validate wear slots using flag masks and component hooks.

### Scripting & Event Hooks

- Define `ItemEventBus` that emits domain events (`item.used`, `item.equipped`, `item.broken`, `item.bound`).
- NATS subjects follow existing naming pattern `inventory.item.*`.
- Hooks trigger Playwright E2E scenarios for regression coverage.

### Observability & Monitoring

- Structured logging via `logger.info("Item instance created", item_instance_id=..., prototype_id=..., player_id=...)`.
- Monitoring dashboard alert for:
  - Duplicate mutation tokens (already integrated).
  - Rapid durability loss (potential exploit).
  - Prototype lookup failures (missing data).

## Administrative Interfaces

- **Summon Command (Concept)**
  - `/summon <prototype_id> [quantity] [item|npc]`: administrative-only ritual for conjuring prototypes into the active room. Provides modern slash UX while keeping legacy telnet compatibility.
  - Validation chain: extend command parser and security validator to recognise the verb, enforce optional quantity (default `1`, bounded to a safe ceiling), and accept hints for target classification (item vs. NPC). Non-admins receive a lore-aware rejection.
  - Item flow: resolve caller, assert admin privilege, look up the prototype via the registry, create runtime instances through the factory, insert stacks into the room-drop ledger (or directly into inventory in future variants), and emit an `admin_summon` event with metadata such as `source=admin_summon` and `summoned_by`.
  - NPC flow (Phase 2+): bridge into the `NPCInstanceService` so the same command can spawn alphabetical horrors when NPC lifecycles support admin conjuration; until then, produce a graceful stub response guiding administrators to `npc spawn`.
  - Safeguards: respect mutation tokens when touching inventories, cap mass summons to avoid griefing, and log every invocation through the admin action logger for subsequent inquests by the Senate.

## Data Model Proposal

```text
ItemPrototype
  prototype_id (PK)
  item_type
  name
  short_description
  long_description
  weight
  base_value
  durability
  flags
  wear_slot_mask
  stacking_rules (JSON)
  usage_restrictions (JSON)
  effect_components (JSON)
  metadata (JSON)

ItemInstance
  item_instance_id (PK)
  prototype_id (FK → ItemPrototype.prototype_id)
  owner_type (ENUM: player, room, npc, container)
  owner_id (UUID or composite)
  quantity
  condition
  flags_override (nullable)
  binding_state
  attunement_state (JSON)
  custom_name (nullable)
  metadata (JSON)
  created_at
  updated_at

ItemComponentState
  id (PK)
  item_instance_id (FK → ItemInstance.item_instance_id)
  component_id
  state_payload (JSON)
  updated_at
```

## API Surface (Draft)

- **Pydantic Models**
  - `ItemPrototypeModel`: Validation for prototype ingestion.
  - `ItemInstanceModel`: Serialization for network transport.
  - `InventoryEntryModel`: Combines instance data with container metadata.
- **Service Interface**
  - `ItemService.get_instance(item_instance_id)`
  - `ItemService.list_instances(owner_type, owner_id)`
  - `ItemService.apply_component_event(item_instance_id, event)`
  - `InventoryService.transfer_item(source_owner, target_owner, item_instance_id, quantity, *, token)`

## Persistence & Migration Plan

- Create Alembic migration introducing `item_instances` and `item_component_states` tables.
- Update test fixtures in `server/tests/conftest.py` to seed minimal exemplar prototypes.
- Provide CLI tools under `scripts/items/` for:
  - `load_prototypes.ps1`: Validate and load prototypes.
  - `export_prototypes.ps1`: Dump prototypes for review.
- Provision dedicated SQLite schemas for each environment:
  - `/data/e2e_test/items/e2e_items.db`
  - `/data/local_test/items/local_items.db`
  - `/data/unit_test_test/items/unit_test_items.db`
- Seed initial data so every equip slot has at least two representative item prototypes (ensuring coverage for armor, weapons, accessories, etc.) once the databases are created.

## Validation & Security

- Enforce COPPA compliance: no item metadata captures personal data.
- Input validation via Pydantic and service-level guards.
- Path security: prototype loader sanitizes file paths and rejects traversal.
- Rate limiting: throttle administrative prototype mutations and item duplication commands.

## Testing Strategy

- **Unit Tests**: Prototype parsing, component behaviors, binding rules (`pytest`).
- **Property Tests**: Ensure flag masks remain invertible and collision-free.
- **Integration Tests**: Inventory command coverage (`server/tests/unit/commands/test_inventory_commands.py` extensions).
- **Playwright Scenarios**: Multi-client equipment flows, sanity effect propagation.
- **Load Tests**: Monitor mutation guard pressure during mass loot events.

## Implementation Phases

1. **Phase 0 – Infrastructure**: Implement prototype schema, registry, and basic instance factory. Introduce SQLAlchemy models.
2. **Phase 1 – Inventory Integration**: Replace raw inventory payloads with `ItemInstance`. Update commands and mutation guard usage.
3. **Phase 2 – Component Expansion**: Add component framework, persistence layer for component state, and scripting hooks.
4. **Phase 3 – Observability & Tooling**: Enhance monitoring alerts, administrative dashboards, and data export tooling.

## Open Questions

- Should prototype sources remain JSON/YAML or migrate to database-backed content authoring?
- What governance process promotes prototype drafts to canonical circulation?
- Do we need real-time prototype diff broadcast to connected clients for GM tooling?
- How do we sequence sanity effects with broader mental health systems still in design?

## Next Steps

- Finalize prototype schema definition (`schemas/items/item_prototype.schema.json`).
- Draft Pydantic models and services per blueprint.
- Coordinate with narrative team on initial catalog (target: 25 baseline prototypes).
- Align monitoring team on new alert thresholds for item anomalies.
