import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { logoutHandler } from '../logoutHandler';

// Mock dependencies
vi.mock('../security', () => ({
  secureTokenStorage: {
    clearToken: vi.fn(),
    getToken: vi.fn(() => 'mock-token'),
  },
}));

vi.mock('../logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
    warn: vi.fn(),
  },
}));

// Mock fetch
global.fetch = vi.fn();

describe('logoutHandler', () => {
  const mockDisconnect = vi.fn();
  const mockClearState = vi.fn();
  const mockNavigateToLogin = vi.fn();

  const defaultOptions = {
    authToken: 'mock-auth-token',
    disconnect: mockDisconnect,
    clearState: mockClearState,
    navigateToLogin: mockNavigateToLogin,
    timeout: 5000,
  };

  beforeEach(() => {
    vi.clearAllMocks();
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  describe('Successful Logout Flow', () => {
    it('should send logout command to server and handle successful response', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          success: true,
          message: 'Logged out successfully',
          session_terminated: true,
          connections_closed: true,
        }),
      };

      (global.fetch as any).mockResolvedValueOnce(mockResponse);

      await logoutHandler(defaultOptions);

      expect(global.fetch).toHaveBeenCalledWith('/commands/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer mock-auth-token',
        },
        body: JSON.stringify({
          command: 'logout',
          args: [],
        }),
        signal: expect.any(AbortSignal),
      });

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should proceed with client-side logout even if server responds with error', async () => {
      const mockResponse = {
        ok: false,
        status: 500,
        json: vi.fn().mockResolvedValue({
          error: 'Server error',
        }),
      };

      (global.fetch as any).mockResolvedValueOnce(mockResponse);

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Timeout Handling', () => {
    it('should proceed with client-side logout after timeout', async () => {
      // Mock fetch to throw AbortError after timeout
      (global.fetch as any).mockImplementation(() =>
        Promise.reject(new DOMException('The operation was aborted.', 'AbortError'))
      );

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle abort errors gracefully', async () => {
      // Mock fetch to throw AbortError
      (global.fetch as any).mockImplementation(() =>
        Promise.reject(new DOMException('The operation was aborted.', 'AbortError'))
      );

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Network Error Handling', () => {
    it('should proceed with client-side logout on network error', async () => {
      (global.fetch as any).mockRejectedValueOnce(new Error('Network error'));

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should proceed with client-side logout on fetch rejection', async () => {
      (global.fetch as any).mockRejectedValueOnce('Connection failed');

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('State Cleanup', () => {
    it('should call clearState function during logout', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      (global.fetch as any).mockResolvedValueOnce(mockResponse);

      await logoutHandler(defaultOptions);

      expect(mockClearState).toHaveBeenCalled();
    });

    it('should call disconnect function during logout', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      (global.fetch as any).mockResolvedValueOnce(mockResponse);

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
    });

    it('should call navigateToLogin function during logout', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      (global.fetch as any).mockResolvedValueOnce(mockResponse);

      await logoutHandler(defaultOptions);

      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Error Logging', () => {
    it('should log server errors but still proceed with logout', async () => {
      const mockResponse = {
        ok: false,
        status: 401,
        json: vi.fn().mockResolvedValue({
          error: 'Unauthorized',
        }),
      };

      (global.fetch as any).mockResolvedValueOnce(mockResponse);

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should log network errors but still proceed with logout', async () => {
      (global.fetch as any).mockRejectedValueOnce(new Error('Network timeout'));

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Custom Timeout Configuration', () => {
    it('should use custom timeout value', async () => {
      // Mock fetch to throw AbortError (simulating timeout)
      (global.fetch as any).mockImplementation(() =>
        Promise.reject(new DOMException('The operation was aborted.', 'AbortError'))
      );

      const customOptions = {
        ...defaultOptions,
        timeout: 2000,
      };

      await logoutHandler(customOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('No Auth Token Handling', () => {
    it('should proceed with client-side logout even without auth token', async () => {
      const optionsWithoutToken = {
        ...defaultOptions,
        authToken: '',
      };

      await logoutHandler(optionsWithoutToken);

      // Should not call server but should still clean up client state
      expect(global.fetch).not.toHaveBeenCalled();
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });
});
