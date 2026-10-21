# CorpseLifecycleService

> 61 nodes · cohesion 0.08

## Key Concepts

- **executeCommand()** (113 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **waitForMessage()** (71 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **ensurePlayableConnection()** (39 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **whisper-movement.spec.ts** (37 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **collect-n-quest.spec.ts** (30 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **dialogue-trees.spec.ts** (17 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **executeCommandWithoutRecovery()** (15 connections) — `client/tests/e2e/runtime/fixtures/auth.ts`
- **ensureQuestGiverPresent()** (8 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **listActiveQuestGiverIds()** (7 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **executeUnmuteAndWaitForAck()** (6 connections) — `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- **executeUnmuteAndWaitForAck()** (6 connections) — `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- **ensureArmitagePresent()** (6 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **listArmitageIds()** (6 connections) — `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- **readSkillsMessageText()** (5 connections) — `client/tests/e2e/runtime/character/revised-character-creation.spec.ts`
- **ensureIthaquaInFoyer()** (5 connections) — `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- **attemptEastHop()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **lookAndWaitForUi()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **moveAwToEasternHallway()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **sendCrossRoomWhisper()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **whisperUntilSenderAck()** (5 connections) — `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- **walkToChapel()** (5 connections) — `client/tests/e2e/runtime/corruption/room-flux-purification.spec.ts`
- **assertCollectNJournalComplete()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **escapeRegExp()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **summonAndPickupCollectItems()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- **turnInCollectNQuest()** (5 connections) — `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- *... and 36 more nodes in this community*

## Relationships

- [ChatModeration](ChatModeration.md) (115 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (63 shared connections)
- [look_command.py](look_command.py.md) (51 shared connections)
- [Test Pruning Candidates - Detailed List](Test_Pruning_Candidates_-_Detailed_List.md) (12 shared connections)
- [PassiveCorruptionFluxService](PassiveCorruptionFluxService.md) (9 shared connections)
- [properties](properties.md) (1 shared connections)

## Source Files

- `client/tests/e2e/runtime/admin/admin-set-stat-command.spec.ts`
- `client/tests/e2e/runtime/character/revised-character-creation.spec.ts`
- `client/tests/e2e/runtime/commands/posture-messages-game-info.spec.ts`
- `client/tests/e2e/runtime/communication/chat-messages.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-basic.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-integration.spec.ts`
- `client/tests/e2e/runtime/communication/local-channel-isolation.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-basic.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-integration.spec.ts`
- `client/tests/e2e/runtime/communication/whisper-movement.spec.ts`
- `client/tests/e2e/runtime/corruption/corruption-cleanse.spec.ts`
- `client/tests/e2e/runtime/corruption/room-flux-purification.spec.ts`
- `client/tests/e2e/runtime/dialogue/dialogue-trees.spec.ts`
- `client/tests/e2e/runtime/fixtures/auth.ts`
- `client/tests/e2e/runtime/follow/follow-commands.spec.ts`
- `client/tests/e2e/runtime/movement/movement-between-rooms.spec.ts`
- `client/tests/e2e/runtime/quest/collect-n-quest.spec.ts`
- `client/tests/e2e/runtime/tutorial/tutorial-instance-lifecycle.spec.ts`

## Audit Trail

- EXTRACTED: 389 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*