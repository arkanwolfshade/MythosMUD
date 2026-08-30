# Server & Client Package Documentation Coverage

**Version 1.0.0** · MythosMUD · 2026-08-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
This directory holds design documents whose primary subject is a **package** — what lives in it,
how its members relate, what it exports, and what invariants callers must not violate — as
distinct from [`docs/subsystems/`](../subsystems/README.md), whose documents describe a
**behavior** (what happens when a player does X) that may span several packages. Both families
are reverse-engineered from code; code is the source of truth in both.

This index promotes the `#648` item 2 code-to-documentation coverage sweep's result from a
one-time issue-comment finding into a maintained artifact, so the next such sweep is a table read
rather than a re-derivation.

## 2. Index

**[SPEC]**

**Discriminator** (the sweep's own, reproduced verbatim so a future reader can apply it
consistently): **Documented** — the package is the primary subject of an ADR, a
`docs/architecture/*.md` doc, another `docs/`-corpus guide, or (as of this pass) a
`docs/packages/*.md` doc — not merely mentioned in passing. **Provisional** — covered only by a
`docs/subsystems/*.md` doc (reverse-engineered from code — a record exists but is unverified,
never certifiable as conformance). **Undocumented** — neither.

### Documented (16)

| Package | Document(s) |
| --- | --- |
| `server/realtime/` | [`REAL_TIME_ARCHITECTURE.md`](../REAL_TIME_ARCHITECTURE.md), [`CONNECTION_MANAGER_ARCHITECTURE.md`](../CONNECTION_MANAGER_ARCHITECTURE.md) |
| `server/commands/` + `server/command_handler/` | [`COMMAND_HANDLER_PATTERNS.md`](../COMMAND_HANDLER_PATTERNS.md), [`COMMAND_MODELS_REFERENCE.md`](../COMMAND_MODELS_REFERENCE.md), [`COMMAND_SECURITY_GUIDE.md`](../COMMAND_SECURITY_GUIDE.md), [`COMMAND_TESTING_GUIDE.md`](../COMMAND_TESTING_GUIDE.md), [`PLAYER_COMMAND_DEVELOPER_GUIDE.md`](../PLAYER_COMMAND_DEVELOPER_GUIDE.md) |
| `server/api/` | [`API_OPENAPI_SPECIFICATION.md`](../architecture/API_OPENAPI_SPECIFICATION.md) |
| `server/persistence/` | [`PERSISTENCE_REPOSITORY_ARCHITECTURE.md`](../PERSISTENCE_REPOSITORY_ARCHITECTURE.md), [`DATABASE_ACCESS_PATTERNS.md`](../DATABASE_ACCESS_PATTERNS.md), [`PERSISTENCE_ASYNC_MIGRATION_GUIDE.md`](../PERSISTENCE_ASYNC_MIGRATION_GUIDE.md) |
| `server/structured_logging/` | [`LOGGING_BEST_PRACTICES.md`](../LOGGING_BEST_PRACTICES.md), [`LOGGING_QUICK_REFERENCE.md`](../LOGGING_QUICK_REFERENCE.md), [`ENHANCED_LOGGING_GUIDE.md`](../ENHANCED_LOGGING_GUIDE.md), [`ERROR_LOGGING_IMPLEMENTATION_GUIDE.md`](../ERROR_LOGGING_IMPLEMENTATION_GUIDE.md), [`PRE_COMMIT_LOGGING_VALIDATION.md`](../PRE_COMMIT_LOGGING_VALIDATION.md) |
| `server/container/` | [`CONTAINER_SYSTEM_ARCHITECTURE.md`](../CONTAINER_SYSTEM_ARCHITECTURE.md), [`CONTAINER_SYSTEM_API_REFERENCE.md`](../CONTAINER_SYSTEM_API_REFERENCE.md), [`CONTAINER_INJECTION_AUDIT.md`](../CONTAINER_INJECTION_AUDIT.md), [ADR-002](../architecture/decisions/ADR-002-application-container-dependency-injection.md) |
| `server/config/` | [`CONFIGURATION_FILES_REFERENCE.md`](../CONFIGURATION_FILES_REFERENCE.md), [`SECURITY_ENVIRONMENT_VARIABLES.md`](../SECURITY_ENVIRONMENT_VARIABLES.md), [ADR-013](../architecture/decisions/ADR-013-pydantic-configuration.md) |
| `server/events/` | [`EVENT_OWNERSHIP_MATRIX.md`](../EVENT_OWNERSHIP_MATRIX.md), [`EVENT_SUBSCRIPTION_CLEANUP_PATTERNS.md`](../EVENT_SUBSCRIPTION_CLEANUP_PATTERNS.md), [ADR-001](../architecture/decisions/ADR-001-layered-architecture-event-driven.md), [ADR-003](../architecture/decisions/ADR-003-dual-event-systems-eventbus-nats.md) |
| `client/src/components/ui-v2/` | [ADR-022](../architecture/decisions/ADR-022-ui-v2-client-transition.md) |
| `db/procedures/` | [ADR-015](../architecture/decisions/ADR-015-postgresql-procedures-migration.md) |
| `server/middleware/` | [`PACKAGE_MIDDLEWARE_DESIGN.md`](PACKAGE_MIDDLEWARE_DESIGN.md) *(new, this pass)* |
| `server/auth/` | [`PACKAGE_AUTH_DESIGN.md`](PACKAGE_AUTH_DESIGN.md) *(new, this pass)* |
| `server/app/` | [`PACKAGE_APP_DESIGN.md`](PACKAGE_APP_DESIGN.md) *(new, this pass)* |
| `server/schemas/` | [`PACKAGE_SCHEMAS_DESIGN.md`](PACKAGE_SCHEMAS_DESIGN.md) *(new, this pass)* |
| `server/models/` | [`PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md) *(new, this pass)* |
| `server/services/` | [`PACKAGE_SERVICES_DESIGN.md`](PACKAGE_SERVICES_DESIGN.md) *(new, this pass)* |

### Provisional (2)

| Package | Document(s) |
| --- | --- |
| `server/game/` | `docs/subsystems/*` coverage only |
| `server/npc/` | `docs/subsystems/*` coverage only |

### Undocumented (26)

Each cites the issue that owns writing its documentation.

| Package | Owning issue |
| --- | --- |
| `client/src/mythosApp/` | [`#742`](https://github.com/arkanwolfshade/MythosMUD/issues/742) |
| `client/src/components/map/` | [`#743`](https://github.com/arkanwolfshade/MythosMUD/issues/743) |
| `client/src/components/ui/` (legacy) | [`#744`](https://github.com/arkanwolfshade/MythosMUD/issues/744) |
| `db/` root DDL files | [`#745`](https://github.com/arkanwolfshade/MythosMUD/issues/745) |
| `server/utils/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `server/domain/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) — see [`PACKAGE_MODELS_DESIGN.md`](PACKAGE_MODELS_DESIGN.md)'s boundary contract for a directly relevant fact: this package is currently empty scaffolding. |
| `server/monitoring/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `server/validators/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `server/time/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `server/` root loose files | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/utils/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/hooks/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/contexts/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/stores/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/pages/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/types/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/api/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/config/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/constants/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/theme/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/` root loose files | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/components/` root loose files | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/components/common/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/components/health/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/components/lucidity/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |
| `client/src/components/magic/` | [`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) |

**Reconciliation:** 16 Documented + 2 Provisional + 26 Undocumented = 44, matching the `#648`
item 2 sweep's original inventory exactly (10 Documented + 2 Provisional + 32 Undocumented at
that time; six of the 32 flipped to Documented in this pass, none unaccounted).

## 3. Related documentation

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the behavioral-axis sibling family.
- `#648` item 2 (code-to-documentation coverage sweep) — the issue comment this index's original
  44-row inventory and discriminator were recovered from.

## 4. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version — promotes the `#648` item 2 sweep result to a maintained index; six `server/` packages flip to Documented, closing `#736`–`#741` |
