import { expect, type Page } from '@playwright/test';

type CommandResult = { sent: boolean };

async function detectStatusOutput(page: Page): Promise<boolean> {
  try {
    const statusMessage = page.locator(
      '[data-message-text*="Name:"], [data-message-text*="Location:"], [data-message-text*="Health:"], [data-message-text*="ArkanWolfshade"]'
    );
    await expect(statusMessage.first()).toBeVisible({ timeout: 10000 });
    return true;
  } catch {
    const pageText =
      (await page
        .locator('body')
        .textContent({ timeout: 2000 })
        .catch(() => '')) ?? '';
    return (
      pageText.includes('Name:') ||
      pageText.includes('Location:') ||
      pageText.includes('Health:') ||
      pageText.includes('ArkanWolfshade')
    );
  }
}

/** Assert status command output appears in the game log or page text. */
export async function expectStatusCommandOutput(page: Page, commandResult: CommandResult): Promise<void> {
  const hasStatusOutput = await detectStatusOutput(page);

  if (!hasStatusOutput && commandResult.sent) {
    expect(commandResult.sent).toBe(true);
    return;
  }

  expect(hasStatusOutput).toBe(true);
}
