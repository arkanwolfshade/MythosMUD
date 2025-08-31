import { useCallback, useEffect, useRef } from 'react';

interface MemorySnapshot {
  timestamp: number;
  usedJSHeapSize: number;
  totalJSHeapSize: number;
  jsHeapSizeLimit: number;
  componentName?: string;
}

interface MemoryLeakDetectorOptions {
  warningThreshold: number; // MB
  criticalThreshold: number; // MB
  checkInterval: number; // milliseconds
  maxSnapshots: number;
}

interface PerformanceMemory {
  usedJSHeapSize: number;
  totalJSHeapSize: number;
  jsHeapSizeLimit: number;
}

interface ExtendedPerformance extends Performance {
  memory?: PerformanceMemory;
}

export class MemoryLeakDetector {
  private snapshots: MemorySnapshot[] = [];
  private intervalId: number | null = null;
  private options: MemoryLeakDetectorOptions;
  private onWarning?: (message: string, snapshot: MemorySnapshot) => void;
  private onCritical?: (message: string, snapshot: MemorySnapshot) => void;

  constructor(options: Partial<MemoryLeakDetectorOptions> = {}) {
    this.options = {
      checkInterval: 5000, // 5 seconds
      warningThreshold: 50, // 50MB
      criticalThreshold: 100, // 100MB
      maxSnapshots: 100,
      ...options,
    };
  }

  start(): void {
    if (this.intervalId) {
      return; // Already running
    }

    this.intervalId = window.setInterval(() => {
      this.checkMemory();
    }, this.options.checkInterval);

    // Take initial snapshot
    this.checkMemory();
  }

  stop(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  setCallbacks(callbacks: {
    onWarning?: (message: string, snapshot: MemorySnapshot) => void;
    onCritical?: (message: string, snapshot: MemorySnapshot) => void;
  }): void {
    this.onWarning = callbacks.onWarning;
    this.onCritical = callbacks.onCritical;
  }

  private checkMemory(): void {
    if (!('memory' in performance)) {
      return;
    }

    const memory = (performance as ExtendedPerformance).memory;
    if (!memory) return;

    const snapshot: MemorySnapshot = {
      timestamp: Date.now(),
      usedJSHeapSize: memory.usedJSHeapSize,
      totalJSHeapSize: memory.totalJSHeapSize,
      jsHeapSizeLimit: memory.jsHeapSizeLimit,
    };

    this.snapshots.push(snapshot);

    // Keep only recent snapshots
    if (this.snapshots.length > this.options.maxSnapshots) {
      this.snapshots = this.snapshots.slice(-this.options.maxSnapshots);
    }

    const usedMB = snapshot.usedJSHeapSize / 1024 / 1024;
    const totalMB = snapshot.totalJSHeapSize / 1024 / 1024;

    // Check for critical memory usage
    if (usedMB > this.options.criticalThreshold) {
      const message = `CRITICAL: Memory usage is ${usedMB.toFixed(2)}MB (${totalMB.toFixed(2)}MB total)`;
      console.error(message, snapshot);
      this.onCritical?.(message, snapshot);
    }
    // Check for warning memory usage
    else if (usedMB > this.options.warningThreshold) {
      const message = `WARNING: Memory usage is ${usedMB.toFixed(2)}MB (${totalMB.toFixed(2)}MB total)`;
      console.warn(message, snapshot);
      this.onWarning?.(message, snapshot);
    }

    // Check for memory leaks (consistent growth over time)
    this.detectMemoryLeak();
  }

  private detectMemoryLeak(): void {
    if (this.snapshots.length < 10) {
      return; // Need at least 10 snapshots to detect trends
    }

    const recentSnapshots = this.snapshots.slice(-10);
    const growthRate = this.calculateGrowthRate(recentSnapshots);

    if (growthRate > 0.1) {
      // 10% growth per check interval
      const message = `POTENTIAL MEMORY LEAK: Memory growing at ${(growthRate * 100).toFixed(2)}% per interval`;
      console.warn(message, recentSnapshots);
      this.onWarning?.(message, recentSnapshots[recentSnapshots.length - 1]);
    }
  }

  private calculateGrowthRate(snapshots: MemorySnapshot[]): number {
    if (snapshots.length < 2) return 0;

    const first = snapshots[0];
    const last = snapshots[snapshots.length - 1];
    const timeDiff = last.timestamp - first.timestamp;
    const memoryDiff = last.usedJSHeapSize - first.usedJSHeapSize;

    if (timeDiff === 0 || first.usedJSHeapSize === 0) return 0;

    return memoryDiff / first.usedJSHeapSize / (timeDiff / this.options.checkInterval);
  }

  getSnapshots(): MemorySnapshot[] {
    return [...this.snapshots];
  }

  getCurrentMemory(): MemorySnapshot | null {
    if (!('memory' in performance)) {
      return null;
    }

    const memory = (performance as ExtendedPerformance).memory;
    if (!memory) return null;

    return {
      timestamp: Date.now(),
      usedJSHeapSize: memory.usedJSHeapSize,
      totalJSHeapSize: memory.totalJSHeapSize,
      jsHeapSizeLimit: memory.jsHeapSizeLimit,
    };
  }

  getMemoryStats(): {
    current: number;
    average: number;
    peak: number;
    growthRate: number;
  } | null {
    if (this.snapshots.length === 0) return null;

    const current = this.snapshots[this.snapshots.length - 1].usedJSHeapSize / 1024 / 1024;
    const average = this.snapshots.reduce((sum, s) => sum + s.usedJSHeapSize, 0) / this.snapshots.length / 1024 / 1024;
    const peak = Math.max(...this.snapshots.map(s => s.usedJSHeapSize)) / 1024 / 1024;
    const growthRate = this.calculateGrowthRate(this.snapshots.slice(-10));

    return {
      current,
      average,
      peak,
      growthRate,
    };
  }

  clear(): void {
    this.snapshots = [];
  }
}

// Hook for using memory leak detector in React components
export const useMemoryLeakDetector = (componentName: string, options?: Partial<MemoryLeakDetectorOptions>) => {
  const detectorRef = useRef<MemoryLeakDetector | null>(null);

  useEffect(() => {
    if (!detectorRef.current) {
      detectorRef.current = new MemoryLeakDetector(options);
      detectorRef.current.setCallbacks({
        onWarning: (message, snapshot) => {
          console.warn(`[${componentName}] ${message}`, snapshot);
        },
        onCritical: (message, snapshot) => {
          console.error(`[${componentName}] ${message}`, snapshot);
        },
      });
    }

    detectorRef.current.start();

    return () => {
      detectorRef.current?.stop();
    };
  }, [componentName, options]);

  const getStats = useCallback(() => {
    return detectorRef.current?.getMemoryStats() || null;
  }, []);

  const getSnapshots = useCallback(() => {
    return detectorRef.current?.getSnapshots() || [];
  }, []);

  return {
    getStats,
    getSnapshots,
  };
};

export { MemoryLeakDetector };
export type { MemoryLeakDetectorOptions, MemorySnapshot };
