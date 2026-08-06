# auth invites rationale

> 18 nodes

## Key Concepts

- **logoutHandler.ts** (26 connections) — `client/src/utils/logoutHandler.ts`
- **logoutHandler()** (12 connections) — `client/src/utils/logoutHandler.ts`
- **sendLogoutCommandToServer()** (6 connections) — `client/src/utils/logoutHandler.ts`
- **readLogoutErrorMessage()** (5 connections) — `client/src/utils/logoutHandler.ts`
- **logoutHandler.test.ts** (4 connections) — `client/src/utils/__tests__/logoutHandler.test.ts`
- **processLogoutHttpResponse()** (4 connections) — `client/src/utils/logoutHandler.ts`
- **runLogoutServerPipeline()** (4 connections) — `client/src/utils/logoutHandler.ts`
- **asRecordUnknown()** (3 connections) — `client/src/utils/logoutHandler.ts`
- **logSuccessfulLogoutResponse()** (3 connections) — `client/src/utils/logoutHandler.ts`
- **performClientSideCleanup()** (3 connections) — `client/src/utils/logoutHandler.ts`
- **createLogoutHandler()** (3 connections) — `client/src/utils/logoutHandler.ts`
- **nestedErrorMessage()** (2 connections) — `client/src/utils/logoutHandler.ts`
- **stringDetail()** (2 connections) — `client/src/utils/logoutHandler.ts`
- **logServerLogoutCommandError()** (2 connections) — `client/src/utils/logoutHandler.ts`
- **createLogoutAbortTimer()** (2 connections) — `client/src/utils/logoutHandler.ts`
- **postLogoutCommandRequest()** (2 connections) — `client/src/utils/logoutHandler.ts`
- **fetchSpy** (1 connections) — `client/src/utils/__tests__/logoutHandler.test.ts`
- **LogoutHandlerOptions** (1 connections) — `client/src/utils/logoutHandler.ts`

## Relationships

- [mythosApp CharacterSelectionScreen chara](mythosApp_CharacterSelectionScreen_chara.md) (7 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (4 shared connections)
- [roomHandlers eventHandlers calculateOccu](roomHandlers_eventHandlers_calculateOccu.md) (3 shared connections)
- [App helpers professionSystemErrorHandlin](App_helpers_professionSystemErrorHandlin.md) (2 shared connections)
- [eventHandlers messageHandlers statusPars](eventHandlers_messageHandlers_statusPars.md) (2 shared connections)
- [map maps useAsciiMap](map_maps_useAsciiMap.md) (1 shared connections)

## Source Files

- `client/src/utils/__tests__/logoutHandler.test.ts`
- `client/src/utils/logoutHandler.ts`

## Audit Trail

- EXTRACTED: 82 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*