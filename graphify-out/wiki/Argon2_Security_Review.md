# Argon2 Security Review

> 21 nodes

## Key Concepts

- **RoomInfoPanel.tsx** (21 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoPanel()** (10 connections) — `client/src/components/RoomInfoPanel.tsx`
- **validateAndFixRoomData()** (4 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoPanel.test.tsx** (4 connections) — `client/src/components/__tests__/RoomInfoPanel.test.tsx`
- **RoomInfoPanel.test.tsx** (3 connections) — `client/src/components/RoomInfoPanel.test.tsx`
- **applyRoomDefaultFields()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **fixOccupantCountMismatch()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **formatLocationName()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **formatDescription()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **formatExitDirections()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **logRoomInfoRenderDebug()** (2 connections) — `client/src/components/RoomInfoPanel.tsx`
- **mockConsoleLog** (1 connections) — `client/src/components/RoomInfoPanel.test.tsx`
- **Room** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoPanelProps** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **KNOWN_LOCATION_PATTERNS** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **OccupantList()** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomOccupantsSection()** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **DEV_FALLBACK_ROOM** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **RoomInfoEmptyState()** (1 connections) — `client/src/components/RoomInfoPanel.tsx`
- **{ mockDebug }** (1 connections) — `client/src/components/__tests__/RoomInfoPanel.test.tsx`
- **Room** (1 connections) — `client/src/components/__tests__/RoomInfoPanel.test.tsx`

## Relationships

- [Draggable Panel UI](Draggable_Panel_UI.md) (2 shared connections)
- [Memory Leak Metrics Tests](Memory_Leak_Metrics_Tests.md) (2 shared connections)
- [Status Effect Tick Tests](Status_Effect_Tick_Tests.md) (2 shared connections)

## Source Files

- `client/src/components/RoomInfoPanel.test.tsx`
- `client/src/components/RoomInfoPanel.tsx`
- `client/src/components/__tests__/RoomInfoPanel.test.tsx`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*