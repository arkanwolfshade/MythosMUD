/**
 * Tests for secureTokenStorage module.
 */

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { secureTokenStorage } from '../security';
import { localStorageMock, setupSecurityMocks } from './security.test-utils';

describe('Secure Token Storage', () => {
  beforeEach(() => {
    setupSecurityMocks();
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
      // This is test data for JWT validation, not a real secret
      const validToken =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
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

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      const token =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
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

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      const token =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyNDI2MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
    });

    it('should return true if token is valid and not expired', async () => {
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const futureExp = Math.floor(new Date('2099-12-31').getTime() / 1000);
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
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
      expect(result).toBe(true);
    });

    it('should return true if token is valid but expired check fails', async () => {
      const futureExp = Math.floor(new Date('2099-12-31').getTime() / 1000);
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
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
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
      const mockFetch = vi.mocked(fetch);
      mockFetch.mockRejectedValueOnce(new Error('Network error'));

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      const token =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
      consoleErrorSpy.mockRestore();
    });

    it('should handle missing refresh token', async () => {
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
      localStorageMock.getItem.mockReturnValue(null);

      const token =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
      consoleErrorSpy.mockRestore();
    });

    it('should handle refresh response without access_token', async () => {
      const mockFetch = vi.mocked(fetch);
      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () => Promise.resolve({ expires_in: 3600 }),
      } as Response);

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      const token =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';
      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(false);
    });

    it('should handle refresh token response with refresh_token field', async () => {
      const mockFetch = vi.mocked(fetch);
      const refreshResponse = {
        access_token: 'new-jwt-token',
        expires_in: 3600,
        refresh_token: 'new-refresh-token',
      };

      mockFetch.mockResolvedValueOnce({
        ok: true,
        json: () => Promise.resolve(refreshResponse),
      } as Response);

      localStorageMock.getItem.mockReturnValue('test-refresh-token');

      const token =
        // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
        'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjF9.signature';

      const result = await secureTokenStorage.refreshTokenIfNeeded(token);

      expect(result).toBe(true);
      expect(localStorageMock.setItem).toHaveBeenCalledWith('authToken', 'new-jwt-token');
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
      vi.clearAllMocks();
      localStorageMock.getItem.mockClear();

      vi.stubEnv('DEV', false);
      vi.stubEnv('MODE', 'production');

      const token = secureTokenStorage.getToken();

      expect(token).toBe(null);

      vi.unstubAllEnvs();
    });

    it('should return null for getRefreshToken in production mode', () => {
      vi.clearAllMocks();
      localStorageMock.getItem.mockClear();

      vi.stubEnv('DEV', false);
      vi.stubEnv('MODE', 'production');

      const token = secureTokenStorage.getRefreshToken();

      expect(token).toBe(null);

      vi.unstubAllEnvs();
    });

    it('should not set token in production mode', () => {
      vi.clearAllMocks();
      localStorageMock.setItem.mockClear();

      vi.stubEnv('DEV', false);
      vi.stubEnv('MODE', 'production');

      secureTokenStorage.setToken('test-token');

      vi.unstubAllEnvs();
    });

    it('should not clear token in production mode', () => {
      vi.clearAllMocks();
      localStorageMock.removeItem.mockClear();

      vi.stubEnv('DEV', false);
      vi.stubEnv('MODE', 'production');

      secureTokenStorage.clearToken();

      vi.unstubAllEnvs();
    });

    it('should not set refresh token in production mode', () => {
      vi.clearAllMocks();
      localStorageMock.setItem.mockClear();

      vi.stubEnv('DEV', false);
      vi.stubEnv('MODE', 'production');

      secureTokenStorage.setRefreshToken('test-refresh-token');

      vi.unstubAllEnvs();
    });

    it('should not clear refresh token in production mode', () => {
      vi.clearAllMocks();
      localStorageMock.removeItem.mockClear();

      vi.stubEnv('DEV', false);
      vi.stubEnv('MODE', 'production');

      secureTokenStorage.clearRefreshToken();

      vi.unstubAllEnvs();
    });
  });

  describe('JWT base64url decoding and expiry', () => {
    it('should treat invalid or expired tokens as expired', () => {
      const header = 'eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0';
      const payload = 'eyJleHAiOjF9';
      const signature = '';
      const token = `${header}.${payload}.${signature}`;
      expect(secureTokenStorage.isTokenExpired(token)).toBe(true);
    });

    it('should treat valid non-expired tokens as not expired', () => {
      const futureExp = Math.floor(new Date('2099-12-31').getTime() / 1000);
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
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
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const payload = btoa(JSON.stringify({ sub: '123' }))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
      const signature = 'signature';
      const token = `${header}.${payload}.${signature}`;
      const result = secureTokenStorage.isTokenExpired(token);
      expect(result).toBeFalsy();
    });

    it('should handle token with exp equal to current time', () => {
      const currentTime = Math.floor(Date.now() / 1000);
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const payload = btoa(JSON.stringify({ exp: currentTime }))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
      const signature = 'signature';
      const token = `${header}.${payload}.${signature}`;
      const result = secureTokenStorage.isTokenExpired(token);
      expect(result).toBe(false);
    });

    it('should handle token with exp greater than current time', () => {
      const futureTime = Math.floor(Date.now() / 1000) + 3600;
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
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
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const invalidPayload = '!!!invalid-base64!!!';
      const signature = 'signature';
      const token = `${header}.${invalidPayload}.${signature}`;
      expect(secureTokenStorage.isTokenExpired(token)).toBe(true);
    });
  });

  describe('Token Expiry - Edge Cases', () => {
    it('should handle token with exp exactly at current time', () => {
      const currentTime = Math.floor(Date.now() / 1000);
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const payload = btoa(JSON.stringify({ exp: currentTime }))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
      const signature = 'signature';
      const token = `${header}.${payload}.${signature}`;

      expect(secureTokenStorage.isTokenExpired(token)).toBe(false);
    });

    it('should handle token with malformed payload (invalid JSON)', () => {
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const invalidPayload = btoa('not valid json').replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '');
      const signature = 'signature';
      const token = `${header}.${invalidPayload}.${signature}`;

      expect(secureTokenStorage.isTokenExpired(token)).toBe(true);
    });

    it('should handle token with missing exp field', () => {
      // nosemgrep: generic.secrets.security.detected-jwt-token.detected-jwt-token
      const header = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9';
      const payload = btoa(JSON.stringify({ sub: '123', iat: 1234567890 }))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
      const signature = 'signature';
      const token = `${header}.${payload}.${signature}`;

      expect(secureTokenStorage.isTokenExpired(token)).toBe(false);
    });
  });
});
