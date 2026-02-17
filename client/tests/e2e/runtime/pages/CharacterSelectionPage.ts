/**
 * Page object for the character selection screen.
 */

import type { Page } from '@playwright/test';

export class CharacterSelectionPage {
  constructor(private readonly page: Page) {}

  async isVisible(): Promise<boolean> {
    return this.page
      .getByRole('heading', { name: /Select Your Character/i })
      .isVisible({ timeout: 2000 })
      .catch(() => false);
  }

  async selectFirstCharacter(): Promise<void> {
    const selectButton = this.page.getByRole('button', { name: /Select Character/i }).first();
    if (await selectButton.isVisible({ timeout: 3000 }).catch(() => false)) {
      await selectButton.click();
    } else {
      const fallback = this.page.getByRole('button', { name: /Select/i }).first();
      if (await fallback.isVisible({ timeout: 3000 }).catch(() => false)) {
        await fallback.click();
      }
    }
    await this.page.waitForLoadState('domcontentloaded', { timeout: 5000 }).catch(() => {});
  }
}
