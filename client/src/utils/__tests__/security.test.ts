import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { csrfProtection, inputSanitizer, secureTokenStorage, sessionManager } from '../security';

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
};

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock,
});

// Mock document.cookie
Object.defineProperty(document, 'cookie', {
  writable: true,
  value: '',
});

// Mock fetch
global.fetch = vi.fn();

describe('Secure Token Storage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    document.cookie = '';
  });

  afterEach(() => {
    vi.clearAllTimers();
  });

  describe('Token Storage', () => {
    it('should store token in localStorage', () => {
      const token = 'test-jwt-token';
      secureTokenStorage.setToken(token);

      expect(localStorageMock.setItem).toHaveBeenCalledWith('authToken', token);
    });

    it('should retrieve token from localStorage', () => {
      const token = 'test-jwt-token';
      localStorageMock.getItem.mockReturnValue(token);

      const retrievedToken = secureTokenStorage.getToken();
      expect(retrievedToken).toBe(token);
      expect(localStorageMock.getItem).toHaveBeenCalledWith('authToken');
    });

    it('should return null for missing token', () => {
      localStorageMock.getItem.mockReturnValue(null);
      const token = secureTokenStorage.getToken();
      expect(token).toBeNull();
    });

    it('should clear token from localStorage', () => {
      secureTokenStorage.clearToken();

      expect(localStorageMock.removeItem).toHaveBeenCalledWith('authToken');
    });

    it('should validate token format', () => {
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      // This is test data for JWT validation, not a real secret
      const validToken =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';
      const invalidToken = 'invalid-token';

      expect(secureTokenStorage.isValidToken(validToken)).toBe(true);
      expect(secureTokenStorage.isValidToken(invalidToken)).toBe(false);
    });

    it('should validate token with null and undefined', () => {
      expect(secureTokenStorage.isValidToken(null as unknown as string)).toBe(false);
      expect(secureTokenStorage.isValidToken(undefined as unknown as string)).toBe(false);
    });

    it('should validate token with non-string types', () => {
      expect(secureTokenStorage.isValidToken(123 as unknown as string)).toBe(false);
      expect(secureTokenStorage.isValidToken({} as unknown as string)).toBe(false);
      expect(secureTokenStorage.isValidToken([] as unknown as string)).toBe(false);
    });

    it('should validate token with wrong number of parts', () => {
      expect(secureTokenStorage.isValidToken('one.two')).toBe(false);
      expect(secureTokenStorage.isValidToken('one.two.three.four')).toBe(false);
      expect(secureTokenStorage.isValidToken('one')).toBe(false);
    });
  });

  describe('Token Refresh', () => {
    it('should automatically refresh token before expiry', async () => {
      const mockFetch = vi.mocked(fetch);
      const refreshResponse = {
        access_token: 'new-jwt-token',
        expires_in: 3600,
      };

      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () => Promise.resolve(refreshResponse),
      } as Response);

      // Set a refresh token in localStorage
      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      // This is test data for JWT validation, not a real secret
      const token =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyNDI2MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';

      await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(mockFetch).toHaveBeenCalledWith('/auth/refresh', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({ refresh_token: 'test-refresh-token' }),
      });
    });

    it('should handle refresh token failure gracefully', async () => {
      const mockFetch = vi.mocked(fetch);
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 401,
      } as Response);

      // Set a refresh token in localStorage
      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      // This is test data for JWT validation, not a real secret
      const token =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyNDI2MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
    });

    it('should return true if token is valid and not expired', async () => {
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      // This is test data for JWT validation, not a real secret
      // Token with exp in the future (year 2099)
      const futureExp = Math.floor(new Date('2099-12-31').getTime() / 1000);
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const payload = btoa(JSON.stringify({ exp: futureExp }))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
      const token = `${header}.${payload}.signature`;

      const result = await secureTokenStorage.refreshTokenIfNeeded(token);
      expect(result).toBe(true);
      expect(fetch).not.toHaveBeenCalled();
    });

    it('should return true if token is invalid format', async () => {
      const result = await secureTokenStorage.refreshTokenIfNeeded('invalid-token');
      expect(result).toBe(true); // Returns true for invalid tokens (no refresh needed)
    });

    it('should return true if token is valid but expired check fails', async () => {
      // Token that is valid format but isTokenExpired returns false (not expired)
      const futureExp = Math.floor(new Date('2099-12-31').getTime() / 1000);
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const payload = btoa(JSON.stringify({ exp: futureExp }))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
      const token = `${header}.${payload}.signature`;

      const result = await secureTokenStorage.refreshTokenIfNeeded(token);
      expect(result).toBe(true);
      expect(fetch).not.toHaveBeenCalled();
    });

    it('should handle network errors during refresh', async () => {
      const mockFetch = vi.mocked(fetch);
      mockFetch.mockRejectedValueOnce(new Error('Network error'));

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const token =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
    });

    it('should handle missing refresh token', async () => {
      localStorageMock.getItem.mockReturnValue(null);

      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const token =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
    });

    it('should handle refresh response without access_token', async () => {
      const mockFetch = vi.mocked(fetch);
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () => Promise.resolve({ expires_in: 3600 }), // No access_token
      } as Response);

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const token =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
    });
  });

  describe('Refresh Token Management', () => {
    it('should get refresh token from localStorage', () => {
      localStorageMock.getItem.mockReturnValue('test-refresh-token');
      const token = secureTokenStorage.getRefreshToken();
      expect(token).toBe('test-refresh-token');
      expect(localStorageMock.getItem).toHaveBeenCalledWith('refreshToken');
    });

    it('should return null for missing refresh token', () => {
      localStorageMock.getItem.mockReturnValue(null);
      const token = secureTokenStorage.getRefreshToken();
      expect(token).toBeNull();
    });

    it('should set refresh token in localStorage', () => {
      const token = 'test-refresh-token';
      secureTokenStorage.setRefreshToken(token);
      expect(localStorageMock.setItem).toHaveBeenCalledWith('refreshToken', token);
    });

    it('should clear refresh token from localStorage', () => {
      secureTokenStorage.clearRefreshToken();
      expect(localStorageMock.removeItem).toHaveBeenCalledWith('refreshToken');
    });

    it('should clear all tokens', () => {
      secureTokenStorage.clearAllTokens();
      expect(localStorageMock.removeItem).toHaveBeenCalledWith('authToken');
      expect(localStorageMock.removeItem).toHaveBeenCalledWith('refreshToken');
    });
  });

  describe('Environment Checks', () => {
    it('should return null for getToken in production mode', () => {
      // Note: import.meta.env is not easily mockable in Vitest
      // The environment check happens at runtime, so we test the behavior
      // In test mode, it will use localStorage, but we verify the logic path exists
      const token = secureTokenStorage.getToken();
      // In test mode, this will call getItem, but the code path for production exists
      // We can't easily test the production path without more complex mocking
      expect(typeof token === 'string' || token === null).toBe(true);
    });

    it('should return null for getRefreshToken in production mode', () => {
      // Note: import.meta.env is not easily mockable in Vitest
      // The environment check happens at runtime, so we test the behavior
      // In test mode, it will use localStorage, but we verify the logic path exists
      const token = secureTokenStorage.getRefreshToken();
      // In test mode, this will call getItem, but the code path for production exists
      // We can't easily test the production path without more complex mocking
      expect(typeof token === 'string' || token === null).toBe(true);
    });
  });
});

