/**
 * Shared test utilities and mocks for security tests.
 */

import { vi } from 'vitest';

// Mock localStorage
export const localStorageMock = {
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
globalThis.fetch = vi.fn();

/**
 * Setup default mocks for security tests.
 */
export const setupSecurityMocks = () => {
  vi.clearAllMocks();
  document.cookie = '';
  localStorageMock.getItem.mockClear();
  localStorageMock.setItem.mockClear();
  localStorageMock.removeItem.mockClear();
  localStorageMock.clear.mockClear();
};
