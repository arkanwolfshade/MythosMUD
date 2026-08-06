# auth invites rationale

> 58 nodes

## Key Concepts

- **security.ts** (36 connections) — `client/src/utils/security.ts`
- **config.ts** (28 connections) — `client/src/utils/config.ts`
- **logoutHandler.ts** (26 connections) — `client/src/utils/logoutHandler.ts`
- **API_V1_BASE** (18 connections) — `client/src/utils/config.ts`
- **getVersionedApiBaseUrl()** (16 connections) — `client/src/utils/config.ts`
- **secureTokenStorage** (14 connections) — `client/src/utils/security.ts`
- **logoutHandler()** (12 connections) — `client/src/utils/logoutHandler.ts`
- **MapView.tsx** (10 connections) — `client/src/components/MapView.tsx`
- **SkillsPage.tsx** (9 connections) — `client/src/pages/SkillsPage.tsx`
- **App.logout.test.tsx** (8 connections) — `client/src/__tests__/App.logout.test.tsx`
- **LogoutFlow.integration.test.tsx** (8 connections) — `client/src/__tests__/LogoutFlow.integration.test.tsx`
- **CSRFProtection** (7 connections) — `client/src/utils/security.ts`
- **sendLogoutCommandToServer()** (6 connections) — `client/src/utils/logoutHandler.ts`
- **config.test.ts** (5 connections) — `client/src/utils/__tests__/config.test.ts`
- **secureTokenStorage.test.ts** (5 connections) — `client/src/utils/__tests__/secureTokenStorage.test.ts`
- **readLogoutErrorMessage()** (5 connections) — `client/src/utils/logoutHandler.ts`
- **MapView()** (4 connections) — `client/src/components/MapView.tsx`
- **startLoginGracePeriod.ts** (4 connections) — `client/src/mythosApp/startLoginGracePeriod.ts`
- **csrfProtection.test.ts** (4 connections) — `client/src/utils/__tests__/csrfProtection.test.ts`
- **logoutHandler.test.ts** (4 connections) — `client/src/utils/__tests__/logoutHandler.test.ts`
- **security.test-utils.ts** (4 connections) — `client/src/utils/__tests__/security.test-utils.ts`
- **processLogoutHttpResponse()** (4 connections) — `client/src/utils/logoutHandler.ts`
- **runLogoutServerPipeline()** (4 connections) — `client/src/utils/logoutHandler.ts`
- **.generateToken()** (4 connections) — `client/src/utils/security.ts`
- **layout.ts** (3 connections) — `client/src/constants/layout.ts`
- *... and 33 more nodes in this community*

## Relationships

- [mythosApp CharacterSelectionScreen chara](mythosApp_CharacterSelectionScreen_chara.md) (18 shared connections)
- [roomHandlers eventHandlers calculateOccu](roomHandlers_eventHandlers_calculateOccu.md) (11 shared connections)
- [map useMapEditing saveMapChanges](map_useMapEditing_saveMapChanges.md) (9 shared connections)
- [game chat moderation](game_chat_moderation.md) (9 shared connections)
- [logout command commands](logout_command_commands.md) (6 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (6 shared connections)
- [map maps useAsciiMap](map_maps_useAsciiMap.md) (5 shared connections)
- [dialogue DialogueEditorPage baseUrl()](dialogue_DialogueEditorPage_baseUrl%28%29.md) (5 shared connections)
- [App helpers professionSystemErrorHandlin](App_helpers_professionSystemErrorHandlin.md) (4 shared connections)
- [mapPageRenderer mapPageState MapPage](mapPageRenderer_mapPageState_MapPage.md) (4 shared connections)
- [persistence services combat](persistence_services_combat.md) (3 shared connections)
- [magic completion game](magic_completion_game.md) (3 shared connections)

## Source Files

- `client/src/__tests__/App.logout.test.tsx`
- `client/src/__tests__/LogoutFlow.integration.test.tsx`
- `client/src/components/MapView.tsx`
- `client/src/components/map/__tests__/MapView.test.tsx`
- `client/src/constants/layout.ts`
- `client/src/mythosApp/startLoginGracePeriod.ts`
- `client/src/pages/SkillsPage.tsx`
- `client/src/pages/__tests__/SkillsPage.test.tsx`
- `client/src/utils/__tests__/config.test.ts`
- `client/src/utils/__tests__/csrfProtection.test.ts`
- `client/src/utils/__tests__/logoutHandler.test.ts`
- `client/src/utils/__tests__/secureTokenStorage.test.ts`
- `client/src/utils/__tests__/security.test-utils.ts`
- `client/src/utils/config.ts`
- `client/src/utils/logoutHandler.ts`
- `client/src/utils/security.ts`

## Audit Trail

- EXTRACTED: 304 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*