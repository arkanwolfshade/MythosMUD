/**
 * Room editor E2E (#627): admin room-property and exit-editing round trip via the map editor.
 *
 * Exercises PUT /rooms/{room_id} and the exits CRUD endpoints end to end through the UI --
 * every change is verified via a page reload (proves persistence, not just optimistic client
 * state) and then reverted, so the shared e2e room data is left exactly as found.
 */

import { expect, test, type Page } from '@playwright/test';
import { loginPlayer } from '../fixtures/auth';
import { TEST_TIMEOUTS } from '../fixtures/test-data';

const ADMIN_USERNAME = 'ArkanWolfshade';
const ADMIN_PASSWORD = 'Cthulhu1';
const PLANE = 'earth';
const ZONE = 'arkhamcity';
const SUB_ZONE = 'sanitarium';

/**
 * mapPageState.ts only threads plane/zone/subZone from the URL when roomId is ALSO present --
 * without one it silently falls back to the zone-wide default with no subzone filter. A roomId
 * is required here to actually scope the editor to the sanitarium subzone rather than rendering
 * every room in arkhamcity.
 */
function mapEditUrl(roomId: string): string {
  return `/map?edit=true&roomId=${roomId}&plane=${PLANE}&zone=${ZONE}&subZone=${SUB_ZONE}`;
}

// Must match server/models/command_base.py::Direction -- see #627's direction-parity fix.
const STANDARD_DIRECTIONS = [
  'north',
  'south',
  'east',
  'west',
  'up',
  'down',
  'northeast',
  'northwest',
  'southeast',
  'southwest',
];

interface RoomSummary {
  id: string;
  name: string;
  environment?: string | null;
  exits: Record<string, string | null>;
}

async function listSubzoneRooms(page: Page): Promise<RoomSummary[]> {
  const response = await page.request.fetch(
    `/v1/api/rooms/list?plane=${PLANE}&zone=${ZONE}&sub_zone=${SUB_ZONE}&include_exits=true`
  );
  expect(response.ok(), 'GET /api/rooms/list should succeed unauthenticated').toBeTruthy();
  const body = (await response.json()) as { rooms: RoomSummary[] };
  return body.rooms;
}

function roomNode(page: Page, roomId: string) {
  return page.getByTestId(`rf__node-${roomId}`);
}

/**
 * useMapLayout recomputes all node positions on every interaction (unrelated pre-existing
 * performance characteristic, not introduced by #627), and rooms without a persisted map_x/
 * map_y fall back to a dense auto-layout grid where adjacent nodes can visually overlap -- a
 * plain click can land on whichever node paints on top, and Firefox under automation load needs
 * generous headroom regardless. force + a long timeout is used for every interactive click in
 * this spec, not just the room node, for the same reasons.
 */
const CLICK_OPTS = { force: true, timeout: 60_000 } as const;

async function clickRoomNode(page: Page, roomId: string): Promise<void> {
  await roomNode(page, roomId).click(CLICK_OPTS);
}

/**
 * Click the toolbar Save button, auto-accepting the native window.confirm() it raises, then
 * wait for the "Unsaved changes" banner to clear -- that only happens once save() resolves.
 *
 * Pre-existing UI bug found while writing this spec: RoomDetailsPanel (z-20) and
 * MapEditToolbar (z-10) both render `absolute top-4 right-4` on the same positioning context,
 * so whenever the details panel is open it always wins the hit-test over the Save button
 * underneath, on any viewport size -- not a Playwright quirk. Closing the panel first here
 * works around it for the test; the underlying overlap was reported separately, out of #627's
 * scope.
 */
async function saveAndConfirm(page: Page): Promise<void> {
  // Panel may already be closed; ignore missing Close so we do not branch in the test body.
  await page
    .getByRole('button', { name: /close panel/i })
    .click(CLICK_OPTS)
    .catch(() => undefined);
  page.once('dialog', dialog => dialog.accept());
  await page.getByRole('button', { name: /save/i }).click(CLICK_OPTS);
  await expect(page.getByText(/unsaved changes/i)).not.toBeVisible({ timeout: 60_000 });
}

/** Seed prerequisites fail the test (do not soft-skip); keeps playwright/no-skipped-test clean. */
function requireDefined<T>(value: T | undefined | null, message: string): T {
  expect(value, message).toBeTruthy();
  if (value == null) {
    throw new Error(message);
  }
  return value;
}

function flippedEnvironment(current: string): string {
  return current === 'indoors' ? 'outdoors' : 'indoors';
}

