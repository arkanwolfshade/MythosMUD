# config rationale config()

> 9 nodes

## Key Concepts

- **stateManagementIntegration.test.ts** (13 connections) — `client/src/stores/__tests__/stateManagementIntegration.test.ts`
- **sessionStore.ts** (9 connections) — `client/src/stores/sessionStore.ts`
- **useSessionStore** (5 connections) — `client/src/stores/sessionStore.ts`
- **sessionStore.test.ts** (2 connections) — `client/src/stores/__tests__/sessionStore.test.ts`
- **SessionState** (1 connections) — `client/src/stores/sessionStore.ts`
- **SessionActions** (1 connections) — `client/src/stores/sessionStore.ts`
- **SessionSelectors** (1 connections) — `client/src/stores/sessionStore.ts`
- **SessionStore** (1 connections) — `client/src/stores/sessionStore.ts`
- **createInitialState()** (1 connections) — `client/src/stores/sessionStore.ts`

## Relationships

- [stores connectionStore commandStore](stores_connectionStore_commandStore.md) (4 shared connections)
- [containers stores containerStore](containers_stores_containerStore.md) (3 shared connections)
- [stateNormalization stores basic](stateNormalization_stores_basic.md) (3 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (2 shared connections)
- [health monitor realtime](health_monitor_realtime.md) (1 shared connections)
- [map useMapEditing saveMapChanges](map_useMapEditing_saveMapChanges.md) (1 shared connections)

## Source Files

- `client/src/stores/__tests__/sessionStore.test.ts`
- `client/src/stores/__tests__/stateManagementIntegration.test.ts`
- `client/src/stores/sessionStore.ts`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*