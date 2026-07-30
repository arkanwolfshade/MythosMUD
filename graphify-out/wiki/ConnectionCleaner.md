# ConnectionCleaner

> 19 nodes

## Key Concepts

- **sanitizeChatMessageForState()** (24 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **messageUtils.ts** (18 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **combatHandlers.ts** (14 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **combatHandlers.test.ts** (12 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/combatHandlers.test.ts`
- **getMessageMetadata()** (5 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **messageUtils.test.ts** (4 connections) — `client/src/components/ui-v2/utils/__tests__/messageUtils.test.ts`
- **handleNpcAttacked()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handlePlayerAttacked()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleNpcDied()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleCombatDeath()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleCombatTargetSwitch()** (3 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleCombatStarted()** (2 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **handleCombatEnded()** (2 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- **getRawTextFromMessage()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **sanitizeMessageText()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **getMessageType()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **getMessageChannel()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **getMessageTypeField()** (2 connections) — `client/src/components/ui-v2/utils/messageUtils.ts`
- **ADR-0016** (1 connections) — `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`

## Relationships

- [monitoring models](monitoring_models.md) (8 shared connections)
- [MythosTimeHud](MythosTimeHud.md) (5 shared connections)
- [Instance](Instance.md) (4 shared connections)
- [HealthMeter](HealthMeter.md) (3 shared connections)
- [useConnectionStateMachine.test](useConnectionStateMachine.test.md) (3 shared connections)
- [player respawn](player_respawn.md) (3 shared connections)
- [Cancel lifecycle/critical tasks first (Phase](Cancel_lifecycle-critical_tasks_first_%28Phase.md) (3 shared connections)
- [fetchSpy](fetchSpy.md) (2 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/combatHandlers.test.ts`
- `client/src/components/ui-v2/eventHandlers/combatHandlers.ts`
- `client/src/components/ui-v2/utils/__tests__/messageUtils.test.ts`
- `client/src/components/ui-v2/utils/messageUtils.ts`

## Audit Trail

- EXTRACTED: 106 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*