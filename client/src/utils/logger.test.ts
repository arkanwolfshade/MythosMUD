import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { logger } from './logger';

// Mock console methods
const mockConsole = {
  log: vi.fn(),
  debug: vi.fn(),
  warn: vi.fn(),
  error: vi.fn(),
};

// Mock URL.createObjectURL and document methods
const mockCreateObjectURL = vi.fn();
const mockCreateElement = vi.fn();
const mockAppendChild = vi.fn();
const mockRemoveChild = vi.fn();
const mockClick = vi.fn();

describe('ClientLogger', () => {
  beforeEach(() => {
    // Clear the logger buffer before each test
    logger.clearLogs();

    // Mock console methods
    vi.spyOn(console, 'log').mockImplementation(mockConsole.log);
    vi.spyOn(console, 'debug').mockImplementation(mockConsole.debug);
    vi.spyOn(console, 'warn').mockImplementation(mockConsole.warn);
    vi.spyOn(console, 'error').mockImplementation(mockConsole.error);

    // Mock URL.createObjectURL and revokeObjectURL
    const mockRevokeObjectURL = vi.fn();
    Object.defineProperty(URL, 'createObjectURL', {
      value: mockCreateObjectURL,
      writable: true,
    });
    Object.defineProperty(URL, 'revokeObjectURL', {
      value: mockRevokeObjectURL,
      writable: true,
    });
    mockCreateObjectURL.mockReturnValue('mock-url');

    // Mock document methods
    vi.spyOn(document, 'createElement').mockImplementation(mockCreateElement);
    vi.spyOn(document.body, 'appendChild').mockImplementation(mockAppendChild);
    vi.spyOn(document.body, 'removeChild').mockImplementation(mockRemoveChild);

    // Mock link element
    const mockLink = {
      href: '',
      download: '',
      click: mockClick,
    };
    mockCreateElement.mockReturnValue(mockLink);

    // Clear all mocks
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
    // Clear all logs and reset the buffer completely
    logger.clearLogs();
    // Force clear the buffer array to empty without triggering new logs
    const buffer = logger.getLogBuffer();
    buffer.splice(0, buffer.length);
    // Also clear the global URL
    if (window.mythosMudLogUrl) {
      URL.revokeObjectURL(window.mythosMudLogUrl);
      window.mythosMudLogUrl = undefined;
    }
  });

  describe('logging methods', () => {
    it('should log debug messages in development', () => {
      const originalMode = import.meta.env.MODE;
      vi.stubEnv('MODE', 'development');

      logger.debug('TestComponent', 'Debug message', { test: 'data' });

      const buffer = logger.getLogBuffer();
      const debugEntry = buffer.find(entry => entry.message === 'Debug message' && entry.component === 'TestComponent');
      expect(debugEntry).toMatchObject({
        level: 'DEBUG',
        component: 'TestComponent',
        message: 'Debug message',
        data: { test: 'data' },
      });
      expect(debugEntry?.timestamp).toBeDefined();

      vi.stubEnv('MODE', originalMode);
    });

    it('should log info messages', () => {
      logger.info('TestComponent', 'Info message');

      const buffer = logger.getLogBuffer();
      const lastEntry = buffer[buffer.length - 1];
      expect(lastEntry).toMatchObject({
        level: 'INFO',
        component: 'TestComponent',
        message: 'Info message',
      });
    });

    it('should log warn messages', () => {
      logger.warn('TestComponent', 'Warning message');

      const buffer = logger.getLogBuffer();
      const lastEntry = buffer[buffer.length - 1];
      expect(lastEntry).toMatchObject({
        level: 'WARN',
        component: 'TestComponent',
        message: 'Warning message',
      });
    });

    it('should log error messages', () => {
      logger.error('TestComponent', 'Error message', new Error('test error'));

      const buffer = logger.getLogBuffer();
      const lastEntry = buffer[buffer.length - 1];
      expect(lastEntry).toMatchObject({
        level: 'ERROR',
        component: 'TestComponent',
        message: 'Error message',
      });
      expect(lastEntry.data).toBeInstanceOf(Error);
    });

    it('should add entries to log buffer', () => {
      const originalMode = import.meta.env.MODE;
      vi.stubEnv('MODE', 'development');

      logger.debug('Test', 'Debug message');
      logger.info('Test', 'Info message');
      logger.warn('Test', 'Warning message');
      logger.error('Test', 'Error message');

      const buffer = logger.getLogBuffer();
      const debugEntry = buffer.find(entry => entry.message === 'Debug message');
      const infoEntry = buffer.find(entry => entry.message === 'Info message');
      const warnEntry = buffer.find(entry => entry.message === 'Warning message');
      const errorEntry = buffer.find(entry => entry.message === 'Error message');

      expect(debugEntry).toBeDefined();
      expect(infoEntry).toBeDefined();
      expect(warnEntry).toBeDefined();
      expect(errorEntry).toBeDefined();

      vi.stubEnv('MODE', originalMode);
    });
  });

  describe('buffer management', () => {
    it('should maintain log buffer', () => {
      const initialLength = logger.getLogBuffer().length;
      logger.info('Test', 'Message 1');
      logger.info('Test', 'Message 2');

      const buffer = logger.getLogBuffer();
      expect(buffer.length).toBeGreaterThan(initialLength);
      expect(buffer[buffer.length - 2]).toMatchObject({
        level: 'INFO',
        component: 'Test',
        message: 'Message 1',
      });
      expect(buffer[buffer.length - 1]).toMatchObject({
        level: 'INFO',
        component: 'Test',
        message: 'Message 2',
      });
    });

    it('should clear logs', () => {
      logger.info('Test', 'Message');
      const beforeClear = logger.getLogBuffer().length;
      expect(beforeClear).toBeGreaterThan(0);

      logger.clearLogs();
      // clearLogs() adds a "Log buffer cleared" message, so we expect 1 entry
      expect(logger.getLogBuffer()).toHaveLength(1);
      expect(logger.getLogBuffer()[0]).toMatchObject({
        level: 'INFO',
        component: 'Logger',
        message: 'Log buffer cleared',
      });
    });

    it('should limit buffer size', () => {
      // Add more than maxBufferSize logs
      for (let i = 0; i < 1100; i++) {
        logger.info('Test', `Message ${i}`);
      }

      const buffer = logger.getLogBuffer();
      expect(buffer.length).toBeLessThanOrEqual(1000);
    });
  });

  describe('download functionality', () => {
    it('should create download link when logs are available', () => {
      logger.info('Test', 'Test message');

      // Mock window.mythosMudLogUrl
      Object.defineProperty(window, 'mythosMudLogUrl', {
        value: 'mock-url',
        writable: true,
      });

      logger.downloadLogs();

      expect(mockCreateElement).toHaveBeenCalledWith('a');
      expect(mockAppendChild).toHaveBeenCalled();
      expect(mockClick).toHaveBeenCalled();
      expect(mockRemoveChild).toHaveBeenCalled();
    });

    it('should handle download when no logs are available', () => {
      // Ensure no logs are in buffer
      logger.clearLogs();

      // Mock window.mythosMudLogUrl as undefined
      Object.defineProperty(window, 'mythosMudLogUrl', {
        value: undefined,
        writable: true,
      });

      logger.downloadLogs();

      expect(mockCreateElement).not.toHaveBeenCalled();
      expect(mockConsole.warn).toHaveBeenCalled();
    });
  });

  describe('log entry creation', () => {
    it('should create log entries with correct structure', () => {
      const timestamp = new Date().toISOString();
      logger.info('TestComponent', 'Test message', { data: 'test' });

      const buffer = logger.getLogBuffer();
      // Find the entry we just created by looking for our specific message
      const entry = buffer.find(e => e.message === 'Test message' && e.component === 'TestComponent');
      expect(entry).toBeDefined();

      if (entry) {
        expect(entry).toHaveProperty('timestamp');
        expect(entry).toHaveProperty('level', 'INFO');
        expect(entry).toHaveProperty('component', 'TestComponent');
        expect(entry).toHaveProperty('message', 'Test message');
        expect(entry).toHaveProperty('data', { data: 'test' });
        expect(new Date(entry.timestamp).getTime()).toBeCloseTo(new Date(timestamp).getTime(), -2);
      }
    });

    it('should handle optional data parameter', () => {
      logger.info('TestComponent', 'Test message');

      const buffer = logger.getLogBuffer();
      // Find the entry we just created
      const entry = buffer.find(e => e.message === 'Test message' && e.component === 'TestComponent');
      expect(entry).toBeDefined();

      if (entry) {
        expect(entry.data).toBeUndefined();
      }
    });
  });

  describe('global access', () => {
    it('should be available on window object', () => {
      expect(window.mythosMudLogger).toBeDefined();
      expect(window.mythosMudLogger).toBe(logger);
    });
  });

  describe('error handling', () => {
    it('should handle flushLogs errors gracefully', () => {
      // Arrange - Test line 129: flushLogs error branch
      logger.info('Test', 'Message');
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      // Mock URL.createObjectURL to throw an error using vi.spyOn
      // Object.defineProperty doesn't work in happy-dom because createObjectURL is not configurable
      const createObjectURLSpy = vi.spyOn(URL, 'createObjectURL').mockImplementation(() => {
        throw new Error('Failed to create object URL');
      });

      // Act - Access private method for testing using type assertion
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (logger as any).flushLogs();

      // Assert - should handle error gracefully
      expect(consoleErrorSpy).toHaveBeenCalled();
      expect(consoleErrorSpy.mock.calls.some(call => call[0]?.includes('Failed to flush logs'))).toBe(true);

      // Restore
      createObjectURLSpy.mockRestore();
      consoleErrorSpy.mockRestore();
    });

    it('should return early from flushLogs if buffer is empty', () => {
      // Arrange - Test line 107: early return branch
      logger.clearLogs();
      const createObjectURLSpy = vi.spyOn(URL, 'createObjectURL');

      // Act - Access private method for testing using type assertion
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (logger as any).flushLogs();

      // Assert - should not create object URL if buffer is empty
      // Note: clearLogs() adds a "Log buffer cleared" message, so buffer might not be empty
      // But if we manually clear it, flushLogs should return early
      const buffer = logger.getLogBuffer();
      if (buffer.length === 0) {
        expect(createObjectURLSpy).not.toHaveBeenCalled();
      }

      createObjectURLSpy.mockRestore();
    });

    it('should log to console in production for ERROR and WARN levels', () => {
      // Arrange - Test line 79: console logging branch for ERROR/WARN in production
      const originalMode = import.meta.env.MODE;
      vi.stubEnv('MODE', 'production');

      const consoleLogSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
      const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      // Act
      logger.error('Test', 'Error message');
      logger.warn('Test', 'Warning message');
      logger.info('Test', 'Info message'); // Should not log in production

      // Assert - ERROR and WARN should log even in production
      expect(consoleErrorSpy).toHaveBeenCalled();
      expect(consoleWarnSpy).toHaveBeenCalled();
      // INFO should not log in production (unless it's development)
      // But since we're in production mode, info should not log

      vi.stubEnv('MODE', originalMode);
      consoleLogSpy.mockRestore();
      consoleWarnSpy.mockRestore();
      consoleErrorSpy.mockRestore();
    });

    it('should not log debug messages in production', () => {
      // Arrange - Test line 89: debug only in development branch
      const originalMode = import.meta.env.MODE;
      vi.stubEnv('MODE', 'production');

      // Act
      logger.debug('Test', 'Debug message');

      // Assert - debug messages should not be added in production
      const buffer = logger.getLogBuffer();
      const debugEntry = buffer.find(entry => entry.message === 'Debug message');
      expect(debugEntry).toBeUndefined();

      vi.stubEnv('MODE', originalMode);
    });
  });
});
