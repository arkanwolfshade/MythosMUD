import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useSessionStore } from '../sessionStore';

describe('Session Store', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset store state
    useSessionStore.getState().reset();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Initial State', () => {
    it('should have correct initial state', () => {
      const state = useSessionStore.getState();

      expect(state.isAuthenticated).toBe(false);
      expect(state.hasCharacter).toBe(false);
      expect(state.characterName).toBe('');
      expect(state.playerName).toBe('');
      expect(state.authToken).toBe('');
      expect(state.inviteCode).toBe('');
      expect(state.isSubmitting).toBe(false);
      expect(state.error).toBe(null);
      expect(state.lastActivity).toBe(null);
      expect(state.sessionTimeout).toBe(30 * 60 * 1000); // 30 minutes
    });
  });

  describe('Authentication State', () => {
    it('should set authentication state', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setAuthenticated(true);
      });

      expect(result.current.isAuthenticated).toBe(true);
    });

    it('should set character state', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setHasCharacter(true);
      });

      expect(result.current.hasCharacter).toBe(true);
    });

    it('should set character name', () => {
      const { result } = renderHook(() => useSessionStore());
      const characterName = 'TestCharacter';

      act(() => {
        result.current.setCharacterName(characterName);
      });

      expect(result.current.characterName).toBe(characterName);
    });

    it('should set player name', () => {
      const { result } = renderHook(() => useSessionStore());
      const playerName = 'TestPlayer';

      act(() => {
        result.current.setPlayerName(playerName);
      });

      expect(result.current.playerName).toBe(playerName);
    });
  });

  describe('Token Management', () => {
    it('should set auth token', () => {
      const { result } = renderHook(() => useSessionStore());
      const token = 'test-auth-token-123';

      act(() => {
        result.current.setAuthToken(token);
      });

      expect(result.current.authToken).toBe(token);
    });

    it('should clear auth token', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setAuthToken('test-token');
        result.current.clearAuthToken();
      });

      expect(result.current.authToken).toBe('');
    });

    it('should validate token format', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setAuthToken('valid-token-123');
      });

      expect(result.current.isValidToken()).toBe(true);

      act(() => {
        result.current.setAuthToken('');
      });

      expect(result.current.isValidToken()).toBe(false);
    });
  });

  describe('Invite Code Management', () => {
    it('should set invite code', () => {
      const { result } = renderHook(() => useSessionStore());
      const inviteCode = 'INVITE123';

      act(() => {
        result.current.setInviteCode(inviteCode);
      });

      expect(result.current.inviteCode).toBe(inviteCode);
    });

    it('should clear invite code', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setInviteCode('TEST123');
        result.current.clearInviteCode();
      });

      expect(result.current.inviteCode).toBe('');
    });

    it('should validate invite code format', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setInviteCode('VALID123');
      });

      expect(result.current.isValidInviteCode()).toBe(true);

      act(() => {
        result.current.setInviteCode('invalid');
      });

      expect(result.current.isValidInviteCode()).toBe(false);
    });
  });

  describe('Form State Management', () => {
    it('should set submitting state', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setSubmitting(true);
      });

      expect(result.current.isSubmitting).toBe(true);
    });

    it('should set error state', () => {
      const { result } = renderHook(() => useSessionStore());
      const errorMessage = 'Authentication failed';

      act(() => {
        result.current.setError(errorMessage);
      });

      expect(result.current.error).toBe(errorMessage);
    });

    it('should clear error state', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setError('Some error');
        result.current.clearError();
      });

      expect(result.current.error).toBe(null);
    });
  });

  describe('Session Activity Tracking', () => {
    it('should update last activity timestamp', () => {
      const { result } = renderHook(() => useSessionStore());
      const timestamp = Date.now();

      act(() => {
        result.current.updateLastActivity(timestamp);
      });

      expect(result.current.lastActivity).toBe(timestamp);
    });

    it('should update last activity automatically on state changes', () => {
      const { result } = renderHook(() => useSessionStore());
      const beforeUpdate = result.current.lastActivity;

      act(() => {
        result.current.setPlayerName('TestPlayer');
      });

      expect(result.current.lastActivity).toBeGreaterThan(beforeUpdate || 0);
    });

    it('should check if session is expired', () => {
      const { result } = renderHook(() => useSessionStore());

      // No activity yet
      expect(result.current.isSessionExpired()).toBe(false);

      // Set activity in the past (beyond timeout)
      act(() => {
        result.current.updateLastActivity(Date.now() - 31 * 60 * 1000); // 31 minutes ago
      });

      expect(result.current.isSessionExpired()).toBe(true);

      // Set recent activity
      act(() => {
        result.current.updateLastActivity(Date.now() - 5 * 60 * 1000); // 5 minutes ago
      });

      expect(result.current.isSessionExpired()).toBe(false);
    });

    it('should set custom session timeout', () => {
      const { result } = renderHook(() => useSessionStore());
      const customTimeout = 60 * 60 * 1000; // 1 hour

      act(() => {
        result.current.setSessionTimeout(customTimeout);
      });

      expect(result.current.sessionTimeout).toBe(customTimeout);
    });
  });

  describe('Login Flow', () => {
    it('should handle complete login flow', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setPlayerName('TestPlayer');
        result.current.setInviteCode('INVITE123');
        result.current.setSubmitting(true);
      });

      expect(result.current.playerName).toBe('TestPlayer');
      expect(result.current.inviteCode).toBe('INVITE123');
      expect(result.current.isSubmitting).toBe(true);

      // Simulate successful login
      act(() => {
        result.current.setAuthToken('auth-token-123');
        result.current.setAuthenticated(true);
        result.current.setHasCharacter(true);
        result.current.setCharacterName('TestCharacter');
        result.current.setSubmitting(false);
        result.current.clearError();
      });

      expect(result.current.isAuthenticated).toBe(true);
      expect(result.current.hasCharacter).toBe(true);
      expect(result.current.characterName).toBe('TestCharacter');
      expect(result.current.isSubmitting).toBe(false);
      expect(result.current.error).toBe(null);
    });
  });

  describe('Logout Flow', () => {
    it('should handle complete logout flow', () => {
      const { result } = renderHook(() => useSessionStore());

      // Set up authenticated state
      act(() => {
        result.current.setAuthenticated(true);
        result.current.setHasCharacter(true);
        result.current.setCharacterName('TestCharacter');
        result.current.setPlayerName('TestPlayer');
        result.current.setAuthToken('auth-token-123');
      });

      // Perform logout
      act(() => {
        result.current.logout();
      });

      expect(result.current.isAuthenticated).toBe(false);
      expect(result.current.hasCharacter).toBe(false);
      expect(result.current.characterName).toBe('');
      expect(result.current.playerName).toBe('');
      expect(result.current.authToken).toBe('');
      expect(result.current.inviteCode).toBe('');
      expect(result.current.error).toBe(null);
    });
  });

  describe('State Reset', () => {
    it('should reset all state to initial values', () => {
      const { result } = renderHook(() => useSessionStore());

      // Modify state
      act(() => {
        result.current.setAuthenticated(true);
        result.current.setHasCharacter(true);
        result.current.setCharacterName('TestCharacter');
        result.current.setPlayerName('TestPlayer');
        result.current.setAuthToken('auth-token-123');
        result.current.setInviteCode('INVITE123');
        result.current.setSubmitting(true);
        result.current.setError('Test error');
        result.current.updateLastActivity(Date.now());
      });

      // Reset state
      act(() => {
        result.current.reset();
      });

      expect(result.current.isAuthenticated).toBe(false);
      expect(result.current.hasCharacter).toBe(false);
      expect(result.current.characterName).toBe('');
      expect(result.current.playerName).toBe('');
      expect(result.current.authToken).toBe('');
      expect(result.current.inviteCode).toBe('');
      expect(result.current.isSubmitting).toBe(false);
      expect(result.current.error).toBe(null);
      expect(result.current.lastActivity).toBe(null);
    });
  });

  describe('Selectors', () => {
    it('should provide login form data selector', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setPlayerName('TestPlayer');
        result.current.setInviteCode('INVITE123');
      });

      const formData = result.current.getLoginFormData();

      expect(formData).toEqual({
        playerName: 'TestPlayer',
        inviteCode: 'INVITE123',
      });
    });

    it('should provide session status selector', () => {
      const { result } = renderHook(() => useSessionStore());

      expect(result.current.getSessionStatus()).toEqual({
        isAuthenticated: false,
        hasCharacter: false,
        isSubmitting: false,
        hasError: false,
      });

      act(() => {
        result.current.setAuthenticated(true);
        result.current.setHasCharacter(true);
        result.current.setError('Test error');
      });

      expect(result.current.getSessionStatus()).toEqual({
        isAuthenticated: true,
        hasCharacter: true,
        isSubmitting: false,
        hasError: true,
      });
    });

    it('should provide user info selector', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setPlayerName('TestPlayer');
        result.current.setCharacterName('TestCharacter');
        result.current.setAuthToken('auth-token-123');
      });

      const userInfo = result.current.getUserInfo();

      expect(userInfo).toEqual({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        hasValidToken: true,
      });
    });

    it('should provide session timeout info selector', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.updateLastActivity(Date.now() - 10 * 60 * 1000); // 10 minutes ago
        result.current.setSessionTimeout(30 * 60 * 1000); // 30 minutes
      });

      const timeoutInfo = result.current.getSessionTimeoutInfo();

      expect(timeoutInfo).toEqual({
        isExpired: false,
        timeRemaining: expect.any(Number),
        timeoutDuration: 30 * 60 * 1000,
      });

      expect(timeoutInfo.timeRemaining).toBeGreaterThan(0);
      expect(timeoutInfo.timeRemaining).toBeLessThanOrEqual(20 * 60 * 1000); // Should be around 20 minutes
    });

    it('should provide session timeout info when lastActivity is null', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setSessionTimeout(30 * 60 * 1000); // 30 minutes
      });

      const timeoutInfo = result.current.getSessionTimeoutInfo();

      expect(timeoutInfo.isExpired).toBe(false);
      expect(timeoutInfo.timeRemaining).toBe(30 * 60 * 1000); // Should be full timeout duration
      expect(timeoutInfo.timeoutDuration).toBe(30 * 60 * 1000);
    });

    it('should provide session timeout info when session is expired', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.updateLastActivity(Date.now() - 31 * 60 * 1000); // 31 minutes ago
        result.current.setSessionTimeout(30 * 60 * 1000); // 30 minutes
      });

      const timeoutInfo = result.current.getSessionTimeoutInfo();

      expect(timeoutInfo.isExpired).toBe(true);
      expect(timeoutInfo.timeRemaining).toBe(0);
      expect(timeoutInfo.timeoutDuration).toBe(30 * 60 * 1000);
    });

    it('should provide user info with empty token', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setPlayerName('TestPlayer');
        result.current.setCharacterName('TestCharacter');
        // Leave token empty
      });

      const userInfo = result.current.getUserInfo();

      expect(userInfo).toEqual({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        hasValidToken: false,
      });
    });

    it('should validate invite code with lowercase letters', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setInviteCode('abc123');
      });

      expect(result.current.isValidInviteCode()).toBe(false); // Should fail - lowercase not allowed
    });

    it('should validate invite code with special characters', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setInviteCode('ABC-123');
      });

      expect(result.current.isValidInviteCode()).toBe(false); // Should fail - hyphens not allowed
    });

    it('should validate invite code that is too short', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setInviteCode('ABC12'); // Only 5 characters
      });

      expect(result.current.isValidInviteCode()).toBe(false); // Should fail - needs at least 6
    });

    it('should validate invite code with correct format', () => {
      const { result } = renderHook(() => useSessionStore());

      act(() => {
        result.current.setInviteCode('ABCDEF123456');
      });

      expect(result.current.isValidInviteCode()).toBe(true);
    });

    it('should check session expired when lastActivity is null', () => {
      const { result } = renderHook(() => useSessionStore());

      // lastActivity should be null initially
      expect(result.current.isSessionExpired()).toBe(false);
    });
  });
});
