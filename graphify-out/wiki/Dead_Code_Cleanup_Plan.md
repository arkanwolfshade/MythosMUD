# Dead Code Cleanup Plan

> 21 nodes · cohesion 0.17

## Key Concepts

- **mapPageRenderer.tsx** (19 connections) — `client/src/pages/mapPageRenderer.tsx`
- **mapPageState.ts** (11 connections) — `client/src/pages/mapPageState.ts`
- **MapPage.tsx** (6 connections) — `client/src/pages/MapPage.tsx`
- **renderMapPageState()** (6 connections) — `client/src/pages/mapPageRenderer.tsx`
- **useMapPageState()** (5 connections) — `client/src/pages/mapPageState.ts`
- **MapPage()** (4 connections) — `client/src/pages/MapPage.tsx`
- **mapPageStatusViews.tsx** (4 connections) — `client/src/pages/mapPageStatusViews.tsx`
- **MapPage.test.tsx** (4 connections) — `client/src/pages/__tests__/MapPage.test.tsx`
- **RoomMapViewerProps** (2 connections) — `client/src/components/map/RoomMapViewer.tsx`
- **renderAuthenticatedMapView()** (2 connections) — `client/src/pages/mapPageRenderer.tsx`
- **renderStatusGate()** (2 connections) — `client/src/pages/mapPageRenderer.tsx`
- **resolveMapViewProps()** (2 connections) — `client/src/pages/mapPageRenderer.tsx`
- **fetchFallbackCurrentRoom()** (2 connections) — `client/src/pages/mapPageState.ts`
- **MapPageState** (2 connections) — `client/src/pages/mapPageState.ts`
- **parseMapRouteParams()** (2 connections) — `client/src/pages/mapPageState.ts`
- **MapPageAuthRequiredView()** (2 connections) — `client/src/pages/mapPageStatusViews.tsx`
- **MapPageErrorView()** (2 connections) — `client/src/pages/mapPageStatusViews.tsx`
- **MapPageLoadingView()** (2 connections) — `client/src/pages/mapPageStatusViews.tsx`
- **AuthenticatedMapProps** (1 connections) — `client/src/pages/mapPageRenderer.tsx`
- **MapViewResolvedProps** (1 connections) — `client/src/pages/mapPageRenderer.tsx`
- **RoomData** (1 connections) — `client/src/pages/mapPageState.ts`

## Relationships

- [Combat Attack Handler](Combat_Attack_Handler.md) (4 shared connections)
- [Room Sync Service](Room_Sync_Service.md) (2 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [Rate Limiter Service](Rate_Limiter_Service.md) (2 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (2 shared connections)

## Source Files

- `client/src/components/map/RoomMapViewer.tsx`
- `client/src/pages/MapPage.tsx`
- `client/src/pages/__tests__/MapPage.test.tsx`
- `client/src/pages/mapPageRenderer.tsx`
- `client/src/pages/mapPageState.ts`
- `client/src/pages/mapPageStatusViews.tsx`

## Audit Trail

- EXTRACTED: 82 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*