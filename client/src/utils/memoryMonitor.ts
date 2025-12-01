import { useEffect } from 'react';
import { MemoryLeakDetector, MemorySnapshot } from './memoryLeakDetector';

interface MemoryReport {
  timestamp: number;
  componentName: string;
  memoryUsage: {
    current: number;
    average: number;
    peak: number;
    growthRate: number;
  };
  resourceStats: {
    timers: number;
    intervals: number;
    webSockets: number;
    customResources: number;
    total: number;
  };
  warnings: string[];
  recommendations: string[];
}

interface MemoryMonitorOptions {
  enableReporting: boolean;
  reportInterval: number; // milliseconds
  warningThreshold: number; // MB
  criticalThreshold: number; // MB
  maxReports: number;
}

/**
 * Memory monitoring service for tracking memory usage across components
 */
export class MemoryMonitor {
  private static instance: MemoryMonitor | null = null;
  private detector: MemoryLeakDetector;
  private reports: MemoryReport[] = [];
  private options: MemoryMonitorOptions;
  private reportIntervalId: number | null = null;
  private componentDetectors: Map<string, MemoryLeakDetector> = new Map();

  private constructor(options: Partial<MemoryMonitorOptions> = {}) {
    this.options = {
      enableReporting: true,
      reportInterval: 60000, // 1 minute
      warningThreshold: 50, // 50MB
      criticalThreshold: 100, // 100MB
      maxReports: 100,
      ...options,
    };

    this.detector = new MemoryLeakDetector({
      checkInterval: 10000, // 10 seconds
      warningThreshold: this.options.warningThreshold,
      criticalThreshold: this.options.criticalThreshold,
      maxSnapshots: 50,
    });

    this.detector.setCallbacks({
      onWarning: (message, snapshot) => {
        this.handleMemoryWarning(message, snapshot);
      },
      onCritical: (message, snapshot) => {
        this.handleMemoryCritical(message, snapshot);
      },
    });

    if (this.options.enableReporting) {
      this.startReporting();
    }
  }

  /**
   * Get singleton instance
   */
  static getInstance(options?: Partial<MemoryMonitorOptions>): MemoryMonitor {
    if (!MemoryMonitor.instance) {
      MemoryMonitor.instance = new MemoryMonitor(options);
    }
    return MemoryMonitor.instance;
  }

  /**
   * Start memory monitoring
   */
  start(): void {
    this.detector.start();
  }

  /**
   * Stop memory monitoring
   */
  stop(): void {
    this.detector.stop();
    if (this.reportIntervalId) {
      clearInterval(this.reportIntervalId);
      this.reportIntervalId = null;
    }
  }

  /**
   * Register a component for memory monitoring
   */
  registerComponent(componentName: string): MemoryLeakDetector {
    if (this.componentDetectors.has(componentName)) {
      return this.componentDetectors.get(componentName)!;
    }

    const componentDetector = new MemoryLeakDetector({
      checkInterval: 15000, // 15 seconds for components
      warningThreshold: this.options.warningThreshold,
      criticalThreshold: this.options.criticalThreshold,
      maxSnapshots: 20,
    });

    componentDetector.setCallbacks({
      onWarning: (message, snapshot) => {
        this.handleComponentMemoryWarning(componentName, message, snapshot);
      },
      onCritical: (message, snapshot) => {
        this.handleComponentMemoryCritical(componentName, message, snapshot);
      },
    });

    this.componentDetectors.set(componentName, componentDetector);
    return componentDetector;
  }

  /**
   * Unregister a component from memory monitoring
   */
  unregisterComponent(componentName: string): void {
    const detector = this.componentDetectors.get(componentName);
    if (detector) {
      detector.stop();
      this.componentDetectors.delete(componentName);
    }
  }

  /**
   * Get memory statistics for a specific component
   */
  getComponentStats(componentName: string): {
    current: number;
    average: number;
    peak: number;
    growthRate: number;
  } | null {
    const detector = this.componentDetectors.get(componentName);
    return detector?.getMemoryStats() || null;
  }

  /**
   * Get overall memory statistics
   */
  getOverallStats(): {
    current: number;
    average: number;
    peak: number;
    growthRate: number;
  } | null {
    return this.detector.getMemoryStats();
  }

  /**
   * Get all memory reports
   */
  getReports(): MemoryReport[] {
    return [...this.reports];
  }

  /**
   * Get recent memory reports
   */
  getRecentReports(count: number = 10): MemoryReport[] {
    return this.reports.slice(-count);
  }

