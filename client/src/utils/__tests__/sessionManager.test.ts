/**
 * Tests for sessionManager module.
 */

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { sessionManager } from '../security';

/**
 * Test-only surface for private SessionManager members (see security.ts).
 * Do not intersect with typeof sessionManager: private fields there collide with
 * these names and reduce the type to never.
 */
type SessionManagerTestHooks = {
  cleanupInterval?: ReturnType<typeof setInterval> | null;
  startCleanupInterval(): void;
  expireSession(sessionId: string): void;
};

function sessionManagerTestHooks(): SessionManagerTestHooks {
  return sessionManager as unknown as SessionManagerTestHooks;
}

describe('Session Management', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    vi.useFakeTimers();
    const sm = sessionManagerTestHooks();
    if (!sm.cleanupInterval) {
      sm.startCleanupInterval();
    }
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('should create new session with timeout', () => {
    const sessionId = sessionManager.createSession('user123', 3600);

    expect(sessionId).toBeDefined();
    expect(sessionManager.isSessionValid(sessionId)).toBe(true);
  });

  it('should expire session after timeout', () => {
    const sessionId = sessionManager.createSession('user123', 1);

    expect(sessionManager.isSessionValid(sessionId)).toBe(true);

    vi.advanceTimersByTime(2000);

    expect(sessionManager.isSessionValid(sessionId)).toBe(false);
  });

  it('should refresh session timeout on activity', () => {
    const sessionId = sessionManager.createSession('user123', 5);

    vi.advanceTimersByTime(3000);
    sessionManager.refreshSession(sessionId, 5);

    vi.advanceTimersByTime(3000);

    expect(sessionManager.isSessionValid(sessionId)).toBe(true);
  });

  it('should clean up expired sessions', () => {
    const session1 = sessionManager.createSession('user1', 1);
    const session2 = sessionManager.createSession('user2', 5);

    vi.advanceTimersByTime(2000);
    sessionManager.cleanupExpiredSessions();

    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(true);
  });

  it('should handle session timeout callback', () => {
    const onTimeout = vi.fn();
    const sessionId = sessionManager.createSession('user123', 1, onTimeout);

    vi.advanceTimersByTime(2000);
    sessionManager.cleanupExpiredSessions();

    expect(onTimeout).toHaveBeenCalledWith(sessionId);
  });

  it('should expire session without onTimeout callback', () => {
    const sessionId = sessionManager.createSession('user123', 1);

    expect(sessionManager.isSessionValid(sessionId)).toBe(true);

    vi.advanceTimersByTime(2000);
    sessionManager.cleanupExpiredSessions();

    expect(sessionManager.isSessionValid(sessionId)).toBe(false);
  });

  it('should handle cleanup when session expires exactly at current time', () => {
    const sessionId = sessionManager.createSession('user123', 1);

    vi.advanceTimersByTime(1000);

    sessionManager.cleanupExpiredSessions();
    expect(sessionManager.isSessionValid(sessionId)).toBe(false);
  });

  it('should handle expireSession when session does not exist', () => {
    const sm = sessionManagerTestHooks();

    sm.expireSession('non-existent-session-id');

    expect(sessionManager.isSessionValid('non-existent-session-id')).toBe(false);
  });

  it('should remove session', () => {
    const sessionId = sessionManager.createSession('user123', 3600);
    expect(sessionManager.isSessionValid(sessionId)).toBe(true);

    const result = sessionManager.removeSession(sessionId);
    expect(result).toBe(true);
    expect(sessionManager.isSessionValid(sessionId)).toBe(false);
  });

  it('should return false when removing non-existent session', () => {
    const result = sessionManager.removeSession('non-existent-session');
    expect(result).toBe(false);
  });

  it('should return false when refreshing non-existent session', () => {
    const result = sessionManager.refreshSession('non-existent-session', 3600);
    expect(result).toBe(false);
  });

  it('should destroy session manager and clear all sessions', () => {
    const session1 = sessionManager.createSession('user1', 3600);
    const session2 = sessionManager.createSession('user2', 3600);

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    sessionManager.destroy();

    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(false);
  });

  it('should destroy session manager when cleanupInterval is null', () => {
    const sm = sessionManagerTestHooks();

    const session1 = sessionManager.createSession('user1', 3600);
    const session2 = sessionManager.createSession('user2', 3600);

    if (sm.cleanupInterval) {
      clearInterval(sm.cleanupInterval);
      sm.cleanupInterval = null;
    }

    const clearIntervalSpy = vi.spyOn(window, 'clearInterval');

    sessionManager.destroy();

    expect(clearIntervalSpy).not.toHaveBeenCalled();
    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(false);

    clearIntervalSpy.mockRestore();
  });

  it('should clear existing cleanup interval when starting new one', () => {
    const session1 = sessionManager.createSession('user1', 1);

    vi.advanceTimersByTime(2000);
    vi.advanceTimersByTime(60000);

    expect(sessionManager.isSessionValid(session1)).toBe(false);
  });

  it('should trigger interval callback to cleanup expired sessions', () => {
    const session1 = sessionManager.createSession('user1', 1);
    const session2 = sessionManager.createSession('user2', 3600);

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    vi.advanceTimersByTime(2000);
    vi.advanceTimersByTime(60000);

    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(true);
  });

  it('should trigger cleanup expired sessions via interval', () => {
    const session1 = sessionManager.createSession('user1', 1);
    const session2 = sessionManager.createSession('user2', 3600);

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    vi.advanceTimersByTime(2000);
    sessionManager.cleanupExpiredSessions();

    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(true);
  });

  it('should clear existing cleanup interval when starting new one', () => {
    const sm = sessionManagerTestHooks();

    if (!sm.cleanupInterval) {
      sm.startCleanupInterval();
    }

    const clearIntervalSpy = vi.spyOn(window, 'clearInterval');
    const setIntervalSpy = vi.spyOn(window, 'setInterval').mockClear();

    const intervalBeforeCall = sm.cleanupInterval;
    expect(intervalBeforeCall).toBeTruthy();

    sm.startCleanupInterval();

    expect(clearIntervalSpy).toHaveBeenCalledWith(intervalBeforeCall);
    expect(setIntervalSpy).toHaveBeenCalled();

    clearIntervalSpy.mockRestore();
    setIntervalSpy.mockRestore();
  });

  it('should start cleanup interval when none exists', () => {
    const sm = sessionManagerTestHooks();

    if (sm.cleanupInterval) {
      clearInterval(sm.cleanupInterval);
      sm.cleanupInterval = null;
    }

    const clearIntervalSpy = vi.spyOn(window, 'clearInterval');
    const setIntervalSpy = vi.spyOn(window, 'setInterval').mockClear();

    sm.startCleanupInterval();

    expect(clearIntervalSpy).not.toHaveBeenCalled();
    expect(setIntervalSpy).toHaveBeenCalled();
    expect(sm.cleanupInterval).toBeTruthy();

    clearIntervalSpy.mockRestore();
    setIntervalSpy.mockRestore();
  });

  it('should call cleanupExpiredSessions from interval callback', () => {
    const sm = sessionManagerTestHooks();

    const cleanupSpy = vi.spyOn(sessionManager, 'cleanupExpiredSessions');

    if (sm.cleanupInterval) {
      clearInterval(sm.cleanupInterval);
      sm.cleanupInterval = null;
    }
    sm.startCleanupInterval();

    const session1 = sessionManager.createSession('user1', 1);
    const session2 = sessionManager.createSession('user2', 3600);

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    vi.advanceTimersByTime(2000);

    expect(sessionManager.isSessionValid(session1)).toBe(false);

    cleanupSpy.mockClear();

    vi.advanceTimersByTime(60000);

    expect(cleanupSpy).toHaveBeenCalled();
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    cleanupSpy.mockRestore();
  });
});
