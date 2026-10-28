/**
 * Shared test utilities and mocks for security tests.
 */

import { vi } from 'vitest';

// Mock localStorage. Annotated rather than inferred: the inferred mock type reaches into a vitest
// internal chunk (`Procedure`), which TS2883 rejects as non-portable for an exported declaration.
export const localStorageMock: {
  getItem: ReturnType<typeof vi.fn>;
  setItem: ReturnType<typeof vi.fn>;
  removeItem: ReturnType<typeof vi.fn>;
  clear: ReturnType<typeof vi.fn>;
} = {
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
