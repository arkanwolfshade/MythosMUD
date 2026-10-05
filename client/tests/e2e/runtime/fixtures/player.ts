/**
 * Player Utilities
 *
 * Helper functions for player management in E2E tests.
 */

import { expect, type Locator, type Page } from '@playwright/test';
import { locationIndicatesDeathVoid, requiredAliveButDeadMessage } from '../../../../src/utils/deathVoidLocation';
import {
  clickWithoutStability,
  ensurePlayableConnection,
  executeCommand,
  getMessages,
  getPageSessionCredentials,
  isVisibleWithin,
  loginPlayer,
  logoutPlayer,
  waitForMessage,
  waitForPlayableSession,
} from './auth';
import { resetE2ePlayerRoomsInDatabase } from './multiplayer';
import { DEFAULT_SPAWN_LOOK_CUE, EASTERN_HALLWAY_LOOK_CUE } from './test-data';

/** Zone key for earth_arkhamcity_sanitarium_room_foyer_001 (npc zone command). */
const SANITARIUM_ZONE_KEY = 'arkhamcity/sanitarium';

/**
 * Best-effort wait: true once `predicate` holds, false if it doesn't within `timeoutMs`.
 * For settle waits that replace fixed sleeps; use `expect` for anything that must hold.
 */
export async function waitUntil(predicate: () => Promise<boolean>, timeoutMs: number): Promise<boolean> {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    if (await predicate()) return true;
    await new Promise(r => setTimeout(r, 250));
  }
  return false;
}

export async function dismissDeathInterstitial(page: Page): Promise<void> {
  const respawnBtn = page.getByRole('button', {
    name: /Rejoin the earthly plane|Returning to the mortal realm/i,
  });
  // Called speculatively while alive too, so only wait for the button when Location already says dead.
  const visible = (await isInDeathVoid(page)) ? await isVisibleWithin(respawnBtn, 5000) : await respawnBtn.isVisible();
  if (visible) {
    await clickWithoutStability(respawnBtn);
    await page
      .getByTestId('command-input')
      .waitFor({ state: 'visible', timeout: 30000 })
      .catch(() => {});
    // Respawn has landed once Location leaves Death > Void (was a fixed 1.5s settle).
    await waitUntil(async () => !(await isInDeathVoid(page)), 5000);
  }
}

async function isInCombatYes(page: Page): Promise<boolean> {
  return page.evaluate(() => /In Combat:\s*Yes/i.test(document.body?.innerText ?? '')).catch(() => false);
}

/** Flee until Character Info shows In Combat: No (or attempts exhausted). */
export async function ensureNotInCombat(page: Page, maxAttempts = 10): Promise<void> {
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    if (!(await isInCombatYes(page))) {
      return;
    }
    await executeCommand(page, 'flee').catch(() => {});
    // Same 1.5s cap as the old fixed sleep, but returns as soon as Character Info shows In Combat: No.
    await waitUntil(async () => !(await isInCombatYes(page)), 1500);
    await dismissDeathInterstitial(page);
  }
}

const CULTIST_INSTANCE_ID_RE = /cultist_of_the_yellow_sign_[a-z0-9_]+/gi;

/** Normalize zone-list matches that glue a trailing "npc" label onto the instance id. */
function normalizeCultistInstanceId(raw: string): string {
  return raw.replace(/npc$/i, '');
}

async function isInDeathVoid(page: Page): Promise<boolean> {
  // Location panel is authoritative; Game Info can retain stale void dumps.
  const body = await page.evaluate(() => document.body?.innerText ?? '').catch(() => '');
  return locationIndicatesDeathVoid(body);
}

/** True when Location shows Death > Void or the respawn interstitial is visible. */
export async function isPlayerDead(page: Page): Promise<boolean> {
  if (await isInDeathVoid(page)) {
    return true;
  }
  const respawnBtn = page.getByRole('button', {
    name: /Rejoin the earthly plane|Returning to the mortal realm/i,
  });
  return respawnBtn.isVisible().catch(() => false);
}

/**
 * Fail fast when a step requires a living player but the page is dead.
 * Do not silent-respawn here — that hides prior-test cleanup bugs.
 */
export async function assertPlayerAlive(page: Page, username: string): Promise<void> {
  if (await isPlayerDead(page)) {
    throw new Error(requiredAliveButDeadMessage(username));
  }
}

