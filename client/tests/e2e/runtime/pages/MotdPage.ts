/**
 * Page object for the MOTD (Message of the Day) / Enter the Realm screen.
 */

import type { Page } from '@playwright/test';

export class MotdPage {
  constructor(private readonly page: Page) {}

  async enterRealm(): Promise<void> {
    const button = this.page
      .getByTestId('motd-enter-realm')
      .or(this.page.getByRole('button', { name: /Enter the Realm/i }));
    await button
      .first()
      .click({ timeout: 5000 })
      .catch(() => {
        return this.page.evaluate(() => {
          const btn = document.querySelector('[data-testid="motd-enter-realm"]') as HTMLElement;
          if (btn) btn.click();
        });
      });
  }

  async waitForGameReady(timeoutMs: number): Promise<void> {
    await Promise.race([
      this.page.getByText('Game Info', { exact: false }).waitFor({ state: 'visible', timeout: timeoutMs }),
      this.page.locator('[data-message-text]').first().waitFor({ state: 'visible', timeout: timeoutMs }),
      this.page.getByTestId('command-input').waitFor({ state: 'visible', timeout: timeoutMs }),
    ]).catch(() => {});
  }
}
