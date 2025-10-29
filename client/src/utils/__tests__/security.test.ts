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
      const validToken =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';
      const invalidToken = 'invalid-token';

      expect(secureTokenStorage.isValidToken(validToken)).toBe(true);
      expect(secureTokenStorage.isValidToken(invalidToken)).toBe(false);
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

      const token =
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyNDI2MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
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

  it('should handle CSRF token expiry', () => {
    const token = csrfProtection.generateToken(1); // 1 second expiry

    expect(csrfProtection.validateToken(token)).toBe(true);

    vi.useFakeTimers();
    vi.advanceTimersByTime(2000);

    expect(csrfProtection.validateToken(token)).toBe(false);

    vi.useRealTimers();
  });
});
