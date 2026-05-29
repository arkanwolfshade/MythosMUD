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

const PROTECTED_CHARACTER_NAME_SET = new Set<string>(PROTECTED_CHARACTER_NAMES);

/** Regex for character names created by E2E tests (revised creation, skills tests). */
export const TEST_CHARACTER_NAME_PATTERN = /^(E2ERevised_|E4Skills_)/;

const MAX_CLEANUP_ITERATIONS = 10;

type CharacterCardLocator = ReturnType<Page['locator']>;

function isProtected(name: string): boolean {
  return PROTECTED_CHARACTER_NAME_SET.has(name.trim());
}

function isTestCharacter(name: string): boolean {
  return TEST_CHARACTER_NAME_PATTERN.test(name?.trim() ?? '');
}

function isDeletableTestCharacter(name: string): boolean {
  const trimmed = name?.trim() ?? '';
  return trimmed !== '' && !isProtected(trimmed) && isTestCharacter(trimmed);
}

async function domClick(locator: CharacterCardLocator): Promise<void> {
  await locator.evaluate((el: HTMLElement) => {
    el.click();
  });
}

async function loginToCharacterSelection(page: Page): Promise<void> {
  const loginPage = new LoginPage(page);
  await loginPage.navigate();
  await loginPage.login('Ithaqua', 'Cthulhu1');
  await page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});

  const characterSelectionHeading = page.getByRole('heading', { name: /Select Your Character/i });
  await characterSelectionHeading.waitFor({ state: 'visible', timeout: TEST_TIMEOUTS.LOGIN }).catch(() => {});
}

async function isCharacterCreationAvailable(page: Page): Promise<boolean> {
  return page
    .getByRole('button', { name: /Create New Character/i })
    .isVisible({ timeout: 1000 })
    .catch(() => false);
}

async function getCharacterNameFromCard(card: CharacterCardLocator): Promise<string> {
  const nameEl = card.locator('h3.character-name');
  return (await nameEl.textContent({ timeout: 2000 }).catch(() => ''))?.trim() ?? '';
}

async function confirmCharacterDeletion(page: Page): Promise<void> {
  await page
    .getByText(/Are you sure/i)
    .waitFor({ state: 'visible', timeout: 5000 })
    .catch(() => {});
  const confirmBtn = page.getByRole('button', { name: 'Confirm Delete' });
  await domClick(confirmBtn);
  await new Promise(r => setTimeout(r, 1500));
}

async function deleteCharacterFromCard(page: Page, card: CharacterCardLocator): Promise<void> {
  const deleteBtn = card.getByRole('button', { name: 'Delete', exact: true });
  await domClick(deleteBtn);
  await confirmCharacterDeletion(page);
}

async function tryDeleteOneTestCharacter(page: Page): Promise<boolean> {
  const cards = page.locator('.character-card');
  const count = await cards.count();

  for (let i = 0; i < count; i++) {
    const card = cards.nth(i);
    const charName = await getCharacterNameFromCard(card);
    if (!isDeletableTestCharacter(charName)) continue;

    const deleteBtn = card.getByRole('button', { name: 'Delete', exact: true });
    if (!(await deleteBtn.isVisible({ timeout: 2000 }).catch(() => false))) continue;

    await deleteCharacterFromCard(page, card);
    return true;
  }
  return false;
}

/**
 * Logs in as Ithaqua, goes to character selection, and deletes every
 * character whose name matches test patterns and is not protected.
 * Safe to call multiple times; no-op if no test characters exist.
 */
export async function cleanupE2ECharacters(page: Page): Promise<void> {
  await loginToCharacterSelection(page);

  for (let iteration = 0; iteration < MAX_CLEANUP_ITERATIONS; iteration += 1) {
    if (await isCharacterCreationAvailable(page)) {
      return;
    }

    const deleted = await tryDeleteOneTestCharacter(page);
    if (!deleted) {
      return;
    }
  }
}
