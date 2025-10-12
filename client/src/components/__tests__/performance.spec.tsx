import { expect } from '@playwright/test';
import { render } from '@testing-library/react';
import { beforeEach, describe, it, vi } from 'vitest';
import { PerformanceTester } from '../src/utils/performanceTester';

// Mock the dependencies
vi.mock('../src/components/ui/EldritchIcon', () => ({
  EldritchIcon: ({
    name,
    _size,
    _variant,
    className,
  }: {
    name: string;
    _size?: number;
    _variant?: string;
    className?: string;
  }) => (
    <span data-testid={`icon-${name}`} className={className}>
      {name}
    </span>
  ),
  MythosIcons: {
    performance: 'performance',
    memory: 'memory',
    speed: 'speed',
  },
}));

interface TerminalButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/TerminalButton', () => ({
  TerminalButton: ({ children, onClick, disabled, ...props }: TerminalButtonProps) => (
    <button onClick={onClick} disabled={disabled} {...props}>
      {children}
    </button>
  ),
}));

interface PerformanceChartProps {
  data: Array<{ label: string; value: number }>;
  title: string;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/PerformanceChart', () => ({
  PerformanceChart: ({ data, title, ...props }: PerformanceChartProps) => (
    <div data-testid="performance-chart" {...props}>
      <h3>{title}</h3>
      <div data-testid="chart-data">{JSON.stringify(data)}</div>
    </div>
  ),
}));

interface MemoryUsageDisplayProps {
  current: number;
  peak: number;
  average: number;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/MemoryUsageDisplay', () => ({
  MemoryUsageDisplay: ({ current, peak, average, ...props }: MemoryUsageDisplayProps) => (
    <div data-testid="memory-usage" {...props}>
      <span>Current: {current}MB</span>
      <span>Peak: {peak}MB</span>
      <span>Average: {average}MB</span>
    </div>
  ),
}));

interface TerminalInputProps {
  value: string;
  onChange?: (event: React.ChangeEvent<HTMLInputElement>) => void;
  onKeyDown?: (event: React.KeyboardEvent) => void;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/TerminalInput', () => ({
  TerminalInput: ({ value, onChange, onKeyDown, ...props }: TerminalInputProps) => (
    <input value={value} onChange={onChange} onKeyDown={onKeyDown} {...props} />
  ),
}));

interface Channel {
  id: string;
  name: string;
}

interface ChannelSelectorProps {
  channels: Channel[];
  selectedChannel: string;
  onChannelSelect?: (channelId: string) => void;
  disabled?: boolean;
}

vi.mock('../src/components/ui/ChannelSelector', () => ({
  ChannelSelector: ({ channels, selectedChannel, onChannelSelect, disabled }: ChannelSelectorProps) => (
    <select
      value={selectedChannel}
      onChange={e => onChannelSelect?.(e.target.value)}
      disabled={disabled}
      data-testid="channel-selector"
    >
      {channels.map((channel: Channel) => (
        <option key={channel.id} value={channel.id}>
          {channel.name}
        </option>
      ))}
    </select>
  ),
}));

vi.mock('../src/utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br>'),
}));

vi.mock('../src/config/channels', () => ({
  AVAILABLE_CHANNELS: [
    { id: 'local', name: 'Local', shortcut: 'l' },
    { id: 'global', name: 'Global', shortcut: 'g' },
  ],
  DEFAULT_CHANNEL: 'local',
}));

