/**
 * Scenario 38: Revised Character Creation (stats → profession → skills → name → create)
 *
 * E2E test for plan 10.8 E1. Ensures the full revised flow completes and the new character
 * appears in the list or game. Uses Ithaqua (run e2e.bat / bootstrap for clean DB).
 * with E2ERevised_/E4Skills_ characters (canonical E2E accounts must use character names
 * ArkanWolfshade and Ithaqua only).
 */

import { expect, test, type Locator, type Page } from '@playwright/test';
import { cleanupE2ECharacters } from '../fixtures/character-cleanup';
import { TEST_TIMEOUTS } from '../fixtures/test-data';
import { LoginPage } from '../pages';

/**
 * Professions screen paints the h1 even when the API returns []; cards mount only with data.
 * Use Promise.all(waitForResponse, click) so a fast /professions response is never missed.
 * Predicate includes r.ok(): the first matching response may be a redirect (e.g. 307); JSON lives on the final hop.
 */
async function acceptStatsAndSelectFirstProfession(page: Page): Promise<void> {
  const [resp] = await Promise.all([
    page.waitForResponse(r => r.url().includes('/professions') && r.request().method() === 'GET' && r.ok(), {
      timeout: 90_000,
    }),
    page.getByRole('button', { name: 'Accept Stats' }).evaluate((el: HTMLElement) => {
      el.click();
    }),
  ]);

  expect(resp.ok(), `GET /professions failed: ${resp.status()}`).toBeTruthy();
  const raw: unknown = await resp.json();
  let count = 0;
  if (Array.isArray(raw)) {
    count = raw.length;
  } else if (raw !== null && typeof raw === 'object' && 'professions' in raw) {
    const inner = (raw as { professions: unknown }).professions;
    count = Array.isArray(inner) ? inner.length : 0;
  }
  expect(
    count,
    `/professions returned ${count} entries (status ${resp.status()}). ` +
      'Run make ensure-e2e-database and restart the E2E server (e2e.bat). ' +
      `Body: ${JSON.stringify(raw).slice(0, 240)}`
  ).toBeGreaterThan(0);

  await expect(page.getByRole('heading', { name: 'Choose Your Profession' })).toBeVisible({ timeout: 30_000 });

  const cards = page.locator('.profession-selection-screen .profession-card');
  await expect
    .poll(async () => cards.count(), {
      timeout: 45_000,
      message: 'Profession cards did not mount after /professions returned data',
    })
    .toBeGreaterThan(0);

  await cards.first().evaluate((el: HTMLElement) => {
    el.click();
  });
  await page.getByRole('button', { name: 'Next' }).evaluate((el: HTMLElement) => {
    el.click();
  });
}

async function loginAsIthaqua(page: Page): Promise<void> {
  const loginPage = new LoginPage(page);
  await loginPage.navigate();
  await loginPage.login('Ithaqua', 'Cthulhu1');
}

async function deleteRevisedTestCharacterToMakeRoom(page: Page, createButton: Locator): Promise<void> {
  const testCharPattern = /^(E2ERevised_|E4Skills_)/;

  for (let attempt = 0; attempt < 6; attempt++) {
    if (await createButton.isVisible({ timeout: 2000 }).catch(() => false)) {
      return;
    }

    const charHeadings = page.locator('h3');
    const headingCount = await charHeadings.count();
    let deletedOne = false;

    for (let i = 0; i < headingCount; i++) {
      const charName =
        (await charHeadings
          .nth(i)
          .textContent()
          .catch(() => '')) ?? '';
      if (!testCharPattern.test(charName)) {
        continue;
      }

      const card = page.locator('.character-card').filter({ hasText: charName });
      const deleteBtn = card.getByRole('button', { name: 'Delete', exact: true });
      if (!(await deleteBtn.isVisible({ timeout: 2000 }).catch(() => false))) {
        continue;
      }

      await deleteBtn.evaluate((el: HTMLElement) => {
        el.click();
      });
      await page.getByText(/Are you sure/i).waitFor({ state: 'visible', timeout: 5000 });
      await page.getByRole('button', { name: 'Confirm Delete' }).evaluate((el: HTMLElement) => {
        el.click();
      });
      await new Promise(r => setTimeout(r, 2000));
      deletedOne = true;
      break;
    }

    if (!deletedOne) {
      break;
    }
  }

  await createButton.waitFor({ state: 'visible', timeout: 20000 });
}

