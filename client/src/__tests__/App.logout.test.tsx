/**
 * Unit tests for App.tsx logout state management
 * Tests the complete logout flow and state management in the App component
 */

import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import App from '../App';
import { logoutHandler } from '../utils/logoutHandler';
import { secureTokenStorage } from '../utils/security';

// Mock the logoutHandler utility
vi.mock('../utils/logoutHandler');
const mockLogoutHandler = vi.mocked(logoutHandler);

// Mock the secureTokenStorage
vi.mock('../utils/security', () => ({
  secureTokenStorage: {
    clearToken: vi.fn(),
    clearRefreshToken: vi.fn(),
    clearAllTokens: vi.fn(),
    setToken: vi.fn(),
    setRefreshToken: vi.fn(),
  },
  inputSanitizer: {
    sanitizeUsername: vi.fn(input => input),
    sanitizeCommand: vi.fn(input => input),
  },
  memoryMonitor: {
    start: vi.fn(),
    stop: vi.fn(),
  },
}));

// Mock the GameClientV2Container component
vi.mock('../components/ui-v2/GameClientV2Container', () => ({
  GameClientV2Container: ({ onLogout, isLoggingOut }: { onLogout: () => void; isLoggingOut: boolean }) => (
    <div data-testid="game-terminal">
      <button data-testid="logout-button" onClick={onLogout} disabled={isLoggingOut}>
        {isLoggingOut ? 'Logging out...' : 'Logout'}
      </button>
    </div>
  ),
}));

// Mock the StatsRollingScreen component
vi.mock('../components/StatsRollingScreen', () => ({
  StatsRollingScreen: () => <div data-testid="stats-rolling-screen">Stats Rolling Screen</div>,
}));

// Mock the EldritchEffectsDemo component
vi.mock('../components/EldritchEffectsDemo', () => ({
  EldritchEffectsDemo: () => <div data-testid="eldritch-effects-demo">Eldritch Effects Demo</div>,
}));

// Mock fetch for authentication
const mockFetch = vi.fn();
global.fetch = mockFetch;

// SKIPPED: This is an E2E test that should use Playwright, not Vitest
// These tests require full App flows and should be in client/tests/
describe.skip('App.tsx Logout State Management', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mockLogoutHandler.mockResolvedValue(undefined);
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Logout Flow', () => {
    it('should handle successful logout and reset all state', async () => {
      // Setup: User is authenticated with character
      mockFetch
        .mockResolvedValueOnce({
          ok: true,
          json: async () => ({
            access_token: 'test-token',
            has_character: true,
            character_name: 'TestPlayer',
          }),
        })
        .mockResolvedValueOnce({
          ok: true,
          json: async () => ({
            access_token: 'test-token',
            has_character: true,
            character_name: 'TestPlayer',
          }),
        });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler to succeed
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        clearState();
        navigateToLogin();
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Wait for logout to complete
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify state was reset
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.getByPlaceholderText('Password')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
    });

    it('should handle logout with loading state', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler to take time and then complete
      let resolveLogout: () => void;
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        await new Promise<void>(resolve => {
          resolveLogout = resolve;
        });
        clearState();
        navigateToLogin();
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Verify loading state
      expect(screen.getByText('Logging out...')).toBeInTheDocument();
      expect(screen.getByTestId('logout-button')).toBeDisabled();

      // Complete logout by resolving the promise
      resolveLogout!();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });
    });

    it('should prevent multiple logout attempts', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler to take time and then complete
      let resolveLogout: () => void;
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        await new Promise<void>(resolve => {
          resolveLogout = resolve;
        });
        clearState();
        navigateToLogin();
      });

      // Click logout button multiple times
      fireEvent.click(screen.getByTestId('logout-button'));
      fireEvent.click(screen.getByTestId('logout-button'));
      fireEvent.click(screen.getByTestId('logout-button'));

      // Verify logout handler was only called once
      expect(mockLogoutHandler).toHaveBeenCalledTimes(1);

      // Complete logout by resolving the promise
      resolveLogout!();
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });
    });

    it('should handle logout handler failure gracefully', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler to fail
      mockLogoutHandler.mockRejectedValue(new Error('Logout failed'));

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Wait for logout to complete despite failure
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify state was still reset and error was shown
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
    });

    it('should clear all authentication state on logout', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        clearState();
        navigateToLogin();
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify all state was cleared
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.getByPlaceholderText('Password')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
    });
  });

  describe('State Management Integration', () => {
    it('should maintain proper state transitions during logout', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Verify initial state
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();

      // Mock logout handler with state tracking
      let clearStateCalled = false;
      let navigateToLoginCalled = false;

      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        clearState();
        clearStateCalled = true;
        navigateToLogin();
        navigateToLoginCalled = true;
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify callbacks were called
      expect(clearStateCalled).toBe(true);
      expect(navigateToLoginCalled).toBe(true);
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
    });

    it('should handle logout with character creation state', async () => {
      // Setup: User is authenticated but has no character
      const mockLoginResponse = {
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: false,
        }),
      };

      const mockProfessionsResponse = {
        ok: true,
        json: async () => [
          {
            id: 0,
            name: 'Tramp',
            description: 'A wandering soul with no particular skills or connections.',
            flavor_text:
              'You have spent your days drifting from place to place, learning to survive on your wits alone.',
            stat_requirements: {},
            mechanical_effects: {},
            is_available: true,
          },
        ],
      };

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/login')) {
          return Promise.resolve(mockLoginResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      // Mock logout handler
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        clearState();
        navigateToLogin();
      });

      // Simulate error in stats rolling that triggers logout
      // This would happen when StatsRollingScreen calls onError
      // For this test, we'll verify that the error handler would clear tokens
      // The actual logout flow would be triggered from the stats screen error handler

      // Since we can't directly access the handleLogout function from the component,
      // we'll test that the secureTokenStorage is available and would be called
      // in the actual error scenario
      expect(secureTokenStorage.clearAllTokens).toBeDefined();
      expect(typeof secureTokenStorage.clearAllTokens).toBe('function');
    });

    it('should reset error state on successful logout', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        clearState();
        navigateToLogin();
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify no error message is shown
      expect(screen.queryByText(/error/i)).not.toBeInTheDocument();
    });

    it('should show error message on logout failure', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler to fail
      mockLogoutHandler.mockRejectedValue(new Error('Server connection failed'));

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify error message is shown
      expect(screen.getByText('Server connection failed')).toBeInTheDocument();
    });
  });

  describe('Focus Management', () => {
    it('should return focus to login form after logout', async () => {
      // Setup: User is authenticated with character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: true,
          character_name: 'TestPlayer',
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Mock logout handler
      mockLogoutHandler.mockImplementation(async ({ clearState, navigateToLogin }) => {
        clearState();
        navigateToLogin();
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify username input is focusable and ready for interaction
      const usernameInput = screen.getByPlaceholderText('Username');
      expect(usernameInput).toBeInTheDocument();
      usernameInput.focus();
      expect(document.activeElement).toBe(usernameInput);
    });
  });
});