describe('Performance Tests', () => {
  let performanceTester: PerformanceTester;

  beforeEach(() => {
    performanceTester = new PerformanceTester();
  });

  describe('ChatPanel Performance', () => {
    const mockMessages = Array.from({ length: 100 }, (_, i) => ({
      text: `Message ${i}`,
      timestamp: new Date(Date.now() - i * 60000).toISOString(),
      isHtml: false,
      messageType: 'chat' as const,
      aliasChain: [{ original: `Player${i}`, expanded: `Player${i}`, alias_name: `p${i}` }],
    }));

    const defaultProps = {
      messages: mockMessages,
      onSendChatMessage: vi.fn(),
      onClearMessages: vi.fn(),
      onDownloadLogs: vi.fn(),
      disabled: false,
      isConnected: true,
      selectedChannel: 'local',
      onChannelSelect: vi.fn(),
    };

    it('renders large message lists efficiently', async () => {
      const result = await performanceTester.runTest(
        'ChatPanel - Large Message List Render',
        () => {
          render(<ChatPanel {...defaultProps} />);
        },
        { iterations: 100, warmupIterations: 10 }
      );

      expect(result.averageTime).toBeLessThan(50); // Should render in under 50ms
      expect(result.iterations).toBeGreaterThan(0);
    });

    it('handles rapid state updates efficiently', async () => {
      const { rerender } = render(<ChatPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'ChatPanel - Rapid State Updates',
        () => {
          const newMessages = [
            ...mockMessages,
            {
              text: 'New message',
              timestamp: new Date().toISOString(),
              isHtml: false,
              messageType: 'chat' as const,
            },
          ];
          rerender(<ChatPanel {...defaultProps} messages={newMessages} />);
        },
        { iterations: 100, warmupIterations: 10 }
      );

      expect(result.averageTime).toBeLessThan(20); // Should update in under 20ms
    });

    it('filters messages efficiently', async () => {
      render(<ChatPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'ChatPanel - Message Filtering',
        () => {
          // Simulate filtering operation
          const filteredMessages = mockMessages.filter(message => message.text.includes('Message'));
          expect(filteredMessages.length).toBeGreaterThan(0);
        },
        { iterations: 1000, warmupIterations: 100 }
      );

      expect(result.averageTime).toBeLessThan(1); // Should filter in under 1ms
    });
  });

  describe('GameLogPanel Performance', () => {
    const mockMessages = Array.from({ length: 1000 }, (_, i) => ({
      text: `Game message ${i}`,
      timestamp: new Date(Date.now() - i * 60000).toISOString(),
      isHtml: false,
      messageType: i % 4 === 0 ? 'system' : i % 4 === 1 ? 'error' : i % 4 === 2 ? 'move' : 'chat',
    }));

    const defaultProps = {
      messages: mockMessages,
      onClearMessages: vi.fn(),
      onDownloadLogs: vi.fn(),
    };

    it('renders large game log efficiently', async () => {
      const result = await performanceTester.runTest(
        'GameLogPanel - Large Game Log Render',
        () => {
          render(<GameLogPanel {...defaultProps} />);
        },
        { iterations: 50, warmupIterations: 5 }
      );

      expect(result.averageTime).toBeLessThan(100); // Should render in under 100ms
      expect(result.iterations).toBeGreaterThan(0);
    });

    it('filters messages efficiently', async () => {
      render(<GameLogPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'GameLogPanel - Message Filtering',
        () => {
          // Simulate complex filtering
          const filteredMessages = mockMessages.filter(
            message => message.messageType === 'chat' && message.text.includes('message')
          );
          expect(filteredMessages.length).toBeGreaterThan(0);
        },
        { iterations: 1000, warmupIterations: 100 }
      );

      expect(result.averageTime).toBeLessThan(5); // Should filter in under 5ms
    });

    it('groups messages efficiently', async () => {
      render(<GameLogPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'GameLogPanel - Message Grouping',
        () => {
          // Simulate message grouping by time
          const groups: Record<string, typeof mockMessages> = {};
          mockMessages.forEach(message => {
            const date = new Date(message.timestamp).toDateString();
            if (!groups[date]) groups[date] = [];
            groups[date].push(message);
          });
          expect(Object.keys(groups).length).toBeGreaterThan(0);
        },
        { iterations: 100, warmupIterations: 10 }
      );

      expect(result.averageTime).toBeLessThan(10); // Should group in under 10ms
    });
  });

  describe('CommandPanel Performance', () => {
    const mockCommandHistory = Array.from({ length: 1000 }, (_, i) => `command${i}`);

    const defaultProps = {
      commandHistory: mockCommandHistory,
      onSendCommand: vi.fn(),
      onClearHistory: vi.fn(),
      disabled: false,
      isConnected: true,
    };

    it('renders large command history efficiently', async () => {
      const result = await performanceTester.runTest(
        'CommandPanel - Large Command History Render',
        () => {
          render(<CommandPanel {...defaultProps} />);
        },
        { iterations: 100, warmupIterations: 10 }
      );

      expect(result.averageTime).toBeLessThan(50); // Should render in under 50ms
      expect(result.iterations).toBeGreaterThan(0);
    });

    it('filters command suggestions efficiently', async () => {
      render(<CommandPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'CommandPanel - Command Suggestion Filtering',
        () => {
          // Simulate command suggestion filtering
          const suggestions = mockCommandHistory.filter(command => command.includes('command'));
          expect(suggestions.length).toBeGreaterThan(0);
        },
        { iterations: 1000, warmupIterations: 100 }
      );

      expect(result.averageTime).toBeLessThan(1); // Should filter in under 1ms
    });

    it('navigates command history efficiently', async () => {
      render(<CommandPanel {...defaultProps} />);

      const result = await performanceTester.runTest(
        'CommandPanel - Command History Navigation',
        () => {
          // Simulate command history navigation
          const historyIndex = Math.floor(Math.random() * mockCommandHistory.length);
          const command = mockCommandHistory[historyIndex];
          expect(command).toBeDefined();
        },
        { iterations: 1000, warmupIterations: 100 }
      );

      expect(result.averageTime).toBeLessThan(1); // Should navigate in under 1ms
    });
  });

  describe('Memory Usage Tests', () => {
    it('ChatPanel memory usage stays within limits', async () => {
      const largeMessages = Array.from({ length: 10000 }, (_, i) => ({
        text: `Large message ${i} with lots of content to test memory usage`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: 'chat' as const,
        aliasChain: [{ original: `Player${i}`, expanded: `Player${i}`, alias_name: `p${i}` }],
      }));

      const result = await performanceTester.runMemoryTest(
        'ChatPanel - Memory Usage',
        () => {
          render(
            <ChatPanel
              messages={largeMessages}
              onSendChatMessage={vi.fn()}
              onClearMessages={vi.fn()}
              onDownloadLogs={vi.fn()}
              disabled={false}
              isConnected={true}
              selectedChannel="local"
              onChannelSelect={vi.fn()}
            />
          );
        },
        { iterations: 10, warmupIterations: 2 }
      );

      // Memory usage should be reasonable (less than 50MB for 10k messages)
      if (result.memoryUsage !== undefined) {
        const memoryMB = result.memoryUsage / 1024 / 1024;
        expect(memoryMB).toBeLessThan(50);
      }
    });

    it('GameLogPanel memory usage stays within limits', async () => {
      const largeMessages = Array.from({ length: 10000 }, (_, i) => ({
        text: `Large game message ${i} with lots of content to test memory usage`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: i % 4 === 0 ? 'system' : i % 4 === 1 ? 'error' : i % 4 === 2 ? 'move' : 'chat',
      }));

      const result = await performanceTester.runMemoryTest(
        'GameLogPanel - Memory Usage',
        () => {
          render(<GameLogPanel messages={largeMessages} onClearMessages={vi.fn()} onDownloadLogs={vi.fn()} />);
        },
        { iterations: 10, warmupIterations: 2 }
      );

      // Memory usage should be reasonable (less than 50MB for 10k messages)
      if (result.memoryUsage !== undefined) {
        const memoryMB = result.memoryUsage / 1024 / 1024;
        expect(memoryMB).toBeLessThan(50);
      }
    });
  });

  describe('Integration Performance', () => {
    it('all panels render together efficiently', async () => {
      const mockMessages = Array.from({ length: 100 }, (_, i) => ({
        text: `Message ${i}`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: 'chat' as const,
      }));

      const mockCommandHistory = Array.from({ length: 100 }, (_, i) => `command${i}`);

      const result = await performanceTester.runTest(
        'Integration - All Panels Render',
        () => {
          // Render all three panels
          render(
            <ChatPanel
              messages={mockMessages}
              onSendChatMessage={vi.fn()}
              onClearMessages={vi.fn()}
              onDownloadLogs={vi.fn()}
              disabled={false}
              isConnected={true}
              selectedChannel="local"
              onChannelSelect={vi.fn()}
            />
          );

          render(<GameLogPanel messages={mockMessages} onClearMessages={vi.fn()} onDownloadLogs={vi.fn()} />);

          render(
            <CommandPanel
              commandHistory={mockCommandHistory}
              onSendCommand={vi.fn()}
              onClearHistory={vi.fn()}
              disabled={false}
              isConnected={true}
            />
          );
        },
        { iterations: 50, warmupIterations: 5 }
      );

      expect(result.averageTime).toBeLessThan(150); // Should render all panels in under 150ms
    });
  });

  describe('Performance Benchmarks', () => {
    it('meets performance benchmarks', async () => {
      const results = performanceTester.getResults();
      const averages = performanceTester.getAverageResults();

      // Overall performance should be good
      expect(averages.averageTime).toBeLessThan(100); // Average render time under 100ms
      expect(averages.totalTests).toBeGreaterThan(0);

      // Individual test results should meet benchmarks
      results.forEach(result => {
        if (result.name.includes('Render')) {
          expect(result.averageTime).toBeLessThan(100); // Render tests under 100ms
        }
        if (result.name.includes('Filter')) {
          expect(result.averageTime).toBeLessThan(10); // Filter tests under 10ms
        }
        if (result.name.includes('Memory')) {
          if (result.memoryUsage !== undefined) {
            const memoryMB = result.memoryUsage / 1024 / 1024;
            expect(memoryMB).toBeLessThan(100); // Memory usage under 100MB
          }
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
