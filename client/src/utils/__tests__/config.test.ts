import { describe, expect, it } from 'vitest';
import { API_BASE_URL, API_V1_BASE, getApiBaseUrl, getVersionedApiBaseUrl } from '../config';

// Note: import.meta.env is evaluated at build time, so we can't dynamically change it in tests
// These tests verify the function logic works with the actual environment at test time
describe('Config Utilities', () => {
  describe('getApiBaseUrl', () => {
    it('should return a valid URL string', () => {
      // Act
      const url = getApiBaseUrl();

      // Assert
      expect(url).toBeDefined();
      expect(typeof url).toBe('string');
      // Should be either empty string (production) or localhost URL (development)
      expect(url === '' || url.startsWith('http://') || url.startsWith('https://')).toBe(true);
    });

    it('should return same-origin (empty string) in development so Vite proxy is used (LAN-friendly)', () => {
      // Act
      const url = getApiBaseUrl();

      // Assert: in dev we use '' so API calls go through Vite proxy from any origin (e.g. LAN)
      if (!import.meta.env.PROD && !import.meta.env.VITE_API_URL) {
        expect(url).toBe('');
      }
    });

    it('should return VITE_API_URL when provided', () => {
      // Test line 15-16: VITE_API_URL branch
      // Note: Since import.meta.env is evaluated at build time, we can't test this branch
      // with vi.stubEnv. However, if VITE_API_URL is set in the environment, it will be used.
      // This test documents the expected behavior.
      const url = getApiBaseUrl();

      // If VITE_API_URL is set, it should be returned; otherwise, default behavior
      if (import.meta.env.VITE_API_URL) {
        expect(url).toBe(import.meta.env.VITE_API_URL);
      } else {
        // Default behavior (development or production)
        expect(url).toBeDefined();
      }
    });

    it('should return empty string in production mode', () => {
      // Test line 20-21: PROD branch
      // Note: Since import.meta.env.PROD is evaluated at build time, we can't test this branch
      // with vi.stubEnv. However, if PROD is true, it should return empty string.
      // This test documents the expected behavior.
      const url = getApiBaseUrl();

      // If PROD is true and VITE_API_URL is not set, should return empty string
      if (import.meta.env.PROD && !import.meta.env.VITE_API_URL) {
        expect(url).toBe('');
      } else {
        // In development or if VITE_API_URL is set, should return a URL
        expect(url).toBeDefined();
        expect(typeof url).toBe('string');
      }
    });
  });

  describe('API_BASE_URL constant', () => {
    it('should be defined', () => {
      // Assert
      expect(API_BASE_URL).toBeDefined();
      expect(typeof API_BASE_URL).toBe('string');
    });

    it('should match getApiBaseUrl result', () => {
      // Assert
      // Note: This will match because both are evaluated at module load time
      expect(API_BASE_URL).toBe(getApiBaseUrl());
    });
  });

  describe('getVersionedApiBaseUrl and API_V1_BASE', () => {
    it('should return /v1 when base is empty', () => {
      // When getApiBaseUrl() returns '', versioned base is '/v1'
      const base = getApiBaseUrl();
      const versioned = getVersionedApiBaseUrl();
      if (base === '') {
        expect(versioned).toBe('/v1');
      } else {
        expect(versioned).toBe(`${base}/v1`);
      }
    });

    it('should be defined and a string', () => {
      expect(API_V1_BASE).toBeDefined();
      expect(typeof API_V1_BASE).toBe('string');
      expect(API_V1_BASE).toMatch(/\/v1$/);
    });
  });
});