  /**
   * Generate a comprehensive memory report
   */
  generateReport(componentName?: string): MemoryReport {
    const memoryStats = componentName ? this.getComponentStats(componentName) : this.getOverallStats();

    const warnings: string[] = [];
    const recommendations: string[] = [];

    if (memoryStats) {
      if (memoryStats.current > this.options.criticalThreshold) {
        warnings.push(`Critical memory usage: ${memoryStats.current.toFixed(2)}MB`);
        recommendations.push('Consider reducing memory usage or implementing garbage collection');
      } else if (memoryStats.current > this.options.warningThreshold) {
        warnings.push(`High memory usage: ${memoryStats.current.toFixed(2)}MB`);
        recommendations.push('Monitor memory usage and consider optimization');
      }

      if (memoryStats.growthRate > 0.1) {
        warnings.push(`Memory leak detected: ${(memoryStats.growthRate * 100).toFixed(2)}% growth rate`);
        recommendations.push('Investigate and fix memory leaks');
      }

      if (memoryStats.peak > memoryStats.current * 1.5) {
        warnings.push('High memory peak detected');
        recommendations.push('Consider implementing memory optimization strategies');
      }
    }

    const report: MemoryReport = {
      timestamp: Date.now(),
      componentName: componentName || 'overall',
      memoryUsage: memoryStats || { current: 0, average: 0, peak: 0, growthRate: 0 },
      resourceStats: this.getResourceStats(),
      warnings,
      recommendations,
    };

    this.addReport(report);
    return report;
  }

  /**
   * Get resource statistics from all components
   */
  private getResourceStats(): {
    timers: number;
    intervals: number;
    webSockets: number;
    customResources: number;
    total: number;
  } {
    // This would need to be integrated with the ResourceManager
    // For now, return placeholder values
    return {
      timers: 0,
      intervals: 0,
      webSockets: 0,
      customResources: 0,
      total: 0,
    };
  }

  /**
   * Start automatic reporting
   */
  private startReporting(): void {
    this.reportIntervalId = window.setInterval(() => {
      this.generateReport();
    }, this.options.reportInterval);
  }

  /**
   * Add a report to the reports array
   */
  private addReport(report: MemoryReport): void {
    this.reports.push(report);

    // Keep only recent reports
    if (this.reports.length > this.options.maxReports) {
      this.reports = this.reports.slice(-this.options.maxReports);
    }
  }

  /**
   * Handle memory warning
   */
  private handleMemoryWarning(message: string, snapshot: MemorySnapshot): void {
    console.warn(`[MemoryMonitor] ${message}`, snapshot);

    // Could send to analytics or logging service
    if (
      typeof window !== 'undefined' &&
      (window as { gtag?: (event: string, data: Record<string, unknown>) => void }).gtag
    ) {
      (window as { gtag: (event: string, data: Record<string, unknown>) => void }).gtag('event', 'memory_warning', {
        memory_usage: snapshot.usedJSHeapSize / 1024 / 1024,
        timestamp: snapshot.timestamp,
      });
    }
  }

  /**
   * Handle critical memory usage
   */
  private handleMemoryCritical(message: string, snapshot: MemorySnapshot): void {
    console.error(`[MemoryMonitor] ${message}`, snapshot);

    // Could send to analytics or logging service
    if (
      typeof window !== 'undefined' &&
      (window as { gtag?: (event: string, data: Record<string, unknown>) => void }).gtag
    ) {
      (window as { gtag: (event: string, data: Record<string, unknown>) => void }).gtag('event', 'memory_critical', {
        memory_usage: snapshot.usedJSHeapSize / 1024 / 1024,
        timestamp: snapshot.timestamp,
      });
    }
  }

  /**
   * Handle component memory warning
   */
  private handleComponentMemoryWarning(componentName: string, message: string, snapshot: MemorySnapshot): void {
    console.warn(`[MemoryMonitor:${componentName}] ${message}`, snapshot);
  }

  /**
   * Handle component memory critical
   */
  private handleComponentMemoryCritical(componentName: string, message: string, snapshot: MemorySnapshot): void {
    console.error(`[MemoryMonitor:${componentName}] ${message}`, snapshot);
  }

  /**
   * Clear all reports
   */
  clearReports(): void {
    this.reports = [];
  }

  /**
   * Export reports as JSON
   */
  exportReports(): string {
    return JSON.stringify(this.reports, null, 2);
  }

  /**
   * Get memory usage summary
   */
  getMemorySummary(): {
    overall: {
      current: number;
      average: number;
      peak: number;
      growthRate: number;
    } | null;
    components: Array<{
      name: string;
      current: number;
      average: number;
      peak: number;
      growthRate: number;
    }>;
    totalReports: number;
    recentWarnings: number;
  } {
    const overall = this.getOverallStats();
    const components = Array.from(this.componentDetectors.entries()).map(([name, detector]) => {
      const stats = detector.getMemoryStats();
      return {
        name,
        current: stats?.current || 0,
        average: stats?.average || 0,
        peak: stats?.peak || 0,
        growthRate: stats?.growthRate || 0,
      };
    });

    const recentWarnings = this.reports.slice(-10).reduce((count, report) => count + report.warnings.length, 0);

    return {
      overall,
      components,
      totalReports: this.reports.length,
      recentWarnings,
    };
  }
}

/**
 * React hook for component-level memory monitoring
 */
export const useMemoryMonitor = (componentName: string) => {
  const monitor = MemoryMonitor.getInstance();
  const detector = monitor.registerComponent(componentName);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      monitor.unregisterComponent(componentName);
    };
  }, [monitor, componentName]);

  return {
    detector,
    getStats: () => monitor.getComponentStats(componentName),
    generateReport: () => monitor.generateReport(componentName),
    unregister: () => monitor.unregisterComponent(componentName),
  };
};

/**
 * Global memory monitor instance
 */
export const memoryMonitor = MemoryMonitor.getInstance();

export type { MemoryMonitorOptions, MemoryReport };
