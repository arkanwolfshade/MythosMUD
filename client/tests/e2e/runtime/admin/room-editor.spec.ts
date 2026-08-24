/**
 * Room editor E2E (#627): admin room-property and exit persistence round trips.
 *
 * Exercises PUT /rooms/{room_id} and the exits CRUD endpoints. Changes are verified via
 * GET /rooms/list (proves RoomRepository memory stays in sync with Postgres, not just DB
 * write success) and then reverted so shared e2e room data is left as found.
 *
 * UI map-editor clicks are intentionally avoided here: Firefox + React Flow layout churn
 * makes modal/tab/Save hit-testing unreliable; the persistence bug this suite guards is
 * server-side.
 */

import { expect, test, type Page } from '@playwright/test';
import { loginPlayer } from '../fixtures/auth';

const ADMIN_USERNAME = 'ArkanWolfshade';
const ADMIN_PASSWORD = 'Cthulhu1';
const PLANE = 'earth';
const ZONE = 'arkhamcity';
const SUB_ZONE = 'sanitarium';

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

async function adminApiHeaders(page: Page): Promise<Record<string, string>> {
  const login = await page.request.post('/v1/auth/login', {
    data: { username: ADMIN_USERNAME, password: ADMIN_PASSWORD },
  });
  expect(login.ok(), `admin login for API: ${login.status()}`).toBeTruthy();
  const body = (await login.json()) as { access_token?: string };
  expect(body.access_token, 'login must return access_token').toBeTruthy();
  return {
    Authorization: `Bearer ${body.access_token}`,
    'Content-Type': 'application/json',
  };
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
    test.setTimeout(120_000);
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
    const headers = await adminApiHeaders(page);

    const put = await page.request.put(`/v1/api/rooms/${encodeURIComponent(room.id)}`, {
      headers,
      data: { environment: newEnvironment },
    });
    expect(put.ok(), `put environment: ${put.status()} ${await put.text()}`).toBeTruthy();

    const afterChange = await listSubzoneRooms(page);
    expect(afterChange.find(r => r.id === room.id)?.environment).toBe(newEnvironment);

    const revert = await page.request.put(`/v1/api/rooms/${encodeURIComponent(room.id)}`, {
      headers,
      data: { environment: originalEnvironment },
    });
    expect(revert.ok(), `revert environment: ${revert.status()} ${await revert.text()}`).toBeTruthy();

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

    const headers = await adminApiHeaders(page);
    const createResp = await page.request.post(`/v1/api/rooms/${encodeURIComponent(source.id)}/exits`, {
      headers,
      data: { direction, target_room_id: target.id },
    });
    expect(createResp.ok(), `create exit: ${createResp.status()} ${await createResp.text()}`).toBeTruthy();

    const afterCreate = await listSubzoneRooms(page);
    expect(afterCreate.find(r => r.id === source.id)?.exits[direction]).toBe(target.id);

    const deleteResp = await page.request.delete(
      `/v1/api/rooms/${encodeURIComponent(source.id)}/exits/${encodeURIComponent(direction)}`,
      { headers }
    );
    expect(deleteResp.ok(), `delete exit: ${deleteResp.status()} ${await deleteResp.text()}`).toBeTruthy();

    const afterDelete = await listSubzoneRooms(page);
    expect(direction in (afterDelete.find(r => r.id === source.id)?.exits ?? {})).toBe(false);
  });
});
