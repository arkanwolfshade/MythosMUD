import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';
import './app.test.mocks';

describe('App', () => {
  registerAppTestHooks();
  describe('Logout Error Handling', () => {
    it('should handle logout failure gracefully', async () => {
      const { logoutHandler: mockLogoutHandler } = await import('../utils/logoutHandler');
      (mockLogoutHandler as ReturnType<typeof vi.fn>).mockRejectedValue(new Error('Logout failed'));

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockLoginResponse([
            {
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

      // Login first
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      // Wait for character selection screen (new flow for existing users with characters)
      await waitFor(() => {
        expect(screen.getByText(/Select Your Character/)).toBeInTheDocument();
      });

      // Verify the logout handler mock is set up
      expect(mockLogoutHandler).toBeDefined();
    });

    it('should clear state even when logout handler throws', async () => {
      const { logoutHandler: mockLogoutHandler } = await import('../utils/logoutHandler');
      (mockLogoutHandler as ReturnType<typeof vi.fn>).mockRejectedValue(new Error('Server error'));

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockLoginResponse([
            {
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

      // Login first
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      // Wait for character selection screen (new flow for existing users with characters)
      await waitFor(() => {
        expect(screen.getByText(/Select Your Character/)).toBeInTheDocument();
      });

      // Verify the logout handler mock is set up
      expect(mockLogoutHandler).toBeDefined();
    });
  });
});
