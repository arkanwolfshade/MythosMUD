# SessionManager

> 13 nodes

## Key Concepts

- **SessionManager** (12 connections) — `client/src/utils/security.ts`
- **.cleanupExpiredSessions()** (3 connections) — `client/src/utils/security.ts`
- **.startCleanupInterval()** (3 connections) — `client/src/utils/security.ts`
- **sessionManager.test.ts** (3 connections) — `client/src/utils/__tests__/sessionManager.test.ts`
- **.constructor()** (2 connections) — `client/src/utils/security.ts`
- **.createSession()** (2 connections) — `client/src/utils/security.ts`
- **.expireSession()** (2 connections) — `client/src/utils/security.ts`
- **.generateSessionId()** (2 connections) — `client/src/utils/security.ts`
- **SessionManagerTestHooks** (1 connections) — `client/src/utils/__tests__/sessionManager.test.ts`
- **.destroy()** (1 connections) — `client/src/utils/security.ts`
- **.isSessionValid()** (1 connections) — `client/src/utils/security.ts`
- **.refreshSession()** (1 connections) — `client/src/utils/security.ts`
- **.removeSession()** (1 connections) — `client/src/utils/security.ts`

## Relationships

- [security.ts](security.ts.md) (2 shared connections)

## Source Files

- `client/src/utils/__tests__/sessionManager.test.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*