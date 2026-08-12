# Chat Channel Design Spec

> 25 nodes

## Key Concepts

- **messageHandlers.ts** (21 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **messageHandlers.test-utils.ts** (15 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **statusParser.ts** (11 connections) — `client/src/utils/statusParser.ts`
- **handleCommandResponse()** (7 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **handleChatMessage.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleChatMessage.test.ts`
- **handleCommandResponse.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts`
- **handleRoomMessage.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleRoomMessage.test.ts`
- **handleSystem.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleSystem.test.ts`
- **createMockContext()** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **createMockAppendMessage()** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **resolveChatTypeFromChannel()** (4 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **handleRoomMessage()** (4 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **statusParser.test.ts** (4 connections) — `client/src/utils/__tests__/statusParser.test.ts`
- **parseStatusResponse()** (4 connections) — `client/src/utils/statusParser.ts`
- **convertToPlayerInterface()** (4 connections) — `client/src/utils/statusParser.ts`
- **handleChatMessage()** (3 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **handleSystem()** (2 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **ParsedPlayerData** (2 connections) — `client/src/utils/statusParser.ts`
- **CHANNEL_TO_TYPE_MAP** (1 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **PlayerWithProfession** (1 connections) — `client/src/utils/statusParser.ts`
- **parseSlashPair()** (1 connections) — `client/src/utils/statusParser.ts`
- **parseIntField()** (1 connections) — `client/src/utils/statusParser.ts`
- **ensureProfession()** (1 connections) — `client/src/utils/statusParser.ts`
- **StatusLineHandler** (1 connections) — `client/src/utils/statusParser.ts`
- **STATUS_LINE_HANDLERS** (1 connections) — `client/src/utils/statusParser.ts`

## Relationships

- [Async Room Loading Tests](Async_Room_Loading_Tests.md) (11 shared connections)
- [Commands System Help](Commands_System_Help.md) (4 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (2 shared connections)
- [API Test Fixtures](API_Test_Fixtures.md) (1 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (1 shared connections)
- [Cursor Bug Agents](Cursor_Bug_Agents.md) (1 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/handleChatMessage.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleRoomMessage.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleSystem.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- `client/src/utils/__tests__/statusParser.test.ts`
- `client/src/utils/statusParser.ts`

## Audit Trail

- EXTRACTED: 117 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*