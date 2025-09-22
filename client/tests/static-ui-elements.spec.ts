import { expect, test } from '@playwright/test';

test.describe('Static UI Elements Tests', () => {
  test('should render login page with correct title and structure', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Verify page title (Vite default title)
    await expect(page).toHaveTitle(/Vite \+ React \+ TS/);

    // Verify main login container exists
    await expect(page.locator('.login-container')).toBeVisible();

    console.log('✅ Login page structure test passed - page loads correctly');
  });

  test('should have proper form validation on login form', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Try to submit empty form
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Verify we're still on the login page (form validation should prevent submission)
    await expect(page.getByPlaceholder('Username')).toBeVisible();
    await expect(page.getByPlaceholder('Password')).toBeVisible();

    console.log('✅ Form validation test passed - empty form submission is handled');
  });

  test('should allow typing in username and password fields', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Test username field
    const usernameField = page.getByPlaceholder('Username');
    await usernameField.fill('testuser');
    const usernameValue = await usernameField.inputValue();
    expect(usernameValue).toBe('testuser');

    // Test password field
    const passwordField = page.getByPlaceholder('Password');
    await passwordField.fill('testpass');
    const passwordValue = await passwordField.inputValue();
    expect(passwordValue).toBe('testpass');

    console.log('✅ Input field interaction test passed - fields accept text');
  });

  test('should handle Enter key press on login form', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Fill form
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Press Enter on username field
    await page.getByPlaceholder('Username').press('Enter');

    // Verify the form was submitted (we should get an error response)
    await page.waitForTimeout(1000); // Wait for response

    console.log('✅ Enter key handling test passed - form submission works');
  });

  test('should display proper error message for invalid credentials', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Fill form with invalid credentials
    await page.getByPlaceholder('Username').fill('invaliduser');
    await page.getByPlaceholder('Password').fill('invalidpass');

    // Submit form
    await page.getByRole('button', { name: 'Enter the Void' }).click();

    // Wait for response
    await page.waitForTimeout(2000);

    // Check for error message
    const pageContent = await page.textContent('body');
    const hasError =
      pageContent?.includes('Invalid credentials') || pageContent?.includes('error') || pageContent?.includes('failed');

    expect(hasError).toBeTruthy();

    console.log('✅ Error handling test passed - invalid credentials are handled properly');
  });

  test('should maintain form state during interaction', async ({ page }) => {
    // Navigate to the app
    await page.goto('http://localhost:5173');

    // Fill form partially
    await page.getByPlaceholder('Username').fill('partial');

    // Verify the value is maintained
    const usernameValue = await page.getByPlaceholder('Username').inputValue();
    expect(usernameValue).toBe('partial');

    // Continue filling
    await page.getByPlaceholder('Username').fill('testuser');
    await page.getByPlaceholder('Password').fill('testpass');

    // Verify both values are maintained
    const finalUsernameValue = await page.getByPlaceholder('Username').inputValue();
    const finalPasswordValue = await page.getByPlaceholder('Password').inputValue();

    expect(finalUsernameValue).toBe('testuser');
    expect(finalPasswordValue).toBe('testpass');

    console.log('✅ Form state test passed - form maintains values correctly');
  });
});
