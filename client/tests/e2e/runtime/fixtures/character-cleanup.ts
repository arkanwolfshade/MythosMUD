/**
 * E2E Character Cleanup
 *
 * Cleans up characters created during E2E tests. NEVER deletes protected
 * characters (ArkanWolfshade, Ithaqua). Only deletes names matching
 * test-creation patterns (e.g. E2ER_, E4Sk_, legacy E2ERevised_, E4Skills_).
 */

import type { Page } from '@playwright/test';
import { LoginPage } from '../pages';
import { TEST_TIMEOUTS } from './test-data';

/** Character names that must never be deleted by E2E cleanup. */
export const PROTECTED_CHARACTER_NAMES = ['ArkanWolfshade', 'Ithaqua'] as const;

const PROTECTED_CHARACTER_NAME_SET = new Set<string>(PROTECTED_CHARACTER_NAMES);

/** Regex for character names created by E2E tests (revised creation, skills tests). */
export const TEST_CHARACTER_NAME_PATTERN = /^(E2ER_|E4Sk_|E2ERevised_|E4Skills_)/;

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

async function getCharacterNameFromCard(card: CharacterCardLocator): Promise<string> {
  const nameEl = card.locator('h3.character-name');
  return (await nameEl.textContent({ timeout: 2000 }).catch(() => ''))?.trim() ?? '';
}

async function confirmCharacterDeletion(page: Page, charName: string): Promise<void> {
  await page
    .getByText(/Are you sure/i)
    .waitFor({ state: 'visible', timeout: 5000 })
    .catch(() => {});
  const confirmBtn = page.getByRole('button', { name: 'Confirm Delete' });
  const deleteResponse = page.waitForResponse(
    r => r.url().includes('/api/players/characters/') && r.request().method() === 'DELETE',
    { timeout: 30_000 }
  );
  await domClick(confirmBtn);
  const resp = await deleteResponse;
  // A 404 means the character is already gone -- exactly what this cleanup fixture wants.
  // It can happen legitimately if the previous iteration's detach wait (below) let the loop
  // re-match a card whose delete had already landed (#777).
  if (!resp.ok() && resp.status() !== 404) {
    throw new Error(`E2E character delete failed: HTTP ${resp.status()}`);
  }
  // Wait for THIS character's card to actually leave the DOM before the next cleanup
  // iteration re-queries .character-card -- waiting for "any card attached" (the old check)
  // is satisfied trivially by the protected Ithaqua card that never leaves, so it resolved
  // before the parent's re-render and let the loop match the same stale card twice, firing
  // a second DELETE for an id the server had already removed (404). Let past a real timeout
  // throw instead of swallowing it -- a card that never detaches is the actual bug to surface,
  // not a signal to silently re-loop over a stale reference.
  await page
    .locator('.character-card')
    .filter({ has: page.locator('h3.character-name', { hasText: charName, exact: true }) })
    .waitFor({ state: 'detached', timeout: TEST_TIMEOUTS.LOGIN });
}

async function deleteCharacterFromCard(page: Page, card: CharacterCardLocator, charName: string): Promise<void> {
  const deleteBtn = card.getByRole('button', { name: 'Delete', exact: true });
  await domClick(deleteBtn);
  await confirmCharacterDeletion(page, charName);
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

    await deleteCharacterFromCard(page, card, charName);
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

  // Do not treat "Create New Character (N/3)" as done — that button stays visible below the
  // 3-character cap and used to make cleanup no-op while leftover E4Skills_* still poisoned login.
  for (let iteration = 0; iteration < MAX_CLEANUP_ITERATIONS; iteration += 1) {
    const deleted = await tryDeleteOneTestCharacter(page);
    if (!deleted) {
      return;
    }
  }
}
