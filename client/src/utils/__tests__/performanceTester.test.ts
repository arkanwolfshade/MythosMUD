import { describe, expect, it, beforeEach, vi } from 'vitest';
import { PerformanceTester, usePerformanceTester } from '../performanceTester';
import { renderHook, act } from '@testing-library/react';
import React from 'react';

describe('PerformanceTester', () => {
  let tester: PerformanceTester;

  beforeEach(() => {
    tester = new PerformanceTester();
    vi.clearAllMocks();
  });

  describe('runTest', () => {
    it('should run test and return results', async () => {
      // Arrange
      const testFunction = vi.fn(() => {
        // Simple synchronous function
      });

      // Act
      const result = await tester.runTest('Test Name', testFunction, {
        iterations: 5,
        warmupIterations: 2,
      });

      // Assert
      expect(result.name).toBe('Test Name');
      expect(result.iterations).toBeGreaterThan(0);
      expect(result.averageTime).toBeGreaterThanOrEqual(0);
      expect(result.minTime).toBeGreaterThanOrEqual(0);
      expect(result.maxTime).toBeGreaterThanOrEqual(0);
      expect(result.totalTime).toBeGreaterThanOrEqual(0);
      expect(result.timestamp).toBeGreaterThan(0);
      expect(testFunction).toHaveBeenCalled();
    });

    it('should handle async test functions', async () => {
      // Arrange
      const testFunction = async () => {
        await new Promise(resolve => setTimeout(resolve, 1));
      };

      // Act
      const result = await tester.runTest('Async Test', testFunction, {
        iterations: 3,
        warmupIterations: 1,
      });

      // Assert
      expect(result.iterations).toBe(3);
      expect(result.averageTime).toBeGreaterThan(0);
    });

    it('should perform warmup iterations', async () => {
      // Arrange
      const testFunction = vi.fn();

      // Act
      await tester.runTest('Warmup Test', testFunction, {
        iterations: 2,
        warmupIterations: 5,
      });

      // Assert - warmup iterations + actual iterations
      expect(testFunction).toHaveBeenCalledTimes(7); // 5 warmup + 2 actual
    });

    it('should respect timeout', async () => {
      // Arrange
      const testFunction = async () => {
        await new Promise(resolve => setTimeout(resolve, 100));
      };

      // Act
      const result = await tester.runTest('Timeout Test', testFunction, {
        iterations: 100,
        timeout: 100, // Very short timeout
      });

      // Assert - should stop early due to timeout
      expect(result.iterations).toBeLessThan(100);
    });

    it('should handle errors in test function gracefully', async () => {
      // Arrange
      const testFunction = vi.fn(() => {
        throw new Error('Test error');
      });
      const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

      // Act
      const result = await tester.runTest('Error Test', testFunction, {
        iterations: 5,
        warmupIterations: 0,
      });

      // Assert
      expect(result.iterations).toBeLessThanOrEqual(5);
      expect(result.iterations).toBeGreaterThanOrEqual(0);
      consoleWarnSpy.mockRestore();
    });

    it('should include memory usage when available', async () => {
      // Arrange
      const testFunction = vi.fn();

      // Act
      const result = await tester.runTest('Memory Test', testFunction, {
        iterations: 1,
        warmupIterations: 0,
      });

      // Assert
      expect(result).toHaveProperty('memoryUsage');
      // memoryUsage may be undefined if not available in test environment
    });
  });

  describe('runComponentRenderTest', () => {
    it('should run component render test', async () => {
      // Arrange
      const renderFunction = () => React.createElement('div', null, 'Test Component');

      // Act
      const result = await tester.runComponentRenderTest('Component Test', renderFunction, {
        iterations: 3,
        warmupIterations: 1,
      });

      // Assert
      expect(result.name).toContain('Component Test');
      expect(result.name).toContain('Render Test');
      expect(result.iterations).toBeGreaterThan(0);
    });
  });

  describe('runMemoryTest', () => {
    it('should run memory test and calculate delta', async () => {
      // Arrange
      const testFunction = vi.fn(() => {
        // Create some objects to use memory
        const arr = new Array(100).fill(0);
        return arr;
      });

      // Act
      const result = await tester.runMemoryTest('Memory Delta Test', testFunction, {
        iterations: 2,
        warmupIterations: 0,
      });

      // Assert
      expect(result.name).toContain('Memory Test');
      expect(result).toHaveProperty('memoryUsage');
    });
  });

  describe('Results Management', () => {
    beforeEach(async () => {
      // Add some test results
      await tester.runTest('Test 1', vi.fn(), { iterations: 1, warmupIterations: 0 });
      await tester.runTest('Test 2', vi.fn(), { iterations: 1, warmupIterations: 0 });
    });

    it('should get all results', () => {
      // Act
      const results = tester.getResults();

      // Assert
      expect(results.length).toBe(2);
      expect(results[0].name).toBe('Test 1');
      expect(results[1].name).toBe('Test 2');
    });

    it('should get results by name', () => {
      // Act
      const results = tester.getResultsByName('Test 1');

      // Assert
      expect(results.length).toBe(1);
      expect(results[0].name).toBe('Test 1');
    });

    it('should get average results', () => {
      // Act
      const averages = tester.getAverageResults();

      // Assert
      expect(averages.totalTests).toBe(2);
      expect(averages.averageTime).toBeGreaterThanOrEqual(0);
      expect(averages.totalTime).toBeGreaterThanOrEqual(0);
    });

    it('should return zero averages for empty results', () => {
      // Arrange
      const emptyTester = new PerformanceTester();

      // Act
      const averages = emptyTester.getAverageResults();

      // Assert
      expect(averages.totalTests).toBe(0);
      expect(averages.averageTime).toBe(0);
      expect(averages.totalTime).toBe(0);
    });
  });

  describe('Report Generation', () => {
    beforeEach(async () => {
      await tester.runTest('Test 1', vi.fn(), { iterations: 2, warmupIterations: 0 });
      await tester.runTest('Test 2', vi.fn(), { iterations: 2, warmupIterations: 0 });
    });

    it('should generate report string', () => {
      // Act
      const report = tester.generateReport();

      // Assert
      expect(report).toContain('Performance Test Report');
      expect(report).toContain('Total Tests: 2');
      expect(report).toContain('Test 1');
      expect(report).toContain('Test 2');
      expect(report).toContain('Average:');
      expect(report).toContain('Min:');
      expect(report).toContain('Max:');
    });

    it('should include timestamp in report', () => {
      // Act
      const report = tester.generateReport();

      // Assert
      expect(report).toContain('Generated:');
    });
  });

  describe('Export Results', () => {
    it('should export results as JSON', async () => {
      // Arrange
      await tester.runTest('Export Test', vi.fn(), { iterations: 1, warmupIterations: 0 });

      // Act
      const exported = tester.exportResults();
      const parsed = JSON.parse(exported);

      // Assert
      expect(Array.isArray(parsed)).toBe(true);
      expect(parsed.length).toBe(1);
      expect(parsed[0].name).toBe('Export Test');
    });
  });

  describe('Clear Results', () => {
    it('should clear all results', async () => {
      // Arrange
      await tester.runTest('Test 1', vi.fn(), { iterations: 1, warmupIterations: 0 });
      expect(tester.getResults().length).toBe(1);

      // Act
      tester.clearResults();

      // Assert
      expect(tester.getResults().length).toBe(0);
    });
  });
});

