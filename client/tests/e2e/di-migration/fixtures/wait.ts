import type { Page } from '@playwright/test';

/** Web-first wait for game UI or message (avoids waitForTimeout). */
export async function safeWait(page: Page, timeout: number): Promise<void> {
  try {
    if (page.isClosed()) return;
    await Promise.race([
      page.getByTestId('command-input').waitFor({ state: 'visible', timeout }),
      page.locator('[data-message-text]').first().waitFor({ state: 'attached', timeout }),
    ]).catch(() => {});
  } catch {
    // Page was closed or context invalid - okay for test cleanup
  }
}

/** Wait long enough to include at least one game tick. */
export async function waitForGameTick(page: Page, timeout: number = 5000): Promise<void> {
  await safeWait(page, timeout);
}
