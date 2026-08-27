# AdminAuthService

> 28 nodes

## Key Concepts

- **playerHandlers.ts** (24 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **healthEventUtils.ts** (16 connections) — `client/src/utils/healthEventUtils.ts`
- **playerHandlers.test.ts** (14 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/playerHandlers.test.ts`
- **buildHealthStatusFromEvent()** (9 connections) — `client/src/utils/healthEventUtils.ts`
- **determineDpTier()** (7 connections) — `client/src/types/health.ts`
- **healthEventUtils.test.ts** (6 connections) — `client/src/utils/__tests__/healthEventUtils.test.ts`
- **buildHealthChangeMessage()** (4 connections) — `client/src/utils/healthEventUtils.ts`
- **handlePlayerDpUpdated()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerRespawned()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerUpdate()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **mergePlayerStats()** (3 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **parseHealthEventNumbers()** (3 connections) — `client/src/utils/healthEventUtils.ts`
- **readDpField()** (3 connections) — `client/src/utils/healthEventUtils.ts`
- **handlePlayerDeliriumRespawned()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerDied()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerEntered()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerEnteredGame()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerLeft()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **handlePlayerLeftGame()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **pickStatNumber()** (2 connections) — `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- **formatSource()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **humanizeReason()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **inferReasonFromDelta()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **parseNumber()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- **resolveInCombat()** (2 connections) — `client/src/utils/healthEventUtils.ts`
- *... and 3 more nodes in this community*

## Relationships

- [nats_exceptions.py](nats_exceptions.py.md) (10 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (4 shared connections)
- [NPCCombatMemory](NPCCombatMemory.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [LogAggregator](LogAggregator.md) (1 shared connections)
- [Feature Requirements Document: Random Stats Generator](Feature_Requirements_Document-_Random_Stats_Generator.md) (1 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/playerHandlers.test.ts`
- `client/src/components/ui-v2/eventHandlers/playerHandlers.ts`
- `client/src/types/__tests__/health.test.ts`
- `client/src/types/health.ts`
- `client/src/utils/__tests__/healthEventUtils.test.ts`
- `client/src/utils/healthEventUtils.ts`

## Audit Trail

- EXTRACTED: 74 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*