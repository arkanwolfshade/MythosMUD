import { expect, type Page } from '@playwright/test';

import { safeWait } from './wait';

async function sendCommandToPage(page: Page, command: string): Promise<boolean> {
  try {
    const commandInput = page.getByTestId('command-input');
    await expect(commandInput).toBeVisible({ timeout: 10000 });
    await commandInput.clear();
    await commandInput.fill(command);
    await commandInput.press('Enter');
  } catch (error) {
    if (page.isClosed()) {
      return false;
    }
    throw error;
  }
  return true;
}

async function waitForSpecificResponse(
  page: Page,
  expectedResponse: string | RegExp
): Promise<{ responseReceived: boolean; responseText?: string }> {
  try {
    const messageLocator = page.locator('[data-message-text]');
    const filteredLocator =
      typeof expectedResponse === 'string'
        ? messageLocator.filter({ hasText: expectedResponse })
        : messageLocator.filter({ hasText: expectedResponse });

    await expect(filteredLocator.first()).toBeVisible({ timeout: 10000 });

    const firstMessage = messageLocator.first();
    const text = (await firstMessage.getAttribute('data-message-text')) || '';
    return { responseReceived: true, responseText: text || undefined };
  } catch {
    return { responseReceived: false };
  }
}

async function waitForAnyResponse(page: Page): Promise<{ responseReceived: boolean; responseText?: string }> {
  try {
    await page.waitForFunction(
      () => {
        const messages = document.querySelectorAll('[data-message-text]');
        return (
          messages.length > 0 &&
          Array.from(messages).some(msg => {
            const text = msg.getAttribute('data-message-text') || '';
            return text.trim().length > 0;
          })
        );
      },
      { timeout: 10000 }
    );

    const messages = page.locator('[data-message-text]');
    const firstMessage = messages.first();
    const text = (await firstMessage.getAttribute('data-message-text')) || '';
    return { responseReceived: true, responseText: text || undefined };
  } catch {
    return { responseReceived: false };
  }
}

async function waitForResponse(
  page: Page,
  expectedResponse?: string | RegExp
): Promise<{ responseReceived: boolean; responseText?: string }> {
  if (expectedResponse) {
    return waitForSpecificResponse(page, expectedResponse);
  }
  return waitForAnyResponse(page);
}

/** Execute a command and optionally wait for a matching game-log response. */
export async function executeCommand(
  page: Page,
  command: string,
  expectedResponse?: string | RegExp
): Promise<{ sent: boolean; responseReceived: boolean; responseText?: string }> {
  const sent = await sendCommandToPage(page, command);
  if (!sent) {
    return { sent: false, responseReceived: false };
  }

  const { responseReceived, responseText } = await waitForResponse(page, expectedResponse);

  try {
    await safeWait(page, 1000);
  } catch {
    // Page closed after send; command was already submitted
  }

  return {
    sent: true,
    responseReceived,
    responseText: responseText || undefined,
  };
}
