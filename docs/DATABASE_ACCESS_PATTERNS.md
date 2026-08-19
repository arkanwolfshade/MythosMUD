# Database Access Patterns

**Version 2.0.0** · MythosMUD · 2026-08-19

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[SPEC]**
**Status:** Binding
**Supersedes:** version 1.x of this document, which described two sanctioned access patterns and advised
preferring SQLAlchemy ORM for new code. **That guidance is reversed.**
**Authority:** [ADR-015](architecture/decisions/ADR-015-postgresql-procedures-migration.md)

## 2. The rule

**[SPEC]**
**All database interactions in server code occur through stored procedures and functions.**

- **Raw SQL is banned in server code, without exception.**
- **Direct `asyncpg.connect()` from services is banned.**
- **SQLAlchemy ORM is permitted only where a third-party dependency requires it**, and only at the sites
  named in §4.
- Raw SQL **is** permitted in database migration scripts — Alembic revisions, `db/`, and
  `data/db/migrations/`. Those are not server code.

## 3. The sanctioned pattern

**[SPEC]**
Call a procedure through the injected async session, with an explicit column list:

```python
result = await session.execute(
    text("SELECT player_id, name, current_dp FROM get_player_by_id(:player_id)"),
    {"player_id": player_id},
)
row = result.mappings().one_or_none()
```

- **`SELECT *` is not allowed in Python.** Column lists are explicit, so a procedure's return shape
  changing is a visible failure rather than a silent one.
- Results are consumed with `result.mappings().all()` or `.scalar()` and mapped to domain objects in
  Python.
- **Transactions stay in Python** — `await session.commit()` / `await session.rollback()`.
- Procedures live one file per domain under `db/procedures/`, applied by
  `scripts/apply_procedures.ps1`. `make build` runs `apply-procedures` first.
- Naming is `verb_entity`: `get_player_by_id`, `upsert_player`, `get_rooms_with_exits`.
- `search_path` is normalised from the database name in `server/database.py`, so procedure names are
  unqualified at the call site.

## 4. Named exceptions

**[SPEC]**
Each exception is listed individually. Anything not on this list is a violation.

| Site | Reason |
| --- | --- |
| `server/auth/users.py` — `SQLAlchemyUserDatabase` | `fastapi-users` requires it. Cannot be routed through a procedure without replacing the authentication library. |

**[NOTE]**
Adding an exception requires amending ADR-015, not just this table.

## 5. Migration status

**[SPEC]**
The codebase does not yet satisfy §2. The following are known non-conforming and are being migrated;
the `.semgrep.yml` allowlist tracks them and its end state is **zero entries** (issue #618).

| Category | Approx. sites | Notes |
| --- | --- | --- |
| Raw SQL in services, API routers, auth | ~15 | Includes `server/api/rooms.py`, `server/auth/endpoints.py`, `server/services/exploration_service.py`, `server/services/npc_service/` |
| Direct `asyncpg.connect()` in services | 4 | `emote_service`, `schedule_service`, `holiday_service`, `zone_config_loader`. In `emote_service` the underlying cause is a synchronous `__init__` calling `asyncio.new_event_loop()` (issue #624) — fix the async boundary, not the SQL string |
| SQLAlchemy ORM `select()` in first-party code | ~28 | Auth, player preferences, lucidity, death/respawn, quest paths |

**[NOTE]**
Counts are from the 2026-08 design/implementation audit and are indicative, not a tracked inventory.

## 6. Error handling

**[SPEC]**
A procedure call that raises surfaces as a SQLAlchemy exception. Wrap at the repository boundary and
translate to a domain exception; do not let driver exceptions escape into services. Transaction rollback
is explicit — see §3.

## 7. Rationale

**[NOTE]**
Query logic lives in one place, the procedure's return shape is a stated contract, integration tests can
assert against that contract, and dev/test/e2e databases receive the same procedures through the same
script. The cost is that procedure definitions must be kept in step with table schema, and type
mismatches surface at the call site until corrected in the procedure.

## 8. References

**[SPEC]**

- [ADR-015: PostgreSQL Procedures and Functions for Data Access](architecture/decisions/ADR-015-postgresql-procedures-migration.md) — the authority for this document
- [ADR-005: Repository Pattern for Data Access](architecture/decisions/ADR-005-repository-pattern-data-access.md)
- [ADR-006: PostgreSQL as Primary Datastore](architecture/decisions/ADR-006-postgresql-primary-datastore.md)
- [PERSISTENCE_REPOSITORY_ARCHITECTURE.md](PERSISTENCE_REPOSITORY_ARCHITECTURE.md)
- [SQLALCHEMY_ASYNC_BEST_PRACTICES.md](SQLALCHEMY_ASYNC_BEST_PRACTICES.md) — applies to the §4 exceptions

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
| 2.0.0 | 2026-08-19 | **Reversal.** Replaced the two-pattern model and the "prefer SQLAlchemy ORM for new code" guidance with the binding procedures-only rule from ADR-015. Removed the asyncpg `$1`-placeholder and `PLAYER_COLUMNS` f-string material, which described a mechanism no longer present in the code. Added named exceptions and the migration backlog. |