/** Collect Cultist of the Yellow Sign instance IDs from npc zone / look text. */
export async function listSanitariumCultistIds(page: Page): Promise<string[]> {
  await executeCommand(page, `npc zone ${SANITARIUM_ZONE_KEY}`);
  await new Promise(r => setTimeout(r, 1200));
  const messages = await getMessages(page);
  const bodyText = await page.evaluate(() => document.body?.innerText ?? '');
  const ids = new Set<string>();
  for (const text of [...messages, bodyText]) {
    for (const match of text.matchAll(CULTIST_INSTANCE_ID_RE)) {
      ids.add(normalizeCultistInstanceId(match[0]));
    }
  }
  return [...ids];
}

/**
 * Despawn Cultist of the Yellow Sign instances left in the sanitarium zone.
 * Requires admin. Uses `npc zone arkhamcity/sanitarium` for instance IDs.
 */
export async function despawnSanitariumCultists(page: Page): Promise<void> {
  const ids = await listSanitariumCultistIds(page);
  for (const id of ids) {
    await executeCommand(page, `npc despawn ${id}`).catch(() => {});
  }
}

/**
 * Respawn after death via the in-app "Rejoin the earthly plane" button only -- retried, but
 * never falling back to ensurePlayableAlive's raw-SQL DB reset.
 *
 * That reset (resetE2ePlayerRoomsInDatabase) fixes current_room_id directly in Postgres, bypassing
 * the server entirely; a container-proximity check right after it can still see the player as
 * being in "limbo_death_void_limbo_death_void" (the respawn button's own server round trip is what
 * actually relocates the player -- admin `set DP` only heals them, it never moves them out of the
 * void room). Use this instead of ensurePlayableAlive whenever the next step is proximity-sensitive
 * (e.g. opening a container in the room the player died in).
 */
async function respawnAfterCombatDeath(page: Page, username: string, password: string): Promise<Page> {
  let live = await ensurePlayableConnection(page, { username, password, timeoutMs: 30000 });
  for (let attempt = 0; attempt < 8; attempt++) {
    await dismissDeathInterstitial(live);
    if (!(await isPlayerDead(live))) {
      // Respawn returns the player to the room they died in -- where the mob that killed them is
      // still standing. It one-shots a freshly respawned player (25 dmg vs 20 DP), sending them
      // straight back to limbo a few seconds later and clobbering the successful respawn's
      // current_room_id write. Clear hostiles first or anything room-sensitive that follows
      // (container proximity checks especially) races a second death.
      await despawnSanitariumCultists(live).catch(() => {});
      live = await ensureStanding(live, 8000).catch(() => live);
      return live;
    }
    await new Promise(r => setTimeout(r, 2000));
  }
  throw new Error(`respawnAfterCombatDeath: still in Death > Void for ${username} after retries`);
}

/**
 * A CorpseOverlay card, narrowed by whether this player may open it.
 *
 * Corpses accumulate in a room across a suite run, and every card renders the same "Corpse",
 * "Grace period ..." and "Open" strings -- so an unscoped locator hits strict-mode violations or
 * silently targets somebody else's corpse.
 */
export function corpseCard(page: Page, opts: { openable: boolean; graceActive?: boolean }): Locator {
  const grace = opts.graceActive === undefined ? '' : `[data-grace-active="${opts.graceActive}"]`;
  return page.locator(`[data-testid="corpse-card"][data-openable="${opts.openable}"]${grace}`);
}

/**
 * The row for `itemText` in a ContainerTransferModal column. Every row has its own "Transfer"
 * button, so a column-wide getByRole('button', { name: 'Transfer' }).first() acts on whichever
 * item the server lists first -- target buttons through this row instead (#980).
 */
export function containerRow(column: Locator, itemText: string): Locator {
  return column.getByRole('listitem').filter({ has: column.page().getByText(itemText, { exact: true }) });
}

/**
 * Click a room corpse's CorpseOverlay Open button, retrying: right after respawn, the server's
 * persisted current_room_id can lag a moment behind the live session (the respawn round trip
 * updates the in-memory/broadcast state immediately but the DB write that /api/containers/open's
 * proximity check reads can trail it briefly), so the very first open attempt can 403. Re-clicking
 * Open is idempotent server-side once it does succeed. Waits for `itemText` (a known item in the
 * corpse) to confirm the transfer modal actually opened.
 */
