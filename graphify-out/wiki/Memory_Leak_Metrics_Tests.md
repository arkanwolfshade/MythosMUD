# Memory Leak Metrics Tests

> 31 nodes

## Key Concepts

- **debugLogger** (25 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentation.tsx** (16 connections) — `client/src/components/GameTerminalPresentation.tsx`
- **.log()** (9 connections) — `client/src/utils/debugLogger.ts`
- **debugLogger.ts** (7 connections) — `client/src/utils/debugLogger.ts`
- **.logToConsole()** (6 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentation.test.tsx** (5 connections) — `client/src/components/__tests__/GameTerminalPresentation.test.tsx`
- **.downloadLogs()** (5 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentation()** (4 connections) — `client/src/components/GameTerminalPresentation.tsx`
- **debugLogger.test.ts** (4 connections) — `client/src/utils/__tests__/debugLogger.test.ts`
- **.warn()** (4 connections) — `client/src/utils/debugLogger.ts`
- **.error()** (4 connections) — `client/src/utils/debugLogger.ts`
- **.initializeConfig()** (3 connections) — `client/src/utils/debugLogger.ts`
- **.debug()** (3 connections) — `client/src/utils/debugLogger.ts`
- **.info()** (3 connections) — `client/src/utils/debugLogger.ts`
- **GameTerminalPresentationProps** (2 connections) — `client/src/components/GameTerminalPresentation.tsx`
- **.constructor()** (2 connections) — `client/src/utils/debugLogger.ts`
- **.getDefaultLogLevel()** (2 connections) — `client/src/utils/debugLogger.ts`
- **.shouldLog()** (2 connections) — `client/src/utils/debugLogger.ts`
- **.createLogEntry()** (2 connections) — `client/src/utils/debugLogger.ts`
- **.addToBuffer()** (2 connections) — `client/src/utils/debugLogger.ts`
- **.formatMessage()** (2 connections) — `client/src/utils/debugLogger.ts`
- **.getLogsAsString()** (2 connections) — `client/src/utils/debugLogger.ts`
- **mockConsole** (1 connections) — `client/src/utils/__tests__/debugLogger.test.ts`
- **constructor()** (1 connections) — `client/src/utils/__tests__/debugLogger.test.ts`
- **LogLevel** (1 connections) — `client/src/utils/debugLogger.ts`
- *... and 6 more nodes in this community*

## Relationships

- [Combat Attack Handler](Combat_Attack_Handler.md) (4 shared connections)
- [Magic System Feature Plan](Magic_System_Feature_Plan.md) (3 shared connections)
- [Movement Monitor Tests](Movement_Monitor_Tests.md) (2 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (2 shared connections)
- [Logging Rotating Handlers](Logging_Rotating_Handlers.md) (2 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (2 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (1 shared connections)
- [Client App State Hooks](Client_App_State_Hooks.md) (1 shared connections)

## Source Files

- `client/src/components/GameTerminalPresentation.tsx`
- `client/src/components/__tests__/GameTerminalPresentation.test.tsx`
- `client/src/utils/__tests__/debugLogger.test.ts`
- `client/src/utils/debugLogger.ts`

## Audit Trail

- EXTRACTED: 123 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*