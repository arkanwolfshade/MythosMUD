# WebSocket Code Review - Branch: feature/sqlite-to-postgresql

> 30 nodes

## Key Concepts

- **domPurifyClient.ts** (14 connections) — `client/src/utils/domPurifyClient.ts`
- **setup.ts** (13 connections) — `client/src/test/setup.ts`
- **getDomPurify()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **resolveSanitizeWindow()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **installLocalStorageShim()** (5 connections) — `client/src/utils/localStorageShim.ts`
- **localStorageShim.ts** (5 connections) — `client/src/utils/localStorageShim.ts`
- **domPurifyClient.test.ts** (5 connections) — `client/src/utils/__tests__/domPurifyClient.test.ts`
- **resolveVitestSanitizeWindow()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **sanitizeWithDomPurify()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **localStorageShim.test.ts** (4 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`
- **installDomPurifyTestWindow()** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **collectWindowCandidates()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **resetDomPurifyClientForTests()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **verifiesDomPurifySanitize()** (3 connections) — `client/src/utils/domPurifyClient.ts`
- **domPurifyTestWindow.ts** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **INCOMING_HTML_DOMPURIFY_CONFIG** (3 connections) — `client/src/utils/security.ts`
- **createDomPurifyTestWindow()** (2 connections) — `client/src/test/domPurifyTestWindow.ts`
- **isUsableStorage()** (2 connections) — `client/src/utils/localStorageShim.ts`
- **peekExistingLocalStorage()** (2 connections) — `client/src/utils/localStorageShim.ts`
- **DOMPurifyInstance** (1 connections) — `client/src/utils/domPurifyClient.ts`
- **constructor()** (1 connections) — `client/src/test/setup.ts`
- **disconnect()** (1 connections) — `client/src/test/setup.ts`
- **observe()** (1 connections) — `client/src/test/setup.ts`
- **takeRecords()** (1 connections) — `client/src/test/setup.ts`
- **unobserve()** (1 connections) — `client/src/test/setup.ts`
- *... and 5 more nodes in this community*

## Relationships

- [NPCBase](NPCBase.md) (4 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (4 shared connections)
- [TestRoomDataFixer](TestRoomDataFixer.md) (1 shared connections)

## Source Files

- `client/src/test/domPurifyTestWindow.ts`
- `client/src/test/setup.ts`
- `client/src/utils/__tests__/domPurifyClient.test.ts`
- `client/src/utils/__tests__/localStorageShim.test.ts`
- `client/src/utils/domPurifyClient.ts`
- `client/src/utils/localStorageShim.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 54 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*