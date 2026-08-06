# realtime dead letter

> 11 nodes

## Key Concepts

- **commandStore.ts** (12 connections) — `client/src/stores/commandStore.ts`
- **useCommandStore** (5 connections) — `client/src/stores/commandStore.ts`
- **commandStore.test.ts** (2 connections) — `client/src/stores/__tests__/commandStore.test.ts`
- **CommandHistoryEntry** (1 connections) — `client/src/stores/commandStore.ts`
- **CommandAlias** (1 connections) — `client/src/stores/commandStore.ts`
- **CommandTrigger** (1 connections) — `client/src/stores/commandStore.ts`
- **CommandState** (1 connections) — `client/src/stores/commandStore.ts`
- **CommandActions** (1 connections) — `client/src/stores/commandStore.ts`
- **CommandSelectors** (1 connections) — `client/src/stores/commandStore.ts`
- **CommandStore** (1 connections) — `client/src/stores/commandStore.ts`
- **createInitialState()** (1 connections) — `client/src/stores/commandStore.ts`

## Relationships

- [stores connectionStore commandStore](stores_connectionStore_commandStore.md) (3 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (2 shared connections)

## Source Files

- `client/src/stores/__tests__/commandStore.test.ts`
- `client/src/stores/commandStore.ts`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*