/**
 * E2E Character Cleanup
 *
 * Cleans up characters created during E2E tests. NEVER deletes protected
 * characters (ArkanWolfshade, Ithaqua). Only deletes names matching
 * test-creation patterns (e.g. E2ERevised_*, E4Skills_*).
 */

import type { Page } from '@playwright/test';
import { LoginPage } from '../pages';
import { TEST_TIMEOUTS } from './test-data';

/** Character names that must never be deleted by E2E cleanup. */
export const PROTECTED_CHARACTER_NAMES = ['ArkanWolfshade', 'Ithaqua'] as const;

/** Regex for character names created by E2E tests (revised creation, skills tests). */
export const TEST_CHARACTER_NAME_PATTERN = /^(E2ERevised_|E4Skills_)/;

function isProtected(name: string): boolean {
  const trimmed = name?.trim() ?? '';
  return PROTECTED_CHARACTER_NAMES.some(p => p === trimmed);
}

function isTestCharacter(name: string): boolean {
  return TEST_CHARACTER_NAME_PATTERN.test(name?.trim() ?? '');
}

/**
 * Logs in as TestAdmin, goes to character selection, and deletes every
 * character whose name matches test patterns and is not protected.
 * Safe to call multiple times; no-op if no test characters exist.
 */
export async function cleanupE2ECharacters(page: Page): Promise<void> {
  const loginPage = new LoginPage(page);
  await loginPage.navigate();
  await loginPage.login('TestAdmin', 'Cthulhu1');
  await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

  const characterSelectionHeading = page.getByRole('heading', { name: /Select Your Character/i });
  await characterSelectionHeading.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }).catch(() => {});

  let deletedAny = true;
  while (deletedAny) {
    deletedAny = false;
    const cards = page.locator('.character-card');
    const count = await cards.count();

    for (let i = 0; i < count; i++) {
      const card = cards.nth(i);
      const nameEl = card.locator('h3.character-name');
      const charName = (await nameEl.textContent({ timeout: 2000 }).catch(() => ''))?.trim() ?? '';
      if (!charName || isProtected(charName) || !isTestCharacter(charName)) continue;

      const deleteBtn = card.locator('button.delete-character-button, button:has-text("Delete")').first();
      if (!(await deleteBtn.isVisible({ timeout: 2000 }).catch(() => false))) continue;

      await deleteBtn.click();
      await page
        .getByText(/Are you sure/i)
        .waitFor({ state: 'visible', timeout: 5000 })
        .catch(() => {});
      const confirmBtn = page.getByRole('button', { name: /Confirm Delete|confirm|yes|delete/i }).first();
      await confirmBtn.click({ timeout: 5000 }).catch(() => {});
      await new Promise(r => setTimeout(r, 1500));
      deletedAny = true;
      break;
    }
  }
}
