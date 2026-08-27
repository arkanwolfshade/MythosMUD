# 🚫 Anti-Patterns NOT Found (Good!)

> 9 nodes

## Key Concepts

- **_PlayerIdCarrier** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenPersistence** (4 connections) — `server/realtime/connection_delegates.py`
- **_TokenValidateManager** (4 connections) — `server/realtime/connection_delegates.py`
- **Protocol** (4 connections)
- **.get_player_by_user_id()** (3 connections) — `server/realtime/connection_delegates.py`
- **Minimal player shape for token validation.** (1 connections) — `server/realtime/connection_delegates.py`
- **Persistence surface used by validate_token_impl.** (1 connections) — `server/realtime/connection_delegates.py`
- **Look up a player by auth user id.** (1 connections) — `server/realtime/connection_delegates.py`
- **ConnectionManager surface used by validate_token_impl.** (1 connections) — `server/realtime/connection_delegates.py`

## Relationships

- [security.ts](security.ts.md) (4 shared connections)
- [submitAuth.ts](submitAuth.ts.md) (1 shared connections)

## Source Files

- `server/realtime/connection_delegates.py`

## Audit Trail

- EXTRACTED: 14 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*