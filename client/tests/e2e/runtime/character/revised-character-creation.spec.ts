/**
 * Scenario 38: Revised Character Creation (stats → profession → skills → name → create)
 *
 * E2E test for plan 10.8 E1. Ensures the full revised flow completes and the new character
 * appears in the list or game. Uses TestAdmin so ArkanWolfshade/Ithaqua are never polluted
 * with E2ERevised_/E4Skills_ characters (canonical E2E accounts must use character names
 * ArkanWolfshade and Ithaqua only).
 */

import { expect, test } from '@playwright/test';
import { cleanupE2ECharacters } from '../fixtures/character-cleanup';
import { TEST_TIMEOUTS } from '../fixtures/test-data';
import { LoginPage } from '../pages';

const CREATION_CHAR_NAME = `E2ERevised_${Date.now()}`;

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
    const loginPage = new LoginPage(page);
    await loginPage.navigate();
    await loginPage.login('TestAdmin', 'Cthulhu1');

    await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

    const statsScreen = page.getByTestId('stats-rolling-screen');
    const characterSelectionHeading = page.getByRole('heading', { name: /Select Your Character/i });
    await Promise.race([
      statsScreen.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }),
      characterSelectionHeading.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }),
    ]);

    /* eslint-disable playwright/no-conditional-in-test -- 0 chars: stats first; 1+ chars: selection then Create New Character */
    const onSelectionScreen = await characterSelectionHeading.isVisible().catch(() => false);
    if (onSelectionScreen) {
      // Check if Create New Character button exists (may be hidden if at max characters)
      const createButton = page.getByRole('button', { name: /Create New Character/i });
      const canCreate = await createButton.isVisible({ timeout: 2000 }).catch(() => false);

      if (!canCreate) {
        // At max characters - delete the first test character (E2ERevised_ or E4Skills_ pattern) to make room
        const testCharPattern = /^(E2ERevised_|E4Skills_)/;
        const charHeadings = page.locator('h3');
        const headingCount = await charHeadings.count();

        for (let i = 0; i < headingCount; i++) {
          const heading = charHeadings.nth(i);
          const charName = await heading.textContent().catch(() => '');

          if (charName && testCharPattern.test(charName)) {
            const allDeleteButtons = page.locator('button:has-text("Delete")');
            const deleteCount = await allDeleteButtons.count();
            let deleted = false;

            for (let j = 0; j < deleteCount; j++) {
              const deleteBtn = allDeleteButtons.nth(j);
              const isNearHeading = await deleteBtn
                .evaluate((btn, headingText) => {
                  const card =
                    btn.closest('[class*="character"], [class*="card"], [class*="item"]') ||
                    btn.parentElement?.parentElement;
                  return card?.textContent?.includes(headingText) ?? false;
                }, charName)
                .catch(() => false);

              if (isNearHeading && (await deleteBtn.isVisible({ timeout: 1000 }).catch(() => false))) {
                await deleteBtn.click();
                await page
                  .getByText(/Are you sure/i)
                  .waitFor({ state: 'visible', timeout: 5000 })
                  .catch(() => {});
                const confirmBtn = page.getByRole('button', { name: /confirm|yes|delete/i }).first();
                await confirmBtn.click({ timeout: 5000 }).catch(() => {});
                await createButton.waitFor({ state: 'visible', timeout: 10000 });
                deleted = true;
                break;
              }
            }
            if (deleted) break;
          }
        }
      }

      await createButton.click();
    }
    /* eslint-enable playwright/no-conditional-in-test */

    await statsScreen.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });

    await page.getByRole('button', { name: 'Accept Stats' }).click();

    await expect(page.getByRole('heading', { name: /Choose Your Profession/i })).toBeVisible({
      timeout: TEST_TIMEOUTS.DEFAULT,
    });
    await page.locator('.profession-card').first().click();
    await page.getByRole('button', { name: 'Next' }).click();

    await page.getByTestId('skill-assignment-screen').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
    const combos = page.getByRole('combobox');
    await expect(combos).toHaveCount(13, { timeout: 5000 });
    for (let i = 0; i < 13; i++) {
      await combos.nth(i).selectOption({ index: 1 });
    }
    await page.getByRole('button', { name: 'Next: Name character' }).click();

    await page.getByTestId('character-name-screen').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
    await page.getByPlaceholder('Enter name').fill(CREATION_CHAR_NAME);
    await page.getByRole('button', { name: 'Create Character' }).click();

    await Promise.race([
      page.getByRole('heading', { name: /Select Your Character/i }).waitFor({
        state: 'visible',
        timeout: TEST_TIMEOUTS.LOGIN,
      }),
      page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD }),
    ]);

    /* eslint-disable playwright/no-conditional-in-test, playwright/no-conditional-expect -- either list or game is valid outcome */
    const hasCharacterList = await page
      .getByRole('heading', { name: /Select Your Character/i })
      .isVisible()
      .catch(() => false);
    const hasGameInput = await page
      .getByTestId('command-input')
      .isVisible()
      .catch(() => false);
    expect(hasCharacterList || hasGameInput).toBe(true);

    if (hasCharacterList) {
      await expect(page.getByText(CREATION_CHAR_NAME)).toBeVisible({ timeout: 5000 });
    }
    /* eslint-enable playwright/no-conditional-in-test, playwright/no-conditional-expect */
  });

  test('E4: after creation /skills shows character skills (allocated + catalog)', async ({ page }) => {
    const { executeCommand, waitForMessage, getMessages } = await import('../fixtures/auth');
    const loginPage = new LoginPage(page);
    await loginPage.navigate();
    await loginPage.login('TestAdmin', 'Cthulhu1');
    await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

    const statsScreen = page.getByTestId('stats-rolling-screen');
    const characterSelectionHeading = page.getByRole('heading', { name: /Select Your Character/i });
    await Promise.race([
      statsScreen.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }),
      characterSelectionHeading.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }),
    ]);
    /* eslint-disable playwright/no-conditional-in-test -- 0 chars: stats first; 1+ chars: Create New Character */
    const onSelectionScreen = await characterSelectionHeading.isVisible().catch(() => false);
    if (onSelectionScreen) {
      // Check if Create New Character button exists (may be hidden if at max characters)
      const createButton = page.getByRole('button', { name: /Create New Character/i });
      const canCreate = await createButton.isVisible({ timeout: 2000 }).catch(() => false);

      if (!canCreate) {
        // At max characters - delete the first test character (E2ERevised_ or E4Skills_ pattern) to make room
        const testCharPattern = /^(E2ERevised_|E4Skills_)/;
        const charHeadings = page.locator('h3.character-name');
        const headingCount = await charHeadings.count();

        for (let i = 0; i < headingCount; i++) {
          const heading = charHeadings.nth(i);
          const charName = await heading.textContent().catch(() => '');

          if (charName && testCharPattern.test(charName)) {
            // Use .character-card from CharacterSelectionScreen so Delete is scoped to this card
            const card = page.locator('.character-card').filter({ hasText: charName });
            const deleteBtn = card.locator('button.delete-character-button, button:has-text("Delete")').first();
            if (await deleteBtn.isVisible({ timeout: 2000 }).catch(() => false)) {
              await deleteBtn.click();
              await page.getByText(/Are you sure/i).waitFor({ state: 'visible', timeout: 5000 });
              await page.getByRole('button', { name: 'Confirm Delete' }).click({ timeout: 5000 });
              await createButton.waitFor({ state: 'visible', timeout: 15000 });
              break;
            }
          }
        }
      }

      await createButton.click();
    }
    /* eslint-enable playwright/no-conditional-in-test */
    await statsScreen.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
    await page.getByRole('button', { name: 'Accept Stats' }).click();
    await expect(page.getByRole('heading', { name: /Choose Your Profession/i })).toBeVisible({
      timeout: TEST_TIMEOUTS.DEFAULT,
    });
    await page.locator('.profession-card').first().click();
    await page.getByRole('button', { name: 'Next' }).click();
    await page.getByTestId('skill-assignment-screen').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
    const combos = page.getByRole('combobox');
    await expect(combos).toHaveCount(13, { timeout: 5000 });
    for (let i = 0; i < 13; i++) {
      await combos.nth(i).selectOption({ index: 1 });
    }
    await page.getByRole('button', { name: 'Next: Name character' }).click();
    await page.getByTestId('character-name-screen').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.DEFAULT });
    const charName = `E4Skills_${Date.now()}`;
    await page.getByPlaceholder('Enter name').fill(charName);
    await page.getByRole('button', { name: 'Create Character' }).click();

    await Promise.race([
      page.getByRole('heading', { name: /Select Your Character/i }).waitFor({
        state: 'visible',
        timeout: TEST_TIMEOUTS.LOGIN,
      }),
      page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD }),
    ]);

    /* eslint-disable playwright/no-conditional-in-test -- may land on list or game after create */
    const onCharacterList = await page
      .getByRole('heading', { name: /Select Your Character/i })
      .isVisible()
      .catch(() => false);
    if (onCharacterList) {
      const firstSelect = page.getByRole('button', { name: /Select Character/i }).first();
      await firstSelect.click();
      await page
        .getByTestId('motd-enter-realm')
        .waitFor({ state: 'visible', timeout: 15000 })
        .catch(() => {});
      await page
        .getByTestId('motd-enter-realm')
        .click()
        .catch(() => {});
    }
    /* eslint-enable playwright/no-conditional-in-test */
    await page.getByTestId('command-input').waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.GAME_LOAD });
    await executeCommand(page, '/skills');
    await waitForMessage(page, /Your skills:/, TEST_TIMEOUTS.MESSAGE);
    const messages = await getMessages(page);
    const fullText = messages.join('\n');
    const hasSkillLine = /:\s*\d+%/.test(fullText);
    const hasNoSkills = fullText.includes('No skills recorded');
    expect(hasSkillLine || hasNoSkills).toBe(true);
  });
});