export async function openCorpseWithRetry(page: Page, itemText: string): Promise<Locator> {
  // Identify the corpse by its CONTENTS, not by position or countdown. A room accumulates
  // corpses across a suite run, and a spec can outlive the 300s grace period, so neither "the
  // first card" nor "the one still counting down" reliably picks the corpse we just made. Try
  // in-grace cards first (normally only ours), then the rest, until a Container column shows the
  // item, and hand that column back so the caller transfers from the right modal.
  const columnWithItem = page
    .getByTestId('transfer-column-container')
    .filter({ has: page.getByText(itemText, { exact: true }) })
    .first();
  const candidates = [
    corpseCard(page, { openable: true, graceActive: true }),
    corpseCard(page, { openable: true, graceActive: false }),
  ];
  await expect(corpseCard(page, { openable: true }).first()).toBeVisible({ timeout: 20000 });

  for (let attempt = 0; attempt < 4; attempt++) {
    for (const cards of candidates) {
      const cardCount = await cards.count();
      for (let index = 0; index < cardCount; index++) {
        const openButton = cards.nth(index).getByRole('button', { name: 'Open' });
        if (!(await openButton.isEnabled().catch(() => false))) {
          continue;
        }
        // CorpseOverlay re-renders every second for its countdown, which can leave Playwright's
        // actionability check never settling. clickWithoutStability dispatches the DOM click
        // directly (same helper dismissDeathInterstitial uses).
        await clickWithoutStability(openButton);
        // A real wait: isVisible({ timeout }) returns immediately, which made this loop click
        // every corpse's Open in quick succession and stack one modal per corpse.
        if (await isVisibleWithin(columnWithItem, 3000)) {
          return columnWithItem;
        }
      }
    }
    // Right after respawn the persisted current_room_id can briefly lag the live session, so
    // /api/containers/open's proximity check 403s; re-clicking is idempotent once it succeeds.
    await new Promise(r => setTimeout(r, 2000));
  }

  await expect(columnWithItem).toBeVisible({ timeout: 15000 });
  return columnWithItem;
}

/**
 * Log out, reset both E2E players' rooms to the spawn room in the database, and log back in.
 * Lands the player in Main Foyer from anywhere, including Death > Void.
 *
 * Must be a real logout before the DB reset: a bare page.goto('/') only drops the WebSocket, the
 * server keeps the player in memory for the linkdead grace period, and session restore reconnects to
 * that in-memory player in its old room, ignoring the reset row (seen: stuck in Sanitarium Chapel).
 * Logging out first also stops the logout's own save from overwriting the reset.
 */
async function relogInAtSpawn(page: Page, username: string, password: string): Promise<Page> {
  // spaFallback bounds the wait when Exit-the-Realm is blocked (void / ward).
  await logoutPlayer(page, 25000, { spaFallback: true }).catch(() => {});
  // Clear the persisted token so loginPlayer gets the login form instead of a session restore.
  await page
    .evaluate(() => {
      localStorage.clear();
      sessionStorage.clear();
    })
    .catch(() => {});
  // Workers=1 default: safe to reset both E2E player rows mid-spec.
  resetE2ePlayerRoomsInDatabase();
  await loginPlayer(page, username, password);
  await waitForPlayableSession(page, 30000);
  await dismissDeathInterstitial(page);
  await executeCommand(page, `admin set DP ${username} 20`).catch(() => {});
  await dismissDeathInterstitial(page);
  const live = await ensurePlayableConnection(page, { username, password, timeoutMs: 30000 });
  await executeCommand(live, 'look').catch(() => {});
  return ensureStanding(live, 8000).catch(() => live);
}

/**
 * Clear death interstitial, combat, and low DP, and put the player in Main Foyer, so later specs
 * see foyer spawn state.
 * Admin DP set is best-effort (non-admins get a harmless failure).
 * Hard-fails if Location stays on Death > Void after recovery attempts, or the player cannot be
 * returned to Main Foyer.
 */
