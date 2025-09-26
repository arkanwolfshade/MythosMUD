import { renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { MemoryMonitor, useMemoryMonitor } from '../memoryMonitor';

// Mock performance.memory
const mockMemory = {
  usedJSHeapSize: 50 * 1024 * 1024, // 50MB
  totalJSHeapSize: 100 * 1024 * 1024, // 100MB
  jsHeapSizeLimit: 200 * 1024 * 1024, // 200MB
};

// Mock performance object
Object.defineProperty(global, 'performance', {
  value: {
    memory: mockMemory,
  },
  writable: true,
});

// Mock window.setInterval and clearInterval
const mockSetInterval = vi.fn().mockReturnValue(123);
const mockClearInterval = vi.fn();

Object.defineProperty(global, 'setInterval', {
  value: mockSetInterval,
  writable: true,
});

Object.defineProperty(global, 'clearInterval', {
  value: mockClearInterval,
  writable: true,
});

// Mock window object
Object.defineProperty(global, 'window', {
  value: {
    setInterval: mockSetInterval,
    clearInterval: mockClearInterval,
    gtag: vi.fn(),
  },
  writable: true,
});

describe('MemoryMonitor', () => {
  let monitor: MemoryMonitor;
  let originalConsoleWarn: typeof console.warn;
  let originalConsoleError: typeof console.error;

  beforeEach(() => {
    vi.clearAllMocks();

    // Mock console methods to prevent stderr noise during tests
    originalConsoleWarn = console.warn;
    originalConsoleError = console.error;
    console.warn = vi.fn();
    console.error = vi.fn();

    // Reset singleton instance
    (MemoryMonitor as { instance: MemoryMonitor | null }).instance = null;
    monitor = MemoryMonitor.getInstance({
      enableReporting: false, // Disable reporting for tests
      warningThreshold: 30,
      criticalThreshold: 80,
    });
  });

  afterEach(() => {
    monitor.stop();

    // Restore original console methods
    console.warn = originalConsoleWarn;
    console.error = originalConsoleError;
  });

  describe('Singleton Pattern', () => {
    it('should return the same instance', () => {
      const instance1 = MemoryMonitor.getInstance();
      const instance2 = MemoryMonitor.getInstance();
      expect(instance1).toBe(instance2);
    });

    it('should create new instance with options on first call', () => {
      const newMonitor = MemoryMonitor.getInstance({
        warningThreshold: 40,
        criticalThreshold: 90,
      });
      expect(newMonitor).toBeInstanceOf(MemoryMonitor);
    });
  });

  describe('Basic Functionality', () => {
    it('should start and stop monitoring', () => {
      monitor.start();
      expect(mockSetInterval).toHaveBeenCalled();

      // Get the interval ID that was set
      const intervalId = mockSetInterval.mock.results[0].value;

      monitor.stop();
      expect(mockClearInterval).toHaveBeenCalledWith(intervalId);
    });

    it('should handle start/stop multiple times', () => {
      monitor.start();
      monitor.start(); // Should not create multiple intervals
      monitor.stop();
      monitor.stop(); // Should not throw
    });
  });

  describe('Component Registration', () => {
    it('should register and unregister components', () => {
      const detector = monitor.registerComponent('TestComponent');
      expect(detector).toBeDefined();

      const stats = monitor.getComponentStats('TestComponent');
      expect(stats).toBeNull(); // No snapshots yet

      monitor.unregisterComponent('TestComponent');
      expect(monitor.getComponentStats('TestComponent')).toBeNull();
    });

    it('should return same detector for same component', () => {
      const detector1 = monitor.registerComponent('TestComponent');
      const detector2 = monitor.registerComponent('TestComponent');
      expect(detector1).toBe(detector2);
    });

    it('should handle unregistering non-existent component', () => {
      expect(() => monitor.unregisterComponent('NonExistent')).not.toThrow();
    });
  });

  describe('Memory Statistics', () => {
    it('should get overall memory statistics', () => {
      const stats = monitor.getOverallStats();
      expect(stats).toBeNull(); // No snapshots yet
    });

    it('should get component memory statistics', () => {
      monitor.registerComponent('TestComponent');
      const stats = monitor.getComponentStats('TestComponent');
      expect(stats).toBeNull(); // No snapshots yet
    });
  });

  describe('Memory Reports', () => {
    it('should generate memory reports', () => {
      const report = monitor.generateReport('TestComponent');

      expect(report).toMatchObject({
        timestamp: expect.any(Number),
        componentName: 'TestComponent',
        memoryUsage: expect.any(Object),
        resourceStats: expect.any(Object),
        warnings: expect.any(Array),
        recommendations: expect.any(Array),
      });
    });

    it('should generate overall memory reports', () => {
      const report = monitor.generateReport();

      expect(report.componentName).toBe('overall');
      expect(report.memoryUsage).toBeDefined();
      expect(report.resourceStats).toBeDefined();
    });

    it('should store and retrieve reports', () => {
      monitor.generateReport('Component1');
      const report2 = monitor.generateReport('Component2');

      const reports = monitor.getReports();
      expect(reports).toHaveLength(2);

      const recentReports = monitor.getRecentReports(1);
      expect(recentReports).toHaveLength(1);
      expect(recentReports[0]).toBe(report2);
    });

    it('should limit number of stored reports', () => {
      // Reset singleton to create new instance with maxReports: 3
      (MemoryMonitor as { instance: MemoryMonitor | null }).instance = null;
      monitor = MemoryMonitor.getInstance({ maxReports: 3 });

      monitor.generateReport('Component1');
      monitor.generateReport('Component2');
      monitor.generateReport('Component3');
      monitor.generateReport('Component4');

      const reports = monitor.getReports();
      expect(reports).toHaveLength(3);
      expect(reports[0].componentName).toBe('Component2'); // First report should be removed
    });
  });

  describe('Memory Warnings and Recommendations', () => {
    it('should generate warnings for high memory usage', () => {
      // Set memory above warning threshold
      (global.performance as { memory: { usedJSHeapSize: number } }).memory.usedJSHeapSize = 40 * 1024 * 1024; // 40MB

      // Start the detector to collect memory data
      monitor.start();

      // Simulate memory check
      const intervalCallback = mockSetInterval.mock.calls[0][0];
      intervalCallback();

      const report = monitor.generateReport();

      expect(report.warnings.some(w => w.includes('High memory usage'))).toBe(true);
      expect(report.recommendations.some(r => r.includes('Monitor memory usage'))).toBe(true);
    });

    it('should generate critical warnings for very high memory usage', () => {
      // Set memory above critical threshold
      (global.performance as { memory: { usedJSHeapSize: number } }).memory.usedJSHeapSize = 90 * 1024 * 1024; // 90MB

      // Start the detector to collect memory data
      monitor.start();

      // Simulate memory check
      const intervalCallback = mockSetInterval.mock.calls[0][0];
      intervalCallback();

      const report = monitor.generateReport();

      expect(report.warnings.some(w => w.includes('Critical memory usage'))).toBe(true);
      expect(report.recommendations.some(r => r.includes('Consider reducing memory usage'))).toBe(true);
    });

    it('should not generate warnings for normal memory usage', () => {
      // Set memory below warning threshold
      (global.performance as { memory: { usedJSHeapSize: number } }).memory.usedJSHeapSize = 20 * 1024 * 1024; // 20MB

      const report = monitor.generateReport();

      expect(report.warnings).toHaveLength(0);
      expect(report.recommendations).toHaveLength(0);
    });
  });

  describe('Utility Methods', () => {
    it('should clear reports', () => {
      monitor.generateReport('TestComponent');
      expect(monitor.getReports()).toHaveLength(1);

      monitor.clearReports();
      expect(monitor.getReports()).toHaveLength(0);
    });

    it('should export reports as JSON', () => {
      monitor.generateReport('TestComponent');
      const exported = monitor.exportReports();

      expect(() => JSON.parse(exported)).not.toThrow();
      const parsed = JSON.parse(exported);
      expect(parsed).toHaveLength(1);
      expect(parsed[0].componentName).toBe('TestComponent');
    });

    it('should get memory summary', () => {
      monitor.registerComponent('Component1');
      monitor.registerComponent('Component2');
      monitor.generateReport('Component1');

      const summary = monitor.getMemorySummary();

      expect(summary).toMatchObject({
        overall: expect.any(Object),
        components: expect.any(Array),
        totalReports: expect.any(Number),
        recentWarnings: expect.any(Number),
      });

      expect(summary.components).toHaveLength(2);
      expect(summary.totalReports).toBe(1);
    });
  });

  describe('Reporting', () => {
    it('should start automatic reporting when enabled', () => {
      // Reset singleton to create new instance
      (MemoryMonitor as { instance: MemoryMonitor | null }).instance = null;

      const reportingMonitor = MemoryMonitor.getInstance({
        enableReporting: true,
        reportInterval: 1000,
      });

      expect(mockSetInterval).toHaveBeenCalledWith(expect.any(Function), 1000);

      reportingMonitor.stop();
    });

    it('should not start automatic reporting when disabled', () => {
      MemoryMonitor.getInstance({
        enableReporting: false,
      });

      // Should not have called setInterval for reporting
      expect(mockSetInterval).not.toHaveBeenCalledWith(expect.any(Function), expect.any(Number));
    });
  });
});

describe('useMemoryMonitor Hook', () => {
  let monitor: MemoryMonitor;
  let originalConsoleWarn: typeof console.warn;
  let originalConsoleError: typeof console.error;

  beforeEach(() => {
    vi.clearAllMocks();

    // Mock console methods to prevent stderr noise during tests
    originalConsoleWarn = console.warn;
    originalConsoleError = console.error;
    console.warn = vi.fn();
    console.error = vi.fn();

    (MemoryMonitor as { instance: MemoryMonitor | null }).instance = null;
    monitor = MemoryMonitor.getInstance({ enableReporting: false });
  });

  afterEach(() => {
    monitor.stop();

    // Restore original console methods
    console.warn = originalConsoleWarn;
    console.error = originalConsoleError;
  });

  it('should register component and return monitoring utilities', () => {
    const { result } = renderHook(() => useMemoryMonitor('TestComponent'));

    expect(result.current.detector).toBeDefined();
    expect(result.current.getStats).toBeInstanceOf(Function);
    expect(result.current.generateReport).toBeInstanceOf(Function);
    expect(result.current.unregister).toBeInstanceOf(Function);
  });

  it('should unregister component on unmount', () => {
    const unregisterSpy = vi.spyOn(monitor, 'unregisterComponent');

    const { unmount } = renderHook(() => useMemoryMonitor('TestComponent'));

    unmount();

    expect(unregisterSpy).toHaveBeenCalledWith('TestComponent');
  });

  it('should return same detector instance on re-render', () => {
    const { result, rerender } = renderHook(() => useMemoryMonitor('TestComponent'));

    const detector1 = result.current.detector;
    rerender();
    const detector2 = result.current.detector;

    expect(detector1).toBe(detector2);
  });
});
