# command factories communication

> 112 nodes

## Key Concepts

- **GameClientV2.tsx** (52 connections) — `client/src/components/ui-v2/GameClientV2.tsx`
- **Room** (36 connections) — `client/src/components/ui-v2/types.ts`
- **Player** (32 connections) — `client/src/components/ui-v2/types.ts`
- **ChatMessage** (32 connections) — `client/src/components/ui-v2/types.ts`
- **GameClientV2AuxiliaryPanels.tsx** (29 connections) — `client/src/components/ui-v2/GameClientV2AuxiliaryPanels.tsx`
- **lucidity.ts** (29 connections) — `client/src/types/lucidity.ts`
- **health.ts** (26 connections) — `client/src/types/health.ts`
- **LucidityStatus** (26 connections) — `client/src/types/lucidity.ts`
- **useGameClientV2ContainerRefsAndBootstrap.ts** (25 connections) — `client/src/components/ui-v2/hooks/useGameClientV2ContainerRefsAndBootstrap.ts`
- **HealthStatus** (25 connections) — `client/src/types/health.ts`
- **CharacterInfoPanel.tsx** (17 connections) — `client/src/components/ui-v2/panels/CharacterInfoPanel.tsx`
- **RescueState** (17 connections) — `client/src/types/lucidity.ts`
- **EventHandlerContext** (15 connections) — `client/src/components/ui-v2/eventHandlers/types.ts`
- **useEventProcessing.test.ts** (14 connections) — `client/src/components/ui-v2/hooks/__tests__/useEventProcessing.test.ts`
- **useRefSynchronization.ts** (14 connections) — `client/src/components/ui-v2/hooks/useRefSynchronization.ts`
- **characterInfoPanelOutline.ts** (13 connections) — `client/src/components/ui-v2/utils/characterInfoPanelOutline.ts`
- **useMythosTimeBootstrap.ts** (12 connections) — `client/src/components/ui-v2/hooks/useMythosTimeBootstrap.ts`
- **GameClientV2RefsBundle** (11 connections) — `client/src/components/ui-v2/hooks/useGameClientV2ContainerRefsAndBootstrap.ts`
- **HealthMeter.tsx** (10 connections) — `client/src/components/health/HealthMeter.tsx`
- **GameStateUpdates** (10 connections) — `client/src/components/ui-v2/eventHandlers/types.ts`
- **CharacterInfoPanel.test.tsx** (10 connections) — `client/src/components/ui-v2/panels/__tests__/CharacterInfoPanel.test.tsx`
- **QuestLogEntry** (10 connections) — `client/src/components/ui-v2/types.ts`
- **LucidityMeter.tsx** (9 connections) — `client/src/components/lucidity/LucidityMeter.tsx`
- **GameClientV2Props** (9 connections) — `client/src/components/ui-v2/GameClientV2.tsx`
- **QuestLogPanel.tsx** (9 connections) — `client/src/components/ui-v2/panels/QuestLogPanel.tsx`
- *... and 87 more nodes in this community*

## Relationships

- [PanelSystem PanelManager panelLayoutClam](PanelSystem_PanelManager_panelLayoutClam.md) (42 shared connections)
- [game terminal lucidity](game_terminal_lucidity.md) (35 shared connections)
- [combat service services](combat_service_services.md) (28 shared connections)
- [GameClientV2Container emptyOccupantsDiag](GameClientV2Container_emptyOccupantsDiag.md) (26 shared connections)
- [lucidityEventUtils mythosTime MythosTime](lucidityEventUtils_mythosTime_MythosTime.md) (17 shared connections)
- [panels chat ChatPanelRuntimeViewParts](panels_chat_ChatPanelRuntimeViewParts.md) (9 shared connections)
- [services combat sync](services_combat_sync.md) (9 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (9 shared connections)
- [eventHandlers messageHandlers statusPars](eventHandlers_messageHandlers_statusPars.md) (7 shared connections)
- [magic completion game](magic_completion_game.md) (7 shared connections)
- [roomHandlers eventHandlers calculateOccu](roomHandlers_eventHandlers_calculateOccu.md) (7 shared connections)
- [mythosApp security submitAuth](mythosApp_security_submitAuth.md) (6 shared connections)

## Source Files

- `client/src/components/GameTerminal.tsx`
- `client/src/components/health/HealthMeter.tsx`
- `client/src/components/health/__tests__/HealthMeter.test.tsx`
- `client/src/components/lucidity/LucidityMeter.tsx`
- `client/src/components/lucidity/__tests__/LucidityMeter.test.tsx`
- `client/src/components/magic/MagicPointsMeter.tsx`
- `client/src/components/magic/__tests__/MagicPointsMeter.test.tsx`
- `client/src/components/ui-v2/GameClientV2.tsx`
- `client/src/components/ui-v2/GameClientV2AuxiliaryPanels.tsx`
- `client/src/components/ui-v2/GameClientV2Minimap.tsx`
- `client/src/components/ui-v2/TentacleBackdrop.tsx`
- `client/src/components/ui-v2/__tests__/GameClientV2.test.tsx`
- `client/src/components/ui-v2/__tests__/TentacleBackdrop.test.tsx`
- `client/src/components/ui-v2/eventHandlers/types.ts`
- `client/src/components/ui-v2/hooks/__tests__/useEventProcessing.test.ts`
- `client/src/components/ui-v2/hooks/useGameClientV2ContainerRefsAndBootstrap.ts`
- `client/src/components/ui-v2/hooks/useHallucinationFeedCleanup.ts`
- `client/src/components/ui-v2/hooks/useMythosTimeBootstrap.ts`
- `client/src/components/ui-v2/hooks/usePlayerStatusEffects.ts`
- `client/src/components/ui-v2/hooks/useRefSynchronization.ts`

## Audit Trail

- EXTRACTED: 773 (100%)
- INFERRED: 3 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*