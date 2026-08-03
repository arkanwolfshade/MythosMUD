# headers middleware security

> 10 nodes

## Key Concepts

- **RoomInfoPanel.tsx** (10 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoPanel()** (6 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoPanel.test.tsx** (4 connections) — `client/src/components/__tests__/RoomInfoPanel.test.tsx`
- **RoomInfoPanel.test.tsx** (3 connections) — `client/src/components/RoomInfoPanel.test.tsx`
- **validateAndFixRoomData()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **mockConsoleLog** (1 connections) — `client/src/components/RoomInfoPanel.test.tsx`
- **Room** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoPanelProps** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **{ mockDebug }** (1 connections) — `client/src/components/__tests__/RoomInfoPanel.test.tsx`
- **Room** (1 connections) — `client/src/components/__tests__/RoomInfoPanel.test.tsx`

## Relationships

- [game terminal lucidity](game_terminal_lucidity.md) (2 shared connections)
- [stores connectionStore commandStore](stores_connectionStore_commandStore.md) (2 shared connections)
- [roomHandlers eventHandlers calculateOccu](roomHandlers_eventHandlers_calculateOccu.md) (2 shared connections)

## Source Files

- `client/src/components/RoomInfoPanel.test.tsx`
- `client/src/components/RoomInfoPanel.tsx`
- `client/src/components/__tests__/RoomInfoPanel.test.tsx`

## Audit Trail

- EXTRACTED: 30 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*