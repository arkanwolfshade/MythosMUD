/// <reference types="node" />
import '@testing-library/jest-dom/vitest';
import { mkdirSync } from 'fs';
import { join } from 'path';
import { afterAll, beforeAll, vi } from 'vitest';
// Ensure coverage temp directory exists
try {
  const cwd = globalThis.process?.cwd?.() ?? '.';
  const coverageTmpDir = join(String(cwd), 'coverage', '.tmp');
  mkdirSync(coverageTmpDir, { recursive: true });
} catch (error) {
  // Directory might already exist, which is fine
  if (error.code !== 'EEXIST') {
    globalThis.console?.warn?.('Failed to create coverage temp directory:', error);
  }
}
// Mock window.matchMedia for components that use media queries
const win = globalThis.window;
if (win) {
  Object.defineProperty(win, 'matchMedia', {
    writable: true,
    value: vi.fn().mockImplementation(query => ({
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
}
// Mock ResizeObserver
globalThis.ResizeObserver = class ResizeObserver {
  observe() {}
  unobserve() {}
  disconnect() {}
};
// Mock IntersectionObserver
globalThis.IntersectionObserver = class IntersectionObserver {
  constructor() {}
  disconnect() {}
  observe() {}
  takeRecords() {
    return [];
  }
  unobserve() {}
};
// Mock scrollIntoView for DOM elements
if (globalThis.Element?.prototype) {
  globalThis.Element.prototype.scrollIntoView = vi.fn();
}
// Mock console methods to reduce noise in tests
const originalConsole = globalThis.console;
const originalError = originalConsole?.error?.bind(originalConsole);
const originalWarn = originalConsole?.warn?.bind(originalConsole);
beforeAll(() => {
  if (!globalThis.console) return;
  globalThis.console.error = (...args) => {
    if (typeof args[0] === 'string' && args[0].includes('Warning: ReactDOM.render is no longer supported')) {
      return;
    }
    originalError?.(...args);
  };
  globalThis.console.warn = (...args) => {
    if (
      typeof args[0] === 'string' &&
      (args[0].includes('componentWillReceiveProps') || args[0].includes('componentWillUpdate'))
    ) {
      return;
    }
    originalWarn?.(...args);
  };
});
afterAll(() => {
  if (!globalThis.console) return;
  if (originalError) globalThis.console.error = originalError;
  if (originalWarn) globalThis.console.warn = originalWarn;
});
