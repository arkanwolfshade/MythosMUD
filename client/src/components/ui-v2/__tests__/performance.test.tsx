/// <reference lib="es2015" />
import { cleanup, render } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { PerformanceTester, type PerformanceTestResult } from '../../../utils/performanceTester';
import { ChatHistoryPanel } from '../panels/ChatHistoryPanel';
import { CommandHistoryPanel } from '../panels/CommandHistoryPanel';
import { CommandInputPanel } from '../panels/CommandInputPanel';
import type { ChatMessage } from '../types';

// Ported from the legacy client/src/components/__tests__/performance.test.tsx (removed in #691,
// ui-v2 retirement cluster 2) against ui-v2's ChatHistoryPanel / CommandHistoryPanel /
// CommandInputPanel. Kept: benchmarks with a genuine ui-v2 analogue (large-list render, rapid
// updates, channel filtering, memory, all-panels-together render, benchmark thresholds). Dropped,
// no ui-v2 analogue: command-suggestion filtering (CommandInputPanel has no suggestion list),
// keyboard history navigation (CommandHistoryPanel is click-to-select, not arrow-key), message
// grouping (ui-v2 has no date-grouped log view -- game-log flows into ChatHistoryPanel as a
// channel, already covered by the channel-filtering benchmark below).
describe('Performance Tests', () => {
  let performanceTester: PerformanceTester;

  beforeEach(() => {
    performanceTester = new PerformanceTester();
  });

  describe('ChatHistoryPanel Performance', () => {
    const mockMessages: ChatMessage[] = Array.from({ length: 100 }, (_, i) => ({
      text: `Message ${i}`,
      timestamp: new Date(Date.now() - i * 60000).toISOString(),
      isHtml: false,
      messageType: 'chat',
      channel: 'local',
      aliasChain: [{ original: `Player${i}`, expanded: `Player${i}`, alias_name: `p${i}` }],
    }));

    const defaultProps = {
      messages: mockMessages,
      onSendChatMessage: vi.fn(),
      onClearMessages: vi.fn(),
      onDownloadLogs: vi.fn(),
      disabled: false,
      isConnected: true,
    };

    it('renders large message lists efficiently', async () => {
      const result = await performanceTester.runTest(
        'ChatHistoryPanel - Large Message List Render',
        () => {
          // RTL appends a new root each render; without cleanup, N iterations stack N trees and
          // inflate timings (looks like a regression or flakiness). Reset DOM before each sample.
          cleanup();
          render(<ChatHistoryPanel {...defaultProps} />);
        },
        { iterations: 20, warmupIterations: 3 }
      );

      // Threshold relaxed for CI/local load: jsdom DOMPurify + SafeHtml per message (~500-650ms).
      expect(result.averageTime).toBeLessThan(700);
      expect(result.iterations).toBeGreaterThan(0);
    }, 15000);

    it('handles rapid state updates efficiently', async () => {
      const { rerender } = render(<ChatHistoryPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'ChatHistoryPanel - Rapid State Updates',
        () => {
          const newMessages: ChatMessage[] = [
            ...mockMessages,
            {
              text: 'New message',
              timestamp: new Date().toISOString(),
              isHtml: false,
              messageType: 'chat',
              channel: 'local',
            },
          ];
          rerender(<ChatHistoryPanel {...defaultProps} messages={newMessages} />);
        },
        { iterations: 20, warmupIterations: 3 }
      );

      // Threshold relaxed for CI/slower machines; 250ms for rapid updates
      expect(result.averageTime).toBeLessThan(250);
    }, 15000);

    it('filters messages by channel efficiently', async () => {
      render(<ChatHistoryPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'ChatHistoryPanel - Channel Filtering',
        () => {
          const filteredMessages = mockMessages.filter(message => message.channel === 'local');
          expect(filteredMessages.length).toBeGreaterThan(0);
        },
        { iterations: 1000, warmupIterations: 100 }
      );

      expect(result.averageTime).toBeLessThan(1); // Should filter in under 1ms
    });
  });

  describe('CommandHistoryPanel Performance', () => {
    const mockCommandHistory = Array.from({ length: 1000 }, (_, i) => `command${i}`);

    it('renders large command history efficiently', async () => {
      const result = await performanceTester.runTest(
        'CommandHistoryPanel - Large Command History Render',
        () => {
          cleanup();
          render(<CommandHistoryPanel commandHistory={mockCommandHistory} onClearHistory={vi.fn()} />);
        },
        { iterations: 100, warmupIterations: 10 }
      );

      expect(result.averageTime).toBeLessThan(50); // Should render in under 50ms
      expect(result.iterations).toBeGreaterThan(0);
    });
  });

  describe('CommandInputPanel Performance', () => {
    it('renders efficiently', async () => {
      const result = await performanceTester.runTest(
        'CommandInputPanel - Render',
        () => {
          cleanup();
          render(<CommandInputPanel onSendCommand={vi.fn()} disabled={false} isConnected={true} />);
        },
        { iterations: 100, warmupIterations: 10 }
      );

      expect(result.averageTime).toBeLessThan(50); // Should render in under 50ms
      expect(result.iterations).toBeGreaterThan(0);
    });
  });

  describe('Memory Usage Tests', () => {
    it('ChatHistoryPanel memory usage stays within limits', async () => {
      // Use 500 messages, 2 iterations to avoid OOM in CI workers
      const largeMessages: ChatMessage[] = Array.from({ length: 500 }, (_, i) => ({
        text: `Large message ${i} with lots of content to test memory usage`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: 'chat',
        channel: 'local',
        aliasChain: [{ original: `Player${i}`, expanded: `Player${i}`, alias_name: `p${i}` }],
      }));

      const result = await performanceTester.runMemoryTest(
        'ChatHistoryPanel - Memory Usage',
        () => {
          cleanup();
          render(
            <ChatHistoryPanel
              messages={largeMessages}
              onSendChatMessage={vi.fn()}
              onClearMessages={vi.fn()}
              onDownloadLogs={vi.fn()}
              disabled={false}
              isConnected={true}
            />
          );
        },
        { iterations: 2, warmupIterations: 0 }
      );

      // Memory usage should be reasonable (less than 50MB)
      if (result.memoryUsage !== undefined) {
        const memoryMB = result.memoryUsage / 1024 / 1024;
        expect(memoryMB).toBeLessThan(50);
      }
    }, 15000);
  });

  describe('Integration Performance', () => {
    it('all panels render together efficiently', async () => {
      const mockMessages: ChatMessage[] = Array.from({ length: 100 }, (_, i) => ({
        text: `Message ${i}`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: 'chat',
        channel: 'local',
      }));

      const mockCommandHistory = Array.from({ length: 100 }, (_, i) => `command${i}`);

      const result = await performanceTester.runTest(
        'Integration - All Panels Render',
        () => {
          cleanup();
          // Render all three panels
          render(
            <ChatHistoryPanel
              messages={mockMessages}
              onSendChatMessage={vi.fn()}
              onClearMessages={vi.fn()}
              onDownloadLogs={vi.fn()}
              disabled={false}
              isConnected={true}
            />
          );

          render(<CommandHistoryPanel commandHistory={mockCommandHistory} onClearHistory={vi.fn()} />);

          render(<CommandInputPanel onSendCommand={vi.fn()} disabled={false} isConnected={true} />);
        },
        { iterations: 10, warmupIterations: 2 }
      );

      // Threshold relaxed for CI: jsdom + DOMPurify 3.4.12 clone-guard + multi-panel render.
      expect(result.averageTime).toBeLessThan(800);
    }, 15000);
  });

  describe('Performance Benchmarks', () => {
    it('meets performance benchmarks', async () => {
      // Run a minimal test to populate results; each it() gets fresh PerformanceTester from beforeEach
      await performanceTester.runTest(
        'Benchmark - Quick Render',
        () => {
          cleanup();
          render(<CommandHistoryPanel commandHistory={[]} />);
        },
        { iterations: 5, warmupIterations: 1 }
      );

      const results = performanceTester.getResults();
      const averages = performanceTester.getAverageResults();

      expect(averages.totalTests).toBeGreaterThan(0);
      expect(averages.averageTime).toBeLessThan(500); // Reasonable threshold for single run

      results.forEach((result: PerformanceTestResult) => {
        if (result.name.includes('Render')) {
          expect(result.averageTime).toBeLessThan(500);
        }
        if (result.name.includes('Filter')) {
          expect(result.averageTime).toBeLessThan(10);
        }
        if (result.name.includes('Memory') && result.memoryUsage !== undefined) {
          const memoryMB = result.memoryUsage / 1024 / 1024;
          expect(memoryMB).toBeLessThan(100);
        }
      });
    });

    it('generates performance report', () => {
      const report = performanceTester.generateReport();
      expect(report).toContain('Performance Test Report');
      expect(report).toContain('Individual Test Results');
      expect(report.length).toBeGreaterThan(100);
    });
  });
});
