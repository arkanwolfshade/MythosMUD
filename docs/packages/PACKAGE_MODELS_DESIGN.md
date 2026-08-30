# Models Package Design

**Version 1.1.0** · MythosMUD · 2026-08-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`server/models/` is the persistence-layer entity definitions: SQLAlchemy ORM classes for every
database-backed domain object (players, rooms, items, NPCs, quests, spells, etc.), plus a
distinct cluster of Pydantic command-parsing models. There is no separate "domain model" package
in the DDD sense — see §3, this is a load-bearing fact for anyone reasoning about where core game
logic types actually live. Reverse-engineered from code; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md)). Written to close
[`#738`](https://github.com/arkanwolfshade/MythosMUD/issues/738).

## 2. Members

**[SPEC]**

| Cluster | Files | Purpose |
| --- | --- | --- |
| Shared base | `base.py` | `Base(DeclarativeBase)` — the single shared SQLAlchemy declarative base every ORM model must inherit, so relationship string-references resolve across the whole model graph. `__init__.py`'s docstring calls this out as load-bearing: a model using its own base breaks cross-model relationship resolution. |
| Player domain | `player.py`, `player_effect.py`, `player_skill.py`, `player_spells.py` | The player entity and its owned sub-tables: active effects, learned skills, known spells. |
| Character build | `profession.py`, `skill.py`, `skill_use_log.py` | Profession/occupation definitions, the skill catalog, and skill-use audit logging. |
| Combat & status | `combat.py`, `health.py`, `lucidity.py` | Combat-related persisted state, health/DP response shapes, lucidity tiers/cooldowns/exposure. |
| World | `room.py`, `world.py`, `calendar.py` | Room entities, world-level state, the in-game calendar (holidays, NPC schedules). |
| Items & containers | `item.py`, `container.py` | `ItemPrototype`/`ItemInstance`/`ItemComponentState` (the prototype/instance split), container component/lock-state/source-type enums. |
| NPC & dialogue | `npc.py`, `dialogue.py` | NPC entity definitions, dialogue tree persistence. |
| Social | `alias.py`, `emote.py` | Player command aliases, emote/emote-alias definitions. |
| Magic | `spell.py`, `spell_db.py` | Spell definitions split between an in-memory/catalog representation (`spell.py`) and the DB-persisted form (`spell_db.py`). |
| Identity & access | `user.py`, `invite.py` | The `User` model (fastapi-users' persisted shape — see [`PACKAGE_AUTH_DESIGN.md`](PACKAGE_AUTH_DESIGN.md)), the `Invite` model backing `server/auth/invites.py`. |
| Progression | `quest.py` | Quest definitions and player quest-progress persistence. |
| Command models | `command.py`, `command_base.py`, `command_admin.py`, `command_alias.py`, `command_channel.py`, `command_combat.py`, `command_communication.py`, `command_exploration.py`, `command_follow.py`, `command_inventory.py`, `command_magic.py`, `command_moderation.py`, `command_party.py`, `command_player_state.py`, `command_utility.py` | A structurally distinct cluster (14 files, ~1,430 lines, nearly a quarter of the package): Pydantic `BaseModel` command-parsing DTOs, one file per command category, plus `command_base.py`'s shared `Direction` enum and base classes. These are not SQLAlchemy models — see §3. |
| Package surface | `game.py`, `__init__.py` | `game.py` holds `AttributeType`/`Stats`/`StatusEffect`/`StatusEffectType` — cross-cutting game-mechanics types re-exported alongside everything else. `__init__.py` re-exports the full public surface of nearly every module above. |

## 3. Boundary contract

**[SPEC]**

**Exports.** `server/models/__init__.py` re-exports essentially the entire package — unlike
`schemas/`'s curated subset, this package's `__init__.py` is close to a flat namespace of
everything defined here.

**Dependents:** `server/persistence/` (documented in `PERSISTENCE_REPOSITORY_ARCHITECTURE.md`)
reads/writes these ORM entities; `server/schemas/` and `server/services/` both import specific
model classes; the command dispatcher (`server/command_handler_unified.py` and
`server/commands/`) consumes the command-model cluster.

**The three-way line — `models/` vs `schemas/` vs `domain/`, drawn explicitly:**

- **`server/models/`** (this package) — SQLAlchemy ORM entities, the actual persisted shape of
  game data. Every non-command-model file here subclasses `base.py`'s shared `Base`.
- **`server/schemas/`** ([documented separately](PACKAGE_SCHEMAS_DESIGN.md)) — Pydantic
  request/response/message DTOs, the wire-facing shape. The dependency runs one way:
  `server/models/` never imports from `server/schemas/` (zero hits by search), but four schema
  files do import from `models/` directly — `combat/combat_schema.py`, `game/weapon.py`,
  `players/player.py`, `rooms/room_write.py` — rather than going through a service/route-handler
  translation layer. Not treated as a finding: a schema referencing a model type it wraps or
  extends is a narrower coupling than the reverse would be, and each of the four is a plausible
  case of a response schema needing the persisted entity's shape directly.
- **`server/domain/`** — **removed.** It was a separate, declared-but-empty hexagonal-architecture
  scaffold (*"entities/, value_objects/, services/, events/, repositories/, exceptions/"*), all
  six subpackages holding only an `__init__.py` with `__all__ = []` — 208 lines total, zero
  entities, and zero references anywhere in the tree outside its own docstring examples. Deleted
  by the `#757` architecture-review remediation; ADR-001 was amended in the same pass to state
  explicitly that its Domain Layer means `server/models/` (this package) + `server/events/`. This
  entry stays as a pointer for anyone who finds `server/domain/` referenced in history or in an
  older doc.

**Invariants a caller must not violate:**

- Every SQLAlchemy-backed model must inherit `base.py`'s shared `Base`, never define its own
  `DeclarativeBase` — `base.py`'s docstring states this is what makes cross-model string-reference
  relationships resolvable at all.
- The command-model cluster is Pydantic, not SQLAlchemy — do not add `Base`/table-mapping
  concerns to `command_*.py` files; they parse commands, they do not persist.

## 4. Key design decisions

**[SPEC]**

- **One shared `Base`, not per-domain bases.** A single `DeclarativeBase` instance for the whole
  model graph, specifically to keep SQLAlchemy's string-reference relationship resolution working
  — the alternative (per-file or per-domain bases) is called out in `base.py`'s own docstring as
  the failure mode this avoids.
- **Prototype/instance split for items** (`ItemPrototype` vs `ItemInstance` in `item.py`) —
  shared template data separated from per-instance state, avoiding duplication of static item
  definitions across every spawned instance.
- **Command models live beside domain models, not in `schemas/`.** A plausible alternative
  design would fold `command_*.py` into `schemas/` (both are Pydantic DTOs with no persistence
  role) — the current split keeps command-parsing next to the game-mechanics types many command
  models reference (`Direction`, stat/effect types in `game.py`), at the cost of `models/`
  containing two structurally different kinds of "model" under one package name.

## 5. Constraints

**[SPEC]**

- Any new ORM entity must subclass `base.py`'s `Base`.
- `__init__.py`'s re-export surface should stay in sync when a module's public classes change —
  no automated check verifies completeness (same gap noted in
  [`PACKAGE_SCHEMAS_DESIGN.md`](PACKAGE_SCHEMAS_DESIGN.md)'s `__init__.py`).

## 6. Developer guide

**[NOTE]**

- **Adding a new persisted entity**: create it here, inheriting `base.py`'s `Base`; add its
  corresponding Pydantic wire schema to `server/schemas/`, not to this package.
- **Adding a new command type**: add a `command_<category>.py` file (or extend an existing one)
  following the pattern of the 14 current command-model files; inherit from `command_base.py`'s
  shared base/enums where applicable.
- **Tests**: `server/tests/unit/models/` mirrors this package's module layout.

## 7. Troubleshooting

**[NOTE]**

- **"failed to locate a name" SQLAlchemy relationship error**: almost always means a model
  somewhere is not inheriting the shared `base.py` `Base` — `base.py`'s own docstring names this
  exact symptom.
- **Confusion about where a DTO "should" live** (`models/` vs `schemas/`): if it's persisted via
  SQLAlchemy, it belongs in `models/`; if it's a request/response/message wire shape, it belongs
  in `schemas/`. If it's a command-parsing shape, it belongs in `models/`'s command-model cluster
  by existing convention, not `schemas/`.

## 8. Related docs

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the sibling reverse-engineered-doc
  family, behavioral rather than structural axis.
- [`PACKAGE_SCHEMAS_DESIGN.md`](PACKAGE_SCHEMAS_DESIGN.md) — the wire-facing counterpart to this
  package's persisted entities.
- [`PERSISTENCE_REPOSITORY_ARCHITECTURE.md`](../PERSISTENCE_REPOSITORY_ARCHITECTURE.md) — how
  these entities are read and written.
- [`PACKAGE_AUTH_DESIGN.md`](PACKAGE_AUTH_DESIGN.md) — consumer of `user.py`/`invite.py`.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version, closes #738 |
| 1.1.0 | 2026-08-30 | Record `server/domain/`'s removal per #757 |
