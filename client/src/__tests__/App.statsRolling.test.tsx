import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import './app.test.mocks';
import { createMockLoginResponse, fetchSpy, registerAppTestHooks } from './app.test.helpers';

describe('App', () => {
  registerAppTestHooks();
  describe('Stats Rolling Flow', () => {
    it('should show stats rolling screen for new character', async () => {
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

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/login')) {
          return Promise.resolve(mockResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
    });

    it('should handle stats acceptance', async () => {
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

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/login')) {
          return Promise.resolve(mockResponse as unknown as Response);
        }
        if (urlString.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats');
      fireEvent.click(acceptButton);

      await waitFor(() => {
        expect(screen.getByRole('heading', { name: /Choose Your Profession/i })).toBeInTheDocument();
      });
    });

    it('should handle stats error', async () => {
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

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/login')) {
          return Promise.resolve(mockResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Trigger error from stats step (plan 10.6: we are already on stats screen)
      const errorButton = screen.getByText('Trigger Error');
      fireEvent.click(errorButton);

      // App handles stats error by clearing creation and showing main app (game terminal when no character).
      // Wait for lazy GameClientV2Container to resolve (Suspense can show Loading in CI).
      const gameTerminal = await screen.findByTestId('game-terminal', {}, { timeout: 5000 });
      expect(gameTerminal).toBeInTheDocument();
      expect(screen.queryByTestId('stats-rolling-screen')).not.toBeInTheDocument();
    });
  });
});
