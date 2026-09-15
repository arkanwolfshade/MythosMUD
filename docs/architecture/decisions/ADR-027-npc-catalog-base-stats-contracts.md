# ADR-027: NPC Catalog Base Stats Contracts

**Version 1.0.0** · MythosMUD · 2026-09-14

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Accepted
**Date:** 2026-09-14

MythosMUD will ingest mechanical creature stats inspired by Call of Cthulhu-style
bestiary tables into existing `npc_definitions`, using Mythos-renamed names and
retuned numbers. Rich mechanics live under JSON `base_stats` (no new metadata
column in this epic). Placement for catalog rows is arena + inert spawn. Shared
dice helpers live in `server/game/dice_expr.py` (moved from the item bridge).

## 2. Context

**[NOTE]**
NPC combat today reads legacy integers: required `determination_points` /
`max_dp` / `xp_value` in `base_stats`, plus `behavior_config.attack_damage` for
outgoing damage. Classic bestiary rows use dice expressions, armor points,
skills, SAN effects, and AI aggression that do not fit that shape alone.

Existing hand-authored Mythos NPCs must keep working. Third-party product names
and verbatim table text must not land in the public tree; DML and intermediate
catalogs live in the private `data/` submodule (same IP policy as ADR-026).

Spawn population columns already exist on `npc_definitions` and on
`npc_spawn_rules`; finishing the column split is a follow-on (#838), not a gate
on catalog DML.

## 3. Decision

**[SPEC]**

### 3.1 Phased delivery

1. **Phase 1 (this ADR + L1):** Public JSON Schema / Pydantic contracts; shared
   `damage_expr` / `roll_damage_expr`; no mass seed.
2. **Phase 2:** Hybrid extract → private `data/npc_catalog/` → SQL generator →
   reviewed arena/inert migrations (`dev` / `unit` / `e2e`); start with core-era.
3. **Phase 3:** NPC combat consumes rich damage + HP/armor; dual-write until
   those paths are green. Skills / % / SAN / AI consumers are follow-ons (#839).
4. **Phase 4:** Browse UI — out of this epic (#840).

### 3.2 Storage and placement

- Upsert into existing `npc_definitions` (not a new prototypes table).
- Catalog rows: `sub_zone_id='arena'`, `room_id=NULL`, inert spawn
  (`spawn_probability=0`, `max_population=0`, `required_npc=false`).
- Identity: `ON CONFLICT` on `(name, sub_zone_id)`; renames are explicit
  migrations.
- `npc_type` from extract hostility: `aggressive_mob` / `passive_mob`.

### 3.3 Rich `base_stats` shape

Nested optional objects alongside legacy DP/attrs (required combat keys remain):

| Key       | Role                                                              |
| --------- | ----------------------------------------------------------------- |
| `catalog` | Namespace, opaque `source_key`, era, canonical/variant linkage    |
| `attacks` | List of attacks (`damage_expr`, skill, legacy min/max dual-write) |
| `armor`   | Armor points / coverage                                           |
| CoC chars | Existing optional strength/constitution/… integers                |

No new SQL column for metadata in this epic.

### 3.4 Dice and dual-write

- Shared module: `server/game/dice_expr.py` (`damage_expr_to_min_max`,
  `roll_damage_expr`).
- Generators dual-write rich fields **and** legacy ints (`determination_points`,
  `max_dp`, `xp_value`; attack min/max from the bridge).
- Combat Phase 3: roll `damage_expr` when present; else existing int paths.

### 3.5 Explicitly out of scope (this ADR / epic)

- Phase 4 browse UI
- Skills / % / SAN / AI combat consumers
- Spawn-column extraction DDL completion
- Zone bindings outside arena / dialogue / quests

## 4. Alternatives Considered

**[SPEC]**

1. **New `npc_prototypes` table** — Rejected: duplicates `npc_definitions` and
   forces spawn/lifecycle rewiring for no gain in Phases 1–3.
2. **New `metadata` JSONB column** — Rejected for this epic; nest under
   `base_stats` and revisit columnization later if query needs prove it.
3. **Live zone spawns in Phase 2** — Rejected: arena + inert keeps catalog
   loadout reviewable without world population side effects.
4. **Combat rewrite before contracts** — Rejected: same megapr risk as ADR-026.

## 5. Consequences

**[SPEC]**

### Positive

- Public contract for private catalog authors and combat Phase 3.
- Existing NPCs and combat remain valid via dual-write / int fallback.
- IP-sensitive content stays in the private submodule.

### Negative

- Dual-write is lossy until combat fully prefers dice.
- Spawn columns remain duplicated until #838.

### Neutral

- `base_stats` remains open to additional lore keys; known mechanical objects
  are validated when present.

## 6. Implementation anchors

**[SPEC]**

- JSON Schema: `schemas/npcs/npc_base_stats.schema.json`
- Pydantic models: `server/game/npcs/base_stats_models.py`
- Shared dice: `server/game/dice_expr.py`
- Catalog DML emitter: `server/game/npcs/catalog_dml.py`
- Combat damage resolve: `server/game/npcs/attack_damage.py`
- Private pipeline: `data/npc_catalog/` (Phase 2)
- Synthetic fixture: `schemas/npcs/fixtures/synthetic_rich_base_stats.json`
- Related: ADR-026 (item catalog), issues #837–#840
