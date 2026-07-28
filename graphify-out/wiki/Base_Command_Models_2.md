# Base Command Models

> 20 nodes · cohesion 0.22

## Key Concepts

- **messageHandlers.ts** (21 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **handleCommandResponse()** (7 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **determineMessageType()** (7 connections) — `client/src/utils/messageTypeUtils.ts`
- **statusParser.ts** (6 connections) — `client/src/utils/statusParser.ts`
- **handleChatMessage.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleChatMessage.test.ts`
- **handleCommandResponse.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts`
- **handleRoomMessage.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleRoomMessage.test.ts`
- **handleSystem.test.ts** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/handleSystem.test.ts`
- **createMockAppendMessage()** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **createMockContext()** (5 connections) — `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- **handleRoomMessage()** (4 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **resolveChatTypeFromChannel()** (4 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **convertToPlayerInterface()** (4 connections) — `client/src/utils/statusParser.ts`
- **parseStatusResponse()** (4 connections) — `client/src/utils/statusParser.ts`
- **statusParser.test.ts** (4 connections) — `client/src/utils/__tests__/statusParser.test.ts`
- **handleChatMessage()** (3 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **handleSystem()** (2 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **ParsedPlayerData** (2 connections) — `client/src/utils/statusParser.ts`
- **CHANNEL_TO_TYPE_MAP** (1 connections) — `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- **PlayerWithProfession** (1 connections) — `client/src/utils/statusParser.ts`

## Relationships

- [Combat Service Bundle](Combat_Service_Bundle.md) (10 shared connections)
- [NPC Population Control](NPC_Population_Control.md) (4 shared connections)
- [Rate Limiter Service](Rate_Limiter_Service.md) (2 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (1 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (1 shared connections)

## Source Files

- `client/src/components/ui-v2/eventHandlers/__tests__/handleChatMessage.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleCommandResponse.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleRoomMessage.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/handleSystem.test.ts`
- `client/src/components/ui-v2/eventHandlers/__tests__/messageHandlers.test-utils.ts`
- `client/src/components/ui-v2/eventHandlers/messageHandlers.ts`
- `client/src/utils/__tests__/statusParser.test.ts`
- `client/src/utils/messageTypeUtils.ts`
- `client/src/utils/statusParser.ts`

## Audit Trail

- EXTRACTED: 99 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*