/**
 * Performance utilities for map rendering.
 *
 * Provides debouncing, throttling, and performance monitoring
 * for the map editor to maintain 60fps targets.
 *
 * As documented in the Pnakotic Manuscripts, proper optimization
 * of dimensional visualization is essential for maintaining
 * the integrity of our eldritch architecture.
 */

/**
 * Debounce a function call.
 *
 * @param func - Function to debounce
 * @param delay - Delay in milliseconds
 * @returns Debounced function
 */

// Generic function type requires any[] for args to accept functions with any parameter types
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function debounce<T extends (...args: any[]) => any>(func: T, delay: number): (...args: Parameters<T>) => void {
  let timeoutId: ReturnType<typeof setTimeout> | null = null;

  return function debounced(...args: Parameters<T>) {
    if (timeoutId !== null) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      func(...args);
      timeoutId = null;
    }, delay);
  };
}

/**
 * Throttle a function call.
 *
 * @param func - Function to throttle
 * @param delay - Delay in milliseconds
 * @returns Throttled function
 */

// Generic function type requires any[] for args to accept functions with any parameter types
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function throttle<T extends (...args: any[]) => any>(func: T, delay: number): (...args: Parameters<T>) => void {
  let lastCall = 0;
  let timeoutId: ReturnType<typeof setTimeout> | null = null;

  return function throttled(...args: Parameters<T>) {
    const now = Date.now();
    const timeSinceLastCall = now - lastCall;

    if (timeSinceLastCall >= delay) {
      lastCall = now;
      func(...args);
    } else {
      if (timeoutId === null) {
        timeoutId = setTimeout(() => {
          lastCall = Date.now();
          func(...args);
          timeoutId = null;
        }, delay - timeSinceLastCall);
      }
    }
  };
}

/**
 * Check if an element is in the viewport.
 *
 * @param element - Element to check
 * @param margin - Margin in pixels (default: 100)
 * @returns True if element is in viewport
 */
export function isInViewport(element: HTMLElement, margin: number = 100): boolean {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= -margin &&
    rect.left >= -margin &&
    rect.bottom <= window.innerHeight + margin &&
    rect.right <= window.innerWidth + margin
  );
}

/**
 * Performance monitor for map rendering.
 */
export class MapPerformanceMonitor {
  private frameCount = 0;
  private lastFpsTime = 0;
  private fps = 60;
  private renderTimes: number[] = [];
  private readonly maxSamples = 100;

  /**
   * Start measuring render time.
   */
  startRender(): number {
    return performance.now();
  }

  /**
   * End measuring render time and record metrics.
   *
   * @param startTime - Start time from startRender()
   */
  endRender(startTime: number): void {
    const renderTime = performance.now() - startTime;
    this.renderTimes.push(renderTime);

    // Keep only last N samples
    if (this.renderTimes.length > this.maxSamples) {
      this.renderTimes.shift();
    }

    // Calculate FPS
    this.frameCount++;
    const now = performance.now();
    if (now - this.lastFpsTime >= 1000) {
      this.fps = this.frameCount;
      this.frameCount = 0;
      this.lastFpsTime = now;
    }
  }

  /**
   * Get current FPS.
   */
  getFps(): number {
    return this.fps;
  }

  /**
   * Get average render time.
   */
  getAverageRenderTime(): number {
    if (this.renderTimes.length === 0) {
      return 0;
    }
    return this.renderTimes.reduce((a, b) => a + b, 0) / this.renderTimes.length;
  }

  /**
   * Get performance statistics.
   */
  getStats(): {
    fps: number;
    averageRenderTime: number;
    maxRenderTime: number;
    minRenderTime: number;
    sampleCount: number;
  } {
    return {
      fps: this.fps,
      averageRenderTime: this.getAverageRenderTime(),
      maxRenderTime: this.renderTimes.length > 0 ? Math.max(...this.renderTimes) : 0,
      minRenderTime: this.renderTimes.length > 0 ? Math.min(...this.renderTimes) : 0,
      sampleCount: this.renderTimes.length,
    };
  }

  /**
   * Reset all metrics.
   */
  reset(): void {
    this.frameCount = 0;
    this.lastFpsTime = 0;
    this.fps = 60;
    this.renderTimes = [];
  }
}

/**
 * Global performance monitor instance.
 */
export const mapPerformanceMonitor = new MapPerformanceMonitor();
