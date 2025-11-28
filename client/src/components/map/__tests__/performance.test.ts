/**
 * Tests for performance optimization utilities.
 *
 * Verifies debouncing, throttling, and performance monitoring
 * functionality for the map editor.
 */

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { debounce, throttle, MapPerformanceMonitor } from '../utils/performance';

describe('Performance Utilities', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  describe('debounce', () => {
    it('should delay function execution', () => {
      const func = vi.fn();
      const debounced = debounce(func, 100);

      debounced();
      expect(func).not.toHaveBeenCalled();

      vi.advanceTimersByTime(100);
      expect(func).toHaveBeenCalledTimes(1);
    });

    it('should cancel previous calls when called multiple times', () => {
      const func = vi.fn();
      const debounced = debounce(func, 100);

      debounced();
      debounced();
      debounced();

      vi.advanceTimersByTime(50);
      expect(func).not.toHaveBeenCalled();

      vi.advanceTimersByTime(50);
      expect(func).toHaveBeenCalledTimes(1);
    });

    it('should pass arguments correctly', () => {
      const func = vi.fn();
      const debounced = debounce(func, 100);

      debounced('arg1', 'arg2', 123);
      vi.advanceTimersByTime(100);

      expect(func).toHaveBeenCalledWith('arg1', 'arg2', 123);
    });
  });

  describe('throttle', () => {
    it('should limit function execution rate', () => {
      const func = vi.fn();
      const throttled = throttle(func, 100);

      throttled();
      expect(func).toHaveBeenCalledTimes(1);

      throttled();
      expect(func).toHaveBeenCalledTimes(1); // Still 1, within throttle window

      vi.advanceTimersByTime(100);
      throttled();
      expect(func).toHaveBeenCalledTimes(2);
    });

    it('should schedule delayed execution if called too frequently', () => {
      const func = vi.fn();
      const throttled = throttle(func, 100);

      throttled(); // First call executes immediately
      expect(func).toHaveBeenCalledTimes(1);

      throttled(); // Second call scheduled
      expect(func).toHaveBeenCalledTimes(1);

      vi.advanceTimersByTime(100);
      expect(func).toHaveBeenCalledTimes(2);
    });
  });

  describe('MapPerformanceMonitor', () => {
    let monitor: MapPerformanceMonitor;

    beforeEach(() => {
      monitor = new MapPerformanceMonitor();
    });

    it('should track render times', () => {
      const startTime = monitor.startRender();
      // Simulate render time
      vi.advanceTimersByTime(10);
      monitor.endRender(startTime);

      const stats = monitor.getStats();
      expect(stats.averageRenderTime).toBeGreaterThan(0);
      expect(stats.sampleCount).toBe(1);
    });

    it('should calculate FPS', () => {
      // Simulate 60 frames
      for (let i = 0; i < 60; i++) {
        const startTime = monitor.startRender();
        vi.advanceTimersByTime(16); // ~60fps
        monitor.endRender(startTime);
      }

      // Advance time by 1 second to trigger FPS calculation
      vi.advanceTimersByTime(1000);

      const fps = monitor.getFps();
      expect(fps).toBeGreaterThanOrEqual(50); // Should be close to 60
    });

    it('should track min and max render times', () => {
      const times = [5, 10, 15, 20, 25];

      times.forEach(time => {
        const startTime = monitor.startRender();
        vi.advanceTimersByTime(time);
        monitor.endRender(startTime);
      });

      const stats = monitor.getStats();
      expect(stats.minRenderTime).toBeGreaterThanOrEqual(5);
      expect(stats.maxRenderTime).toBeLessThanOrEqual(25);
    });

    it('should reset metrics', () => {
      const startTime = monitor.startRender();
      vi.advanceTimersByTime(10);
      monitor.endRender(startTime);

      expect(monitor.getStats().sampleCount).toBe(1);

      monitor.reset();
      expect(monitor.getStats().sampleCount).toBe(0);
      expect(monitor.getFps()).toBe(60); // Default FPS
    });
  });
});
