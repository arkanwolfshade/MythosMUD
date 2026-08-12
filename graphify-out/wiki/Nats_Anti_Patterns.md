# Nats Anti Patterns

> 14 nodes

## Key Concepts

- **useMythosAppState.ts** (32 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **useReducerStateSlices()** (6 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **useMythosAppState.test.ts** (3 connections) — `client/src/mythosApp/__tests__/useMythosAppState.test.ts`
- **resolveNextState()** (3 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **makeAuthSetter()** (3 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **makeCreationSetter()** (3 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **useAuthSliceSetters()** (3 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **useCreationSliceSetters()** (3 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **authSliceReducer()** (2 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **creationSliceReducer()** (2 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **hoisted** (1 connections) — `client/src/mythosApp/__tests__/useMythosAppState.test.ts`
- **PendingSkillsPayload** (1 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **INITIAL_AUTH_SLICE** (1 connections) — `client/src/mythosApp/useMythosAppState.ts`
- **INITIAL_CREATION_SLICE** (1 connections) — `client/src/mythosApp/useMythosAppState.ts`

## Relationships

- [Warning Remediation Plan](Warning_Remediation_Plan.md) (7 shared connections)
- [Communication Command Classes](Communication_Command_Classes.md) (6 shared connections)
- [WebSocket Player Helpers](WebSocket_Player_Helpers.md) (3 shared connections)
- [Realtime Event Handlers](Realtime_Event_Handlers.md) (2 shared connections)
- [Chat Panel Separation](Chat_Panel_Separation.md) (2 shared connections)
- [Active Lucidity Service](Active_Lucidity_Service.md) (2 shared connections)

## Source Files

- `client/src/mythosApp/__tests__/useMythosAppState.test.ts`
- `client/src/mythosApp/useMythosAppState.ts`

## Audit Trail

- EXTRACTED: 60 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*