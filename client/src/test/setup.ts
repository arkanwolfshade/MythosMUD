/// <reference types="node" />
// Vitest: use afterEach(vi.clearAllMocks()) or afterEach(spy.mockRestore()) when using vi.mock or vi.spyOn(global).
// TypeScript: In tests, `as any` for mock setup (e.g. vi.mock return values, global overrides) is acceptable when
// typing the mock is impractical. Prefer vi.mocked(module) or typed mock interfaces where feasible.
import '@testing-library/jest-dom/vitest';
import { mkdirSync } from 'fs';
import { join } from 'path';
import { afterAll, beforeAll, vi } from 'vitest';

// Type definition for global in test environment
declare global {
  var global: typeof globalThis;
}

// Ensure coverage temp directory exists
try {
  const coverageTmpDir = join(process.cwd(), 'coverage', '.tmp');
  mkdirSync(coverageTmpDir, { recursive: true });
} catch (error) {
  // Directory might already exist, which is fine
  if ((error as NodeJS.ErrnoException).code !== 'EEXIST') {
    console.warn('Failed to create coverage temp directory:', error);
  }
}

// Mock window.matchMedia for components that use media queries
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation((query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(), // deprecated
    removeListener: vi.fn(), // deprecated
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});

// Mock ResizeObserver
global.ResizeObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}));

// Mock IntersectionObserver
global.IntersectionObserver = vi.fn().mockImplementation(() => ({
  observe: vi.fn(),
  unobserve: vi.fn(),
  disconnect: vi.fn(),
}));

// Mock scrollIntoView for DOM elements
Element.prototype.scrollIntoView = vi.fn();

// Mock console methods to reduce noise in tests
const originalError = console.error;
const originalWarn = console.warn;

beforeAll(() => {
  console.error = (...args: unknown[]) => {
    if (typeof args[0] === 'string' && args[0].includes('Warning: ReactDOM.render is no longer supported')) {
      return;
    }
    originalError.call(console, ...args);
  };

  console.warn = (...args: unknown[]) => {
    if (
      typeof args[0] === 'string' &&
      (args[0].includes('componentWillReceiveProps') || args[0].includes('componentWillUpdate'))
    ) {
      return;
    }
    originalWarn.call(console, ...args);
  };
});

afterAll(() => {
  console.error = originalError;
  console.warn = originalWarn;
});
