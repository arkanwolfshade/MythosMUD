# Connection Cleaner Tests

> 37 nodes

## Key Concepts

- **projectorHandlersMessages.ts** (26 connections) — `client/src/components/ui-v2/eventLog/projectorHandlersMessages.ts`
- **projectorRoom.ts** (25 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **projectorHandlersState.ts** (23 connections) — `client/src/components/ui-v2/eventLog/projectorHandlersState.ts`
- **projectorMessageUtils.ts** (11 connections) — `client/src/components/ui-v2/eventLog/projectorMessageUtils.ts`
- **messageMapper.ts** (8 connections) — `client/src/components/ui-v2/eventLog/messageMapper.ts`
- **messageMapper.test.ts** (7 connections) — `client/src/components/ui-v2/eventLog/__tests__/messageMapper.test.ts`
- **deriveRoomFromRoomUpdate()** (6 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **deriveRoomFromRoomOccupants()** (5 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **buildChatMessage()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorMessageUtils.ts`
- **appendMessage()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorMessageUtils.ts`
- **appendMovementMessage()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorMessageUtils.ts`
- **roomWithOccupantsFromArrays()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **roomWithPreservedOccupants()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **createRoomUpdateWithPreservedOccupants()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **deriveRoomFromRoomState()** (4 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **formatNpcTookDamageLine()** (3 connections) — `client/src/components/ui-v2/eventLog/messageMapper.ts`
- **formatNpcAttackedLine()** (3 connections) — `client/src/components/ui-v2/eventLog/messageMapper.ts`
- **formatPlayerAttackedLine()** (3 connections) — `client/src/components/ui-v2/eventLog/messageMapper.ts`
- **mergePlayerDpFromPlayerAttackedPayload()** (3 connections) — `client/src/components/ui-v2/eventLog/messageMapper.ts`
- **normalizeOccupantArrays()** (3 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **mergeTopLevelOccupants()** (3 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **getRoomDataFromEvent()** (3 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **resolvePreservedOccupantArrays()** (3 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **deriveRoomFromGameState()** (3 connections) — `client/src/components/ui-v2/eventLog/projectorRoom.ts`
- **messageHandlers** (2 connections) — `client/src/components/ui-v2/eventLog/projectorHandlersMessages.ts`
- *... and 12 more nodes in this community*

## Relationships

- [Communication Command Handlers](Communication_Command_Handlers.md) (14 shared connections)
- [Structured Error Logging Tasks](Structured_Error_Logging_Tasks.md) (7 shared connections)
- [API Test Fixtures](API_Test_Fixtures.md) (5 shared connections)
- [Character Stats Model](Character_Stats_Model.md) (5 shared connections)
- [Room Planning Archive](Room_Planning_Archive.md) (4 shared connections)
- [Status Effect Tick Tests](Status_Effect_Tick_Tests.md) (2 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (2 shared connections)

## Source Files

- `client/src/components/ui-v2/eventLog/__tests__/messageMapper.test.ts`
- `client/src/components/ui-v2/eventLog/messageMapper.ts`
- `client/src/components/ui-v2/eventLog/projectorHandlersMessages.ts`
- `client/src/components/ui-v2/eventLog/projectorHandlersState.ts`
- `client/src/components/ui-v2/eventLog/projectorMessageUtils.ts`
- `client/src/components/ui-v2/eventLog/projectorRoom.ts`

## Audit Trail

- EXTRACTED: 191 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*