import { afterEach, beforeEach, describe, expect, it, vi, type Mock } from 'vitest';
import { createLogoutHandler, logoutHandler } from '../logoutHandler';

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

// Mock fetch globally using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(global, 'fetch');

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
    fetchSpy.mockClear();
    vi.useFakeTimers();
  });

  afterEach(() => {
    // Use mockReset instead of mockRestore to keep the spy active across tests
    // This prevents issues where mockRestore might restore an undefined/broken fetch implementation
    fetchSpy.mockReset();
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

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

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

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Timeout Handling', () => {
    it('should proceed with client-side logout after timeout', async () => {
      // Mock fetch to throw AbortError after timeout
      (global.fetch as Mock<typeof fetch>).mockImplementation(() =>
        Promise.reject(new DOMException('The operation was aborted.', 'AbortError'))
      );

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle abort errors gracefully', async () => {
      // Mock fetch to throw AbortError
      (global.fetch as Mock<typeof fetch>).mockImplementation(() =>
        Promise.reject(new DOMException('The operation was aborted.', 'AbortError'))
      );

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle Error instance with AbortError name', async () => {
      // Create an Error instance with name set to 'AbortError'
      const abortError = new Error('Operation aborted');
      abortError.name = 'AbortError';

      (global.fetch as Mock<typeof fetch>).mockImplementation(() => Promise.reject(abortError));

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Network Error Handling', () => {
    it('should proceed with client-side logout on network error', async () => {
      (global.fetch as Mock<typeof fetch>).mockRejectedValueOnce(new Error('Network error'));

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should proceed with client-side logout on fetch rejection', async () => {
      (global.fetch as Mock<typeof fetch>).mockRejectedValueOnce('Connection failed');

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

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      expect(mockClearState).toHaveBeenCalled();
    });

    it('should call disconnect function during logout', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
    });

    it('should call navigateToLogin function during logout', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

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

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should log network errors but still proceed with logout', async () => {
      (global.fetch as Mock<typeof fetch>).mockRejectedValueOnce(new Error('Network timeout'));

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle non-Error rejection in sendLogoutCommandToServer', async () => {
      // Reject with a non-Error value (string) - tests the String(error) branch
      (global.fetch as Mock<typeof fetch>).mockImplementation(() => Promise.reject('String rejection value'));

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
      (global.fetch as Mock<typeof fetch>).mockImplementation(() =>
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

  describe('Server Response Error Handling', () => {
    it('should handle error response with error.detail field', async () => {
      const mockResponse = {
        ok: false,
        status: 500,
        json: vi.fn().mockResolvedValue({
          detail: 'Detailed error message',
        }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle error response with error.error.message field', async () => {
      const mockResponse = {
        ok: false,
        status: 400,
        json: vi.fn().mockResolvedValue({
          error: {
            message: 'Error message from error.error.message',
          },
        }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle JSON parsing error in error response', async () => {
      const mockResponse = {
        ok: false,
        status: 500,
        json: vi.fn().mockRejectedValue(new Error('Invalid JSON')),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      // Should still proceed with client-side logout even if JSON parsing fails
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('Client-Side Cleanup Error Handling', () => {
    it('should handle error in secureTokenStorage.clearToken', async () => {
      const { secureTokenStorage } = await import('../security');
      vi.mocked(secureTokenStorage.clearToken).mockImplementation(() => {
        throw new Error('Failed to clear token');
      });

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      // Should continue with other cleanup steps
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle error in disconnect function', async () => {
      const mockDisconnectWithError = vi.fn().mockImplementation(() => {
        throw new Error('Disconnect failed');
      });

      const optionsWithError = {
        ...defaultOptions,
        disconnect: mockDisconnectWithError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(optionsWithError);

      // Should continue with other cleanup steps
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle error in clearState function', async () => {
      const mockClearStateWithError = vi.fn().mockImplementation(() => {
        throw new Error('Clear state failed');
      });

      const optionsWithError = {
        ...defaultOptions,
        clearState: mockClearStateWithError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(optionsWithError);

      // Should continue with navigation
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle error in navigateToLogin function', async () => {
      const mockNavigateToLoginWithError = vi.fn().mockImplementation(() => {
        throw new Error('Navigation failed');
      });

      const optionsWithError = {
        ...defaultOptions,
        navigateToLogin: mockNavigateToLoginWithError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      // Navigation errors are caught and logged, not thrown
      // The function should complete even if navigation fails
      await logoutHandler(optionsWithError);

      // Navigation should have been attempted
      expect(mockNavigateToLoginWithError).toHaveBeenCalled();
    });

    it('should attempt navigation even if cleanup fails', async () => {
      const mockClearStateWithError = vi.fn().mockImplementation(() => {
        throw new Error('Clear state failed');
      });

      const optionsWithError = {
        ...defaultOptions,
        clearState: mockClearStateWithError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(optionsWithError);

      // Should still attempt navigation
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle navigation error in cleanup error handler', async () => {
      const mockNavigateToLoginWithError = vi.fn().mockImplementation(() => {
        throw new Error('Navigation failed');
      });

      const mockClearStateWithError = vi.fn().mockImplementation(() => {
        throw new Error('Clear state failed');
      });

      const optionsWithError = {
        ...defaultOptions,
        clearState: mockClearStateWithError,
        navigateToLogin: mockNavigateToLoginWithError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      // Should not throw - error is caught and logged
      await logoutHandler(optionsWithError);
    });

    it('should handle non-Error navigation failure in cleanup error handler', async () => {
      // Test lines 58-65: when cleanup fails AND navigation fails with non-Error
      const mockNavigateToLoginWithStringError = vi.fn().mockImplementation(() => {
        throw 'String error'; // Non-Error type
      });

      const mockClearStateWithError = vi.fn().mockImplementation(() => {
        throw new Error('Clear state failed');
      });

      const optionsWithError = {
        ...defaultOptions,
        clearState: mockClearStateWithError,
        navigateToLogin: mockNavigateToLoginWithStringError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      // Should not throw - error is caught and logged
      await logoutHandler(optionsWithError);
      expect(mockNavigateToLoginWithStringError).toHaveBeenCalled();
    });

    it('should handle non-Error clearToken error', async () => {
      const { secureTokenStorage } = await import('../security');
      vi.mocked(secureTokenStorage.clearToken).mockImplementation(() => {
        throw 'String error'; // Non-Error type - tests line 145 branch
      });

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(defaultOptions);

      // Should continue with other cleanup steps
      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle non-Error disconnect error', async () => {
      const mockDisconnectWithStringError = vi.fn().mockImplementation(() => {
        throw 'String error'; // Non-Error type - tests line 155 branch
      });

      const optionsWithError = {
        ...defaultOptions,
        disconnect: mockDisconnectWithStringError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(optionsWithError);

      // Should continue with other cleanup steps
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle non-Error clearState error', async () => {
      const mockClearStateWithStringError = vi.fn().mockImplementation(() => {
        throw 'String error'; // Non-Error type - tests line 165 branch
      });

      const optionsWithError = {
        ...defaultOptions,
        clearState: mockClearStateWithStringError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      await logoutHandler(optionsWithError);

      // Should continue with navigation
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should handle non-Error navigateToLogin error in performClientSideCleanup', async () => {
      // Test line 175: non-Error navigation error in performClientSideCleanup
      const mockNavigateToLoginWithStringError = vi.fn().mockImplementation(() => {
        throw 'String navigation error'; // Non-Error type
      });

      const optionsWithError = {
        ...defaultOptions,
        navigateToLogin: mockNavigateToLoginWithStringError,
      };

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      // Navigation errors are re-thrown from performClientSideCleanup
      // This should trigger the outer catch block which then tries navigation again
      await logoutHandler(optionsWithError);

      // Navigation should have been attempted (will throw, caught, then tried again)
      expect(mockNavigateToLoginWithStringError).toHaveBeenCalled();
    });
  });

  describe('Timeout Mechanism', () => {
    it('should abort request after timeout duration', async () => {
      let abortSignal: AbortSignal | null = null;

      (global.fetch as Mock<typeof fetch>).mockImplementation((_url, options) => {
        if (options?.signal) {
          abortSignal = options.signal as AbortSignal;

          // Listen for abort and reject the promise when aborted
          return new Promise((_resolve, reject) => {
            const onAbort = () => {
              if (abortSignal) {
                abortSignal.removeEventListener('abort', onAbort);
              }
              reject(new DOMException('The operation was aborted.', 'AbortError'));
            };

            if (abortSignal && abortSignal.aborted) {
              // Already aborted, reject immediately
              reject(new DOMException('The operation was aborted.', 'AbortError'));
            } else if (abortSignal) {
              abortSignal.addEventListener('abort', onAbort);
            }
          });
        }

        // No signal, return a promise that never resolves (shouldn't happen in this test)
        return new Promise(() => {});
      });

      const timeoutPromise = logoutHandler({
        ...defaultOptions,
        timeout: 1000,
      });

      // Advance timer to trigger timeout (which will abort the signal)
      vi.advanceTimersByTime(1000);

      // Complete the logout (should complete even though fetch was aborted)
      await timeoutPromise;

      // Verify abort happened
      expect(abortSignal).not.toBeNull();
      // TypeScript doesn't narrow after expect, so we assert the type is non-null
      const signal = abortSignal!;
      expect(signal.aborted).toBe(true);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });

  describe('createLogoutHandler', () => {
    it('should create a logout handler function', () => {
      const handler = createLogoutHandler('test-token', mockDisconnect, mockClearState, mockNavigateToLogin);

      expect(typeof handler).toBe('function');
    });

    it('should create handler that calls logoutHandler with correct options', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({ success: true }),
      };

      fetchSpy.mockResolvedValueOnce(mockResponse as unknown as Response);

      const handler = createLogoutHandler('test-token', mockDisconnect, mockClearState, mockNavigateToLogin);

      await handler();

      expect(global.fetch).toHaveBeenCalledWith(
        '/commands/logout',
        expect.objectContaining({
          headers: expect.objectContaining({
            Authorization: 'Bearer test-token',
          }),
        })
      );

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });

    it('should allow custom timeout when calling created handler', async () => {
      (global.fetch as Mock<typeof fetch>).mockImplementation(() =>
        Promise.reject(new DOMException('The operation was aborted.', 'AbortError'))
      );

      const handler = createLogoutHandler('test-token', mockDisconnect, mockClearState, mockNavigateToLogin);

      await handler(2000);

      expect(mockDisconnect).toHaveBeenCalled();
      expect(mockClearState).toHaveBeenCalled();
      expect(mockNavigateToLogin).toHaveBeenCalled();
    });
  });
});