async function openStatsRollingFromLogin(page: Page): Promise<void> {
  await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

  const statsScreen = page.getByTestId('stats-rolling-screen');
  const characterSelectionHeading = page.getByRole('heading', { name: /Select Your Character/i });
  await Promise.race([
    statsScreen.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }),
    characterSelectionHeading.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }),
  ]);

  const onSelectionScreen = await characterSelectionHeading.isVisible().catch(() => false);
  if (onSelectionScreen) {
    const createButton = page.getByRole('button', { name: /Create New Character/i });
    await deleteRevisedTestCharacterToMakeRoom(page, createButton);

    await createButton.evaluate((el: HTMLElement) => {
      el.click();
    });
  }

  await statsScreen.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
}

async function assignAllSkillsAndProceedToName(page: Page): Promise<void> {
  await page.getByTestId('skill-assignment-screen').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
  const combos = page.getByRole('combobox');
  await expect(combos).toHaveCount(13, { timeout: 5000 });
  for (let i = 0; i < 13; i++) {
    await combos.nth(i).selectOption({ index: 1 });
  }
  await page.getByRole('button', { name: 'Next: Name character' }).click();
}

async function submitCharacterName(page: Page, characterName: string): Promise<void> {
  await page.getByTestId('character-name-screen').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
  await page.getByPlaceholder('Enter name').fill(characterName);
  const [createResponse] = await Promise.all([
    page.waitForResponse(r => r.url().includes('/create-character') && r.request().method() === 'POST' && r.ok(), {
      timeout: 90_000,
    }),
    page
      .waitForResponse(
        r =>
          r.url().includes('/characters') &&
          r.request().method() === 'GET' &&
          r.ok() &&
          !r.url().includes('create-character'),
        { timeout: 90_000 }
      )
      .catch(() => null),
    page.getByRole('button', { name: 'Create Character' }).evaluate((el: HTMLElement) => {
      el.click();
    }),
  ]);
  expect(createResponse.ok(), `POST create-character failed: ${createResponse.status()}`).toBeTruthy();
}

async function recoverCharacterSelectionAfterCreation(page: Page): Promise<void> {
  if (page.isClosed()) {
    return;
  }

  const onLogin = await page
    .getByTestId('username-input')
    .isVisible({ timeout: 2000 })
    .catch(() => false);
  if (!onLogin) {
    await page.goto('/');
    await page.waitForLoadState('domcontentloaded');
  }

  const loginPage = new LoginPage(page);
  if (
    await page
      .getByTestId('username-input')
      .isVisible({ timeout: 5000 })
      .catch(() => false)
  ) {
    await loginPage.login('Ithaqua', 'Cthulhu1');
  }

  await page
    .getByRole('heading', { name: /Select Your Character/i })
    .waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN });
}

/** True when creation refresh failed and the UI is on stats, name, or not on selection. */
async function needsRecoveryFromWrongCreationScreen(page: Page): Promise<boolean> {
  const onSelection = await page
    .getByRole('heading', { name: /Select Your Character/i })
    .isVisible()
    .catch(() => false);
  if (!onSelection) {
    return true;
  }
  const onStats = await page
    .getByTestId('stats-rolling-screen')
    .isVisible()
    .catch(() => false);
  if (onStats) {
    return true;
  }
  return await page
    .getByTestId('character-name-screen')
    .isVisible()
    .catch(() => false);
}

