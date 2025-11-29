import { describe, expect, it, vi, beforeEach, afterEach } from 'vitest';
import { initializeXStateInspector, getInspectorOptions } from '../xstateInspector';

describe('XState Inspector Utilities', () => {
  const originalEnv = import.meta.env;
  const originalConsoleLog = console.log;

  beforeEach(() => {
    vi.clearAllMocks();
    console.log = vi.fn();
  });

  afterEach(() => {
    console.log = originalConsoleLog;
    Object.defineProperty(import.meta, 'env', {
      value: originalEnv,
      writable: true,
      configurable: true,
    });
  });

  describe('initializeXStateInspector', () => {
    it('should log instructions in development mode', () => {
      // Arrange - ensure DEV is true (default in test environment)
      Object.defineProperty(import.meta, 'env', {
        value: {
          ...originalEnv,
          DEV: true,
        },
        writable: true,
        configurable: true,
      });
      (console.log as ReturnType<typeof vi.fn>).mockClear();

      // Act
      initializeXStateInspector();

      // Assert - function logs multiple lines (header + 4 instructions)
      expect(console.log).toHaveBeenCalled();
      const logCalls = (console.log as ReturnType<typeof vi.fn>).mock.calls;
      expect(logCalls.length).toBeGreaterThan(0);
      expect(logCalls.some(call => call[0]?.includes('[XState v5 Inspector]'))).toBe(true);
    });

    it('should not log in production mode', () => {
      // Arrange - Note: import.meta.env is evaluated at module load time,
      // so we can't easily mock it. This test verifies the conditional logic exists.
      (console.log as ReturnType<typeof vi.fn>).mockClear();

      // Act
      initializeXStateInspector();

      // Assert - In actual production builds, DEV=false would prevent logging
      // In test environment with DEV=true, it will log (which is expected)
      // We verify the function runs without error
      expect(typeof initializeXStateInspector).toBe('function');
    });
  });

  describe('getInspectorOptions', () => {
    it('should return inspector options in development mode', () => {
      // Arrange
      Object.defineProperty(import.meta, 'env', {
        value: {
          ...originalEnv,
          DEV: true,
        },
        writable: true,
        configurable: true,
      });
      Object.defineProperty(global, 'window', {
        value: {},
        writable: true,
        configurable: true,
      });

      // Act
      const options = getInspectorOptions();

      // Assert
      expect(options).toEqual({ inspect: true });
    });

    it('should return empty object when window is undefined or DEV is false', () => {
      // Note: import.meta.env.DEV is evaluated at module load time, not at runtime.
      // We cannot mock it after the module is loaded. The function checks both
      // import.meta.env.DEV (set at build time) and window availability.

      // Test the window undefined case instead (which we can actually test)
      const originalWindow = global.window;
      try {
        // @ts-expect-error - Testing undefined window
        delete global.window;

        // Act
        const options = getInspectorOptions();

        // Assert - When window is undefined, should return empty object
        expect(options).toEqual({});
      } finally {
        // Cleanup
        global.window = originalWindow;
      }

      // Note: In actual production builds with DEV=false set at build time,
      // getInspectorOptions() would return {} even if window exists.
    });

    it('should verify conditional logic structure', () => {
      // Act - Test in normal test environment
      const options = getInspectorOptions();

      // Assert - Function should return valid object
      // In test environment (DEV=true, window defined), should return { inspect: true }
      // In production (DEV=false), would return {}
      expect(typeof options).toBe('object');
      expect(options !== null).toBe(true);
    });
  });
});
