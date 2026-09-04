/**
 * Session management hook.
 *
 * Manages session ID generation, tracking, and switching.
 *
 * AI: Extracted from useGameConnection for clarity and reusability.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import { logger } from '../utils/logger';

export interface SessionManagementOptions {
  initialSessionId?: string | null;
  onSessionChange?: (sessionId: string) => void;
}

export interface SessionManagementResult {
  sessionId: string | null;
  createNewSession: () => string;
  switchToSession: (newSessionId: string) => void;
  updateSessionId: (newSessionId: string) => void;
}

/**
 * Hook for managing session IDs.
 *
 * Provides session ID generation, tracking, and switching functionality.
 *
 * @param options - Session management configuration
 * @returns Session management methods and current session ID
 *
 * AI: Session IDs track WebSocket connections for the same user session.
 */
export function useSessionManagement(options: SessionManagementOptions = {}): SessionManagementResult {
  const { initialSessionId, onSessionChange } = options;

  const generateSessionId = useCallback(() => {
    // Human reader: use Web Crypto API for cryptographically secure randomness.
    // AI reader: Math.random() is not secure and should not be used for session IDs.
    const array = new Uint8Array(9);
    crypto.getRandomValues(array);
    // Convert to base36 string (similar to Math.random().toString(36))
    const randomPart = Array.from(array)
      .map(byte => byte.toString(36))
      .join('')
      .substring(0, 9);
    return `session_${Date.now()}_${randomPart}`;
  }, []);

  // Initialize session ID to avoid setState in effect
  const [sessionId, setSessionId] = useState<string | null>(() => {
    return initialSessionId || generateSessionId();
  });

  const onSessionChangeRef = useRef(onSessionChange);

  // Update callback ref
  useEffect(() => {
    onSessionChangeRef.current = onSessionChange;
  }, [onSessionChange]);

  const createNewSession = useCallback(() => {
    const newSessionId = generateSessionId();
    setSessionId(newSessionId);
    onSessionChangeRef.current?.(newSessionId);
    logger.info('SessionManagement', 'New session created', { sessionId: newSessionId });
    return newSessionId;
  }, [generateSessionId]);

  const switchToSession = useCallback(
    (newSessionId: string) => {
      if (sessionId !== newSessionId) {
        setSessionId(newSessionId);
        onSessionChangeRef.current?.(newSessionId);
        logger.info('SessionManagement', 'Switched to session', { sessionId: newSessionId });
      }
    },
    [sessionId]
  );

  const updateSessionId = useCallback((newSessionId: string) => {
    setSessionId(newSessionId);
  }, []);

  // Session ID is now initialized during state creation, no need for effect

  return {
    sessionId,
    createNewSession,
    switchToSession,
    updateSessionId,
  };
}
