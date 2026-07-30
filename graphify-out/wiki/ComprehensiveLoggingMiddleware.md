# ComprehensiveLoggingMiddleware

> 13 nodes

## Key Concepts

- **SessionManager** (12 connections) — `client/src/utils/security.ts`
- **sessionManager.test.ts** (3 connections) — `client/src/utils/__tests__/sessionManager.test.ts`
- **.cleanupExpiredSessions()** (3 connections) — `client/src/utils/security.ts`
- **.startCleanupInterval()** (3 connections) — `client/src/utils/security.ts`
- **.constructor()** (2 connections) — `client/src/utils/security.ts`
- **.createSession()** (2 connections) — `client/src/utils/security.ts`
- **.expireSession()** (2 connections) — `client/src/utils/security.ts`
- **.generateSessionId()** (2 connections) — `client/src/utils/security.ts`
- **SessionManagerTestHooks** (1 connections) — `client/src/utils/__tests__/sessionManager.test.ts`
- **.isSessionValid()** (1 connections) — `client/src/utils/security.ts`
- **.refreshSession()** (1 connections) — `client/src/utils/security.ts`
- **.removeSession()** (1 connections) — `client/src/utils/security.ts`
- **.destroy()** (1 connections) — `client/src/utils/security.ts`

## Relationships

- [fetchSpy](fetchSpy.md) (2 shared connections)

## Source Files

- `client/src/utils/__tests__/sessionManager.test.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*