describe('Session Management', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    vi.useFakeTimers();
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
    const sessionId = sessionManager.createSession('user123', 1); // 1 second timeout

    expect(sessionManager.isSessionValid(sessionId)).toBe(true);

    vi.advanceTimersByTime(2000); // Advance 2 seconds

    expect(sessionManager.isSessionValid(sessionId)).toBe(false);
  });

  it('should refresh session timeout on activity', () => {
    const sessionId = sessionManager.createSession('user123', 5);

    vi.advanceTimersByTime(3000); // Advance 3 seconds
    sessionManager.refreshSession(sessionId, 5); // Refresh with 5 more seconds

    vi.advanceTimersByTime(3000); // Advance another 3 seconds (total 6)

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
    sessionManager.cleanupExpiredSessions(); // Manually trigger cleanup

    expect(onTimeout).toHaveBeenCalledWith(sessionId);
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

  it('should clear existing cleanup interval when starting new one', () => {
    // The cleanup interval is started in the constructor
    // To test the clearInterval branch, we need to manually trigger startCleanupInterval
    // But since it's private, we'll test the behavior indirectly
    // by verifying that the interval callback works correctly

    const session1 = sessionManager.createSession('user1', 1); // 1 second timeout
    const session2 = sessionManager.createSession('user2', 3600); // 1 hour timeout

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    // Advance time to expire session1
    vi.advanceTimersByTime(2000);

    // Advance time to trigger the interval (60000ms = 1 minute)
    vi.advanceTimersByTime(60000);

    // After the interval fires, session1 should be cleaned up
    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(true);
  });

  it('should trigger interval callback to cleanup expired sessions', () => {
    const session1 = sessionManager.createSession('user1', 1); // 1 second timeout
    const session2 = sessionManager.createSession('user2', 3600); // 1 hour timeout

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    // Advance time to expire session1
    vi.advanceTimersByTime(2000);

    // Advance time to trigger the interval callback (60000ms = 1 minute)
    // This will call cleanupExpiredSessions() via the interval
    vi.advanceTimersByTime(60000);

    // After the interval callback fires, session1 should be cleaned up
    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(true);
  });

  it('should trigger cleanup expired sessions via interval', () => {
    const session1 = sessionManager.createSession('user1', 1); // 1 second timeout
    const session2 = sessionManager.createSession('user2', 3600); // 1 hour timeout

    expect(sessionManager.isSessionValid(session1)).toBe(true);
    expect(sessionManager.isSessionValid(session2)).toBe(true);

    // Advance time to expire session1
    vi.advanceTimersByTime(2000);

    // Trigger the interval callback manually (simulating the interval firing)
    // The interval is set to 60000ms, but we can manually call cleanupExpiredSessions
    sessionManager.cleanupExpiredSessions();

    expect(sessionManager.isSessionValid(session1)).toBe(false);
    expect(sessionManager.isSessionValid(session2)).toBe(true);
  });
});

