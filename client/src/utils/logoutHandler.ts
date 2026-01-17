/**
 * Logout handler utility for MythosMUD client
 * Handles server-side logout command, client-side state cleanup, and graceful error handling
 */

import { logger } from './logger.js';
import { secureTokenStorage } from './security.js';

export interface LogoutHandlerOptions {
  /** Authentication token for server logout command */
  authToken: string;
  /** Function to disconnect from game server */
  disconnect: () => void;
  /** Function to clear all client-side state */
  clearState: () => void;
  /** Function to navigate back to login screen */
  navigateToLogin: () => void;
  /** Timeout in milliseconds for server logout command (default: 5000) */
  timeout?: number;
}

/**
 * Handles the complete logout flow:
 * 1. Sends logout command to server (with timeout)
 * 2. Performs client-side state cleanup
 * 3. Disconnects from server
 * 4. Returns to login screen
 * 5. Always proceeds with client-side logout even if server fails
 */
export async function logoutHandler(options: LogoutHandlerOptions): Promise<void> {
  const { authToken, disconnect, clearState, navigateToLogin, timeout = 5000 } = options;

  logger.info('logoutHandler', 'Starting logout process', {
    hasAuthToken: !!authToken,
    timeout,
  });

  try {
    // Step 1: Send logout command to server (with timeout)
    if (authToken) {
      await sendLogoutCommandToServer(authToken, timeout);
    }

    logger.info('logoutHandler', 'Server logout command completed');
  } catch (error) {
    // Log error but continue with client-side cleanup
    logger.error('logoutHandler', 'Server logout command failed, proceeding with client cleanup', {
      error: error instanceof Error ? error.message : String(error),
    });
  }

  // Step 2: Always perform client-side cleanup regardless of server response
  try {
    await performClientSideCleanup(disconnect, clearState, navigateToLogin);
    logger.info('logoutHandler', 'Client-side logout cleanup completed');
  } catch (error) {
    logger.error('logoutHandler', 'Client-side logout cleanup failed', {
      error: error instanceof Error ? error.message : String(error),
    });
    // Still try to navigate to login even if cleanup fails
    try {
      navigateToLogin();
    } catch (navError) {
      logger.error('logoutHandler', 'Failed to navigate to login screen', {
        error: navError instanceof Error ? navError.message : String(navError),
      });
    }
  }
}

/**
 * Sends logout command to server with timeout handling
 */
async function sendLogoutCommandToServer(authToken: string, timeout: number): Promise<void> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => {
    controller.abort();
    logger.warn('logoutHandler', 'Server logout command timed out', { timeout });
  }, timeout);

  try {
    const response = await fetch('/commands/logout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${authToken}`,
      },
      body: JSON.stringify({
        command: 'logout',
        args: [],
      }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      let errorMessage = `Server logout failed (${response.status})`;
      try {
        const rawData: unknown = await response.json();
        const errorData = typeof rawData === 'object' && rawData !== null ? (rawData as Record<string, unknown>) : {};
        // Type-safe error message extraction
        const errorObj = errorData?.error;
        const errorMessageFromError =
          typeof errorObj === 'object' &&
          errorObj !== null &&
          'message' in errorObj &&
          typeof errorObj.message === 'string'
            ? errorObj.message
            : undefined;
        const detailMessage = typeof errorData?.detail === 'string' ? errorData.detail : undefined;
        errorMessage = errorMessageFromError || detailMessage || errorMessage;
      } catch {
        // Ignore JSON parsing errors, use default message
      }
      throw new Error(errorMessage);
    }

    const rawData: unknown = await response.json();
    // Logout response may be empty or contain a simple message
    const data = typeof rawData === 'object' && rawData !== null ? (rawData as Record<string, unknown>) : {};
    logger.info('logoutHandler', 'Server logout command successful', {
      success: data.success,
      message: data.message,
      sessionTerminated: data.session_terminated,
      connectionsClosed: data.connections_closed,
    });
  } catch (error) {
    clearTimeout(timeoutId);

    if (error instanceof Error && error.name === 'AbortError') {
      logger.warn('logoutHandler', 'Server logout command aborted due to timeout', { timeout });
    } else {
      logger.error('logoutHandler', 'Server logout command failed', {
        error: error instanceof Error ? error.message : String(error),
      });
    }

    // Re-throw to be handled by caller
    throw error;
  }
}

/**
 * Performs client-side cleanup operations
 */
async function performClientSideCleanup(
  disconnect: () => void,
  clearState: () => void,
  navigateToLogin: () => void
): Promise<void> {
  // Step 1: Clear authentication tokens
  try {
    secureTokenStorage.clearToken();
    logger.info('logoutHandler', 'Authentication tokens cleared');
  } catch (error) {
    logger.error('logoutHandler', 'Failed to clear authentication tokens', {
      error: error instanceof Error ? error.message : String(error),
    });
  }

  // Step 2: Disconnect from game server
  try {
    disconnect();
    logger.info('logoutHandler', 'Game server disconnected');
  } catch (error) {
    logger.error('logoutHandler', 'Failed to disconnect from game server', {
      error: error instanceof Error ? error.message : String(error),
    });
  }

  // Step 3: Clear client state
  try {
    clearState();
    logger.info('logoutHandler', 'Client state cleared');
  } catch (error) {
    logger.error('logoutHandler', 'Failed to clear client state', {
      error: error instanceof Error ? error.message : String(error),
    });
  }

  // Step 4: Navigate to login screen
  try {
    navigateToLogin();
    logger.info('logoutHandler', 'Navigated to login screen');
  } catch (error) {
    logger.error('logoutHandler', 'Failed to navigate to login screen', {
      error: error instanceof Error ? error.message : String(error),
    });
    throw error; // Re-throw navigation errors as they're critical
  }
}

/**
 * Creates a logout handler with default options
 */
export function createLogoutHandler(
  authToken: string,
  disconnect: () => void,
  clearState: () => void,
  navigateToLogin: () => void
) {
  return (timeout?: number) =>
    logoutHandler({
      authToken,
      disconnect,
      clearState,
      navigateToLogin,
      timeout,
    });
}
