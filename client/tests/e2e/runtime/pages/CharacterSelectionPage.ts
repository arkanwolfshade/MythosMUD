/**
 * Page object for the character selection screen.
 */

import { expect, type Page } from '@playwright/test';

import { TEST_TIMEOUTS } from '../fixtures/test-data';

function isSelectCharacterPost(responseUrl: string, method: string): boolean {
  return responseUrl.includes('select-character') && method === 'POST';
}

export class CharacterSelectionPage {
  constructor(private readonly page: Page) {}

  async isVisible(): Promise<boolean> {
    return this.page
      .getByRole('heading', { name: /Select Your Character/i })
      .isVisible({ timeout: 2000 })
      .catch(() => false);
  }

  async selectFirstCharacter(): Promise<void> {
    await this.selectCharacterByName(null);
  }

  /**
   * Select a character card by display name. When name is null, falls back to the first card
   * (only safe when the account has a single playable character).
   */
  async selectCharacterByName(characterName: string | null): Promise<void> {
    const card =
      characterName === null
        ? this.page.locator('.character-card').first()
        : this.page.locator('.character-card').filter({
            has: this.page.locator('h3.character-name', { hasText: new RegExp(`^${escapeRegExp(characterName)}$`) }),
          });
    const selectButton = card.getByTestId('select-character-button');
    await expect(selectButton).toBeVisible({
      timeout: TEST_TIMEOUTS.LOGIN,
      message:
        characterName === null
          ? 'No character card with Select Character'
          : `Character card not found for name "${characterName}"`,
    });

    const selectResponse = this.page.waitForResponse(
      response => isSelectCharacterPost(response.url(), response.request().method()),
      { timeout: TEST_TIMEOUTS.LOGIN }
    );

    // Firefox: CSS transitions on .character-card can block Playwright "stable" actionability.
    // DOM click + waitForResponse verifies the flow without relying on click stability.
    await selectButton.evaluate((el: HTMLElement) => {
      el.click();
    });

    const response = await selectResponse;
    if (!response.ok()) {
      throw new Error(`Select character failed: HTTP ${response.status()} ${response.url()}`);
    }

    await expect(
      this.page.getByTestId('motd-enter-realm').or(this.page.getByTestId('command-input-panel'))
    ).toBeVisible({
      timeout: TEST_TIMEOUTS.LOGIN,
    });
  }
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
