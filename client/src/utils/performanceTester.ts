import { useCallback, useRef } from 'react';

interface PerformanceTestConfig {
  iterations: number;
  warmupIterations: number;
  timeout: number; // milliseconds
}

interface PerformanceTestResult {
  name: string;
  averageTime: number;
  minTime: number;
  maxTime: number;
  totalTime: number;
  iterations: number;
  memoryUsage?: number;
  timestamp: number;
}

interface PerformanceMemory {
  usedJSHeapSize: number;
  totalJSHeapSize: number;
  jsHeapSizeLimit: number;
}

interface ExtendedPerformance extends Performance {
  memory?: PerformanceMemory;
}

export class PerformanceTester {
  private results: PerformanceTestResult[] = [];

  async runTest(
    name: string,
    testFunction: () => void | Promise<void>,
    config?: Partial<PerformanceTestConfig>
  ): Promise<PerformanceTestResult> {
    const testConfig: PerformanceTestConfig = {
      iterations: 100,
      warmupIterations: 10,
      timeout: 30000, // 30 seconds
      ...config,
    };

    const times: number[] = [];
    const startTime = Date.now();

    // Warmup phase
    for (let i = 0; i < testConfig.warmupIterations; i++) {
      try {
        await testFunction();
        // Don't record warmup times
      } catch (error) {
        // nosemgrep: javascript.lang.security.audit.unsafe-formatstring.unsafe-formatstring
        // This is internal test logging with controlled iteration number, not user input
        console.warn(`Warmup iteration ${i} failed:`, error);
      }
    }

    // Actual test phase
    for (let i = 0; i < testConfig.iterations; i++) {
      // Check timeout
      if (Date.now() - startTime > testConfig.timeout) {
        console.warn(`Test "${name}" timed out after ${testConfig.timeout}ms`);
        break;
      }

      try {
        const testStart = performance.now();
        await testFunction();
        const testEnd = performance.now();
        times.push(testEnd - testStart);
      } catch (error) {
        console.warn(`Test iteration ${i} failed:`, error);
      }
    }

    // Calculate statistics
    const totalTime = times.reduce((sum, time) => sum + time, 0);
    const averageTime = totalTime / times.length;
    const minTime = Math.min(...times);
    const maxTime = Math.max(...times);

    // Get memory usage if available
    let memoryUsage: number | undefined;
    if ('memory' in performance) {
      memoryUsage = (performance as ExtendedPerformance).memory?.usedJSHeapSize;
    }

    const result: PerformanceTestResult = {
      name,
      averageTime,
      minTime,
      maxTime,
      totalTime,
      iterations: times.length,
      memoryUsage,
      timestamp: Date.now(),
    };

    this.results.push(result);
    return result;
  }

  async runComponentRenderTest(
    name: string,
    renderFunction: () => React.ReactElement,
    config?: Partial<PerformanceTestConfig>
  ): Promise<PerformanceTestResult> {
    return this.runTest(
      `${name} - Render Test`,
      () => {
        // This would need to be integrated with React testing utilities
        // For now, we'll just measure the function execution time
        renderFunction();
      },
      config
    );
  }

  async runMemoryTest(
    name: string,
    testFunction: () => void | Promise<void>,
    config?: Partial<PerformanceTestConfig>
  ): Promise<PerformanceTestResult> {
    const initialMemory =
      'memory' in performance ? (performance as ExtendedPerformance).memory?.usedJSHeapSize || 0 : 0;

    const result = await this.runTest(`${name} - Memory Test`, testFunction, config);

    const finalMemory = 'memory' in performance ? (performance as ExtendedPerformance).memory?.usedJSHeapSize || 0 : 0;
    const memoryDelta = finalMemory - initialMemory;

    return {
      ...result,
      name: `${name} - Memory Test`,
      memoryUsage: memoryDelta,
    };
  }

  getResults(): PerformanceTestResult[] {
    return [...this.results];
  }

  getResultsByName(name: string): PerformanceTestResult[] {
    return this.results.filter(result => result.name.includes(name));
  }

  getAverageResults(): {
    averageTime: number;
    totalTests: number;
    totalTime: number;
  } {
    if (this.results.length === 0) {
      return { averageTime: 0, totalTests: 0, totalTime: 0 };
    }

    const totalTime = this.results.reduce((sum, result) => sum + result.totalTime, 0);
    const averageTime = this.results.reduce((sum, result) => sum + result.averageTime, 0) / this.results.length;

    return {
      averageTime,
      totalTests: this.results.length,
      totalTime,
    };
  }

  generateReport(): string {
    const results = this.getResults();
    const averages = this.getAverageResults();

    let report = `Performance Test Report\n`;
    report += `Generated: ${new Date().toISOString()}\n`;
    report += `Total Tests: ${averages.totalTests}\n`;
    report += `Total Time: ${averages.totalTime.toFixed(2)}ms\n`;
    report += `Average Time: ${averages.averageTime.toFixed(2)}ms\n\n`;

    report += `Individual Test Results:\n`;
    report += `=====================\n\n`;

    results.forEach((result, index) => {
      report += `${index + 1}. ${result.name}\n`;
      report += `   Average: ${result.averageTime.toFixed(2)}ms\n`;
      report += `   Min: ${result.minTime.toFixed(2)}ms\n`;
      report += `   Max: ${result.maxTime.toFixed(2)}ms\n`;
      report += `   Total: ${result.totalTime.toFixed(2)}ms\n`;
      report += `   Iterations: ${result.iterations}\n`;
      if (result.memoryUsage !== undefined) {
        report += `   Memory: ${(result.memoryUsage / 1024 / 1024).toFixed(2)}MB\n`;
      }
      report += `   Timestamp: ${new Date(result.timestamp).toISOString()}\n\n`;
    });

    return report;
  }

  clearResults(): void {
    this.results = [];
  }

  exportResults(): string {
    return JSON.stringify(this.results, null, 2);
  }
}

// Hook for using performance tester in React components
export const usePerformanceTester = () => {
  const testerRef = useRef<PerformanceTester | null>(null);

  // Initialize ref only once using recommended pattern
  if (testerRef.current == null) {
    testerRef.current = new PerformanceTester();
  }

  const runTest = useCallback(
    async (name: string, testFunction: () => void | Promise<void>, config?: Partial<PerformanceTestConfig>) => {
      return testerRef.current?.runTest(name, testFunction, config);
    },
    []
  );

  const runComponentTest = useCallback(
    async (name: string, renderFunction: () => React.ReactElement, config?: Partial<PerformanceTestConfig>) => {
      return testerRef.current?.runComponentRenderTest(name, renderFunction, config);
    },
    []
  );

  const runMemoryTest = useCallback(
    async (name: string, testFunction: () => void | Promise<void>, config?: Partial<PerformanceTestConfig>) => {
      return testerRef.current?.runMemoryTest(name, testFunction, config);
    },
    []
  );

  const getResults = useCallback(() => {
    return testerRef.current?.getResults();
  }, []);

  const generateReport = useCallback(() => {
    return testerRef.current?.generateReport();
  }, []);

  return {
    runTest,
    runComponentTest,
    runMemoryTest,
    getResults,
    generateReport,
  };
};

export type { PerformanceTestConfig, PerformanceTestResult };
