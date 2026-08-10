# Memory Leak Metrics Tests

> 51 nodes

## Key Concepts

- **debugLogger** (25 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentation.tsx** (16 connections) — `client/src/components/GameTerminalPresentation.tsx`
- **ChatPanel()** (11 connections) — `client/src/components/panels/ChatPanelRuntime.tsx`
- **ChatPanel.tsx** (9 connections) — `client/src/components/panels/ChatPanel.tsx`
- **chat-panel.spec.tsx** (9 connections) — `client/src/components/panels/__tests__/chat-panel.spec.tsx`
- **.log()** (9 connections) — `client/src/utils/debugLogger.ts`
- **ChatPanel.test.tsx** (7 connections) — `client/src/components/__tests__/ChatPanel.test.tsx`
- **chat-panel.test.tsx** (7 connections) — `client/src/components/panels/__tests__/chat-panel.test.tsx`
- **debugLogger.ts** (7 connections) — `client/src/utils/debugLogger.ts`
- **ChatPanel.edgeCases.test.tsx** (6 connections) — `client/src/components/__tests__/ChatPanel.edgeCases.test.tsx`
- **.logToConsole()** (6 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentation.test.tsx** (5 connections) — `client/src/components/__tests__/GameTerminalPresentation.test.tsx`
- **chatPanelTestHelpers.ts** (5 connections) — `client/src/components/__tests__/chatPanelTestHelpers.ts`
- **.downloadLogs()** (5 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentation()** (4 connections) — `client/src/components/GameTerminalPresentation.tsx`
- **debugLogger.test.ts** (4 connections) — `client/src/utils/__tests__/debugLogger.test.ts`
- **.warn()** (4 connections) — `client/src/utils/debugLogger.ts`
- **.error()** (4 connections) — `client/src/utils/debugLogger.ts`
- **createChatPanelDefaultProps()** (3 connections) — `client/src/components/__tests__/chatPanelTestHelpers.ts`
- **chatPanelTestSetup.tsx** (3 connections) — `client/src/components/__tests__/chatPanelTestSetup.tsx`
- **mockConsoleLog** (3 connections) — `client/src/components/__tests__/chatPanelTestSetup.tsx`
- **ChatPanelCore.tsx** (3 connections) — `client/src/components/panels/ChatPanelCore.tsx`
- **.initializeConfig()** (3 connections) — `client/src/utils/debugLogger.ts`
- **.debug()** (3 connections) — `client/src/utils/debugLogger.ts`
- **.info()** (3 connections) — `client/src/utils/debugLogger.ts`
- *... and 26 more nodes in this community*

## Relationships

- [Combat Attack Handler](Combat_Attack_Handler.md) (5 shared connections)
- [Logging Rotating Handlers](Logging_Rotating_Handlers.md) (5 shared connections)
- [Draggable Panel UI](Draggable_Panel_UI.md) (5 shared connections)
- [Client App State Hooks](Client_App_State_Hooks.md) (3 shared connections)
- [Movement Monitor Tests](Movement_Monitor_Tests.md) (2 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (2 shared connections)
- [Argon2 Security Review](Argon2_Security_Review.md) (2 shared connections)
- [Command Input Validator](Command_Input_Validator.md) (2 shared connections)
- [NPC Combat Rewards Tests](NPC_Combat_Rewards_Tests.md) (2 shared connections)
- [NPC Combat Integration](NPC_Combat_Integration.md) (1 shared connections)

## Source Files

- `client/src/components/GameTerminalPresentation.tsx`
- `client/src/components/__tests__/ChatPanel.edgeCases.test.tsx`
- `client/src/components/__tests__/ChatPanel.test.tsx`
- `client/src/components/__tests__/GameTerminalPresentation.test.tsx`
- `client/src/components/__tests__/chatPanelTestHelpers.ts`
- `client/src/components/__tests__/chatPanelTestSetup.tsx`
- `client/src/components/panels/ChatPanel.tsx`
- `client/src/components/panels/ChatPanelCore.tsx`
- `client/src/components/panels/ChatPanelRuntime.tsx`
- `client/src/components/panels/__tests__/chat-panel.spec.tsx`
- `client/src/components/panels/__tests__/chat-panel.test.tsx`
- `client/src/utils/__tests__/debugLogger.test.ts`
- `client/src/utils/debugLogger.ts`

## Audit Trail

- EXTRACTED: 199 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*