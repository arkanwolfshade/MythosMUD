/**
 * Page object for the login screen (App.tsx login form).
 */

import { expect, type Page } from '@playwright/test';

const BASE_URL = 'http://localhost:5173';

export class LoginPage {
  constructor(private readonly page: Page) {}

  async navigate(): Promise<void> {
    await this.page.goto(BASE_URL, { waitUntil: 'load' });
  }

  async login(username: string, password: string): Promise<void> {
    await expect(this.page.getByTestId('username-input')).toBeVisible({ timeout: 30000 });
    await this.page.getByTestId('username-input').fill(username);
    await this.page.getByTestId('password-input').fill(password);
    await this.page.getByTestId('login-button').click();
  }
}