export async function ensurePlayableAlive(page: Page, username: string, password: string): Promise<Page> {
  let live = await ensurePlayableConnection(page, { username, password, timeoutMs: 30000 });
  await dismissDeathInterstitial(live);
  await ensureNotInCombat(live, 4);
  await executeCommand(live, `admin set DP ${username} 20`).catch(() => {});
  await dismissDeathInterstitial(live);
  live = await ensureStanding(live, 8000).catch(() => live);

  // Void blocks most commands. Full DP in limbo skips the death interstitial, so SPA re-login alone
  // reloads persisted limbo — drop client, heal DB rows, then re-enter.
  let recoveredFromVoid = false;
  if (await isInDeathVoid(live)) {
    recoveredFromVoid = true;
    await dismissDeathInterstitial(live);
    await executeCommand(live, `admin set DP ${username} 20`).catch(() => {});
    await dismissDeathInterstitial(live);
  }
  if (await isInDeathVoid(live)) {
    recoveredFromVoid = true;
    live = await relogInAtSpawn(live, username, password);
  }

  if (await isInDeathVoid(live)) {
    throw new Error(`ensurePlayableAlive: still in Death > Void for ${username}`);
  }

  // After void recovery, spawn should be foyer; require it so movement/combat specs do not proceed blind.
  if (recoveredFromVoid) {
    await executeCommand(live, 'look').catch(() => {});
    await expect(live.getByText(DEFAULT_SPAWN_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  }

  // Honour "foyer spawn state": ensureNotInCombat's flee (above) or an earlier spec's movement can
  // leave the player a room or more away, and the corruption specs then failed looking for Main
  // Foyer from the Patient Bedroom. Walk back when one step away; otherwise relog at spawn.
  const beforeReturn = live;
  live = await ensureInMainFoyer(beforeReturn).catch(() => relogInAtSpawn(beforeReturn, username, password));
  const location = await currentLocation(live);
  if (!/Main Foyer/i.test(location)) {
    throw new Error(`ensurePlayableAlive: ${username} is in "${location}", not Main Foyer`);
  }
  return live;
}

/** Location panel line, e.g. "Arkham City > Sanitarium > Main Foyer" (Game Info keeps stale room dumps). */
export async function currentLocation(page: Page): Promise<string> {
  const body = await page.evaluate(() => document.body?.innerText ?? '').catch(() => '');
  return body.match(/Location\s*\n\s*([^\n]+)/i)?.[1]?.trim() ?? '';
}

/**
 * The single way back to Main Foyer from each room a flee out of it can land in (the foyer's
 * up/south/west/east neighbours, per the room exits in the database).
 */
const WAY_BACK_TO_MAIN_FOYER: [RegExp, string][] = [
  [/Sanitarium Entrance/i, 'north'],
  [/Eastern Hallway - Section 1/i, 'west'],
  [/Western Hallway - Section 1/i, 'east'],
  [/Patient Bedroom/i, 'down'],
];

/**
 * Put the player in Main Foyer, the respawn room, before a corpse-producing death (#917).
 *
 * A corpse lies where its owner died, but respawn always returns them to Main Foyer. When
 * ensureNotInCombat's flee had left the player a room away, they died there, respawned in the foyer,
 * and the spec looked for the corpse in the wrong room.
 */
async function ensureInMainFoyer(page: Page): Promise<Page> {
  let live = page;
  const inFoyer = async () => /Main Foyer/i.test(await currentLocation(live));
  if (await inFoyer()) return live;
  live = await prepareForDirectionalMove(live);
  if (await inFoyer()) return live;
  const here = await currentLocation(live);
  const way = WAY_BACK_TO_MAIN_FOYER.find(([room]) => room.test(here))?.[1];
  if (!way) {
    throw new Error(`ensureInMainFoyer: no known way back to Main Foyer from "${here}"`);
  }
  await executeCommand(live, `go ${way}`);
  await expect.poll(inFoyer, { timeout: 20000, message: `return to Main Foyer from "${here}"` }).toBe(true);
  return live;
}

/** Aggressive mob used to trigger real combat death (see combat-messages-game-info.spec.ts). */
const COMBAT_NPC_ID = 58;
const COMBAT_NPC_NAME = 'Cultist of the Yellow Sign';

/**
 * Kill the player through genuine combat so the server's real death path fires
 * (server/services/combat_death_handler.py::_create_corpse_on_death) -- this is the ONLY reachable
 * way to create a container in this game today (environmental and wearable containers have no
 * live data; the generic `admin set DP -9` tick-death path used elsewhere does not create a corpse).
 *
 * Spawns ONE cultist, drops the player to 5 DP, and attacks it. A cultist hits for ~25, so its
 * first landed hit takes the player from 5 straight past -10 -- an unambiguous combat death.
 *
 * One attacker is enough, and more would be wrong: a participant can be in only one combat at a
 * time (combat_service_start.validate_combat_can_start), so extra cultists are refused on every
 * aggro attempt and never land a hit. The tick's wounded-decay death (which creates no corpse)
 * can't pre-empt this either: game_tick_death._player_in_active_combat skips decay while the
 * player is in an active combat.
 *
 * The fight happens in Main Foyer (the respawn room), and `corpsesBefore` counts the openable,
 * in-grace corpse cards there just before it, so the caller can tell a fresh corpse from one an
 * earlier run left inside its 300s grace period.
 */
async function killPlayerViaCombat(
  page: Page,
  creds: { username: string; password: string }
): Promise<{ live: Page; corpsesBefore: number }> {
  let live = await ensurePlayableConnection(page, { ...creds, timeoutMs: 45000 });
  await dismissDeathInterstitial(live);
  await ensureNotInCombat(live, 4);
  live = await ensureStanding(live, 10000);
  await despawnSanitariumCultists(live);
  live = await ensureInMainFoyer(live);
  const corpsesBefore = await corpseCard(live, { openable: true, graceActive: true }).count();
  await executeCommand(live, `npc spawn ${COMBAT_NPC_ID}`);
  await new Promise(r => setTimeout(r, 800));

  // DP 5: still alive (so the tick's wounded-decay death, which creates no corpse, can't claim
  // them) but low enough that a single ~25-damage cultist hit lands well past -10, making the
  // killing blow unambiguously combat damage. Note the e2e teardown leaves DP at 50, above the
  // player's own max of 20, so without this a kill takes three rounds through the wounded band.
  await executeCommand(live, `admin set DP ${creds.username} 5`);
  await new Promise(r => setTimeout(r, 500));

  const ids = await listSanitariumCultistIds(live);
  const target = ids[0] ?? COMBAT_NPC_NAME;
  await executeCommand(live, `attack ${target}`);

  // Re-issue the attack periodically -- a dropped first command or a slow combat round cadence
  // (worse with a second connected player in the room) can otherwise leave the poll waiting on
  // nothing. Re-attacking an already-attacking player is a harmless no-op server-side.
  for (let attempt = 0; attempt < 6; attempt++) {
    // Poll for death for up to 10s (was a fixed 10s sleep), re-attacking only if it hasn't happened.
    const dead = await waitUntil(() => isPlayerDead(live).catch(() => false), 10000);
    if (dead) return { live, corpsesBefore };
    await executeCommand(live, `attack ${target}`).catch(() => {});
  }

  await expect
    .poll(async () => isPlayerDead(live), { timeout: 30000, message: 'player death via real combat' })
    .toBe(true);
  return { live, corpsesBefore };
}

/** True once `locator` matches more than `baseline` elements, false if that doesn't happen in time. */
async function countGrowsWithin(locator: Locator, baseline: number, timeoutMs: number): Promise<boolean> {
  return waitUntil(async () => (await locator.count()) > baseline, timeoutMs);
}

/**
 * Kill the player, respawn them, and guarantee their corpse is actually present in the room.
 *
 * A single kill is not enough: the tick loop can finish off a mortally-wounded player before the
 * mob's next swing lands, and that death path creates no corpse (see killPlayerViaCombat). Retry
 * the whole cycle until the CorpseOverlay shows one. Returns a live, standing page in the room
 * with the corpse visible.
 */
export async function killPlayerAndProduceCorpse(
  page: Page,
  creds: { username: string; password: string },
  maxAttempts = 3
): Promise<Page> {
  let live = page;
  for (let attempt = 0; attempt < maxAttempts; attempt++) {
    const killed = await killPlayerViaCombat(live, creds);
    live = await respawnAfterCombatDeath(killed.live, creds.username, creds.password);
    // `look` forces a fresh room_state, which is what carries the corpse summary to a player who
    // was dead when container.created fired.
    await executeCommand(live, 'look').catch(() => {});
    // Our fresh corpse is one this player may open AND whose grace is still counting down -- and
    // it must be NEW: an earlier run's corpse can still be in grace (300s), and matching it let a
    // death in another room pass here and fail later as an "empty corpse" (#917).
    const inGrace = corpseCard(live, { openable: true, graceActive: true });
    if (await countGrowsWithin(inGrace, killed.corpsesBefore, 25000)) {
      return live;
    }
  }
  throw new Error(`killPlayerAndProduceCorpse: no corpse appeared for ${creds.username} after ${maxAttempts} deaths`);
}

/**
 * Flee combat and stand so `go` is not rejected as "You can't go that way."
 * (MovementService blocks combat/posture with that generic message.)
 */
export async function prepareForDirectionalMove(page: Page): Promise<Page> {
  await ensureNotInCombat(page, 6);
  return ensureStanding(page, 10000);
}

/**
 * Foyer east -> Eastern Hallway. Retries after flee/stand; admin teleport east if combat still blocks go.
 */
export async function goEastFromFoyer(page: Page): Promise<Page> {
  let live = await prepareForDirectionalMove(page);
  await executeCommand(live, 'go east');
  try {
    await waitForMessage(live, /You (move|go) east|Eastern Hallway/i, 20000);
  } catch {
    live = await prepareForDirectionalMove(live);
    await ensureNotInCombat(live, 12);
    await executeCommand(live, 'go east');
    try {
      await waitForMessage(live, /You (move|go) east|Eastern Hallway/i, 25000);
    } catch {
      // move_player returns "You can't go that way." while in combat; admin teleport bypasses that gate.
      const session = getPageSessionCredentials(live);
      const who = session?.username ?? 'ArkanWolfshade';
      await executeCommand(live, `teleport ${who} east`);
      await waitForMessage(live, /teleport|Eastern Hallway|You (move|go) east/i, 25000);
    }
  }
  await executeCommand(live, 'look').catch(() => {});
  await expect(live.getByText(EASTERN_HALLWAY_LOOK_CUE).first()).toBeVisible({ timeout: 20000 });
  return live;
}

/**
 * Ensure the player is standing before movement.
 * Server rejects "go" when sitting; call this before any movement command.
 * Waits for either the posture UI "standing" or the game message (e.g. "You rise to your feet.")
 * so we pass as soon as the server confirms; the Character Info panel can update later.
 * Uses .first() on posture locator (strict mode) and Promise.race with game message.
 *
 * @param page - Playwright page instance
 * @param timeoutMs - Max wait for standing confirmation (default: 10000)
 */
export async function ensureStanding(page: Page, timeoutMs: number = 10000): Promise<Page> {
  let live = page;
  const onLogin = await live
    .getByTestId('username-input')
    .isVisible()
    .catch(() => false);
  if (onLogin) {
    const session = getPageSessionCredentials(live);
    if (session) {
      await loginPlayer(live, session.username, session.password);
      await waitForPlayableSession(live, Math.max(timeoutMs, 15000));
    } else {
      throw new Error('Cannot ensure standing: on login screen with no saved session credentials');
    }
  }

  const alreadyStanding = await live.evaluate(() => {
    const bodyText = document.body?.innerText ?? '';
    return (
      /Posture:\s*standing\b/i.test(bodyText) ||
      /Posture\s*\n\s*standing\b/i.test(bodyText) ||
      /You are already standing/i.test(bodyText)
    );
  });
  if (alreadyStanding) {
    return live;
  }

  const session = getPageSessionCredentials(live);
  if (session) {
    live = await ensurePlayableConnection(live, {
      username: session.username,
      password: session.password,
      timeoutMs: Math.max(timeoutMs, 20000),
    });
  }

  await live.bringToFront().catch(() => {});
  await executeCommand(live, 'stand');
  const halfMs = Math.max(Math.floor(timeoutMs / 2), 4000);
  const standingPredicate = () => {
    const t = document.body?.innerText ?? '';
    if (/You rise to your feet|You are already standing/i.test(t)) return true;
    if (/Posture:\s*standing\b/i.test(t)) return true;
    if (/Posture\s*\n\s*standing\b/i.test(t)) return true;
    return false;
  };
  try {
    await live.waitForFunction(standingPredicate, undefined, { timeout: halfMs });
    return live;
  } catch {
    // Re-issue stand once (sitting/prone lag or first command dropped under load).
    await executeCommand(live, 'stand');
    await live.waitForFunction(standingPredicate, undefined, {
      timeout: Math.max(timeoutMs - halfMs, 5000),
    });
    return live;
  }
}
