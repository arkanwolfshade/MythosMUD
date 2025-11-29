import { describe, expect, it, beforeEach, vi, afterEach } from 'vitest';
import { renderHook, act } from '@testing-library/react';
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
    expect(stats?.minRenderTime).toBeLessThanOrEqual(stats!.averageRenderTime);
    expect(stats?.maxRenderTime).toBeGreaterThanOrEqual(stats!.averageRenderTime);
    expect(stats?.recentMetrics.length).toBeLessThanOrEqual(10);
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