test.describe('room editor (#627)', () => {
  test.describe.configure({ mode: 'serial' });

  test.beforeEach(async ({ page }) => {
    // useMapLayout recomputes all node positions on every interaction (unrelated pre-existing
    // performance characteristic, not introduced by #627) -- Firefox under load needs generous
    // headroom on top of this suite's usual budget.
    test.setTimeout(300_000);
    await loginPlayer(page, ADMIN_USERNAME, ADMIN_PASSWORD);
  });

  test('room property edit persists across reload, then reverts', async ({ page }) => {
    const rooms = await listSubzoneRooms(page);
    const room = requireDefined(
      rooms.find(r => r.name?.trim()),
      'No named rooms found in earth/arkhamcity/sanitarium seed data'
    );

    const originalEnvironment = room.environment ?? '';
    const newEnvironment = flippedEnvironment(originalEnvironment);

    await page.goto(mapEditUrl(room.id), { waitUntil: 'domcontentloaded' });
    await roomNode(page, room.id).waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });

    const setEnvironment = async (value: string): Promise<void> => {
      await clickRoomNode(page, room.id);
      // RoomDetailsPanel and MapEditToolbar are both `absolute top-4 right-4`, one stacked on
      // the other by z-index alone -- force bypasses Firefox's hit-test ambiguity at that shared
      // anchor rather than waiting out a spurious actionability timeout.
      await page.getByRole('button', { name: 'Edit Room' }).click(CLICK_OPTS);
      await page.getByRole('tab', { name: /properties/i }).click(CLICK_OPTS);
      await page.getByLabel(/environment type/i).selectOption(value);
      await page.getByRole('button', { name: /update room/i }).click(CLICK_OPTS);
      await saveAndConfirm(page);
    };

    await setEnvironment(newEnvironment);

    await page.reload({ waitUntil: 'domcontentloaded' });
    const afterChange = await listSubzoneRooms(page);
    expect(afterChange.find(r => r.id === room.id)?.environment).toBe(newEnvironment);

    // Revert so the shared e2e room data is left as found.
    await setEnvironment(originalEnvironment);

    await page.reload({ waitUntil: 'domcontentloaded' });
    const reverted = await listSubzoneRooms(page);
    expect(reverted.find(r => r.id === room.id)?.environment).toBe(originalEnvironment);
  });

  test('exit create/delete round trip persists and cleans up', async ({ page }) => {
    const rooms = await listSubzoneRooms(page);
    const source = requireDefined(
      rooms.find(r => r.name?.trim()),
      'No named rooms found in earth/arkhamcity/sanitarium seed data'
    );
    const target = requireDefined(
      rooms.find(r => r.id !== source.id && r.name?.trim()),
      'Need at least two named rooms in earth/arkhamcity/sanitarium seed data'
    );
    const direction = requireDefined(
      STANDARD_DIRECTIONS.find(d => !(d in source.exits)),
      `Room ${source.id} already has every standard exit direction occupied`
    );

    const edgeId = `${source.id}-${direction}-${target.id}`;

    await page.goto(mapEditUrl(source.id), { waitUntil: 'domcontentloaded' });
    await roomNode(page, source.id).waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });

    // Create the exit.
    await clickRoomNode(page, source.id);
    await page.getByRole('button', { name: 'Create Exit' }).click(CLICK_OPTS);
    await page.getByLabel(/to room:/i).selectOption(target.id);
    await page.getByLabel('Direction:').selectOption(direction);
    await page.getByRole('button', { name: /create exit/i }).click(CLICK_OPTS);
    await saveAndConfirm(page);

    await page.reload({ waitUntil: 'domcontentloaded' });
    const afterCreate = await listSubzoneRooms(page);
    expect(afterCreate.find(r => r.id === source.id)?.exits[direction]).toBe(target.id);

    // Delete it again, leaving the shared e2e room data as found.
    await page.locator(`[data-id="${edgeId}"]`).first().click(CLICK_OPTS);
    await page.getByRole('button', { name: 'Delete Exit' }).click(CLICK_OPTS);
    await page.getByRole('button', { name: 'Confirm Delete' }).click(CLICK_OPTS);
    await saveAndConfirm(page);

    await page.reload({ waitUntil: 'domcontentloaded' });
    const afterDelete = await listSubzoneRooms(page);
    expect(direction in (afterDelete.find(r => r.id === source.id)?.exits ?? {})).toBe(false);
  });
});
