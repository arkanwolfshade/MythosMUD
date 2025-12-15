import { useCallback, useEffect, useRef } from 'react';

interface PerformanceMetrics {
  renderTime: number;
  memoryUsage?: number;
  componentName: string;
  timestamp: number;
}

interface UsePerformanceMonitorOptions {
  componentName: string;
  enabled?: boolean;
  onMetrics?: (metrics: PerformanceMetrics) => void;
  threshold?: number; // Warning threshold in milliseconds
}

interface PerformanceMemory {
  usedJSHeapSize: number;
  totalJSHeapSize: number;
  jsHeapSizeLimit: number;
}

interface ExtendedPerformance extends Performance {
  memory?: PerformanceMemory;
}

export const usePerformanceMonitor = (options: UsePerformanceMonitorOptions) => {
  const { componentName, enabled = true, onMetrics, threshold = 16 } = options;
  const renderStartTime = useRef<number>(0);
  const metricsRef = useRef<PerformanceMetrics[]>([]);

  // Start measuring render time
  const startRender = useCallback(() => {
    if (!enabled) return;
    renderStartTime.current = performance.now();
  }, [enabled]);

  // End measuring render time
  const endRender = useCallback(() => {
    if (!enabled) return;

    const renderTime = performance.now() - renderStartTime.current;
    const timestamp = Date.now();

    // Get memory usage if available
    let memoryUsage: number | undefined;
    if ('memory' in performance) {
      memoryUsage = (performance as ExtendedPerformance).memory?.usedJSHeapSize;
    }

    const metrics: PerformanceMetrics = {
      renderTime,
      memoryUsage,
      componentName,
      timestamp,
    };

    metricsRef.current.push(metrics);

    // Keep only last 100 metrics
    if (metricsRef.current.length > 100) {
      metricsRef.current = metricsRef.current.slice(-100);
    }

    // Check if render time exceeds threshold
    if (renderTime > threshold) {
      console.warn(
        `Performance warning: ${componentName} took ${renderTime.toFixed(2)}ms to render (threshold: ${threshold}ms)`
      );
    }

    // Call callback if provided
    onMetrics?.(metrics);
  }, [enabled, componentName, threshold, onMetrics]);

  // Get performance statistics
  const getStats = useCallback(() => {
    const metrics = metricsRef.current;
    if (metrics.length === 0) return null;

    const renderTimes = metrics.map(m => m.renderTime);
    const avgRenderTime = renderTimes.reduce((a, b) => a + b, 0) / renderTimes.length;
    const maxRenderTime = Math.max(...renderTimes);
    const minRenderTime = Math.min(...renderTimes);

    return {
      totalRenders: metrics.length,
      averageRenderTime: avgRenderTime,
      maxRenderTime,
      minRenderTime,
      recentMetrics: metrics.slice(-10),
    };
  }, []);

  // Monitor memory usage
  useEffect(() => {
    if (!enabled) return;

    const interval = setInterval(() => {
      if ('memory' in performance) {
        const memory = (performance as ExtendedPerformance).memory;
        if (memory) {
          const usedMB = memory.usedJSHeapSize / 1024 / 1024;
          const totalMB = memory.totalJSHeapSize / 1024 / 1024;

          if (usedMB > 100) {
            // Warning at 100MB
            console.warn(
              `Memory warning: ${componentName} using ${usedMB.toFixed(2)}MB of ${totalMB.toFixed(2)}MB total`
            );
          }
        }
      }
    }, 5000); // Check every 5 seconds

    return () => {
      clearInterval(interval);
    };
  }, [enabled, componentName]);

  // Don't return metrics directly - they should be accessed via getStats()
  // Returning ref values directly during render violates React's rules
  return {
    startRender,
    endRender,
    getStats,
  };
};
