import { describe, expect, it } from 'vitest';
import { getApiBaseUrl, API_BASE_URL } from '../config';

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

    it('should return localhost:54731 in development mode', () => {
      // Act
      const url = getApiBaseUrl();

      // Assert
      // In test environment, should default to development
      if (!import.meta.env.PROD) {
        expect(url).toBe('http://localhost:54731');
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
});
