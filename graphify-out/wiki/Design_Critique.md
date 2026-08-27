# Design Critique

> 21 nodes

## Key Concepts

- **collect-n-quest.spec.ts** (28 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **getMessages()** (27 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **executeCommandWithoutRecovery()** (17 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **dialogue-trees.spec.ts** (17 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **ensureQuestGiverPresent()** (8 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **listActiveQuestGiverIds()** (7 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **ensureArmitagePresent()** (6 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **listArmitageIds()** (6 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **assertCollectNJournalComplete()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **escapeRegExp()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **summonAndPickupCollectItems()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **turnInCollectNQuest()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **despawnArmitage()** (4 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **loginAdminPlayable()** (4 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **askCollectNQuest()** (4 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **despawnQuestGiverInstances()** (4 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **ensureAdminInFoyer()** (4 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **abandonCollectNQuest()** (3 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **assertQuestGiverVisible()** (3 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **DIALOGUE** (1 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **COLLECT_N** (1 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`

## Relationships

- [CombatValidator](CombatValidator.md) (26 shared connections)
- [test_command_processor.py](test_command_processor.py.md) (22 shared connections)
- [quality_fragmentation_ai_guardrails.py](quality_fragmentation_ai_guardrails.py.md) (17 shared connections)
- [Test Pruning Candidates - Detailed List](Test_Pruning_Candidates_-_Detailed_List.md) (5 shared connections)
- [NATSConfig](NATSConfig.md) (2 shared connections)

## Source Files

- `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- `client/tests/e2e/runtime/fixtures/auth.ts`
- `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*