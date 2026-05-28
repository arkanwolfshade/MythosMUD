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

const CREATION_CHAR_NAME = `E2ERevised_${Date.now()}`;

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
    page.getByRole('button', { name: 'Accept Stats' }).click(),
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

  await cards.first().click();
  await page.getByRole('button', { name: 'Next' }).click();
}

async function loginAsIthaqua(page: Page): Promise<void> {
  const loginPage = new LoginPage(page);
  await loginPage.navigate();
  await loginPage.login('Ithaqua', 'Cthulhu1');
}

async function deleteRevisedTestCharacterToMakeRoom(page: Page, createButton: Locator): Promise<void> {
  const testCharPattern = /^(E2ERevised_|E4Skills_)/;
  const charHeadings = page.locator('h3');
  const headingCount = await charHeadings.count();

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
    const deleteBtn = card.locator('button.delete-character-button, button:has-text("Delete")').first();
    if (!(await deleteBtn.isVisible({ timeout: 2000 }).catch(() => false))) {
      continue;
    }

    await deleteBtn.click();
    await page.getByText(/Are you sure/i).waitFor({ state: 'visible', timeout: 5000 });
    await page.getByRole('button', { name: /Confirm Delete|confirm|yes|delete/i }).click({ timeout: 5000 });
    await createButton.waitFor({ state: 'visible', timeout: 15000 });
    break;
  }
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
    const canCreate = await createButton.isVisible({ timeout: 2000 }).catch(() => false);

    if (!canCreate) {
      await deleteRevisedTestCharacterToMakeRoom(page, createButton);
    }

    await createButton.click();
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
  await page.getByRole('button', { name: 'Create Character' }).click();
}

async function waitForCharacterCreationLanding(
  page: Page
): Promise<{ hasCharacterList: boolean; hasGameInput: boolean }> {
  await Promise.race([
    page.getByRole('heading', { name: /Select Your Character/i }).waitFor({
      state: 'visible',
      timeout: TEST_TIMEOUTS.LOGIN,
    }),
    page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD }),
  ]);

  const hasCharacterList = await page
    .getByRole('heading', { name: /Select Your Character/i })
    .isVisible()
    .catch(() => false);
  const hasGameInput = await page
    .getByTestId('command-input')
    .isVisible()
    .catch(() => false);
  return { hasCharacterList, hasGameInput };
}

async function enterGameFromCharacterListIfNeeded(page: Page): Promise<void> {
  const onCharacterList = await page
    .getByRole('heading', { name: /Select Your Character/i })
    .isVisible()
    .catch(() => false);
  if (!onCharacterList) {
    return;
  }

  await page
    .getByRole('button', { name: /Select Character/i })
    .first()
    .click();
  await page
    .getByTestId('motd-enter-realm')
    .waitFor({ state: 'visible', timeout: 15000 })
    .catch(() => {});
  await page
    .getByTestId('motd-enter-realm')
    .click()
    .catch(() => {});
}

async function readSkillsMessageText(page: Page): Promise<string> {
  const { executeCommand, waitForMessage, getMessages } = await import('../fixtures/auth');
  await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
  await executeCommand(page, '/skills');
  await waitForMessage(page, /Your skills:/, TEST_TIMEOUTS.MESSAGE);
  return (await getMessages(page)).join('\n');
}

test.describe('Revised Character Creation', () => {
  test.afterAll(async ({ browser }) => {
    const page = await browser.newPage();
    try {
      await cleanupE2ECharacters(page);
    } finally {
      await page.close();
    }
  });

  test('should complete stats → profession → skills → name → create and show character', async ({ page }) => {
    await loginAsIthaqua(page);
    await openStatsRollingFromLogin(page);
    await acceptStatsAndSelectFirstProfession(page);
    await assignAllSkillsAndProceedToName(page);
    await submitCharacterName(page, CREATION_CHAR_NAME);

    const { hasCharacterList, hasGameInput } = await waitForCharacterCreationLanding(page);
    /* eslint-disable playwright/no-conditional-in-test, playwright/no-conditional-expect -- either list or game is valid outcome */
    expect(hasCharacterList || hasGameInput).toBe(true);
    if (hasCharacterList) {
      await expect(page.getByText(CREATION_CHAR_NAME)).toBeVisible({ timeout: 5000 });
    }
    /* eslint-enable playwright/no-conditional-in-test, playwright/no-conditional-expect */
  });

  test('E4: after creation /skills shows character skills (allocated + catalog)', async ({ page }) => {
    await loginAsIthaqua(page);
    await openStatsRollingFromLogin(page);
    await acceptStatsAndSelectFirstProfession(page);
    await assignAllSkillsAndProceedToName(page);
    const charName = `E4Skills_${Date.now()}`;
    await submitCharacterName(page, charName);
    await waitForCharacterCreationLanding(page);
    await enterGameFromCharacterListIfNeeded(page);
    const fullText = await readSkillsMessageText(page);
    expect(/:\s*\d+%/.test(fullText) || fullText.includes('No skills recorded')).toBe(true);
  });
});
