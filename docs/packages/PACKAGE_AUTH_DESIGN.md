# Auth Package Design

**Version 1.0.0** · MythosMUD · 2026-08-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`server/auth/` builds MythosMUD's authentication and registration surface on top of the
`fastapi-users` library: Argon2 password hashing, JWT issuance/validation with restart
invalidation, invite-gated registration, and the FastAPI dependency functions every protected
route uses to identify the caller. This document is reverse-engineered from code; code is the
source of truth (see [`docs/subsystems/README.md`](../subsystems/README.md) for the same posture
applied to behavioral subsystems). Written to close
[`#737`](https://github.com/arkanwolfshade/MythosMUD/issues/737).

## 2. Members

**[SPEC]**

| Cluster | Files | Purpose |
| --- | --- | --- |
| Password hashing | `argon2_utils.py` | `hash_password` / `verify_password` / `needs_rehash` — Argon2id via `create_hasher_with_params`, parameters read from `ARGON2_TIME_COST` / `ARGON2_MEMORY_COST` / `ARGON2_PARALLELISM` / `ARGON2_HASH_LENGTH` env vars. See `#89` in §4 — this is already Argon2, not the passlib migration that issue describes. |
| User identity & fastapi-users wiring | `users.py` | `UserManager` (overrides `_hash_password`/`_verify_password` to Argon2), `get_auth_backend` / `get_username_auth_backend` (JWT bearer transport + `RestartInvalidatingJWTStrategy`), the module-level `fastapi_users = FastAPIUsers[User, uuid.UUID](...)` instance, and `get_current_user` / `get_current_active_user` — the two dependency factories every other auth check builds on. |
| Authorization dependencies | `dependencies.py` | `get_current_superuser`, `get_current_verified_user`, `get_optional_current_user`, `require_invite_code` — thin `Depends()`-composable wrappers layered on `users.py`'s two base dependencies. |
| Invite lifecycle | `invites.py` | `InviteManager` (CRUD: create/list/validate/use/cleanup-expired) plus the two free functions `reserve_invite` / `capture_invite` that implement registration's reserve-then-capture transaction (§3). |
| JWT strategy | `jwt_strategy.py`, `token_epoch.py` | `RestartInvalidatingJWTStrategy.read_token` rejects any token whose `srv` claim doesn't match the current process's epoch. `token_epoch.py` holds that epoch as module-level state, set once at startup. |
| Registration/login HTTP surface | `endpoints.py` | `UserCreate`/`LoginRequest`/`LoginResponse` schemas, `register_user`, `login_user`, `get_current_user_info`, `list_invites`, `create_invite`. The route handlers themselves — everything above is infrastructure this file assembles. |
| Bogus-email generation | `email_utils.py` | `generate_unique_bogus_email` / `is_bogus_email` / `validate_bogus_email_format` — `fastapi-users` requires an email field; MythosMUD is username-first, so registration without an email synthesizes one in this reserved, recognizable format. |
| Package surface | `__init__.py` | Re-exports `get_user_manager`, `get_auth_backend`, `InviteManager`, `get_current_user`, `get_current_active_user` — the five names the rest of the server is expected to import from `server.auth` directly. |

## 3. Boundary contract

**[SPEC]**

**Exports** (via `__init__.py`, the intended import surface): `get_user_manager`,
`get_auth_backend`, `InviteManager`, `get_current_user`, `get_current_active_user`. Everything
else — `dependencies.py`'s wrappers, `endpoints.py`'s route functions, `argon2_utils.py`,
`email_utils.py`, `token_epoch.py` — is imported from its own module path by callers that need
it (route registration in `server/app/factory.py`, other services checking auth state).

**Dependents:** every FastAPI route requiring authentication, authorization, or invite
validation, across `server/api/`, `server/commands/`, and elsewhere — this package is the single
point where "who is this request" gets answered.

**Invariants a caller must not violate:**

- **What `auth/` is supposed to enforce, stated explicitly (the gap `#737` was filed to close):**
  registration requires a valid, unused invite code; passwords are hashed with Argon2id, never
  stored or compared in plaintext; a JWT is only accepted if its signature, audience, and `srv`
  (server-epoch) claim all validate against the current process.
- **Invite validation and consumption is a two-phase transaction, not a single check.**
  `reserve_invite` (AUTH phase — SQL-level row lock via `SELECT reserve_invite(:invite_code)`,
  held for the rest of the surrounding transaction) must run *before* the `User` object is
  built; `capture_invite` (CAPTURE phase) must run *after* `session.flush()` (so `user.id` is
  populated) and *before* `session.commit()`, so a capture failure rolls the user back. Both
  procedures are SQL stored procedures (`db/procedures/`, ADR-015), not Python-side locking — see
  `_persist_new_user` (`endpoints.py:221-260`) for the orchestration. Skipping either phase, or
  reordering them relative to flush/commit, reopens the class of bug `#733` fixed (see below).
- **`UserCreate.invite_code` is a required `str`, with a non-blank validator
  (`endpoints.py:87-91`).** This is the state of the fix for `#733` — *"open registration
  bypasses the invite-only requirement when `invite_code` is omitted"*, found by the `#648`
  item-4 security sweep and closed by `#749`'s atomic reserve/capture mechanism. No caller can
  construct a `UserCreate` without a non-empty invite code at the schema level; the reserve/
  capture transaction above is the second, DB-level enforcement of the same invariant.
- **JWTs carry a `srv` (server epoch) claim**, set once via `set_auth_epoch` at startup
  (`server/app/lifespan.py:198`, a fresh UUID hex per process start) and checked on every
  `read_token` call (`jwt_strategy.py:40-49`). A token issued before the last restart is rejected
  even if its signature is otherwise valid — this is what "restart invalidation" means in
  `RestartInvalidatingJWTStrategy`'s name; there is no persisted revocation list, the epoch
  mismatch *is* the revocation mechanism.
- **Two authentication backends exist** (`get_auth_backend`, email-keyed; `get_username_auth_backend`, username-keyed via `UsernameAuthenticationBackend.login`) — callers must pick the one matching their login surface; conflating them mismatches the credential fastapi-users expects.

## 4. Key design decisions

**[SPEC]**

- **Argon2id, not bcrypt or passlib.** `UserManager._hash_password`/`_verify_password`
  (`users.py:63-69`) override fastapi-users' default bcrypt-via-passlib with direct calls into
  `argon2_utils.py`. `#89` ("migrate from passlib to Argon2") is **already done** at the
  package's core; if `#89` is still open, its remaining scope is elsewhere (verify before
  closing — this doc does not adjudicate that, only records what `server/auth/` itself does).
