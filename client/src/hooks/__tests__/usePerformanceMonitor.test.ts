import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { usePerformanceMonitor } from '../usePerformanceMonitor';

describe('usePerformanceMonitor', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('should initialize with component name', () => {
    // Act
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Assert
    expect(result.current.startRender).toBeDefined();
    expect(result.current.endRender).toBeDefined();
    expect(result.current.getStats).toBeDefined();
  });

  it('should measure render time', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act
    act(() => {
      result.current.startRender();
    });

    // Simulate some work
    act(() => {
      vi.advanceTimersByTime(10);
      result.current.endRender();
    });

    // Assert
    const stats = result.current.getStats();
    expect(stats).toBeDefined();
    expect(stats?.totalRenders).toBe(1);
    expect(stats?.averageRenderTime).toBeGreaterThan(0);
  });

  it('should track multiple renders', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act
    for (let i = 0; i < 3; i++) {
      act(() => {
        result.current.startRender();
        vi.advanceTimersByTime(5);
        result.current.endRender();
      });
    }

    // Assert
    const stats = result.current.getStats();
    expect(stats?.totalRenders).toBe(3);
    expect(stats?.averageRenderTime).toBeGreaterThan(0);
  });

  it('should calculate statistics correctly', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    const renderTimes = [5, 10, 15, 20, 5];

    // Act
    renderTimes.forEach(time => {
      act(() => {
        result.current.startRender();
        vi.advanceTimersByTime(time);
        result.current.endRender();
      });
    });

    // Assert
    const stats = result.current.getStats();
    expect(stats?.totalRenders).toBe(5);
    expect(stats).not.toBeNull();
    if (stats) {
      expect(stats.minRenderTime).toBeLessThanOrEqual(stats.averageRenderTime);
      expect(stats.maxRenderTime).toBeGreaterThanOrEqual(stats.averageRenderTime);
      expect(stats.recentMetrics.length).toBeLessThanOrEqual(10);
    }
  });

  it('should warn when render time exceeds threshold', () => {
    // Arrange
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    const { result, unmount } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
        threshold: 8, // 8ms threshold
      })
    );

    // Act
    act(() => {
      result.current.startRender();
      vi.advanceTimersByTime(10); // Exceeds threshold
      result.current.endRender();
    });

    // Clean up immediately
    unmount();

    // Assert - should have render time warning
    const calls = consoleWarnSpy.mock.calls;
    const renderTimeWarnings = calls.filter(
      call => call[0]?.toString().includes('Performance warning') && call[0]?.toString().includes('TestComponent')
    );
    expect(renderTimeWarnings.length).toBeGreaterThan(0);
    consoleWarnSpy.mockRestore();
  });

  it('should not warn when render time is below threshold', () => {
    // Arrange
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    const { result, unmount } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
        threshold: 20,
      })
    );

    // Act
    act(() => {
      result.current.startRender();
      vi.advanceTimersByTime(5); // Below threshold
      result.current.endRender();
    });

    // Clean up immediately to stop memory monitoring interval
    unmount();

    // Assert - no render time warnings (memory warnings might occur from interval, ignore those)
    const calls = consoleWarnSpy.mock.calls;
    const renderTimeWarnings = calls.filter(call => call[0]?.toString().includes('Performance warning'));
    expect(renderTimeWarnings.length).toBe(0);
    consoleWarnSpy.mockRestore();
  });

  it('should call onMetrics callback when provided', () => {
    // Arrange
    const onMetrics = vi.fn();
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
        onMetrics,
      })
    );

    // Act
    act(() => {
      result.current.startRender();
      vi.advanceTimersByTime(5);
      result.current.endRender();
    });

    // Assert
    expect(onMetrics).toHaveBeenCalled();
    expect(onMetrics).toHaveBeenCalledWith(
      expect.objectContaining({
        componentName: 'TestComponent',
        renderTime: expect.any(Number),
        timestamp: expect.any(Number),
      })
    );
  });

  it('should include memory usage when available', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act
    act(() => {
      result.current.startRender();
      vi.advanceTimersByTime(5);
      result.current.endRender();
    });

    // Assert
    const stats = result.current.getStats();
    expect(stats?.recentMetrics[0]).toHaveProperty('memoryUsage');
    // memoryUsage may be undefined if not available in test environment
  });

  it('should set memoryUsage when performance.memory is available', () => {
    // Arrange - Test line 48: memory branch when available
    interface ExtendedPerformance extends Performance {
      memory?: {
        usedJSHeapSize: number;
        totalJSHeapSize: number;
        jsHeapSizeLimit: number;
      };
    }

    const mockMemory = {
      usedJSHeapSize: 50000000, // 50MB
      totalJSHeapSize: 100000000,
      jsHeapSizeLimit: 200000000,
    };

    // Mock performance.memory if it doesn't exist
    const originalPerformance = global.performance;
    if (!('memory' in global.performance)) {
      Object.defineProperty(global.performance, 'memory', {
        value: mockMemory,
        writable: true,
        configurable: true,
      });
    }

    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act
    act(() => {
      result.current.startRender();
      vi.advanceTimersByTime(5);
      result.current.endRender();
    });

    // Assert - memoryUsage should be set when memory is available
    const stats = result.current.getStats();
    if ('memory' in global.performance) {
      expect(stats?.recentMetrics[0].memoryUsage).toBeDefined();
      expect(typeof stats?.recentMetrics[0].memoryUsage).toBe('number');
    }

    // Restore original performance if we modified it
    if (!('memory' in originalPerformance)) {
      delete (global.performance as ExtendedPerformance).memory;
    }
  });

  it('should warn when memory usage exceeds 100MB', () => {
    // Arrange - Test lines 100-108: memory monitoring interval with warning
    interface ExtendedPerformance extends Performance {
      memory?: {
        usedJSHeapSize: number;
        totalJSHeapSize: number;
        jsHeapSizeLimit: number;
      };
    }

    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    const mockMemory = {
      usedJSHeapSize: 150 * 1024 * 1024, // 150MB (exceeds 100MB threshold)
      totalJSHeapSize: 200 * 1024 * 1024,
      jsHeapSizeLimit: 400 * 1024 * 1024,
    };

    // Mock performance.memory if it doesn't exist
    const hadMemory = 'memory' in global.performance;
    if (!hadMemory) {
      Object.defineProperty(global.performance, 'memory', {
        value: mockMemory,
        writable: true,
        configurable: true,
      });
    } else {
      // Update existing memory
      (global.performance as ExtendedPerformance).memory = mockMemory;
    }

    const { unmount } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
        enabled: true,
      })
    );

    // Act - advance timer to trigger memory check interval (5 seconds)
    act(() => {
      vi.advanceTimersByTime(5000);
    });

    // Assert - should have memory warning
    const calls = consoleWarnSpy.mock.calls;
    const memoryWarnings = calls.filter(
      call => call[0]?.toString().includes('Memory warning') && call[0]?.toString().includes('TestComponent')
    );
    expect(memoryWarnings.length).toBeGreaterThan(0);

    // Cleanup
    unmount();
    consoleWarnSpy.mockRestore();

    // Restore original performance if we modified it
    if (!hadMemory) {
      delete (global.performance as ExtendedPerformance).memory;
    }
  });

  it('should check memory when memory is available but below threshold', () => {
    // Arrange - Test lines 100-106: memory monitoring when memory exists but < 100MB
    interface ExtendedPerformance extends Performance {
      memory?: {
        usedJSHeapSize: number;
        totalJSHeapSize: number;
        jsHeapSizeLimit: number;
      };
    }

    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    const mockMemory = {
      usedJSHeapSize: 50 * 1024 * 1024, // 50MB (below 100MB threshold)
      totalJSHeapSize: 200 * 1024 * 1024,
      jsHeapSizeLimit: 400 * 1024 * 1024,
    };

    const hadMemory = 'memory' in global.performance;
    if (!hadMemory) {
      Object.defineProperty(global.performance, 'memory', {
        value: mockMemory,
        writable: true,
        configurable: true,
      });
    } else {
      (global.performance as ExtendedPerformance).memory = mockMemory;
    }

    const { unmount } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
        enabled: true,
      })
    );

    // Act - advance timer to trigger memory check interval (5 seconds)
    act(() => {
      vi.advanceTimersByTime(5000);
    });

    // Assert - should NOT have memory warning (below threshold)
    const calls = consoleWarnSpy.mock.calls;
    const memoryWarnings = calls.filter(call => call[0]?.toString().includes('Memory warning'));
    expect(memoryWarnings.length).toBe(0);

    // Cleanup
    unmount();
    consoleWarnSpy.mockRestore();

    if (!hadMemory) {
      delete (global.performance as ExtendedPerformance).memory;
    }
  });

  it('should limit metrics to last 100', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act - create more than 100 renders
    for (let i = 0; i < 105; i++) {
      act(() => {
        result.current.startRender();
        vi.advanceTimersByTime(1);
        result.current.endRender();
      });
    }

    // Assert
    const stats = result.current.getStats();
    expect(stats?.totalRenders).toBe(100); // Limited to 100
  });

  it('should return null stats when no renders recorded', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act
    const stats = result.current.getStats();

    // Assert
    expect(stats).toBeNull();
  });

  it('should be disabled when enabled is false', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
        enabled: false,
      })
    );

    // Act
    act(() => {
      result.current.startRender();
      result.current.endRender();
    });

    // Assert
    const stats = result.current.getStats();
    expect(stats).toBeNull(); // No metrics recorded
  });

  it('should provide recent metrics in stats', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    // Act - create 15 renders
    for (let i = 0; i < 15; i++) {
      act(() => {
        result.current.startRender();
        vi.advanceTimersByTime(1);
        result.current.endRender();
      });
    }

    // Assert
    const stats = result.current.getStats();
    expect(stats?.recentMetrics.length).toBe(10); // Last 10 metrics
  });

  it('should track minimum and maximum render times', () => {
    // Arrange
    const { result } = renderHook(() =>
      usePerformanceMonitor({
        componentName: 'TestComponent',
      })
    );

    const renderTimes = [2, 15, 5, 20, 1];

    // Act
    renderTimes.forEach(time => {
      act(() => {
        result.current.startRender();
        vi.advanceTimersByTime(time);
        result.current.endRender();
      });
    });

    // Assert
    const stats = result.current.getStats();
    expect(stats?.minRenderTime).toBeLessThanOrEqual(2);
    expect(stats?.maxRenderTime).toBeGreaterThanOrEqual(20);
  });
});
