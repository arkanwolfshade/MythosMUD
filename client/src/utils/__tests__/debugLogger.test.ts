import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { debugLogger } from '../debugLogger';

// Mock console methods
const mockConsole = {
  debug: vi.fn(),
  log: vi.fn(),
  warn: vi.fn(),
  error: vi.fn(),
};

// Mock environment variables
const originalEnv = process.env;

describe('debugLogger', () => {
  beforeEach(() => {
    // Reset mocks
    vi.clearAllMocks();

    // Mock console
    Object.assign(console, mockConsole);

    // Reset environment
    process.env = { ...originalEnv };
  });

  afterEach(() => {
    process.env = originalEnv;
  });

  describe('environment-based logging', () => {
    it('should log debug messages in development', () => {
      process.env.NODE_ENV = 'development';
      const logger = debugLogger('TestComponent');

      logger.debug('Test debug message', { test: 'data' });

      expect(mockConsole.debug).toHaveBeenCalledWith(
        expect.stringContaining('[DEBUG] [TestComponent] Test debug message'),
        { test: 'data' }
      );
    });

    it('should not log debug messages in production', () => {
      process.env.NODE_ENV = 'production';
      const logger = debugLogger('TestComponent');

      logger.debug('Test debug message', { test: 'data' });

      expect(mockConsole.debug).not.toHaveBeenCalled();
    });

    it('should always log error messages regardless of environment', () => {
      process.env.NODE_ENV = 'production';
      const logger = debugLogger('TestComponent');

      logger.error('Test error message', { error: 'data' });

      expect(mockConsole.error).toHaveBeenCalledWith(
        expect.stringContaining('[ERROR] [TestComponent] Test error message'),
        { error: 'data' }
      );
    });

    it('should respect custom log level configuration', () => {
      process.env.NODE_ENV = 'development';
      process.env.VITE_LOG_LEVEL = 'WARN';
      const logger = debugLogger('TestComponent');

      logger.debug('Debug message');
      logger.info('Info message');
      logger.warn('Warning message');
      logger.error('Error message');

      expect(mockConsole.debug).not.toHaveBeenCalled();
      expect(mockConsole.log).not.toHaveBeenCalled();
      expect(mockConsole.warn).toHaveBeenCalled();
      expect(mockConsole.error).toHaveBeenCalled();
    });
  });

  describe('log levels', () => {
    beforeEach(() => {
      process.env.NODE_ENV = 'development';
    });

    it('should log info messages correctly', () => {
      const logger = debugLogger('TestComponent');

      logger.info('Test info message', { info: 'data' });

      expect(mockConsole.log).toHaveBeenCalledWith(
        expect.stringContaining('[INFO] [TestComponent] Test info message'),
        { info: 'data' }
      );
    });

    it('should log warning messages correctly', () => {
      const logger = debugLogger('TestComponent');

      logger.warn('Test warning message', { warning: 'data' });

      expect(mockConsole.warn).toHaveBeenCalledWith(
        expect.stringContaining('[WARN] [TestComponent] Test warning message'),
        { warning: 'data' }
      );
    });

    it('should log error messages correctly', () => {
      const logger = debugLogger('TestComponent');

      logger.error('Test error message', { error: 'data' });

      expect(mockConsole.error).toHaveBeenCalledWith(
        expect.stringContaining('[ERROR] [TestComponent] Test error message'),
        { error: 'data' }
      );
    });
  });

  describe('log format', () => {
    beforeEach(() => {
      process.env.NODE_ENV = 'development';
    });

    it('should include timestamp in log format', () => {
      const logger = debugLogger('TestComponent');
      const beforeTime = new Date().toISOString();

      logger.info('Test message');

      const afterTime = new Date().toISOString();
      const logCall = mockConsole.log.mock.calls[0][0];

      // Extract timestamp from log message
      const timestampMatch = logCall.match(/\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)\]/);
      expect(timestampMatch).toBeTruthy();

      const logTime = timestampMatch![1];
      expect(logTime >= beforeTime && logTime <= afterTime).toBe(true);
    });

    it('should include component name in log format', () => {
      const logger = debugLogger('MyComponent');

      logger.info('Test message');

      expect(mockConsole.log).toHaveBeenCalledWith(expect.stringContaining('[MyComponent]'), expect.anything());
    });

    it('should handle messages without data', () => {
      const logger = debugLogger('TestComponent');

      logger.info('Simple message');

      expect(mockConsole.log).toHaveBeenCalledWith(
        expect.stringContaining('[INFO] [TestComponent] Simple message'),
        ''
      );
    });
  });

  describe('build-time debug removal', () => {
    it('should have debug method available in development', () => {
      process.env.NODE_ENV = 'development';
      const logger = debugLogger('TestComponent');

      expect(typeof logger.debug).toBe('function');
    });

    it('should handle debug method calls gracefully in production', () => {
      process.env.NODE_ENV = 'production';
      const logger = debugLogger('TestComponent');

      // Should not throw error even if debug is called
      expect(() => logger.debug('Test message')).not.toThrow();
    });
  });
});
