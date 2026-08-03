# command parser rationale

> 17 nodes

## Key Concepts

- **setup.ts** (13 connections) — `client/src/test/setup.ts`
- **localStorageShim.ts** (5 connections) — `client/src/utils/localStorageShim.ts`
- **installLocalStorageShim()** (5 connections) — `client/src/utils/localStorageShim.ts`
- **localStorageShim.test.ts** (4 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`
- **domPurifyTestWindow.ts** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **installDomPurifyTestWindow()** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- **createDomPurifyTestWindow()** (2 connections) — `client/src/test/domPurifyTestWindow.ts`
- **isUsableStorage()** (2 connections) — `client/src/utils/localStorageShim.ts`
- **peekExistingLocalStorage()** (2 connections) — `client/src/utils/localStorageShim.ts`
- **observe()** (1 connections) — `client/src/test/setup.ts`
- **unobserve()** (1 connections) — `client/src/test/setup.ts`
- **disconnect()** (1 connections) — `client/src/test/setup.ts`
- **constructor()** (1 connections) — `client/src/test/setup.ts`
- **takeRecords()** (1 connections) — `client/src/test/setup.ts`
- **defaultFetchMock** (1 connections) — `client/src/test/setup.ts`
- **deleteProp()** (1 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`
- **get()** (1 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (2 shared connections)
- [panels GameClientV2Dock gameLogPanelUtil](panels_GameClientV2Dock_gameLogPanelUtil.md) (1 shared connections)

## Source Files

- `client/src/test/domPurifyTestWindow.ts`
- `client/src/test/setup.ts`
- `client/src/utils/__tests__/localStorageShim.test.ts`
- `client/src/utils/localStorageShim.ts`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*