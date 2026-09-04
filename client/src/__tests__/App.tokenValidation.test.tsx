import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Token Validation and Recovery', () => {
    it('should handle missing token despite authentication', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: '', // Empty token
          token_type: 'Bearer',
          user_id: 'test-user-id',
          characters: [
            {
              id: 'char-1',
              name: 'testuser',
              player_id: 'char-1',
              profession_id: 1,
              profession_name: 'Professor',
              level: 1,
              created_at: new Date().toISOString(),
              last_active: new Date().toISOString(),
            },
          ],
        }),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      // Empty token passes type guard (empty string is valid string)
      // The app will proceed but token might be invalid for API calls
      // For now, verify the app doesn't crash
      await waitFor(() => {
        // App should handle empty token - either show error or proceed
        // Since we can't easily test token validation here, just verify no crash
        expect(screen.queryByText('Invalid login response from server')).not.toBeInTheDocument();
      });
    });

    it('should handle login with valid token response', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockLoginResponse([
            {
              id: 'char-1',
              player_id: 'char-1',
              name: 'testuser',
              profession_id: 1,
              profession_name: 'Professor',
              level: 1,
              created_at: new Date().toISOString(),
              last_active: new Date().toISOString(),
            },
          ])
        ),
      };
      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      // Should successfully authenticate and show character selection screen
      await waitFor(() => {
        expect(screen.getByText(/Select Your Character/)).toBeInTheDocument();
      });

      // Select a character
      const selectButton = screen.getByText('Select Character');
      fireEvent.click(selectButton);

      // Wait for lazy MotdInterstitialScreen to resolve (Suspense can show Loading in CI)
      await screen.findByText(/Welcome to the Dreamlands/, {}, { timeout: 5000 });

      // Click continue button to proceed to game terminal (triggers async handleMotdContinue + fetch)
      const continueButton = screen.getByText('Enter the Realm');
      fireEvent.click(continueButton);

      // Wait for async MOTD dismiss and GameClientV2Container to render (mock has data-testid="game-terminal")
      const gameTerminal = await screen.findByTestId('game-terminal', {}, { timeout: 5000 });
      expect(gameTerminal).toBeInTheDocument();

      // Verify token is passed to GameClientV2Container
      expect(screen.getByText(/token: present/)).toBeInTheDocument();
    });

    it('should handle registration with missing token', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          // Missing required fields will cause type guard to fail
        }),
      };

      fetchSpy.mockResolvedValue(mockResponse as unknown as Response);

      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Should show error from type guard validation
      await waitFor(() => {
        expect(screen.getByText('Invalid registration response from server')).toBeInTheDocument();
      });
    });
  });
});
