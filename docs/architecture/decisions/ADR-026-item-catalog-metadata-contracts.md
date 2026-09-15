# ADR-026: Item Catalog Metadata Contracts

**Version 1.0.0** · MythosMUD · 2026-09-13

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-09-13

MythosMUD will ingest mechanical item stats inspired by Call of Cthulhu-style
tables into `item_prototypes`, using Mythos-renamed names and retuned numbers.
Phase 1 locks **public contracts** (ADR + JSON Schema + Pydantic) only. Private
catalog rows, DML migrations, PDF extract, and combat dice resolution ship later.

## 2. Context

**[NOTE]**
Combat today resolves weapons through integer `WeaponStats`
(`min_damage`, `max_damage`, `modifier`, `damage_types`, `magical`) on
`metadata.weapon`, consumed by `server/game/weapons.py` and
`player_schema_converter`. Classic CoC-style tables use dice expressions, skill %,
range, attacks, ammo, armor points, and tome mechanics that do not fit that
shape alone.

Existing fictional Mythos prototypes must keep working. Third-party product
names and verbatim table text must not land in the public MythosMUD tree; DML
and intermediate catalogs live in the private `data/` submodule.

## 3. Decision

**[SPEC]**

### 3.1 Phased delivery

1. **Phase 1 (this ADR):** Public JSON Schema / Pydantic contracts; dual-write
   bridge helper (`damage_expr` → legacy min/max); no mass seed.
2. **Phase 2:** Hybrid PDF/table extract → private intermediate catalog →
   SQL generator → idempotent private migrations (`dev` / `unit` / `e2e`).
3. **Phase 3:** Combat consumes rich metadata; retire dual-write when safe;
   optional promotion of hot JSONB fields to SQL columns at launch finalization.

### 3.2 Inclusion and IP

- Include any row with mechanical numbers (weapons, armor, tools, tomes,
  artifacts, scenario uniques).
- Store Mythos-renamed display names; stats may be retuned for MythosMUD.
- Public repo: ADR + schemas/models only. Private `data/`: catalog JSON, rename
  maps, provenance notes, generated DML/migrations.

### 3.3 Storage shape

- Mechanical detail lives in JSONB `item_prototypes.metadata` for now.
- No new SQL columns in Phase 1–2. Columnization is deferred until launch
  finalization when query/filter needs are proven.

Documented optional `metadata` objects:

| Key         | Role                                                            |
| ----------- | --------------------------------------------------------------- |
| `weapon`    | Rich combat fields + legacy `WeaponStats` integers (dual-write) |
| `armor`     | Armor points / coverage                                         |
| `tome`      | Sanity / Mythos-knowledge style numbers (Mythos-tuned)          |
| `equipment` | Skill or other mechanical bonuses                               |
| `catalog`   | Namespace, canonical/variant linkage, era, opaque `source_key`  |

### 3.4 Coexistence and dedupe

- Parallel namespace for catalog-imported items; do not replace legacy Mythos
  prototypes until a later consolidation pass.
- One canonical prototype per logical item; create variant rows only when stats
  or era rules differ; scenario uniques remain separate rows.

### 3.5 Combat bridge

Until combat understands dice/skill/range/ammo/armor:

- Dual-write: populate rich fields **and** legacy integer `WeaponStats` on
  wieldable weapons.
- Use a documented lossy `damage_expr` → `(min_damage, max_damage)` helper for
  generators; combat paths stay on integers until Phase 3.

### 3.6 Explicitly out of scope (this ADR)

- Combat dice resolution / skill rolls / ammo / range enforcement
- Full source-corpus extract and DML volume
- SQL column promotion
- Retiring or remapping existing Mythos prototypes

## 4. Alternatives Considered

**[SPEC]**

1. **Preserve CoC fields only, no schema extension** — Rejected: leaves combat
   redesign without a public contract and invites ad-hoc JSON.
2. **Translate everything to integers at extract time** — Rejected: throws away
   data required by inclusion policy.
3. **First-class SQL columns immediately** — Rejected: heterogeneous tome /
   artifact / scenario shapes explode columns; JSONB matches current table.
4. **ADR + combat rewrite in one effort** — Rejected: couples extract quality,
   schema mistakes, and balance into one megapr.
5. **Verbatim third-party product names in public DML** — Rejected: IP risk.

## 5. Consequences

**[SPEC]**

### Positive

- Clear public contract for private catalog authors and future combat work.
- Existing prototypes and combat remain valid.
- IP-sensitive content stays in the private submodule.

### Negative

- Dual-write is lossy; dice expressions are flattened for current combat.
- Catalog and combat timelines are decoupled; rich fields are inert until
  Phase 3.

### Neutral

- `metadata` remains open to additional lore keys; known mechanical objects are
  validated when present.

## 6. Implementation anchors

**[SPEC]**

- JSON Schema: `schemas/items/item_prototype.schema.json`
- Pydantic metadata models: `server/game/items/metadata_models.py`
- Bridge helper: `server/game/items/damage_expr.py`
- Catalog DML emitter: `server/game/items/catalog_dml.py`
- Private catalog pipeline: `data/item_catalog/` (see README)
- Synthetic fixture: `schemas/items/fixtures/synthetic_rich_metadata_prototype.json`
