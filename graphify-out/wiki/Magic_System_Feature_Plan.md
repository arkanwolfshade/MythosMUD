# Magic System Feature Plan

> 60 nodes

## Key Concepts

- **GameTerminal.tsx** (46 connections) — `client/src/components/GameTerminal.tsx`
- **playerHandlers.ts** (23 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **healthEventUtils.ts** (16 connections) — `client/src/utils/healthEventUtils.ts`
- **playerHandlers.test.ts** (14 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/playerHandlers.test.ts`
- **RescueStatusBanner.tsx** (9 connections) — `client/src/components/lucidity/RescueStatusBanner.tsx`
- **determineDpTier()** (9 connections) — `client/src/types/health.ts`
- **buildHealthStatusFromEvent()** (9 connections) — `client/src/utils/healthEventUtils.ts`
- **GameTerminal()** (8 connections) — `client/src/components/GameTerminal.tsx`
- **game-terminal-integration.spec.tsx** (7 connections) — `client/src/components/__tests__/game-terminal-integration.spec.tsx`
- **game-terminal-integration.test.tsx** (7 connections) — `client/src/components/__tests__/game-terminal-integration.test.tsx`
- **healthEventUtils.test.ts** (6 connections) — `client/src/utils/__tests__/healthEventUtils.test.ts`
- **IncapacitatedBanner.tsx** (5 connections) — `client/src/components/health/IncapacitatedBanner.tsx`
- **RescueStatusBanner.test.tsx** (5 connections) — `client/src/components/lucidity/__tests__/RescueStatusBanner.test.tsx`
- **DismissButton.tsx** (5 connections) — `client/src/components/ui/DismissButton.tsx`
- **GameTerminal.test.tsx** (4 connections) — `client/src/components/__tests__/GameTerminal.test.tsx`
- **DismissButton()** (4 connections) — `client/src/components/ui/DismissButton.tsx`
- **buildHealthChangeMessage()** (4 connections) — `client/src/utils/healthEventUtils.ts`
- **buildHealthStatus()** (3 connections) — `client/src/components/GameTerminal.tsx`
- **RescueStatusBanner** (3 connections) — `client/src/components/lucidity/RescueStatusBanner.tsx`
- **handlePlayerRespawned()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerUpdate()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerDpUpdated()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **readDpField()** (3 connections) — `client/src/utils/healthEventUtils.ts`
- **parseHealthEventNumbers()** (3 connections) — `client/src/utils/healthEventUtils.ts`
- **GameTerminal.test.tsx** (2 connections) — `client/src/components/GameTerminal.test.tsx`
- *... and 35 more nodes in this community*

## Relationships

- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (30 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (5 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (5 shared connections)
- [Logging Rotating Handlers](Logging_Rotating_Handlers.md) (3 shared connections)
- [Memory Leak Metrics Tests](Memory_Leak_Metrics_Tests.md) (3 shared connections)
- [Movement Monitor Tests](Movement_Monitor_Tests.md) (2 shared connections)
- [Lucidity Rate Overrides](Lucidity_Rate_Overrides.md) (2 shared connections)
- [Dependency Upgrade Report](Dependency_Upgrade_Report.md) (2 shared connections)
- [API Test Fixtures](API_Test_Fixtures.md) (2 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (2 shared connections)
- [Admin Shutdown Commands](Admin_Shutdown_Commands.md) (1 shared connections)
- [Client App State Hooks](Client_App_State_Hooks.md) (1 shared connections)

## Source Files

- `client/src/components/GameTerminal.test.tsx`
- `client/src/components/GameTerminal.tsx`
- `client/src/components/__tests__/GameTerminal.test.tsx`
- `client/src/components/__tests__/game-terminal-integration.spec.tsx`
- `client/src/components/__tests__/game-terminal-integration.test.tsx`
- `client/src/components/health/IncapacitatedBanner.tsx`
- `client/src/components/lucidity/RescueStatusBanner.tsx`
- `client/src/components/lucidity/__tests__/RescueStatusBanner.test.tsx`
- `client/src/components/ui-v2/eventHandlers/__tests__/playerHandlers.test.ts`
- `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- `client/src/components/ui/DismissButton.tsx`
- `client/src/types/__tests__/health.test.ts`
- `client/src/types/health.ts`
- `client/src/utils/__tests__/healthEventUtils.test.ts`
- `client/src/utils/healthEventUtils.ts`

## Audit Trail

- EXTRACTED: 257 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*