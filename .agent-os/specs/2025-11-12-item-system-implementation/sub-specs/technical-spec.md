# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-11-12-item-system-implementation/spec.md

## Phase 0 – Prototype Registry & Schema

- Define JSON schema (`schemas/items/item_prototype.schema.json`) covering all fields from the blueprint, including flag bitmasks, component arrays, metadata payloads, and equip slot masks.
- Implement validation CLI (`scripts/items/validate_prototypes.ps1`) invoking Pydantic models to lint prototype files and emit structured logs via `get_logger`.
- Build the Prototype Registry service (`server/game/items/prototype_registry.py`) exposing immutable lookup operations, tag queries, and hot-reload hooks; enforce 120-character limits and flag resolution.
- Testing:
  - Unit: schema validation edge cases, flag resolution helpers, registry lookups (invalid/missing prototypes).
  - Integration: load sample prototypes through the registry and assert observability emits warnings for malformed entries.
  - Playwright: N/A (documented as not applicable for this phase).

## Phase 1 – Item Factory & Guarded Integration

- Create `ItemFactory` capable of instantiating item instances with unique UUIDv7 identifiers, quantity handling, overrides, and origin metadata.
- Extend inventory services to operate on `item_instance_id` rather than raw payloads; ensure mutation guard tokens wrap multi-step transactions.
- Update component hooks to consume the new instance structures while preserving existing feature toggles.
- Testing:
  - Unit: item factory creation, override application, mutation guard token issuance.
  - Integration: equip/unequip flows using sample prototypes, verifying guard enforcement and structured events.
  - Playwright: Scenario validating equipment changes propagate to clients without regression.

## Phase 2 – Persistence & Database Provisioning

- Introduce Alembic migration for `item_instances` and `item_component_states` tables, aligning with proposed data model.
- Provision SQLite databases at `/data/e2e_test/items/e2e_items.db`, `/data/local_test/items/local_items.db`, and `/data/unit_test/items/unit_test_items.db`; scripts respect COPPA storage rules.
- Seed each database with at least two prototypes per equip slot (head, torso, legs, main hand, off hand, accessory, etc.) using CLI utilities, ensuring deterministic IDs for test assertions.
- Testing:
  - Unit: migration helpers, seed script validations, CRUD operations on SQLAlchemy models.
  - Integration: end-to-end persistence round trips for item creation, transfer, and deletion.
  - Playwright: Regression scenario ensuring seeded items appear in admin tooling and inventory interfaces.

## Phase 3 – Administrative Summon Command

- Expand command parser and security validator to recognise `/summon`; enforce quantity bounds, prototype ID format, and optional target-type hints.
- Implement `handle_summon_command` to validate admin privileges, fetch prototypes via the registry, create item instances, deposit them into the current room, and emit `admin_summon` structured logs.
- Provide NPC summoning stub wiring (`NPCInstanceService` placeholder call) returning a clear message until implementation is complete; ensure logging differentiates between item and NPC requests.
- Testing:
  - Unit: command parser validation, admin permission checks, item instantiation via summon handler, NPC stub response.
  - Integration: simulate admin sessions summoning items and confirming room drops plus audit log entries.
  - Playwright: multiplayer scenario validating summoned items appear for connected players and that NPC requests surface stub messaging.

## Phase 4 – Testing & Observability Harness

- Implement monitoring alerts for registry load failures, summon misuse (quantity spikes), and durability anomalies leveraging existing observability stack.
- Extend audit logging to include metadata (`source=admin_summon`, `summoned_by`, `quantity`) and ensure mutation guard anomalies raise alerts.
- Document operational runbooks describing seed regeneration, summon etiquette, and recovery from failed migrations.
- Testing:
  - Unit: logging utilities, alert configuration serialization, runbook linting if automated.
  - Integration: smoke tests validating alerts trigger under simulated error conditions.
  - Playwright: scenario verifying audit logs appear in admin dashboards where applicable.
