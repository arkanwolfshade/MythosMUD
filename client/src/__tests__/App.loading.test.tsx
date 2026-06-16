import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Loading States', () => {
    it('should show loading state during login', async () => {
      let resolveLogin!: (value: Response) => void;
      const loginPromise = new Promise<Response>(resolve => {
        resolveLogin = resolve;
      });
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
      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : (url as Request).url;
        if (String(urlString).includes('auth/login')) {
          return loginPromise;
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Authenticating…')).toBeInTheDocument();
      });
      expect(screen.getByRole('button', { name: 'Authenticating…' })).toBeDisabled();

      resolveLogin(mockResponse as unknown as Response);
      await waitFor(() => {
        expect(
          screen.queryByRole('heading', { name: /Select Your Character/i }) ?? screen.queryByTestId('game-terminal')
        ).toBeTruthy();
      });
    });

    it('should show loading state during registration', async () => {
      // Mock a slow response
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
      };

      const mockProfessionsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: [
            {
              id: 0,
              name: 'Tramp',
              description: 'A wandering soul with no particular skills or connections.',
              flavor_text:
                'You have spent your days drifting from place to place, learning to survive on your wits alone.',
              stat_requirements: [],
              mechanical_effects: [],
              is_available: true,
            },
          ],
        }),
      };

      vi.useFakeTimers();
      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return new Promise<Response>(resolve =>
            setTimeout(() => {
              resolve(mockResponse as unknown as Response);
            }, 100)
          );
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

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

      // Should show loading state
      expect(screen.getByText('Registering…')).toBeInTheDocument();
      expect(registerButton).toBeDisabled();

      await vi.advanceTimersByTimeAsync(100);
      vi.useRealTimers();
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
    });
  });
});
