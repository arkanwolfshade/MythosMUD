import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../../stores/gameStore';
import { GameLogPanel } from '../GameLogPanel';

// Mock the dependencies - GameLogPanel uses MythosIcons.log
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; className?: string }) => (
    <span data-testid={`icon-${name}`} className={className}>
      {name}
    </span>
  ),
  MythosIcons: {
    log: 'log',
    system: 'system',
    clear: 'clear',
    download: 'download',
  },
}));

interface TerminalButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  [key: string]: unknown;
}

vi.mock('../../ui/TerminalButton', () => ({
  TerminalButton: ({ children, onClick, disabled, ...props }: TerminalButtonProps) => (
    <button onClick={onClick} disabled={disabled} {...props}>
      {children}
    </button>
  ),
}));

vi.mock('../../../utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br>'),
}));

describe('GameLogPanel', () => {
  // Chat messages are excluded from GameLogPanel; use system, error, move, etc.
  const mockMessages = [
    {
      text: 'System message',
      timestamp: '2024-01-01T12:01:00Z',
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'Error message',
      timestamp: '2024-01-01T12:02:00Z',
      isHtml: false,
      messageType: 'error',
    },
    {
      text: 'You moved north',
      timestamp: '2024-01-01T12:03:00Z',
      isHtml: false,
      messageType: 'move',
    },
    {
      text: 'Emote message',
      timestamp: '2024-01-01T12:04:00Z',
      isHtml: false,
      messageType: 'emote',
      aliasChain: [{ original: 'Player1', expanded: 'Player1', alias_name: 'p1' }],
    },
  ];

  const defaultProps = {
    messages: mockMessages,
    onClearMessages: vi.fn(),
    onDownloadLogs: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Basic Rendering', () => {
    it('renders game log panel with header', () => {
      render(<GameLogPanel {...defaultProps} />);

      expect(screen.getByText('Game Log')).toBeInTheDocument();
      expect(screen.getByTestId('icon-log')).toBeInTheDocument();
    });

    it('displays non-chat messages by default', () => {
      render(<GameLogPanel {...defaultProps} />);

      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.getByText('Error message')).toBeInTheDocument();
      expect(screen.getByText('You moved north')).toBeInTheDocument();
      expect(screen.getByText('Emote message')).toBeInTheDocument();
    });

    it('excludes chat messages from display', () => {
      const withChat = [
        ...mockMessages,
        { text: 'Chat only', timestamp: '2024-01-01T12:05:00Z', isHtml: false, messageType: 'chat' },
      ];
      render(<GameLogPanel {...defaultProps} messages={withChat} />);

      expect(screen.queryByText('Chat only')).not.toBeInTheDocument();
    });

    it('shows empty state when no messages', () => {
      render(<GameLogPanel {...defaultProps} messages={[]} />);

      expect(screen.getByText('No messages to display')).toBeInTheDocument();
    });
  });

  describe('Message Filtering', () => {
    it('filters messages by type', () => {
      render(<GameLogPanel {...defaultProps} />);

      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'system' } });

      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.queryByText('Error message')).not.toBeInTheDocument();
      expect(screen.queryByText('You moved north')).not.toBeInTheDocument();
    });

    it('filters messages by time range', () => {
      render(<GameLogPanel {...defaultProps} />);

      const timeFilter = screen.getByDisplayValue('All Time');
      fireEvent.change(timeFilter, { target: { value: '5' } });

      expect(timeFilter).toHaveValue('5');
    });

    it('filters messages by search query', () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'System' } });

      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.queryByText('Error message')).not.toBeInTheDocument();
    });

    it('combines type and search filters', () => {
      render(<GameLogPanel {...defaultProps} />);

      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'system' } });

      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'System' } });

      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.queryByText('Error message')).not.toBeInTheDocument();
    });
  });

  describe('Filter Controls', () => {
    it('clears all filters', () => {
      render(<GameLogPanel {...defaultProps} />);

      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'system' } });

      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'System' } });

      const clearFiltersButton = screen.getByText('Clear Filters');
      fireEvent.click(clearFiltersButton);

      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.getByText('Error message')).toBeInTheDocument();
      expect(screen.getByText('You moved north')).toBeInTheDocument();
    });
  });

  describe('Message Display', () => {
    it('displays message timestamps', () => {
      render(<GameLogPanel {...defaultProps} />);

      const messageItems = screen.getAllByTestId('game-log-message');
      expect(messageItems.length).toBeGreaterThanOrEqual(2);
      // Each message has a timestamp span (format varies by locale)
      messageItems.forEach(el => {
        const timeSpan = el.querySelector('.text-xs.text-mythos-terminal-text-secondary');
        expect(timeSpan).toBeTruthy();
        expect(timeSpan?.textContent).toMatch(/\d{1,2}:\d{2}:\d{2}/);
      });
    });

    it('displays alias information for messages with aliasChain', () => {
      render(<GameLogPanel {...defaultProps} />);

      expect(screen.getByText(/Alias:/)).toBeInTheDocument();
      expect(screen.getByText(/p1/)).toBeInTheDocument();
    });

    it('renders messages with appropriate content', () => {
      render(<GameLogPanel {...defaultProps} />);

      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.getByText('Error message')).toBeInTheDocument();
      expect(screen.getByText('Emote message')).toBeInTheDocument();
    });
  });

  describe('Action Buttons', () => {
    it('calls onClearMessages when Clear Log is clicked', () => {
      render(<GameLogPanel {...defaultProps} />);

      const clearButton = screen.getByText('Clear Log');
      fireEvent.click(clearButton);

      expect(defaultProps.onClearMessages).toHaveBeenCalled();
    });

    it('calls onDownloadLogs when Download is clicked', () => {
      render(<GameLogPanel {...defaultProps} />);

      const downloadButton = screen.getByText('Download');
      fireEvent.click(downloadButton);

      expect(defaultProps.onDownloadLogs).toHaveBeenCalled();
    });
  });

  describe('Performance', () => {
    it('handles large message lists efficiently', () => {
      const largeMessageList = Array.from({ length: 1000 }, (_, i) => ({
        text: `Message ${i}`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: 'system' as const,
      }));

      render(<GameLogPanel {...defaultProps} messages={largeMessageList} />);

      expect(screen.getByText('Message 0')).toBeInTheDocument();
      expect(screen.getByText('Message 999')).toBeInTheDocument();
    });
  });

  describe('Error Handling', () => {
    it('handles malformed messages gracefully', () => {
      const malformedMessages = [
        {
          text: 'Valid message',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          messageType: 'system',
        },
        {
          text: 'Invalid message',
        } as ChatMessage,
      ];

      render(<GameLogPanel {...defaultProps} messages={malformedMessages} />);

      expect(screen.getByText('Valid message')).toBeInTheDocument();
    });

    it('handles missing props gracefully', () => {
      const { container } = render(<GameLogPanel messages={[]} />);

      expect(container).toBeInTheDocument();
    });
  });

  describe('Keyboard and Input', () => {
    it('supports search input interaction', () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'test' } });
      expect(searchInput).toHaveValue('test');

      fireEvent.keyDown(searchInput, { key: 'Enter' });
      fireEvent.keyDown(searchInput, { key: 'Escape' });
      expect(searchInput).toBeInTheDocument();
    });
  });
});
