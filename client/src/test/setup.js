/// <reference types="node" />
import '@testing-library/jest-dom/vitest';
import { mkdirSync } from 'fs';
import { join } from 'path';
import { afterAll, beforeAll, vi } from 'vitest';
// Ensure coverage temp directory exists
try {
  const coverageTmpDir = join(process.cwd(), 'coverage', '.tmp');
  mkdirSync(coverageTmpDir, { recursive: true });
} catch (error) {
  // Directory might already exist, which is fine
  if (error.code !== 'EEXIST') {
    console.warn('Failed to create coverage temp directory:', error);
  }
}
// Mock window.matchMedia for components that use media queries
Object.defineProperty(window, 'matchMedia', {
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
  console.error = (...args) => {
    if (typeof args[0] === 'string' && args[0].includes('Warning: ReactDOM.render is no longer supported')) {
      return;
    }
    originalError.call(console, ...args);
  };
  console.warn = (...args) => {
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