async function pollUntilCharacterListed(page: Page, nameLocator: Locator, cardLocator: Locator): Promise<void> {
  if (await nameLocator.isVisible().catch(() => false)) {
    return;
  }

  if (await needsRecoveryFromWrongCreationScreen(page)) {
    await recoverCharacterSelectionAfterCreation(page);
  }

  await expect(cardLocator).toBeVisible({ timeout: 5000 });
}

/**
 * After POST create-character, the client refreshes the character list. Under E2E load that refresh
 * can fail and creationCompleteActions resets the flow to stats — re-login to recover (not reload).
 */
async function assertCharacterVisibleOnList(page: Page, characterName: string): Promise<void> {
  const cardLocator = page.locator('.character-card').filter({ hasText: characterName });
  const nameLocator = page.locator('h3.character-name').filter({ hasText: characterName });

  await page
    .getByRole('heading', { name: /Select Your Character/i })
    .or(page.locator('.character-selection-screen'))
    .waitFor({ state: 'visible', timeout: 30_000 })
    .catch(async () => {
      await recoverCharacterSelectionAfterCreation(page);
    });

  await expect(async () => pollUntilCharacterListed(page, nameLocator, cardLocator)).toPass({
    timeout: 120_000,
    intervals: [1000, 2000, 3000],
  });
}

async function enterGameWithCharacter(page: Page, characterName: string): Promise<void> {
  const card = page.locator('.character-card').filter({
    has: page.locator('h3.character-name', { hasText: characterName }),
  });
  await card.getByRole('button', { name: 'Select Character' }).evaluate((el: HTMLElement) => {
    el.click();
  });
  await page
    .getByTestId('motd-enter-realm')
    .waitFor({ state: 'visible', timeout: 15000 })
    .catch(() => {});
  await page
    .getByTestId('motd-enter-realm')
    .evaluate((el: HTMLElement) => {
      el.click();
    })
    .catch(() => {});
  await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
}

async function readSkillsMessageText(page: Page): Promise<string> {
  const { executeCommand, waitForMessage, getMessages } = await import('../fixtures/auth');
  await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
  await executeCommand(page, '/skills');
  await waitForMessage(page, /Your skills:/, TEST_TIMEOUTS.MESSAGE);
  return (await getMessages(page)).join('\n');
}

test.describe('Revised Character Creation', () => {
  test.beforeAll(async ({ browser }) => {
    const page = await browser.newPage();
    try {
      await cleanupE2ECharacters(page);
    } finally {
      await page.close();
    }
  });

  test.afterAll(async ({ browser }) => {
    const page = await browser.newPage();
    try {
      await cleanupE2ECharacters(page);
    } finally {
      await page.close();
    }
  });

  test('should complete stats → profession → skills → name → create and show character', async ({ page }) => {
    const creationCharName = `E2ERevised_${Date.now()}`;
    await loginAsIthaqua(page);
    await openStatsRollingFromLogin(page);
    await acceptStatsAndSelectFirstProfession(page);
    await assignAllSkillsAndProceedToName(page);
    await submitCharacterName(page, creationCharName);
    await assertCharacterVisibleOnList(page, creationCharName);
    await expect(page.locator('h3.character-name').filter({ hasText: creationCharName })).toBeVisible({
      timeout: 15_000,
    });
  });

  test('E4: after creation /skills shows character skills (allocated + catalog)', async ({ page }) => {
    await loginAsIthaqua(page);
    await openStatsRollingFromLogin(page);
    await acceptStatsAndSelectFirstProfession(page);
    await assignAllSkillsAndProceedToName(page);
    const charName = `E4Skills_${Date.now()}`;
    await submitCharacterName(page, charName);
    await assertCharacterVisibleOnList(page, charName);
    await enterGameWithCharacter(page, charName);
    const fullText = await readSkillsMessageText(page);
    expect(/:\s*\d+%/.test(fullText) || fullText.includes('No skills recorded')).toBe(true);
  });
});
