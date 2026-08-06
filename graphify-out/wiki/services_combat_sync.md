# services combat sync

> 25 nodes

## Key Concepts

- **playerHandlers.ts** (22 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **playerHandlers.test.ts** (14 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/playerHandlers.test.ts`
- **healthEventUtils.ts** (12 connections) — `client/src/utils/healthEventUtils.ts`
- **determineDpTier()** (9 connections) — `client/src/types/health.ts`
- **buildHealthStatusFromEvent()** (7 connections) — `client/src/utils/healthEventUtils.ts`
- **useGameClientV2ContainerHealthSync.ts** (6 connections) — `client/src/components/ui-v2/hooks/useGameClientV2ContainerHealthSync.ts`
- **deriveHealthStatusFromPlayer()** (6 connections) — `client/src/types/health.ts`
- **healthEventUtils.test.ts** (6 connections) — `client/src/utils/__tests__/healthEventUtils.test.ts`
- **useGameClientV2ContainerHealthSync()** (4 connections) — `client/src/components/ui-v2/hooks/useGameClientV2ContainerHealthSync.ts`
- **buildHealthChangeMessage()** (4 connections) — `client/src/utils/healthEventUtils.ts`
- **handlePlayerRespawned()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerDpUpdated()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerEnteredGame()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerEntered()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerLeftGame()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerLeft()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerDied()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerDeliriumRespawned()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerUpdate()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **health.test.ts** (2 connections) — `client/src/types/__tests__/health.test.ts`
- **parseNumber()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **toReasonString()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **humanizeReason()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **formatSource()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **HEALTH_LOG_TAGS** (2 connections) — `client/src/utils/healthEventUtils.ts`

## Relationships

- [combat service services](combat_service_services.md) (19 shared connections)
- [GameClientV2Container emptyOccupantsDiag](GameClientV2Container_emptyOccupantsDiag.md) (5 shared connections)
- [eventHandlers messageHandlers statusPars](eventHandlers_messageHandlers_statusPars.md) (4 shared connections)
- [combat services persistence](combat_services_persistence.md) (2 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/playerHandlers.test.ts`
- `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- `client/src/components/ui-v2/hooks/useGameClientV2ContainerHealthSync.ts`
- `client/src/types/__tests__/health.test.ts`
- `client/src/types/health.ts`
- `client/src/utils/__tests__/healthEventUtils.test.ts`
- `client/src/utils/healthEventUtils.ts`

## Audit Trail

- EXTRACTED: 122 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*