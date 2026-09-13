/**
 * The contract between what the database stores and what React Flow draws.
 *
 * These two constants live apart from `layout.ts` because four modules need them -
 * `mapUtils` (load), `useMapLayout` (load), `saveMapChanges` (save) and `layout`
 * (the force-layout guard) - and a save path should not have to import the layout
 * engine to know how to convert a coordinate.
 */

/**
 * Pixels per grid unit.
 *
 * `rooms.map_x` / `map_y` are GRID UNITS: one step per room. That is what the server's
 * CoordinateGenerator BFS writes and what `AsciiMapRenderer` reads via `int(map_x)`.
 * React Flow positions are PIXELS.
 *
 * Before #829 the editor saved raw React Flow pixels straight back into those columns,
 * so a single drag-and-save silently reinterpreted a whole zone's coordinates and
 * corrupted the ASCII minimap, which reads the same columns as grid cells. Multiply on
 * load, divide on save, and never store pixels.
 */
export const GRID_PITCH = 120;

/**
 * Above this many UNPOSITIONED nodes, skip the force simulation entirely.
 *
 * `applyForceLayout` runs `iterations` (800) passes of O(n^2) charge plus O(E^2)
 * edge-pair plus O(E*N) edge-vs-node work, synchronously inside a `useMemo`. At Arkham's
 * ~480 street rooms that is on the order of a billion operations and freezes the tab.
 *
 * This is a hard stop with a loud fallback rather than a scaled iteration count on
 * purpose: quietly reducing iterations turns a freeze into subtly worse placement that
 * nobody can diagnose. In practice it should never fire, because rooms with authored
 * coordinates never reach the simulation at all - it exists for a zone whose coordinates
 * were never generated.
 */
export const MAX_FORCE_LAYOUT_NODES = 200;
