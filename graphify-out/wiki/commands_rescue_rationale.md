# commands rescue rationale

> 49 nodes

## Key Concepts

- **config.ts** (28 connections) — `client/src/utils/config.ts`
- **deleteCharacterFlow.ts** (25 connections) — `client/src/mythosApp/deleteCharacterFlow.ts`
- **1774539086359-useMythosAppState.ts** (24 connections) — `client/src/mythosApp/1774539086359-useMythosAppState.ts`
- **creationCompleteFlow.ts** (20 connections) — `client/src/mythosApp/creationCompleteFlow.ts`
- **CharacterInfo** (20 connections) — `client/src/types/auth.ts`
- **characterSessionApi.ts** (18 connections) — `client/src/mythosApp/characterSessionApi.ts`
- **API_V1_BASE** (18 connections) — `client/src/utils/config.ts`
- **CharacterSelectionScreen.tsx** (17 connections) — `client/src/components/CharacterSelectionScreen.tsx`
- **useAuthSessionRestore.ts** (15 connections) — `client/src/mythosApp/useAuthSessionRestore.ts`
- **auth.ts** (15 connections) — `client/src/types/auth.ts`
- **runDeleteCharacterFlow()** (11 connections) — `client/src/mythosApp/deleteCharacterFlow.ts`
- **mapServerCharacters.ts** (10 connections) — `client/src/mythosApp/mapServerCharacters.ts`
- **assertServerCharacterResponseArray()** (9 connections) — `client/src/utils/apiTypeGuards.ts`
- **isServerCharacterResponse()** (8 connections) — `client/src/utils/apiTypeGuards.ts`
- **parseSelectCharacterResult()** (7 connections) — `client/src/mythosApp/characterSessionApi.ts`
- **toCharacterInfoFromList()** (7 connections) — `client/src/mythosApp/mapServerCharacters.ts`
- **useAuthSessionRestore()** (7 connections) — `client/src/mythosApp/useAuthSessionRestore.ts`
- **isServerCharacterResponseArray()** (7 connections) — `client/src/utils/apiTypeGuards.ts`
- **refreshCharactersAfterCreation()** (6 connections) — `client/src/mythosApp/creationCompleteFlow.ts`
- **stringIndicatesServerUnavailable()** (6 connections) — `client/src/mythosApp/serverAvailability.ts`
- **useReducerStateSlices()** (5 connections) — `client/src/mythosApp/1774539086359-useMythosAppState.ts`
- **restoreCharactersOnMount()** (5 connections) — `client/src/mythosApp/characterSessionApi.ts`
- **config.test.ts** (5 connections) — `client/src/utils/__tests__/config.test.ts`
- **extractErrorMessageFromResponseBody()** (4 connections) — `client/src/components/CharacterSelectionScreen.tsx`
- **fetchCharactersList()** (4 connections) — `client/src/components/CharacterSelectionScreen.tsx`
- *... and 24 more nodes in this community*

## Relationships

- [mythosApp useMythosAppState useStatsRoll](mythosApp_useMythosAppState_useStatsRoll.md) (45 shared connections)
- [mythosApp CharacterSelectionScreen chara](mythosApp_CharacterSelectionScreen_chara.md) (27 shared connections)
- [apiTypeGuards FIELDS SHARED](apiTypeGuards_FIELDS_SHARED.md) (19 shared connections)
- [zone configuration npc](zone_configuration_npc.md) (9 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (8 shared connections)
- [mythosApp appLazyScreens mythosAppViewMo](mythosApp_appLazyScreens_mythosAppViewMo.md) (7 shared connections)
- [map useMapEditing saveMapChanges](map_useMapEditing_saveMapChanges.md) (6 shared connections)
- [roomHandlers eventHandlers calculateOccu](roomHandlers_eventHandlers_calculateOccu.md) (4 shared connections)
- [memoryMonitor memoryLeakDetector constru](memoryMonitor_memoryLeakDetector_constru.md) (2 shared connections)
- [containers stores containerStore](containers_stores_containerStore.md) (2 shared connections)
- [lucidityEventUtils mythosTime MythosTime](lucidityEventUtils_mythosTime_MythosTime.md) (2 shared connections)
- [Game Terminal UI](Game_Terminal_UI.md) (2 shared connections)

## Source Files

- `client/src/components/CharacterSelectionScreen.tsx`
- `client/src/mythosApp/1774539086359-useMythosAppState.ts`
- `client/src/mythosApp/characterSessionApi.ts`
- `client/src/mythosApp/creationCompleteFlow.ts`
- `client/src/mythosApp/deleteCharacterFlow.ts`
- `client/src/mythosApp/mapServerCharacters.ts`
- `client/src/mythosApp/serverAvailability.ts`
- `client/src/mythosApp/useAuthSessionRestore.ts`
- `client/src/types/auth.ts`
- `client/src/utils/__tests__/config.test.ts`
- `client/src/utils/apiTypeGuards.ts`
- `client/src/utils/config.ts`

## Audit Trail

- EXTRACTED: 347 (98%)
- INFERRED: 7 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*