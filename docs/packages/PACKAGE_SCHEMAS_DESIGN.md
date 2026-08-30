# Schemas Package Design

**Version 1.0.0** · MythosMUD · 2026-08-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`server/schemas/` holds every Pydantic request/response/message schema in the server, organized
into 14 domain subdirectories plus a `shared/` cluster of base classes and cross-cutting types.
This is the wire-facing layer: what a client sends and what the server sends back, across REST,
WebSocket, and NATS. Reverse-engineered from code; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md)). Written to close
[`#739`](https://github.com/arkanwolfshade/MythosMUD/issues/739).

## 2. Members

**[SPEC]**

Every subdirectory is already a named cluster — this package is pre-organized by domain, so §2
lists the 14 domain clusters directly rather than imposing a separate grouping.

| Cluster (directory) | Purpose |
| --- | --- |
| `shared/` | `SecureBaseModel` / `ResponseBaseModel` (base.py, §3) — the security-config base classes every request/response schema is meant to inherit; `inventory_schema.py`, `target_metadata.py`, `target_resolution.py` — cross-cutting types used by multiple domains. |
| `auth/` | `UserCreate`/`UserRead`/`UserUpdate`, `InviteCreate`/`InviteRead`/`InviteUpdate` — the wire shapes for [`PACKAGE_AUTH_DESIGN.md`](PACKAGE_AUTH_DESIGN.md)'s endpoints. |
| `players/` | The largest domain cluster (8 files): character creation/selection requests, class/profession definitions, skills, stat values, effects, respawn. |
| `rooms/` | Room read/write/data shapes — three files split by read vs. write vs. internal-data concerns. |
| `realtime/` | WebSocket message envelopes, NATS message shapes, presence data — the wire contract for `server/realtime/` (documented separately, `REAL_TIME_ARCHITECTURE.md`). |
| `combat/`, `game/`, `quest/`, `dialogue/`, `containers/`, `maps/`, `calendar/`, `metrics/`, `admin/` | One file (or two, for `game/` and `containers/`/`metrics/`) each — request/response shapes scoped to that domain's endpoints. |

`__init__.py` re-exports a curated subset of each subdirectory's public schemas — not
everything; a subdirectory can define internal-only schemas its `__init__.py` doesn't surface.

## 3. Boundary contract

**[SPEC]**

**Exports.** `server/schemas/__init__.py` re-exports selected names from each domain
subdirectory — this is the intended top-level import surface (`from server.schemas import
UserCreate`, etc.). Domain-internal schemas not listed there are imported from their own module
path.

**Dependents:** every FastAPI route (request/response typing), every WebSocket/NATS message
handler in `server/realtime/`, and — per the finding below — inconsistently, `server/models/`
(§3's models↔schemas boundary, documented fully in
[`PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md)).

**The stated invariant, and where it is not held:**

`shared/base.py`'s own docstring states the intended contract explicitly: *"All models that
handle user input or API requests should inherit from [`SecureBaseModel`] to ensure consistent
security settings across the codebase"* — `extra="forbid"` (rejects unexpected fields),
`validate_assignment=True`, `str_strip_whitespace=True`, `validate_default=True`.

**[BUG]** Only 8 of 38 non-`__init__`/non-`base.py` schema files reference
`SecureBaseModel`/`ResponseBaseModel` at all; the remaining 30 subclass Pydantic's `BaseModel`
directly, with no equivalent `model_config`. This includes actual request schemas that accept
untrusted client input — e.g. `players/player_requests.py`'s `CreateCharacterRequest`,
`SelectCharacterRequest`, `RollStatsRequest`, and seven other request classes in the same file,
none of which set `extra="forbid"`. Practical effect: these schemas silently accept and discard
unrecognized extra fields in a request body rather than rejecting them, which is weaker input
validation than the package's own documented intent and inconsistent across the 38 files (some
enforce it, most don't, with no visible rule for which). Filed as
[`#755`](https://github.com/arkanwolfshade/MythosMUD/issues/755) — remediation touches 30 files'
validation behavior, out of scope for a documentation change.

## 4. Key design decisions

**[SPEC]**

- **Domain subdirectory, not schema kind, is the organizing axis.** Request and response schemas
  for the same domain live in the same file/directory (e.g. `players/player_requests.py`) rather
  than being split into parallel `requests/`/`responses/` trees — keeps a domain's full wire
  contract in one place at the cost of not being able to answer "list all request schemas" by
  directory alone.
- **`shared/` exists for exactly two reasons**: base classes (`base.py`) and genuinely
  cross-domain types (`inventory_schema.py`, `target_metadata.py`, `target_resolution.py`) used
  by more than one domain cluster. A type used by only one domain belongs in that domain's file,
  not here.

## 5. Constraints

**[SPEC]**

- New request/response schemas **should** inherit `SecureBaseModel`/`ResponseBaseModel` per
  `shared/base.py`'s stated intent — not currently enforced by lint, type-check, or test (§3's
  finding is exactly this gap).
- `__init__.py`'s re-export list must be kept in sync manually when a domain subdirectory adds a
  new schema meant for top-level import — no automation verifies this list is complete.

## 6. Developer guide

**[NOTE]**

- **Adding a new request/response schema**: place it in the matching domain subdirectory; inherit
  `SecureBaseModel` (input) or `ResponseBaseModel` (output) from `shared/base.py` rather than
  bare `BaseModel`, per the package's own stated (if inconsistently followed) convention.
- **Adding a schema used by more than one domain**: place it in `shared/`, not in whichever
  domain happened to need it first.
- **Tests**: `server/tests/unit/schemas/` mirrors this package's subdirectory layout.

## 7. Troubleshooting

**[NOTE]**

- **A request with an unexpected extra field is silently accepted instead of rejected**: check
  whether that request's schema inherits `SecureBaseModel` — per §3, most currently don't.
- **Circular import between `schemas/` and `models/`**: see
  [`PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md)'s boundary-contract section for which
  direction of import is expected.

## 8. Related docs

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the sibling reverse-engineered-doc
  family, behavioral rather than structural axis.
- [`PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md) — the domain model layer this package's
  schemas are the wire-facing counterpart to.
- [`PACKAGE_AUTH_DESIGN.md`](PACKAGE_AUTH_DESIGN.md) — consumer of `auth/`'s schemas.
- [`API_OPENAPI_SPECIFICATION.md`](../architecture/API_OPENAPI_SPECIFICATION.md) — the REST
  contract these schemas implement.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version, closes #739 |