- **Username-first identity over fastapi-users' email-first default.** fastapi-users requires an
  email; MythosMUD users log in by username. `email_utils.py`'s bogus-email generator and
  `UsernameAuthenticationBackend` both exist to bridge that mismatch rather than fork the
  library.
- **Server-epoch JWT invalidation instead of a token blocklist.** Rejects all pre-restart tokens
  in O(1) per-request comparison, at the cost of invalidating every session on every restart
  (including deploys). No partial/per-user token revocation exists in this package — not
  currently a needed feature, not a gap this doc treats as a finding.
- **Reserve/capture as a two-phase SQL transaction, not a Python-level check-then-act.** Directly
  answers the class of race `#733`'s original finding exposed: a check that isn't atomic with
  its consequence is not enforcement. Both phases delegate to stored procedures rather than
  Python-side row locking, keeping the atomicity guarantee at the database, not the application.

## 5. Constraints

**[SPEC]**

- `MAX_PASSWORD_LENGTH = 1024`, defined identically in both `argon2_utils.py` and
  `endpoints.py` (duplicated constant, not shared — a minor drift, not filed; see §4.7's
  evidence bar, recorded here as a citation rather than an issue since it carries no behavioral
  risk).
- `reserve_invite`/`capture_invite` must be called within the same `AsyncSession`/transaction as
  the user-row insert — calling them against a different session breaks the lock-holding
  guarantee they depend on.
- `set_auth_epoch` must be called exactly once, at startup, before any request is served,
  or `read_token` rejects every token as an epoch mismatch.

## 6. Developer guide

**[NOTE]**

- **Adding a new protected route**: use `Depends(get_current_active_user)` (or
  `get_current_superuser`/`get_current_verified_user` from `dependencies.py` for elevated
  checks) — do not call `fastapi_users.current_user(...)` directly outside `users.py`; that
  construction is meant to live in exactly one place.
- **Changing Argon2 parameters**: set the `ARGON2_*` env vars; `needs_rehash` detects
  parameter drift on next login and can drive a lazy rehash if one is added.
- **Tests**: `server/tests/unit/auth/` mirrors this package's module layout.

## 7. Troubleshooting

**[NOTE]**

- **All sessions invalidated after a deploy**: expected — `set_auth_epoch` runs on every
  startup, invalidating every previously issued JWT. Not a bug.
- **Registration fails with "Invalid invite code" despite the code looking valid**: check
  whether the invite was already reserved by another concurrent request — `reserve_invite`'s row
  lock means only one registration can hold a given invite at a time.
- **New protected route returns 401 unexpectedly**: confirm the JWT's `srv` claim matches the
  current process epoch, not a stale token from before the last restart.

## 8. Related docs

**[SPEC]**

- [`docs/subsystems/README.md`](../subsystems/README.md) — the sibling reverse-engineered-doc
  family, behavioral rather than structural axis.
- [ADR-020](../architecture/decisions/ADR-020-websocket-authentication-and-csrf.md) — WebSocket
  auth/CSRF specifically; narrower than this package.
- [ADR-015](../architecture/decisions/ADR-015-postgresql-procedures-migration.md) — the
  stored-procedure contract `reserve_invite`/`capture_invite` rely on.
- [`SECURITY_ENVIRONMENT_VARIABLES.md`](../SECURITY_ENVIRONMENT_VARIABLES.md) — env-driven
  security configuration, including the `ARGON2_*` knobs.

## 9. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-08-29 | Initial version, closes #737 |
