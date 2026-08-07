# conftest mock rationale

> 12 nodes

## Key Concepts

- **useConnectionStateMachine.ts** (8 connections) — `client/src/hooks/useConnectionStateMachine.ts`
- **useConnectionState.ts** (7 connections) — `client/src/hooks/useConnectionState.ts`
- **useConnectionState()** (4 connections) — `client/src/hooks/useConnectionState.ts`
- **connectionMachine** (4 connections) — `client/src/hooks/useConnectionStateMachine.ts`
- **ConnectionContext** (3 connections) — `client/src/hooks/useConnectionStateMachine.ts`
- **useConnectionState.test.ts** (2 connections) — `client/src/hooks/__tests__/useConnectionState.test.ts`
- **useConnectionStateMachine.test.ts** (2 connections) — `client/src/hooks/__tests__/useConnectionStateMachine.test.ts`
- **UseConnectionStateResult** (2 connections) — `client/src/hooks/useConnectionState.ts`
- **useConnectionStateMachine.test.ts** (2 connections) — `client/src/hooks/useConnectionStateMachine.test.ts`
- **ConnectionState** (1 connections) — `client/src/hooks/useConnectionStateMachine.ts`
- **ConnectionEvent** (1 connections) — `client/src/hooks/useConnectionStateMachine.ts`
- **ConnectionMachineInput** (1 connections) — `client/src/hooks/useConnectionStateMachine.ts`

## Relationships

- [roomHandlers eventHandlers calculateOccu](roomHandlers_eventHandlers_calculateOccu.md) (3 shared connections)

## Source Files

- `client/src/hooks/__tests__/useConnectionState.test.ts`
- `client/src/hooks/__tests__/useConnectionStateMachine.test.ts`
- `client/src/hooks/useConnectionState.ts`
- `client/src/hooks/useConnectionStateMachine.test.ts`
- `client/src/hooks/useConnectionStateMachine.ts`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*