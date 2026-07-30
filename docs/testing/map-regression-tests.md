# Map regression tests proposal

**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
Tests to add so that the map bugs fixed on the `bug/map` branch do not regress.

## 2. Behaviours fixed (from changelist)

**[NOTE]**

1. **Server – ASCII map context**: Single flow for room load, exploration filter, coordinate generation, and
   `current_room_id` via `_prepare_ascii_map_context`; consistent error handling via `_handle_ascii_map_error`.
2. **Server – Minimap**: Auth/player/room resolution in `_get_minimap_player_and_room_id`; minimap logic in
   `map_minimap.generate_minimap_html` so current room is always included and fallback coordinates apply correctly.
3. **Server – Exit rendering**: Correct horizontal/vertical exit characters (—, >, <, |, v, ^) and viewport bounds
   via `_resolve_exit_target`, `_get_exit_entries_for_room`, `_horizontal_exit_char_between`,
   `_vertical_exit_char_between` in `AsciiMapRenderer`.
4. **Client – AsciiMapViewer**: Logic moved to `useAsciiMap`, viewport sync from server, keyboard handler in
   `asciiMapViewerUtils`; loading/error/content views in `AsciiMapViewerViews`.
5. **Client – AsciiMinimap**: Uses shared `fetchAsciiMinimap` from `api/maps`; effective plane/zone/subZone
   derived from `currentRoomId` when props are missing; `variant` inline vs floating; button semantics and
   inline “No location” placeholder.

---

## 3. Unit tests

**[SPEC]**

### Client

| Area    | File                                                              | What to test                                                                                                                                                                             |
| ------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hook    | `client/src/components/map/__tests__/useAsciiMap.test.ts`         | Viewport sync from server response; initial loading; error state; fetchMap; selected plane/zone/subZone sync when props change; viewport reset when currentRoomId changes.               |
| Utils   | `client/src/components/map/__tests__/asciiMapViewerUtils.test.ts` | `createViewportKeyHandler`: ArrowUp/Down/Left/Right and Home update viewport; no-op when target is input/textarea.                                                                       |
| API     | `client/src/api/__tests__/maps.test.ts`                           | `fetchAsciiMap` / `fetchAsciiMinimap`: correct URL and query params for given options; 4xx/5xx throws; invalid JSON/shape throws; valid response returned.                               |
| Viewer  | `client/src/components/map/__tests__/AsciiMapViewer.test.tsx`     | Renders loading then content when fetch succeeds; shows error + retry when fetch fails; room click calls onRoomSelect with data-room-id.                                                 |
| Minimap | `client/src/components/map/__tests__/AsciiMinimap.test.tsx`       | Effective plane/zone/subZone from currentRoomId when plane/zone/subZone omitted; variant inline shows “No location” when no currentRoomId; uses fetchAsciiMinimap with effective params. |

### Server

| Area            | File                                                          | What to test                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Helpers         | `server/tests/unit/api/test_map_helpers.py`                   | `build_zone_pattern(plane, zone, sub_zone)`; `build_room_dict(row)` with and without optional fields.                                                                                             |
| Minimap helpers | `server/tests/unit/api/test_map_minimap_helpers.py`           | `_append_room_with_fallback_coords_if_needed`; `_apply_minimap_fallback_coordinates` (admin grid vs non-admin current room only).                                                                 |
| Renderer exits  | `server/tests/unit/services/test_ascii_map_renderer_exits.py` | `_horizontal_exit_char_between` and `_vertical_exit_char_between` return —, >, < and \|, v, ^ for bidirectional/one-way; `_resolve_exit_target` and `_get_exit_entries_for_room` with mock rooms. |

---

## 4. E2E (Playwright)

**[SPEC]**

| Scenario        | File                                                  | What to test                                                                                                                       |
| --------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Map page load   | `client/tests/e2e/runtime/map/ascii-map-page.spec.ts` | Authenticated user can open /map (e.g. from main menu or direct URL); page shows loading then map content or error; no hard crash. |
| Minimap in game | Same or `minimap-visible.spec.ts`                     | After entering game, UI shows minimap (or “No location” in inline variant); clicking opens full map.                               |

E2E depends on test env having at least one room with coordinates; if not, test “map page loads and shows loading/error” only.

---

## 5. Implementation status

**[SPEC]**

- [x] Client: useAsciiMap.test.ts
- [x] Client: asciiMapViewerUtils.test.ts
- [x] Client: api/maps.test.ts
- [ ] Client: AsciiMapViewer.test.tsx
- [ ] Client: AsciiMinimap.test.tsx
- [x] Server: test_map_helpers.py
- [x] Server: test_map_minimap_helpers.py
- [x] Server: test_ascii_map_renderer_exits.py
- [ ] E2E: ascii-map-page.spec.ts (and optionally minimap-visible.spec.ts)

## 6. Changelog

**[SPEC]**

| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
