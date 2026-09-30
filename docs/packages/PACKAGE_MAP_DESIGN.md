# Map Package Design

**Version 1.0.0** · MythosMUD · 2026-09-29

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
`client/src/components/map/` holds **two independent map renderers that share almost nothing**:

1. **The ASCII stack** — the server renders the map as an HTML string; the client fetches it and
   shows it in a fixed viewport (`AsciiMapViewer`) or as a small in-panel minimap (`AsciiMinimap`).
2. **The React Flow stack** — the client fetches a room list and builds a node-and-edge graph with
   `reactflow`. `RoomMapViewer` is the read-only player view; `RoomMapEditor` is the admin editor
   that drags rooms, creates and deletes exits, edits room properties and saves them back.

They meet at one component (`MapControls`) and at the server's shared `rooms.map_x` / `map_y`
columns (§4). This document is reverse-engineered from code; code is the source of truth (see
[`docs/subsystems/README.md`](../subsystems/README.md) for the same posture applied to behavioral
subsystems).

Written to close [`#743`](https://github.com/arkanwolfshade/MythosMUD/issues/743). The map is a
client-side feature that predates the `ui-v2/` migration and is **not** part of it
([ADR-022](../architecture/decisions/ADR-022-ui-v2-client-transition.md)); `ui-v2` embeds
`AsciiMinimap` and reaches the rest through `components/MapView.tsx`.

## 2. Members

**[SPEC]**

### ASCII stack

| File                        | Exports                                                | Purpose                                                                                                                                  |
| --------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `AsciiMapViewer.tsx`        | `AsciiMapViewer`, `AsciiMapViewerProps`                | Full-map viewer. Wires `useAsciiMap`, a `window` key listener for viewport panning, and click-to-select via `data-room-id`.             |
| `AsciiMapViewerViews.tsx`   | `AsciiMapViewerContent`, `AsciiMapViewerError`, `AsciiMapViewerLoading` | Presentational pieces; renders server HTML through `SafeHtml`; hosts `MapControls`.                                    |
| `asciiMapViewerUtils.ts`    | `VIEWPORT_BUTTON_CLASS`, `createViewportKeyHandler`    | Arrow-key → viewport delta handler and shared button class.                                                                              |
| `useAsciiMap.ts`            | `UseAsciiMapParams`, `UseAsciiMapResult`, `useAsciiMap`| Type home for the hook; `useAsciiMap` is a re-export of `useAsciiMapState`.                                                              |
| `useAsciiMapState.ts`       | `useAsciiMapState`                                     | Fetch + viewport + plane/zone/sub-zone selection state; calls `fetchAsciiMap`.                                                           |
| `AsciiMinimap.tsx`          | `AsciiMinimap`, `AsciiMinimapProps`                    | Small server-rendered minimap; calls `fetchAsciiMinimap`; re-fetches on room change.                                                     |

### React Flow stack — viewer

| File                     | Exports                               | Purpose                                                                                                                                                                  |
| ------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `RoomMapViewer.tsx`      | `RoomMapViewer`, `RoomMapViewerProps` | Read-only graph. `useRoomMapData` → `roomsToNodes` / `createEdgesFromRooms` → `useMapLayout` (force layout, stored coordinates on) → `ReactFlow`. Search box, `RoomDetailsPanel`. |
| `AsciiNoise.tsx`         | `AsciiNoise`                          | Deranged-tier overlay: seeded noise (`generateAsciiNoise`, `mulberry32` from `utils/directionHallucination`) that covers the real graph on purpose (#626).                |
| `RoomDetailsPanel.tsx`   | `RoomDetailsPanel`                    | Selected-room side panel; takes `tier` / `playerId` to hallucinate exits when deranged.                                                                                  |
| `config.ts`              | `nodeTypes`, `edgeTypes`, `getNodeTypes`, `getEdgeTypes` | The React Flow type registry: `room`, `intersection` nodes; `exit` edge. Module-level constants so `ReactFlow` sees stable identities.                 |
| `types.ts`               | `Room`, `RoomNodeData`, `ExitEdgeData`, … | Map-local domain types. `Room` is **not** `ui-v2/types.ts`'s live-game `Room`: it carries `map_x`, `map_y`, `entities`, `room_environment`.                          |
| `nodes/RoomNode.tsx`, `nodes/IntersectionNode.tsx`, `nodes/DepartureMarkers.tsx` | node components | Room box; street-intersection node; markers for exits that leave the loaded sub-zone (`departures`).                                       |
| `edges/ExitEdge.tsx`     | `ExitEdge`                            | Directional exit edge with flag styling.                                                                                                                                 |
| `hooks/useRoomMapData.ts`| `useRoomMapData`                      | `GET {base}/api/rooms/list?plane&zone&sub_zone&include_exits&filter_explored`; validates with `isRoomsListApiResponse`.                                                  |
| `hooks/useMapLayout.ts`  | `useMapLayout`                        | Grid or force layout, stored-coordinate use, debounced recompute, `savePositions`, `resetToAutoLayout`.                                                                  |
| `utils/mapUtils.ts`      | `roomToNode`, `roomsToNodes`, `createEdgesFromRooms`, `transformRoomsToMapData`, `RoomMapData` | Server room → React Flow node/edge; grid-unit → pixel on load; `departures` detection.                      |
| `utils/layout.ts`        | `applyForceLayout`, `applyGridLayout`, `calculateGridPosition`, configs, `GRID_PITCH` (re-export) | Layout engines (675 lines; the force simulation is O(n²) — §5).                                               |
| `utils/mapGeometry.ts`   | `GRID_PITCH`, `MAX_FORCE_LAYOUT_NODES`| The contract between DB coordinates and React Flow pixels (§4). Two constants, no imports, deliberately apart from `layout.ts`.                                           |
| `utils/performance.ts`   | `debounce`, throttle and timing helpers | Generic; consumed by `useMapLayout`.                                                                                                                                   |

### React Flow stack — editor (admin)

| File                              | Exports                                                                         | Purpose                                                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `RoomMapEditor.tsx`               | `RoomMapEditor`                                                                 | One-line public entry: re-exports from `RoomMapEditorRuntime`. Import this, not the runtime file.                                    |
| `RoomMapEditorRuntime.tsx`        | `RoomMapEditor`                                                                 | The component: `ReactFlow` + `MapEditToolbar` + modals + panels.                                                                    |
| `RoomMapEditorRuntime.hooks.ts`   | `RoomMapEditorProps`, `MAP_EDITOR_DIRECTIONS`, `useRoomMapEditorData / Editing / Modals / Selection` | The editor's state, split by concern.                                                                          |
| `hooks/useMapEditing.ts`          | `useMapEditing`, `MapEditingChanges`, `EdgeCreationData`, `EdgeValidationResult`| Pending-change model: node moves, new/deleted/updated edges, room updates; undo / redo; validation.                                  |
| `utils/saveMapChanges.ts`         | `saveMapChanges`, `saveNodePositions`, `saveEdgeChanges`, `saveRoomUpdates`, `recalculateCoordinates` | Persists a `MapEditingChanges` set (§3 endpoints). Divides pixels by `GRID_PITCH` before writing.                     |
| `MapEditToolbar.tsx`              | `MapEditToolbar`                                                                | Save / undo / redo / reset / recalculate controls.                                                                                          |
| `EdgeCreationModal.tsx`, `EdgeCreationModalParts.tsx`, `useEdgeCreationModal.ts`, `edgeModalLogic.ts` | modal + hook + pure logic | New-exit dialog, split into view, parts, state hook and validation logic.                                   |
| `EdgeDetailsPanel.tsx`            | `EdgeDetailsPanel`                                                              | Selected-edge panel (edit flags / description / target, delete).                                                                    |
| `RoomEditModal.tsx`, `RoomEditModalForm.tsx`, `RoomEditModalTabs.tsx`, `useRoomEditModal.ts` | modal + form + tabs + hook | Edit name, description, `room_environment` (#663).                                                                    |

### Shared

| File                | Exports       | Purpose                                                                                                        |
| ------------------- | ------------- | -------------------------------------------------------------------------------------------------------------- |
| `MapControls.tsx`   | `MapControls` | Plane / zone / sub-zone selectors and viewport buttons. Used by `AsciiMapViewerViews`, `RoomMapViewer`, `RoomMapEditorRuntime`. |

Tests: `map/__tests__/` (component + hook), `map/{hooks,nodes,edges,utils}/__tests__/`. See also
[`docs/testing/map-regression-tests.md`](../testing/map-regression-tests.md).

## 3. Boundary contract

**[SPEC]**

**Entry points.**

| Consumer                                        | Reaches                                | How                                                                                      |
| ----------------------------------------------- | -------------------------------------- | ---------------------------------------------------------------------------------------- |
| `components/ui-v2/GameClientV2MinimapSection.tsx` | `AsciiMinimap`                       | Inline minimap in the minimap panel.                                                     |
| `components/MapView.tsx`                         | `AsciiMapViewer`                       | Full-screen overlay (Esc to close), opened from `GameClientV2ContainerView`.             |
| `pages/mapPageRenderer.tsx` (via `pages/MapPage`, lazy `/map` route in `AppRouter.tsx`) | `RoomMapViewer`, `RoomMapEditor` | `?edit=true` selects the editor; otherwise the viewer, with `tier` and `playerId` relayed for the hallucination overlay. |
| `api/maps.ts`                                    | (called by) `AsciiMinimap`, `useAsciiMapState` | `fetchAsciiMinimap`, `fetchAsciiMap`; URL building, bearer header, response validation.  |

Only `RoomMapEditor.tsx`, `RoomMapViewer.tsx`, `AsciiMapViewer.tsx` and `AsciiMinimap.tsx` are
imported from outside the directory; everything else is internal. (`components/MapView.tsx`,
`pages/*` and `api/maps.ts` are owned by
[`#746`](https://github.com/arkanwolfshade/MythosMUD/issues/746) and are cited here as
collaborators only.)

**Server endpoints used.**

| Method | Path                                          | Used by                                   | Notes                                    |
| ------ | --------------------------------------------- | ----------------------------------------- | ---------------------------------------- |
| GET    | `/api/maps/ascii`                             | `useAsciiMapState`                        | Returns `{ map_html, … }`.               |
| GET    | `/api/maps/ascii/minimap`                     | `AsciiMinimap`                            | `size` defaults to 5.                    |
| GET    | `/api/rooms/list`                             | `useRoomMapData`                          | `filter_explored` is on for any authenticated caller (player view); the server returns all rooms to admins. |
| POST   | `/api/rooms/{id}/position`                    | `saveNodePositions`                       | Admin only.                              |
| POST / PUT / DELETE | `/api/rooms/{id}/exits[…]`       | `saveEdgeChanges`                         | Admin only.                              |
| PUT    | `/api/rooms/{id}`                             | `saveRoomUpdates`                         | Admin only.                              |
| POST   | `/api/maps/coordinates/recalculate`           | `recalculateCoordinates`                  | Admin only (server BFS regenerates `map_x` / `map_y`). |

**Invariants a caller must not violate:**

- **Server HTML goes through `SafeHtml`.** `AsciiMapViewerViews` and `AsciiMinimap` render the
  server string via `components/common/SafeHtml`, which DOMPurify-sanitises it first. Nothing under
  `map/` uses `dangerouslySetInnerHTML`; keep it that way.
- **Edit-mode gating is a UI convenience, not authorization.** `?edit=true` on the page URL is all
  the client checks. Every write endpoint above enforces admin on the server
  (`validate_admin_room_action`, `server/api/rooms.py`); the client must never be relied on to
  hide edit capability.
- **Never store React Flow pixels in `map_x` / `map_y`.** See §4.
- **The map renders the requested sub-zone only.** An exit whose target is outside the loaded set
  is not an edge; it is a `departures` marker on the source node.
- **`nodeTypes` / `edgeTypes` must be module-level constants** (`config.ts`). Building them inside a
  component makes `ReactFlow` remount every node on every render.

## 4. Key design decisions

**[SPEC]**

- **Two renderers, one dataset.** The ASCII renderer exists for the in-game minimap and low-cost
  viewing (the server owns the layout); React Flow exists for exploration and editing (the client
  owns the layout). Both read the same `rooms.map_x` / `map_y`.
- **Grid units in the database, pixels in the browser (#829).** `map_x` / `map_y` are **grid
  units** — one step per room — written by the server's `CoordinateGenerator` BFS and read by the
  ASCII renderer via `int(map_x)`. React Flow works in pixels. `GRID_PITCH = 120` converts:
  multiply on load (`mapUtils`, `useMapLayout`), divide on save (`saveMapChanges`). Before #829 the
  editor saved raw pixels into those columns, so one drag-and-save corrupted a whole zone and the
  ASCII minimap. `mapGeometry.ts` is a separate file so the save path does not import the layout
  engine just to convert a coordinate.
- **A hard stop for the force layout, not a scaled one.** Above `MAX_FORCE_LAYOUT_NODES = 200`
  *unpositioned* nodes the force simulation is skipped entirely. `applyForceLayout` is 800
  iterations of O(n²) plus edge-pair work run synchronously in a `useMemo`; at Arkham's ~480 street
  rooms that freezes the tab. A loud fallback was chosen over quietly reducing iterations, which
  would turn a freeze into placement nobody can diagnose. Rooms with authored coordinates never
  reach the simulation.
- **`departures` instead of phantom nodes.** Because the map is fetched per sub-zone, the room on
  the far side of a cross-sub-zone exit is absent, and without a marker the only way into a
  building looks like a dead end. `DepartureMarkers` render the leaving directions.
- **Server-authoritative hallucination overlay (#626 / ADR-024 lineage).** For `tier ===
  'deranged'` the viewer overlays `AsciiNoise` seeded by `seedFrom(currentRoomId, playerId)` and
  passes `tier` down to `RoomDetailsPanel`. The **editor ignores the tier** on purpose: the editor
  must never lie to an admin.
- **`RoomMapEditor` alias chain collapsed (this change).** The public entry used to re-export
  through four one-line files (`RoomMapEditorImpl` → `Core` → `Feature` → `Scene` →
  `RoomMapEditorRuntime`), guarded by an alias-identity test. All four hop files and
  `__tests__/RoomMapEditorAliases.test.ts` were deleted; `RoomMapEditor.tsx` now re-exports from
  `RoomMapEditorRuntime` directly. External import paths are unchanged.
- **Editor split by concern rather than by size.** View / parts / state hook / pure logic is the
  pattern for both modals (`EdgeCreationModal*`, `RoomEditModal*`); most splits exist to keep
  individual functions under the repo's complexity limits.

## 5. Constraints

**[SPEC]**

- **`useAsciiMap.ts` is a type file with a re-export.** The hook implementation is
  `useAsciiMapState.ts`; `useAsciiMap` is `export { useAsciiMapState as useAsciiMap }`. Import the
  hook from either, but types come from `useAsciiMap.ts` only.
- **The `Room` type is duplicated.** `components/MapView.tsx` declares its own local `Room`
  interface (no `entities`, no `room_environment`) rather than importing `map/types.ts`. Widening
  `map/types.Room` does not update it.
- **Force layout cost.** For 200 unpositioned nodes the simulation is still ~800 × O(n²); it is
  bounded, not cheap. Debounce lives in `useMapLayout` (`utils/performance.ts`).
- **`AsciiMapViewer` binds arrow keys on `window`** for its whole mounted lifetime, with no focus
  check. A second mounted `AsciiMapViewer` (or any other global key handler) receives the same keys.
- **`filter_explored` is client-requested.** `RoomMapViewer` sends `filter_explored=true` for any
  caller with an auth token, including admins viewing without `?edit=true`; whether an admin
  receives the full set is a server decision, not something this package can assert.
- **Layout lives in two places.** The ASCII layout is computed by the server; the React Flow layout
  by `utils/layout.ts`. Neither knows about the other, so a room can sit at different apparent
  positions in the two views when no stored coordinates exist.
- **Tests mock at the concrete path.** `RoomMapViewer.test-utils.tsx` and
  `roomMapEditorTestSetup.tsx` centralise mocks; add new mocks there rather than per-file
  (`vi.mock` targets the component file, as in
  [`PACKAGE_UI_PRIMITIVES_DESIGN.md`](PACKAGE_UI_PRIMITIVES_DESIGN.md) §6).

## 6. Developer guide

**[NOTE]**

- **Adding a node or edge type**: add the component under `nodes/` or `edges/`, register it in
  `config.ts`, and extend `RoomNodeData` / `ExitEdgeData` in `types.ts`.
- **Touching coordinates**: convert with `GRID_PITCH` from `utils/mapGeometry.ts` and nothing else.
  If a value reaches the API, it must be grid units. Extend `saveMapChanges.test.ts` and
  `mapUtils.test.ts` when changing either direction.
- **Adding an editor operation**: model it as a field on `MapEditingChanges` (`useMapEditing`),
  persist it in `saveMapChanges.ts`, and surface it in `MapEditToolbar` or a panel. Keep the
  server-side admin check in step with it.
- **Adding a player-visible map effect** (like the deranged overlay): apply it in `RoomMapViewer`
  only. The editor's contract is to show the truth.
- **Tests**: Vitest + Testing Library. React Flow is heavy in jsdom; reuse
  `RoomMapViewer.test-utils.tsx` / `roomMapEditorTestSetup.tsx`, and see `performance.test.ts`
  and `lazyLoading.test.tsx` for the existing perf and code-split checks.

## 7. Troubleshooting

**[NOTE]**

- **Rooms are scattered or piled up after an editor save**: coordinates were written in pixels.
  Check `saveMapChanges` still divides by `GRID_PITCH`, then run "recalculate" (server BFS) to
  regenerate `map_x` / `map_y` for the zone.
- **Tab freezes opening a large zone**: the zone has more than `MAX_FORCE_LAYOUT_NODES` rooms
  with no stored coordinates; the fallback should have fired. If it did not, check
  `useMapLayout` is passing `useStoredCoordinates`.
- **A building's entrance is not visible**: expected if the exit leads outside the loaded
  sub-zone — look for a `DepartureMarkers` arrow on the source room rather than an edge.
- **Map is noise for a player but fine for an admin in edit mode**: deranged-tier overlay by
  design (#626); the editor ignores `tier`.
- **Minimap shows stale rooms**: `AsciiMinimap` fetches on room change only; there is no polling.
- **`RoomMapEditor` import fails after this change**: import from `components/map/RoomMapEditor`;
  the removed `RoomMapEditorImpl` / `Core` / `Feature` / `Scene` paths no longer exist.

## 8. Related docs

**[SPEC]**

- [`docs/testing/map-regression-tests.md`](../testing/map-regression-tests.md) — map regression
  test proposal.
- [`docs/ROOM_ENVIRONMENT_REFERENCE.md`](../ROOM_ENVIRONMENT_REFERENCE.md) — room environment
  values the editor's `room_environment` field selects from.
- [ADR-022 — UI-v2 client transition](../architecture/decisions/ADR-022-ui-v2-client-transition.md)
  — the component layer that embeds the minimap.
- [ADR-024 — Server-authoritative perceived reality](../architecture/decisions/ADR-024-server-authoritative-perceived-reality.md)
  — background for the hallucination overlay.
- [`docs/architecture/CLIENT_SERVER_AUTHORITY_REGISTER_2026-09.md`](../architecture/CLIENT_SERVER_AUTHORITY_REGISTER_2026-09.md)
  — client/server authority audit that references the map.
- [`docs/packages/README.md`](README.md) — the package coverage index this doc is entered into.

## 9. Changelog

**[SPEC]**

| Version | Date       | Change                                                                                   |
| ------- | ---------- | ---------------------------------------------------------------------------------------- |
| 1.0.0   | 2026-09-29 | Initial version; collapses the `RoomMapEditor` re-export chain; closes #743              |
