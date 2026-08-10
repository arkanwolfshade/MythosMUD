# Fresh Session Test Guide

> 26 nodes

## Key Concepts

- **domPurifyClient.ts** (14 connections) — `client/src/utils/domPurifyClient.ts`
- **setup.ts** (13 connections) — `client/src/test/setup.ts`
- **domPurifyClient.test.ts** (5 connections) — `client/src/utils/__tests__/domPurifyClient.test.ts`
- **resolveSanitizeWindow()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **getDomPurify()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **verifiesDomPurifySanitize()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **resolveVitestSanitizeWindow()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **sanitizeWithDomPurify()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **domPurifyTestWindow.ts** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **installDomPurifyTestWindow()** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **collectWindowCandidates()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **resetDomPurifyClientForTests()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **localStorageShim.ts** (3 connections) — `client/src/utils/localStorageShim.ts`
- **installLocalStorageShim()** (3 connections) — `client/src/utils/localStorageShim.ts`
- **INCOMING_HTML_DOMPURIFY_CONFIG** (3 connections) — `client/src/utils/security.ts`
- **createDomPurifyTestWindow()** (2 connections) — `client/src/test/domPurifyTestWindow.ts`
- **localStorageShim.test.ts** (2 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`
- **DOMPurifyInstance** (2 connections) — `client/src/utils/domPurifyClient.ts`
- **observe()** (1 connections) — `client/src/test/setup.ts`
- **unobserve()** (1 connections) — `client/src/test/setup.ts`
- **disconnect()** (1 connections) — `client/src/test/setup.ts`
- **constructor()** (1 connections) — `client/src/test/setup.ts`
- **takeRecords()** (1 connections) — `client/src/test/setup.ts`
- **defaultFetchMock** (1 connections) — `client/src/test/setup.ts`
- **INCOMING_HTML_PROBE_CONFIG** (1 connections) — `client/src/utils/domPurifyClient.ts`
- *... and 1 more nodes in this community*

## Relationships

- [Realtime Event Handlers](Realtime_Event_Handlers.md) (4 shared connections)
- [Client App State Hooks](Client_App_State_Hooks.md) (4 shared connections)
- [Logging Rotating Handlers](Logging_Rotating_Handlers.md) (1 shared connections)

## Source Files

- `client/src/test/domPurifyTestWindow.ts`
- `client/src/test/setup.ts`
- `client/src/utils/__tests__/domPurifyClient.test.ts`
- `client/src/utils/__tests__/localStorageShim.test.ts`
- `client/src/utils/domPurifyClient.ts`
- `client/src/utils/localStorageShim.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*