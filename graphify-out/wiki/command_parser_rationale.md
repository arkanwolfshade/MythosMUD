# command parser rationale

> 60 nodes

## Key Concepts

- **GameInfoPanel.tsx** (17 connections) — `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
- **ansiToHtml.ts** (16 connections) — `client/src/utils/ansiToHtml.ts`
- **ansiToHtmlWithBreaks()** (15 connections) — `client/src/utils/ansiToHtml.ts`
- **SafeHtml.tsx** (14 connections) — `client/src/components/common/SafeHtml.tsx`
- **ChatMessage.tsx** (14 connections) — `client/src/components/panels/chat/ChatMessage.tsx`
- **domPurifyClient.ts** (14 connections) — `client/src/utils/domPurifyClient.ts`
- **setup.ts** (13 connections) — `client/src/test/setup.ts`
- **SafeHtml()** (11 connections) — `client/src/components/common/SafeHtml.tsx`
- **ChatMessagesList.tsx** (9 connections) — `client/src/components/panels/chat/ChatMessagesList.tsx`
- **ChatMessage()** (7 connections) — `client/src/components/panels/chat/ChatMessage.tsx`
- **ansiToHtml()** (6 connections) — `client/src/utils/ansiToHtml.ts`
- **GameInfoPanel()** (5 connections) — `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
- **domPurifyClient.test.ts** (5 connections) — `client/src/utils/__tests__/domPurifyClient.test.ts`
- **resolveSanitizeWindow()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **getDomPurify()** (5 connections) — `client/src/utils/domPurifyClient.ts`
- **localStorageShim.ts** (5 connections) — `client/src/utils/localStorageShim.ts`
- **installLocalStorageShim()** (5 connections) — `client/src/utils/localStorageShim.ts`
- **GameInfoPanel.test.tsx** (4 connections) — `client/src/components/ui-v2/panels/__tests__/GameInfoPanel.test.tsx`
- **localStorageShim.test.ts** (4 connections) — `client/src/utils/__tests__/localStorageShim.test.ts`
- **verifiesDomPurifySanitize()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **resolveVitestSanitizeWindow()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **sanitizeWithDomPurify()** (4 connections) — `client/src/utils/domPurifyClient.ts`
- **ChatMessagesList()** (3 connections) — `client/src/components/panels/chat/ChatMessagesList.tsx`
- **chatMessageVisibleInGameInfo()** (3 connections) — `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
- **domPurifyTestWindow.ts** (3 connections) — `client/src/test/domPurifyTestWindow.ts`
- *... and 35 more nodes in this community*

## Relationships

- [panels chat ChatPanelRuntimeViewParts](panels_chat_ChatPanelRuntimeViewParts.md) (15 shared connections)
- [panels chatPanelRuntimeUtils chatPanelEx](panels_chatPanelRuntimeUtils_chatPanelEx.md) (8 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (7 shared connections)
- [game terminal lucidity](game_terminal_lucidity.md) (7 shared connections)
- [panels GameClientV2Dock gameLogPanelUtil](panels_GameClientV2Dock_gameLogPanelUtil.md) (6 shared connections)
- [map maps useAsciiMap](map_maps_useAsciiMap.md) (4 shared connections)
- [panels chatPanelRefactoredDerived ChatPa](panels_chatPanelRefactoredDerived_ChatPa.md) (2 shared connections)
- [PanelContextRuntime contexts package](PanelContextRuntime_contexts_package.md) (1 shared connections)

## Source Files

- `client/src/components/common/SafeHtml.tsx`
- `client/src/components/common/__tests__/SafeHtml.test.tsx`
- `client/src/components/panels/chat/ChatMessage.tsx`
- `client/src/components/panels/chat/ChatMessagesList.tsx`
- `client/src/components/panels/chat/__tests__/ChatMessage.test.tsx`
- `client/src/components/panels/chat/__tests__/ChatMessagesList.test.tsx`
- `client/src/components/ui-v2/panels/GameInfoPanel.tsx`
- `client/src/components/ui-v2/panels/__tests__/GameInfoPanel.test.tsx`
- `client/src/test/domPurifyTestWindow.ts`
- `client/src/test/setup.ts`
- `client/src/utils/__tests__/domPurifyClient.test.ts`
- `client/src/utils/__tests__/localStorageShim.test.ts`
- `client/src/utils/ansiToHtml.test.ts`
- `client/src/utils/ansiToHtml.ts`
- `client/src/utils/domPurifyClient.ts`
- `client/src/utils/localStorageShim.ts`
- `client/src/utils/security.ts`
- `client/src/utils/testAnsi.ts`

## Audit Trail

- EXTRACTED: 256 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*