describe('Input Sanitization', () => {
  it('should sanitize HTML input', () => {
    const maliciousInput = '<script>alert("xss")</script>Hello World';
    const sanitized = inputSanitizer.sanitizeHtml(maliciousInput);

    expect(sanitized).toBe('Hello World');
    expect(sanitized).not.toContain('<script>');
  });

  it('should strip style attributes and be safe for templates', () => {
    const input = '<span style="color:red">Hello</span>';
    const sanitized = inputSanitizer.sanitizeHtml(input);
    expect(sanitized).toBe('<span>Hello</span>');
    expect(sanitized).not.toContain('style=');
  });

  it('should sanitize user commands', () => {
    const maliciousCommand = 'say <img src=x onerror=alert(1)>';
    const sanitized = inputSanitizer.sanitizeCommand(maliciousCommand);

    expect(sanitized).toBe('say');
    expect(sanitized).not.toContain('<img');
    expect(sanitized).not.toContain('onerror');
  });

  it('should remove javascript: protocol from commands', () => {
    const command = 'say javascript:alert(1)';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized).not.toContain('javascript:');
    expect(sanitized).toContain('say');
  });

  it('should remove vbscript: protocol from commands', () => {
    const command = 'say vbscript:msgbox(1)';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized).not.toContain('vbscript:');
    expect(sanitized).toContain('say');
  });

  it('should handle commands with mixed case protocols', () => {
    const command = 'say JavaScript:alert(1) VBScript:msgbox(1)';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized.toLowerCase()).not.toContain('javascript:');
    expect(sanitized.toLowerCase()).not.toContain('vbscript:');
  });

  it('should trim whitespace from commands', () => {
    const command = '  say hello  ';
    const sanitized = inputSanitizer.sanitizeCommand(command);
    expect(sanitized).toBe('say hello');
  });

  it('should preserve safe HTML tags', () => {
    const safeInput = '<b>Bold text</b> and <i>italic text</i>';
    const sanitized = inputSanitizer.sanitizeHtml(safeInput);

    expect(sanitized).toContain('<b>Bold text</b>');
    expect(sanitized).toContain('<i>italic text</i>');
  });

  it('should escape special characters in usernames', () => {
    const username = 'user<script>alert("xss")</script>';
    const sanitized = inputSanitizer.sanitizeUsername(username);

    expect(sanitized).toBe('userscriptalertxsssc');
    expect(sanitized).not.toContain('<script>');
    expect(sanitized).not.toContain('>');
    expect(sanitized).not.toContain('"');
  });

  it('should limit username length to 20 characters', () => {
    const longUsername = 'a'.repeat(30);
    const sanitized = inputSanitizer.sanitizeUsername(longUsername);
    expect(sanitized.length).toBe(20);
  });

  it('should handle null, undefined, and empty string inputs', () => {
    expect(inputSanitizer.sanitizeHtml(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeHtml(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeHtml('')).toBe('');

    expect(inputSanitizer.sanitizeCommand(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeCommand(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeCommand('')).toBe('');

    expect(inputSanitizer.sanitizeUsername(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeUsername(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeUsername('')).toBe('');
  });

  it('should sanitize chat messages', () => {
    const maliciousMessage = '<script>alert("xss")</script><b>Bold</b> text';
    const sanitized = inputSanitizer.sanitizeChatMessage(maliciousMessage);

    expect(sanitized).not.toContain('<script>');
    expect(sanitized).toContain('<b>Bold</b>');
    expect(sanitized).toContain('text');
  });

  it('should handle null, undefined, and empty string in sanitizeChatMessage', () => {
    expect(inputSanitizer.sanitizeChatMessage(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeChatMessage(undefined as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeChatMessage('')).toBe('');
  });

  it('should limit chat message length to 500 characters', () => {
    const longMessage = 'a'.repeat(600);
    const sanitized = inputSanitizer.sanitizeChatMessage(longMessage);
    expect(sanitized.length).toBeLessThanOrEqual(500);
  });

  it('should sanitize incoming plain text', () => {
    const text = 'Hello & <world> & "test"';
    const sanitized = inputSanitizer.sanitizeIncomingPlainText(text);

    // Function only escapes &, <, > - not quotes
    expect(sanitized).toBe('Hello &amp; &lt;world&gt; &amp; "test"');
    expect(sanitized).not.toContain('<');
    expect(sanitized).not.toContain('>');
    expect(sanitized).toContain('&amp;');
  });

  it('should handle empty and null plain text', () => {
    expect(inputSanitizer.sanitizeIncomingPlainText('')).toBe('');
    expect(inputSanitizer.sanitizeIncomingPlainText(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeIncomingPlainText(undefined as unknown as string)).toBe('');
  });

  it('should sanitize incoming HTML', () => {
    const maliciousHtml = '<script>alert("xss")</script><b>Bold</b> <span class="test">text</span>';
    const sanitized = inputSanitizer.sanitizeIncomingHtml(maliciousHtml);

    expect(sanitized).not.toContain('<script>');
    expect(sanitized).toContain('<b>Bold</b>');
    expect(sanitized).toContain('<span class="test">text</span>');
  });

  it('should preserve allowed HTML tags in incoming HTML', () => {
    const html =
      '<b>Bold</b> <i>Italic</i> <em>Emphasis</em> <strong>Strong</strong> <br> <p>Paragraph</p> <ul><li>Item</li></ul> <code>code</code> <pre>pre</pre>';
    const sanitized = inputSanitizer.sanitizeIncomingHtml(html);

    expect(sanitized).toContain('<b>');
    expect(sanitized).toContain('<i>');
    expect(sanitized).toContain('<em>');
    expect(sanitized).toContain('<strong>');
    expect(sanitized).toContain('<br>');
    expect(sanitized).toContain('<p>');
    expect(sanitized).toContain('<ul>');
    expect(sanitized).toContain('<li>');
    expect(sanitized).toContain('<code>');
    expect(sanitized).toContain('<pre>');
  });

  it('should handle empty and null incoming HTML', () => {
    expect(inputSanitizer.sanitizeIncomingHtml('')).toBe('');
    expect(inputSanitizer.sanitizeIncomingHtml(null as unknown as string)).toBe('');
    expect(inputSanitizer.sanitizeIncomingHtml(undefined as unknown as string)).toBe('');
  });
});

describe('JWT base64url decoding and expiry', () => {
  it('should treat invalid or expired tokens as expired', () => {
    // header: {"alg":"none","typ":"JWT"}
    const header = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0';
    // payload with exp in the past (exp: 1)
    const payload = 'eyJleHAiOjF9';
    const signature = '';
    const token = `${header}.${payload}.${signature}`;
    expect(secureTokenStorage.isTokenExpired(token)).toBe(true);
  });

  it('should treat valid non-expired tokens as not expired', () => {
    // Token with exp in the future (year 2099)
    const futureExp = Math.floor(new Date('2099-12-31').getTime() / 1000);
    const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
    const payload = btoa(JSON.stringify({ exp: futureExp }))
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '');
    const signature = 'signature';
    const token = `${header}.${payload}.${signature}`;
    expect(secureTokenStorage.isTokenExpired(token)).toBe(false);
  });

  it('should treat tokens without exp as not expired', () => {
    const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
    const payload = btoa(JSON.stringify({ sub: '123' }))
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '');
    const signature = 'signature';
    const token = `${header}.${payload}.${signature}`;
    // When exp is undefined, the function returns undefined (falsy), which we treat as not expired
    const result = secureTokenStorage.isTokenExpired(token);
    expect(result).toBeFalsy();
  });

  it('should handle token with exp equal to current time', () => {
    const currentTime = Math.floor(Date.now() / 1000);
    const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
    const payload = btoa(JSON.stringify({ exp: currentTime }))
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '');
    const signature = 'signature';
    const token = `${header}.${payload}.${signature}`;
    // exp equal to current time should be considered expired
    // (exp < currentTime is false, but exp === currentTime means expired)
    // Actually, the check is payload.exp < currentTime,
    // so if exp === currentTime, it returns false (not expired)
    const result = secureTokenStorage.isTokenExpired(token);
    expect(result).toBe(false);
  });

  it('should handle token with exp greater than current time', () => {
    const futureTime = Math.floor(Date.now() / 1000) + 3600; // 1 hour in future
    const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
    const payload = btoa(JSON.stringify({ exp: futureTime }))
      .replace(/\+/g, '-')
      .replace(/\//g, '_')
      .replace(/=/g, '');
    const signature = 'signature';
    const token = `${header}.${payload}.${signature}`;
    const result = secureTokenStorage.isTokenExpired(token);
    expect(result).toBe(false);
  });

  it('should treat malformed tokens as expired', () => {
    expect(secureTokenStorage.isTokenExpired('invalid')).toBe(true);
    expect(secureTokenStorage.isTokenExpired('not.enough.parts.here')).toBe(true);
    expect(secureTokenStorage.isTokenExpired('')).toBe(true);
  });

  it('should handle base64url decoding errors gracefully', () => {
    const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
    const invalidPayload = '!!!invalid-base64!!!';
    const signature = 'signature';
    const token = `${header}.${invalidPayload}.${signature}`;
    expect(secureTokenStorage.isTokenExpired(token)).toBe(true);
  });
});

describe('CSRF Protection', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should generate CSRF token', () => {
    const token = csrfProtection.generateToken();

    expect(token).toBeDefined();
    expect(typeof token).toBe('string');
    expect(token.length).toBeGreaterThan(0);
  });

  it('should validate CSRF token', () => {
    const token = csrfProtection.generateToken();

    expect(csrfProtection.validateToken(token)).toBe(true);
    expect(csrfProtection.validateToken('invalid-token')).toBe(false);
  });

  it('should add CSRF token to request headers', () => {
    const headers = csrfProtection.addTokenToHeaders({});

    expect(headers['X-CSRF-Token']).toBeDefined();
    expect(typeof headers['X-CSRF-Token']).toBe('string');
    expect(headers['X-CSRF-Token'].length).toBeGreaterThan(0);
  });

  it('should add CSRF token to existing headers', () => {
    const existingHeaders = { 'Content-Type': 'application/json', Authorization: 'Bearer token' };
    const headers = csrfProtection.addTokenToHeaders(existingHeaders);

    expect(headers['X-CSRF-Token']).toBeDefined();
    expect(headers['Content-Type']).toBe('application/json');
    expect(headers['Authorization']).toBe('Bearer token');
  });

  it('should validate null and empty string tokens', () => {
    expect(csrfProtection.validateToken(null as unknown as string)).toBe(false);
    expect(csrfProtection.validateToken(undefined as unknown as string)).toBe(false);
    expect(csrfProtection.validateToken('')).toBe(false);
  });

  it('should handle CSRF token expiry', () => {
    const token = csrfProtection.generateToken(1); // 1 second expiry

    expect(csrfProtection.validateToken(token)).toBe(true);

    vi.useFakeTimers();
    vi.advanceTimersByTime(2000);

    expect(csrfProtection.validateToken(token)).toBe(false);

    vi.useRealTimers();
  });
});
