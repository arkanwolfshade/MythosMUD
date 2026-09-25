# Database Architecture

**Version 1.0.0** · MythosMUD · 2026-09-16

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
This document is the single authoritative guide to how MythosMUD's Python code reaches PostgreSQL:
the two access patterns, the repository layer, connection pooling, and async/SQLAlchemy conventions.
It consolidates four previously separate guides (`DATABASE_ACCESS_PATTERNS.md`,
`PERSISTENCE_REPOSITORY_ARCHITECTURE.md`, `DATABASE_POOL_CONFIGURATION.md`,
`SQLALCHEMY_ASYNC_BEST_PRACTICES.md`) so the access-layer family has one home instead of four, each
drifting independently. Reverse-engineered from code; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md)). For the data model itself — the 45 tables,
their relationships, and how a database is provisioned — see
[`docs/packages/PACKAGE_DB_DESIGN.md`](../packages/PACKAGE_DB_DESIGN.md). Written to close
[`#745`](https://github.com/arkanwolfshade/MythosMUD/issues/745).

This is the **verb** to `PACKAGE_DB_DESIGN.md`'s **noun** — see that document's §1 for the axis this
split follows ([`docs/packages/README.md`](../packages/README.md) §1).

## 2. Access patterns

**[SPEC]**
The codebase uses two database access patterns side by side:

1. **AsyncPersistenceLayer** (async `asyncpg`) — performance-critical operations, direct database
   access, no ORM overhead.
2. **SQLAlchemy ORM** (async) — preferred for new code, relationships, complex queries.

The legacy synchronous `PersistenceLayer` (psycopg2) and SQLite have both been fully removed
(ADR-006 §3). `server/config/models/server_db.py`'s URL validator rejects any `DATABASE_URL` that
does not start with `postgresql`, with the explicit message *"SQLite is no longer supported."*

### 2.1 Pattern 1: AsyncPersistenceLayer

**[SPEC]**
**Location**: `server/async_persistence.py` (`class AsyncPersistenceLayer`)

**When to use**: performance-critical operations; async without ORM features; direct `asyncpg`
connection pool access; simple queries without relationships.

**Characteristics**:

- Raw SQL with parameterized placeholders (`$1`, `$2`, …)
- Connection pooling with configurable pool size (§4)
- Exposed as `ApplicationContainer.async_persistence`; how a service reaches it depends on whether
  the container constructs that service (see ADR-002 §3's injection-vs-service-location rule)

**Example — service constructed by a bundle (the common case)**: accept `async_persistence` as a
constructor parameter, injected at the bundle's construction site. Never reach into
`ApplicationContainer.get_instance()` from inside such a service — see
[`CONTAINER_INJECTION_AUDIT.md`](../CONTAINER_INJECTION_AUDIT.md).

```python
class MyService:
    def __init__(self, async_persistence: AsyncPersistenceLayer) -> None:
        self._async_persistence = async_persistence

    async def get_player(self, player_id: uuid.UUID) -> Player | None:
        return await self._async_persistence.get_player_by_id(player_id)


# server/container/bundles/my_bundle.py
self.my_service = MyService(async_persistence=container.async_persistence)
```

**Example — a domain entity, mixin, or free function the container does not construct** (sanctioned
service location; see ADR-002 §3):

```python
from server.container import ApplicationContainer  # server/container/ package

container = ApplicationContainer.get_instance()
async_persistence = container.async_persistence
player = await async_persistence.get_player_by_id(player_id)
```

**Limitations**: no eager loading (raw SQL), manual relationship handling, more verbose than ORM.

### 2.2 Pattern 2: SQLAlchemy ORM (async)

**[SPEC]**
**Location**: `server/database.py` (`get_async_session()`, `get_session_maker()`), `server/services/`,
`server/game/`

**When to use — preferred for all new code**: relationship access (e.g. `Player.user`), complex
joins, eager loading to prevent N+1 queries, type-safe model access.

```python
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from server.database import get_async_session
from server.models.player import Player

async for session in get_async_session():
    stmt = select(Player).options(selectinload(Player.user)).where(Player.player_id == player_id)
    result = await session.execute(stmt)
    player = result.scalar_one_or_none()
```

**Always use eager loading when accessing relationships** — lazy access from an async context
triggers an additional query per row (N+1):

```python
# Good
stmt = select(Player).options(selectinload(Player.user)).where(Player.player_id == player_id)

# Bad — player.user below triggers an additional query
stmt = select(Player).where(Player.player_id == player_id)
```

### 2.3 Decision tree

**[NOTE]**

```
Do you need relationships (e.g., Player.user)?
├─ Yes → SQLAlchemy ORM (§2.2)
└─ No  → AsyncPersistenceLayer (§2.1)
```

### 2.4 Raw SQL in async SQLAlchemy contexts

**[SPEC]**
A raw SQL string passed directly to an async `session.execute()` raises
`sqlalchemy.exc.ObjectNotExecutableError`. Wrap it with `text()`:

```python
from sqlalchemy import text

await session.execute(text("SELECT COUNT(*) FROM players WHERE level > :level"), {"level": 10})
```

Use `text()` for raw SQL and database-specific features an ORM `select()` can't express cleanly (e.g.
`ORDER BY RANDOM()`); use plain ORM `select()`/`insert()`/`update()` for everything else — prefer the
ORM path when both are viable. `make lint-sqlalchemy` (`scripts/lint_sqlalchemy_async.py`) catches raw
strings passed without `text()`, and runs in pre-commit.

## 3. The repository layer

**[SPEC]**
`server/persistence/repositories/` holds one repository class per domain, each encapsulating database
access for that domain — clear separation of concerns, testable in isolation, dependencies injected
via constructor rather than global state.

```
async_persistence.py (AsyncPersistenceLayer, the async facade / main entry point)
        │ delegates to
        ▼
server/persistence/repositories/  ──►  SQLAlchemy async  ──►  PostgreSQL (asyncpg)
        │
        └─ constructed directly by the container for services it builds (§3.2)
```

### 3.1 Repository roster

**[SPEC]**
18 repository classes exist across 21 modules (three of `player_repository.py`'s companions —
`_mappers.py`, `_room.py`, `_save.py` — are internal helper modules, not separate repositories). This
table is enforced by
`server/tests/unit/infrastructure/test_database_architecture_repository_roster.py`, symmetric to
`test_db_design_table_roster.py`'s check on `PACKAGE_DB_DESIGN.md` §5: a repository class added or
removed without a matching update here fails that test.

| Repository | Purpose | Notes |
| --- | --- | --- |
| `PlayerRepository` | Player CRUD/query — get/save/delete, batch fetch, room validation | Split across `player_repository.py` + `_mappers.py`/`_room.py`/`_save.py`; retry with exponential backoff |
| `RoomRepository` | Room lookup | In-memory cache loaded at startup; no queries after that |
| `HealthRepository` | Player HP | Atomic JSONB field updates — see §3.3 |
| `ExperienceRepository` | XP and stat fields | Atomic updates; whitelist-based field validation |
| `ProfessionRepository` | Profession catalog lookup | Simple async queries, no dependencies |
| `ContainerRepository` | Container CRUD | Wraps `container_persistence.py` via `asyncio.to_thread()` |
| `ItemRepository` | Item instance creation/existence | Wraps `item_instance_persistence.py` via `asyncio.to_thread()` |
| `ItemCatalogRepository` | Paginated `item_prototypes` catalog listing | Backed by the `list_item_prototypes_page` stored procedure |
| `EmoteRepository` | Emote/pose logging | |
| `PlayerEffectRepository` | Tick-based status effects | See [ADR-019](decisions/ADR-019-player-effects-system.md) |
| `PlayerSkillRepository`, `SkillRepository`, `SkillUseLogRepository` | Skills catalog, per-character values, use logging | |
| `PlayerSpellRepository`, `SpellRepository` | Spell catalog, per-character known spells | |
| `DialogueDefinitionRepository` | NPC dialogue trees | |
| `QuestDefinitionRepository`, `QuestInstanceRepository` | Quest definitions and per-character state | See [ADR-010](decisions/ADR-010-quest-subsystem.md) |

**[NOTE]**
The spell, skill, dialogue and quest repositories are **not exposed on `AsyncPersistenceLayer`**. They
are constructed by the container and injected directly into their services (see
`server/container/bundles/game.py` and `bundles/magic.py`) — intended wiring, not a boundary
violation; see the persistence rule in
[`BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md`](../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md).

### 3.2 Usage patterns

**[NOTE]**

**Direct usage:**

```python
from server.persistence.repositories import PlayerRepository, HealthRepository

player_repo = PlayerRepository(room_cache=async_persistence._room_cache, event_bus=event_bus)
health_repo = HealthRepository(event_bus=event_bus)

async def process_combat(attacker_id: UUID, target_id: UUID, damage: int):
    attacker = await player_repo.get_player_by_id(attacker_id)
    target = await player_repo.get_player_by_id(target_id)
    await health_repo.damage_player(target, damage, "combat")
    await player_repo.save_player(target)
```

**FastAPI dependency injection:**

```python
from fastapi import APIRouter, Depends

router = APIRouter()

async def get_player_repo():
    return PlayerRepository(room_cache=async_persistence._room_cache)

@router.get("/players/{player_id}")
async def get_player(player_id: UUID, player_repo: PlayerRepository = Depends(get_player_repo)):
    player = await player_repo.get_player_by_id(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player
```

### 3.3 Atomic updates

**[SPEC]**
`HealthRepository` and `ExperienceRepository` update a single JSONB field without loading and
rewriting the whole row, preventing lost-update races under concurrent combat/XP events:

```sql
UPDATE players
SET stats = jsonb_set(stats, '{current_health}', ...)
WHERE player_id = :player_id
```

## 4. Connection pooling

**[SPEC]**
Two pool implementations, configured in `server/config/models/server_db.py`
(`ServerDbConfig`/settings model — field names below are validated positive by
`validate_pool_config`):

| Pool | Location | Field | Default | Env var |
| --- | --- | --- | --- | --- |
| SQLAlchemy `AsyncAdaptedQueuePool` | `server/database.py` | `pool_size` | 5 | `DATABASE_POOL_SIZE` |
| | | `max_overflow` | 10 | `DATABASE_MAX_OVERFLOW` |
| | | `pool_timeout` | 30s | `DATABASE_POOL_TIMEOUT` |
| `asyncpg.Pool` | `server/async_persistence.py` | `asyncpg_pool_min_size` | 1 | `DATABASE_ASYNCPG_POOL_MIN_SIZE` |
| | | `asyncpg_pool_max_size` | 10 | `DATABASE_ASYNCPG_POOL_MAX_SIZE` |
| | | `asyncpg_command_timeout` | 60s | `DATABASE_ASYNCPG_COMMAND_TIMEOUT` |

Maximum concurrent SQLAlchemy connections is `pool_size + max_overflow` (15 at defaults). Tests use
`NullPool` (no pooling) for isolation. `pool_pre_ping=True` (default) checks connection health before
use, at the cost of a small per-checkout overhead.

**[NOTE]** Sizing is workload-dependent and not separately validated by this doc — treat any specific
"recommended production values" as guidance to re-derive from real traffic, not a fixed table to copy.
Watch for `PoolAcquireTimeoutError` (pool exhausted — too small, or connections held too long) and
rising connection-wait time as the two leading indicators.

## 5. Direction of travel

**[NOTE]**
Everything above this section is `[SPEC]` — implemented fact. This section is intentionally the
opposite: prescriptive guidance about where database access code should move, kept in `[NOTE]`/`[?]`
blocks so an AI agent reading this file under the `AI READING INSTRUCTION` above weights it
differently from implemented reality (per `docs/subsystems/README.md`'s and `docs/packages/README.md`'s
stated convention that these docs are reverse-engineered and code is the source of truth — this is the
one section of this family that is not). Every item below is sourced to something that already exists;
nothing here is invented for this pass.

| Direction | Source | Status |
| --- | --- | --- |
| SQLAlchemy ORM preferred for new database-access code over raw `asyncpg` | `DATABASE_ACCESS_PATTERNS.md` §2 (this doc's §2 predecessor) | Aspirational — no lint gate |
| Stored procedures/functions (`db/procedures/*.sql`) as the data-access boundary for SQL, not raw Python-embedded SQL | [ADR-015](decisions/ADR-015-postgresql-procedures-migration.md) | **Enforced** — `scripts/lint_raw_sql_in_python.py`, run by `make lint` and pre-commit |
| SQL style (naming, explicit joins, no `select *`, parameterized queries) | [`POSTGRESQL_CONTRIBUTOR_GUIDE.md`](../POSTGRESQL_CONTRIBUTOR_GUIDE.md) | **Enforced** — `make sqlfluff`, `make lint-sql-guardrails` / `scripts/lint_sql_guardrails.py`, pre-commit |
| Redis for distributed cache | [ADR-006](decisions/ADR-006-postgresql-primary-datastore.md) §4 | Aspirational — deferred, `RoomRepository`'s in-memory cache is the only cache today |
| `AsyncPersistenceLayer`'s remaining f-string SQL (compile-time-constant column lists, safe from injection but an anti-pattern) migrating to SQLAlchemy sessions | `DATABASE_ACCESS_PATTERNS.md` §12 (this doc's predecessor) | Aspirational — architectural change, not scheduled |

**[?]** The performance rationale for keeping two access patterns (§2) is itself unverified: the
archived `PERSISTENCE_ASYNC_MIGRATION_GUIDE.md` §10 "Benchmark Results" backing
`AsyncPersistenceLayer`'s speed advantage over the ORM are explicitly labeled **"(Estimated)"** —
never actually measured against this codebase. Whether consolidating to a single access pattern is
worth pursuing is a real open question, but it is an architecture decision (touching
`server/async_persistence.py`, every ADR-002 injection site, and the atomic-JSONB-update pattern in
§3.3) outside this document's scope to resolve — noted here rather than silently assumed settled.

## 6. References

**[SPEC]**

- [`POSTGRESQL_CONTRIBUTOR_GUIDE.md`](../POSTGRESQL_CONTRIBUTOR_GUIDE.md) — SQL style rules; not
  merged here, cited by two lint scripts' failure output by filename
- [`docs/packages/PACKAGE_DB_DESIGN.md`](../packages/PACKAGE_DB_DESIGN.md) — the data model this
  access layer reads and writes
- [ADR-005](decisions/ADR-005-repository-pattern-data-access.md),
  [ADR-006](decisions/ADR-006-postgresql-primary-datastore.md),
  [ADR-007](decisions/ADR-007-fastapi-async-await.md),
  [ADR-015](decisions/ADR-015-postgresql-procedures-migration.md)
- [`CONTAINER_INJECTION_AUDIT.md`](../CONTAINER_INJECTION_AUDIT.md) — injection-vs-service-location
  rule referenced in §2.1
- [`BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md`](../BOUNDED_CONTEXTS_AND_SERVICE_BOUNDARIES.md) —
  the persistence-ownership rule referenced in §3.1

---

*"In the restricted archives, we learn that different incantations serve different purposes. The raw
SQL rituals provide direct power, while the ORM ceremonies offer safety and convenience. Choose wisely
based on your needs, but always prefer the ORM for new work, lest you summon the N+1 query demon."*

## 7. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-09-16 | Initial version — consolidates `DATABASE_ACCESS_PATTERNS.md`, `PERSISTENCE_REPOSITORY_ARCHITECTURE.md`, `DATABASE_POOL_CONFIGURATION.md`, `SQLALCHEMY_ASYNC_BEST_PRACTICES.md`; repository roster corrected (adds `ItemCatalogRepository`, the one repository class missing from the prior doc); SQLite-era §2.4 examples replaced with PostgreSQL-accurate ones (SQLite fully removed per ADR-006); adds §5 direction-of-travel section; closes #745 |