describe('usePerformanceTester Hook', () => {
  it('should initialize tester', () => {
    // Act
    const { result } = renderHook(() => usePerformanceTester());

    // Assert
    expect(result.current.runTest).toBeDefined();
    expect(result.current.runComponentTest).toBeDefined();
    expect(result.current.runMemoryTest).toBeDefined();
    expect(result.current.getResults).toBeDefined();
    expect(result.current.generateReport).toBeDefined();
  });

  it('should run test through hook', async () => {
    // Arrange
    const { result } = renderHook(() => usePerformanceTester());

    // Act
    let testResult;
    await act(async () => {
      testResult = await result.current.runTest('Hook Test', vi.fn(), {
        iterations: 1,
        warmupIterations: 0,
      });
    });

    // Assert
    expect(testResult).toBeDefined();
    expect(testResult?.name).toBe('Hook Test');
  });

  it('should get results through hook', async () => {
    // Arrange
    const { result } = renderHook(() => usePerformanceTester());

    await act(async () => {
      await result.current.runTest('Test 1', vi.fn(), {
        iterations: 1,
        warmupIterations: 0,
      });
    });

    // Act
    const results = result.current.getResults();

    // Assert
    expect(results.length).toBe(1);
    expect(results[0].name).toBe('Test 1');
  });

  it('should generate report through hook', async () => {
    // Arrange
    const { result } = renderHook(() => usePerformanceTester());

    await act(async () => {
      await result.current.runTest('Report Test', vi.fn(), {
        iterations: 1,
        warmupIterations: 0,
      });
    });

    // Act
    const report = result.current.generateReport();

    // Assert
    expect(report).toContain('Performance Test Report');
    expect(report).toContain('Report Test');
  });

  it('should maintain same tester instance across re-renders', async () => {
    // Arrange
    const { result, rerender } = renderHook(() => usePerformanceTester());

    await act(async () => {
      await result.current.runTest('Test 1', vi.fn(), {
        iterations: 1,
        warmupIterations: 0,
      });
    });

    const initialResults = result.current.getResults();

    // Act
    rerender();

    // Assert - should still have the same results
    expect(result.current.getResults().length).toBe(initialResults.length);
  });
});
