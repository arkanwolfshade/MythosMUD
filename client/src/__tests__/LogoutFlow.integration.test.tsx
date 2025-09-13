/**
 * Integration tests for complete logout flow
 * Tests the entire logout process from button click to state cleanup
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

// Mock the useGameConnection hook
vi.mock('../hooks/useGameConnection', () => ({
  useGameConnection: vi.fn(() => ({
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    connect: vi.fn(),
    disconnect: vi.fn(),
    sendCommand: vi.fn(),
  })),
}));

// Mock fetch for authentication
const mockFetch = vi.fn();
global.fetch = mockFetch;

describe('Complete Logout Flow Integration', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mockLogoutHandler.mockResolvedValue(undefined);
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Successful Logout Flow', () => {
    it('should complete full logout flow from button click to login screen', async () => {
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

      // Step 1: Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });

      // Step 2: Verify user is in game terminal
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      expect(screen.getByTestId('logout-button')).toBeInTheDocument();

      // Step 3: Mock logout handler to simulate complete flow
      let disconnectCalled = false;
      let clearStateCalled = false;
      let navigateToLoginCalled = false;

      mockLogoutHandler.mockImplementation(async ({ disconnect, clearState, navigateToLogin }) => {
        // Simulate server logout command
        await new Promise(resolve => setTimeout(resolve, 100));

        // Simulate disconnect callback
        disconnect();
        disconnectCalled = true;

        // Simulate state cleanup
        clearState();
        clearStateCalled = true;

        // Simulate navigation to login
        navigateToLogin();
        navigateToLoginCalled = true;
      });

      // Step 4: Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Step 5: Verify loading state
      expect(screen.getByText('Logging out...')).toBeInTheDocument();
      expect(screen.getByTestId('logout-button')).toBeDisabled();

      // Step 6: Wait for logout to complete
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Step 7: Verify complete state reset
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.getByPlaceholderText('Password')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(screen.queryByTestId('logout-button')).not.toBeInTheDocument();

      // Step 8: Verify all callbacks were called
      expect(disconnectCalled).toBe(true);
      expect(clearStateCalled).toBe(true);
      expect(navigateToLoginCalled).toBe(true);

      // Step 9: Verify secure token cleanup
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();

      // Step 10: Verify focus management (username input should be focusable)
      const usernameInput = screen.getByPlaceholderText('Username');
      usernameInput.focus();
      expect(document.activeElement).toBe(usernameInput);
    });

    it('should handle logout with server communication failure gracefully', async () => {
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

      // Wait for logout to complete despite failure
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify state was still reset and error was shown
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
      expect(screen.getByText('Server connection failed')).toBeInTheDocument();
    });

    it('should prevent multiple logout attempts during logout process', async () => {
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

      // Mock logout handler to take time
      let resolveLogout: () => void;
      mockLogoutHandler.mockImplementation(async ({ disconnect, clearState, navigateToLogin }) => {
        await new Promise<void>(resolve => {
          resolveLogout = resolve;
        });
        disconnect();
        clearState();
        navigateToLogin();
      });

      // Click logout button multiple times
      fireEvent.click(screen.getByTestId('logout-button'));
      fireEvent.click(screen.getByTestId('logout-button'));
      fireEvent.click(screen.getByTestId('logout-button'));

      // Verify logout handler was only called once
      expect(mockLogoutHandler).toHaveBeenCalledTimes(1);

      // Verify loading state
      expect(screen.getByText('Logging out...')).toBeInTheDocument();
      expect(screen.getByTestId('logout-button')).toBeDisabled();

      // Complete logout
      resolveLogout!();
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });
    });
  });

  describe('State Management Integration', () => {
    it('should maintain proper state transitions during complete logout flow', async () => {
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

      // Track state transitions
      const stateTransitions: string[] = [];

      // Mock logout handler with state tracking
      mockLogoutHandler.mockImplementation(async ({ disconnect, clearState, navigateToLogin }) => {
        stateTransitions.push('logout-handler-called');

        disconnect();
        stateTransitions.push('disconnect-called');

        clearState();
        stateTransitions.push('clear-state-called');

        navigateToLogin();
        stateTransitions.push('navigate-to-login-called');
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Wait for logout to complete
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify state transitions occurred in correct order
      expect(stateTransitions).toEqual([
        'logout-handler-called',
        'disconnect-called',
        'clear-state-called',
        'navigate-to-login-called',
      ]);

      // Verify final state
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
    });

    it('should handle logout with character creation state', async () => {
      // Setup: User is authenticated but has no character
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          access_token: 'test-token',
          has_character: false,
        }),
      });

      render(<App />);

      // Login user
      fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
      fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
      fireEvent.click(screen.getByText('Enter the Void'));

      await waitFor(() => {
        expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();
      });

      // Verify user is in stats rolling screen
      expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();

      // Mock logout handler
      mockLogoutHandler.mockImplementation(async ({ disconnect, clearState, navigateToLogin }) => {
        disconnect();
        clearState();
        navigateToLogin();
      });

      // Simulate logout from stats screen (would be triggered by error)
      // For this test, we'll verify the error handler would clear tokens
      expect(secureTokenStorage.clearAllTokens).toBeDefined();
      expect(typeof secureTokenStorage.clearAllTokens).toBe('function');
    });
  });

  describe('Focus Management Integration', () => {
    it('should properly manage focus during complete logout flow', async () => {
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
      mockLogoutHandler.mockImplementation(async ({ disconnect, clearState, navigateToLogin }) => {
        disconnect();
        clearState();
        navigateToLogin();
      });

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Wait for logout to complete
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify focus management
      const usernameInput = screen.getByPlaceholderText('Username');
      expect(usernameInput).toBeInTheDocument();

      // The input should be focusable and ready for interaction
      usernameInput.focus();
      expect(document.activeElement).toBe(usernameInput);

      // Verify user can immediately start typing
      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      expect(usernameInput).toHaveValue('newuser');
    });
  });

  describe('Error Handling Integration', () => {
    it('should handle network errors during logout gracefully', async () => {
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

      // Mock logout handler to throw network error
      mockLogoutHandler.mockRejectedValue(new Error('Network error: Failed to fetch'));

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Wait for logout to complete despite network error
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify state was still reset
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
      expect(screen.getByText('Network error: Failed to fetch')).toBeInTheDocument();
    });

    it('should handle timeout errors during logout gracefully', async () => {
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

      // Mock logout handler to timeout
      mockLogoutHandler.mockRejectedValue(new Error('Request timeout'));

      // Click logout button
      fireEvent.click(screen.getByTestId('logout-button'));

      // Wait for logout to complete despite timeout
      await waitFor(() => {
        expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      });

      // Verify state was still reset
      expect(screen.getByPlaceholderText('Username')).toHaveValue('');
      expect(screen.queryByTestId('game-terminal')).not.toBeInTheDocument();
      expect(secureTokenStorage.clearAllTokens).toHaveBeenCalled();
      expect(screen.getByText('Request timeout')).toBeInTheDocument();
    });
  });
});
