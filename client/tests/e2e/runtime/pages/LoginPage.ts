/**
 * Page object for the login screen (App.tsx login form).
 */

import { expect, type Page } from '@playwright/test';

const BASE_URL = 'http://127.0.0.1:5173';

function isLoginPost(responseUrl: string, method: string): boolean {
  return responseUrl.includes('/auth/login') && method === 'POST';
}

export class LoginPage {
  constructor(private readonly page: Page) {}

  async navigate(): Promise<void> {
    await this.page.goto(BASE_URL, { waitUntil: 'load' });
  }

  async login(username: string, password: string): Promise<void> {
    await expect(this.page.getByTestId('username-input')).toBeVisible({ timeout: 30000 });
    await this.page.getByTestId('username-input').fill(username);
    await this.page.getByTestId('password-input').fill(password);

    const loginResponse = this.page.waitForResponse(
      response => isLoginPost(response.url(), response.request().method()),
      { timeout: 30000 }
    );

    const loginButton = this.page.getByTestId('login-button');
    await loginButton.evaluate((el: HTMLElement) => {
      el.click();
    });

    const response = await loginResponse;
    if (!response.ok()) {
      throw new Error(`Login failed: HTTP ${response.status()} ${response.url()}`);
    }
  }
}
