# Feature Requirements Document: Random Stats Generator

> 26 nodes

## Key Concepts

- **messageHandlers.ts** (21 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **messageHandlers.test-utils.ts** (15 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **statusParser.ts** (11 connections) — `client/src/utils/statusParser.ts`
- **EventHandler** (7 connections) — `client/src/components/ui-v2/eventHandlers/types.ts`
- **handleCommandResponse()** (6 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **handleCommandResponse.test.ts** (6 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts`
- **createMockAppendMessage()** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **createMockContext()** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **handleChatMessage.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleChatMessage.test.ts`
- **handleRoomMessage.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleRoomMessage.test.ts`
- **handleSystem.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleSystem.test.ts`
- **handleRoomMessage()** (4 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **resolveChatTypeFromChannel()** (4 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **convertToPlayerInterface()** (4 connections) — `client/src/utils/statusParser.ts`
- **parseStatusResponse()** (4 connections) — `client/src/utils/statusParser.ts`
- **statusParser.test.ts** (4 connections) — `client/src/utils/__tests__/statusParser.test.ts`
- **handleChatMessage()** (3 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **ParsedPlayerData** (2 connections) — `client/src/utils/statusParser.ts`
- **handleSystem()** (2 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **PlayerWithProfession** (1 connections) — `client/src/utils/statusParser.ts`
- **StatusLineHandler** (1 connections) — `client/src/utils/statusParser.ts`
- **ensureProfession()** (1 connections) — `client/src/utils/statusParser.ts`
- **parseIntField()** (1 connections) — `client/src/utils/statusParser.ts`
- **parseSlashPair()** (1 connections) — `client/src/utils/statusParser.ts`
- **CHANNEL_TO_TYPE_MAP** (1 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- *... and 1 more nodes in this community*

## Relationships

- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (7 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (6 shared connections)
- [test_player_death_service.py](test_player_death_service.py.md) (4 shared connections)
- [NATSMessageBroker](NATSMessageBroker.md) (2 shared connections)
- [NPCCombatMemory](NPCCombatMemory.md) (2 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [AdminAuthService](AdminAuthService.md) (1 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/handleChatMessage.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleRoomMessage.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleSystem.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- `client/src/components/ui-v2/eventHandlers/types.ts`
- `client/src/utils/__tests__/statusParser.test.ts`
- `client/src/utils/statusParser.ts`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*