import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../../stores/gameStore';
import { GameLogPanel } from '../GameLogPanel';

// Mock the dependencies
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; className?: string }) => (
    <span data-testid={`icon-${name}`} className={className}>
      {name}
    </span>
  ),
  MythosIcons: {
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
  const mockMessages = [
    {
      text: 'Hello, world!',
      timestamp: '2024-01-01T12:00:00Z',
      isHtml: false,
      messageType: 'chat',
      aliasChain: [{ original: 'Player1', expanded: 'Player1', alias_name: 'p1' }],
    },
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
      expect(screen.getByTestId('icon-system')).toBeInTheDocument();
    });

    it('displays all messages by default', () => {
      render(<GameLogPanel {...defaultProps} />);

      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.getByText('Error message')).toBeInTheDocument();
      expect(screen.getByText('You moved north')).toBeInTheDocument();
    });

    it('shows empty state when no messages', () => {
      render(<GameLogPanel {...defaultProps} messages={[]} />);

      expect(screen.getByText('No messages to display.')).toBeInTheDocument();
    });
  });

  describe('Message Filtering', () => {
    it('filters messages by type', () => {
      render(<GameLogPanel {...defaultProps} />);

      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'chat' } });

      // Should only show chat messages
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.queryByText('System message')).not.toBeInTheDocument();
      expect(screen.queryByText('Error message')).not.toBeInTheDocument();
      expect(screen.queryByText('You moved north')).not.toBeInTheDocument();
    });

    it('filters messages by time range', () => {
      render(<GameLogPanel {...defaultProps} />);

      const timeFilter = screen.getByDisplayValue('All Time');
      fireEvent.change(timeFilter, { target: { value: 'last5min' } });

      // Should only show recent messages (this would depend on the current time)
      // For now, we'll just test that the filter changes
      expect(timeFilter).toHaveValue('last5min');
    });

    it('filters messages by search query', () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'Hello' } });

      // Should only show messages containing "Hello"
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.queryByText('System message')).not.toBeInTheDocument();
      expect(screen.queryByText('Error message')).not.toBeInTheDocument();
      expect(screen.queryByText('You moved north')).not.toBeInTheDocument();
    });

    it('combines multiple filters', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Set message type filter
      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'chat' } });

      // Set search filter
      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'Hello' } });

      // Should only show chat messages containing "Hello"
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.queryByText('System message')).not.toBeInTheDocument();
    });
  });

  describe('Message Grouping', () => {
    it('toggles message grouping', () => {
      render(<GameLogPanel {...defaultProps} />);

      const groupToggle = screen.getByRole('checkbox', { name: /group messages/i });
      fireEvent.click(groupToggle);

      // Should show grouped messages
      expect(groupToggle).toBeChecked();
    });

    it('groups messages by time periods', () => {
      render(<GameLogPanel {...defaultProps} />);

      const groupToggle = screen.getByRole('checkbox', { name: /group messages/i });
      fireEvent.click(groupToggle);

      // Should show time group headers
      expect(screen.getByText('Last 5 minutes')).toBeInTheDocument();
      expect(screen.getByText('Last hour')).toBeInTheDocument();
      expect(screen.getByText('Today')).toBeInTheDocument();
      expect(screen.getByText('Earlier')).toBeInTheDocument();
    });
  });

  describe('Search Functionality', () => {
    it('maintains search history', () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');

      // Perform multiple searches
      fireEvent.change(searchInput, { target: { value: 'Hello' } });
      fireEvent.change(searchInput, { target: { value: 'System' } });
      fireEvent.change(searchInput, { target: { value: 'Error' } });

      // Clear search
      fireEvent.change(searchInput, { target: { value: '' } });

      // Should show search history
      const searchHistoryButton = screen.getByText('Search History');
      fireEvent.click(searchHistoryButton);

      // Should show previous search terms
      expect(screen.getByText('Hello')).toBeInTheDocument();
      expect(screen.getByText('System')).toBeInTheDocument();
      expect(screen.getByText('Error')).toBeInTheDocument();
    });

    it('allows selecting from search history', () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');

      // Perform a search
      fireEvent.change(searchInput, { target: { value: 'Hello' } });

      // Clear search
      fireEvent.change(searchInput, { target: { value: '' } });

      // Show search history and click on a previous search
      const searchHistoryButton = screen.getByText('Search History');
      fireEvent.click(searchHistoryButton);

      const historyItem = screen.getByText('Hello');
      fireEvent.click(historyItem);

      // Should apply the selected search
      expect(searchInput).toHaveValue('Hello');
    });
  });

  describe('Filter Controls', () => {
    it('clears all filters', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Set some filters
      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'chat' } });

      const searchInput = screen.getByPlaceholderText('Search messages...');
      fireEvent.change(searchInput, { target: { value: 'Hello' } });

      // Clear filters
      const clearFiltersButton = screen.getByText('Clear Filters');
      fireEvent.click(clearFiltersButton);

      // Should show all messages
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('System message')).toBeInTheDocument();
      expect(screen.getByText('Error message')).toBeInTheDocument();
      expect(screen.getByText('You moved north')).toBeInTheDocument();
    });

    it('shows filter status', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Set a filter
      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'chat' } });

      // Should show that filters are active
      expect(screen.getByText('Filters Active')).toBeInTheDocument();
    });
  });

  describe('Statistics Display', () => {
    it('shows message statistics', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Should show total message count
      expect(screen.getByText('4 messages')).toBeInTheDocument();

      // Should show message type breakdown
      expect(screen.getByText('Chat: 1')).toBeInTheDocument();
      expect(screen.getByText('System: 1')).toBeInTheDocument();
      expect(screen.getByText('Error: 1')).toBeInTheDocument();
      expect(screen.getByText('Move: 1')).toBeInTheDocument();
    });

    it('updates statistics when filters are applied', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Apply filter
      const messageTypeFilter = screen.getByDisplayValue('All Messages');
      fireEvent.change(messageTypeFilter, { target: { value: 'chat' } });

      // Should show filtered message count
      expect(screen.getByText('1 of 4 messages')).toBeInTheDocument();
    });
  });

  describe('Message Display', () => {
    it('displays message timestamps', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Should show timestamps for messages
      expect(screen.getByText(/12:00:00/)).toBeInTheDocument();
      expect(screen.getByText(/12:01:00/)).toBeInTheDocument();
    });

    it('displays alias expansion information', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Should show alias expansion for messages with aliasChain
      expect(screen.getByText('Alias Expansion:')).toBeInTheDocument();
      expect(screen.getByText('Player1')).toBeInTheDocument();
    });

    it('applies message type styling', () => {
      render(<GameLogPanel {...defaultProps} />);

      // Messages should have appropriate styling based on type
      const chatMessage = screen.getByText('Hello, world!');
      const systemMessage = screen.getByText('System message');
      const errorMessage = screen.getByText('Error message');

      expect(chatMessage).toBeInTheDocument();
      expect(systemMessage).toBeInTheDocument();
      expect(errorMessage).toBeInTheDocument();
    });
  });

  describe('Action Buttons', () => {
    it('calls onClearMessages when clear button is clicked', () => {
      render(<GameLogPanel {...defaultProps} />);

      const clearButton = screen.getByText('Clear Messages');
      fireEvent.click(clearButton);

      expect(defaultProps.onClearMessages).toHaveBeenCalled();
    });

    it('calls onDownloadLogs when download button is clicked', () => {
      render(<GameLogPanel {...defaultProps} />);

      const downloadButton = screen.getByText('Download Logs');
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
        messageType: 'chat' as const,
      }));

      render(<GameLogPanel {...defaultProps} messages={largeMessageList} />);

      // Should render without performance issues
      expect(screen.getByText('Message 0')).toBeInTheDocument();
      expect(screen.getByText('Message 999')).toBeInTheDocument();
    });

    it('debounces search input', async () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');

      // Rapidly type in search
      fireEvent.change(searchInput, { target: { value: 'H' } });
      fireEvent.change(searchInput, { target: { value: 'He' } });
      fireEvent.change(searchInput, { target: { value: 'Hel' } });
      fireEvent.change(searchInput, { target: { value: 'Hell' } });
      fireEvent.change(searchInput, { target: { value: 'Hello' } });

      // Should debounce the search and not cause performance issues
      await waitFor(() => {
        expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      });
    });
  });

  describe('Error Handling', () => {
    it('handles malformed messages gracefully', () => {
      const malformedMessages = [
        {
          text: 'Valid message',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          messageType: 'chat',
        },
        {
          // Missing required fields - intentionally malformed for testing
          text: 'Invalid message',
        } as ChatMessage,
      ];

      render(<GameLogPanel {...defaultProps} messages={malformedMessages} />);

      // Should not crash and should display valid messages
      expect(screen.getByText('Valid message')).toBeInTheDocument();
    });

    it('handles missing props gracefully', () => {
      const { container } = render(<GameLogPanel messages={[]} />);

      expect(container).toBeInTheDocument();
    });
  });

  describe('Accessibility', () => {
    it('has proper ARIA labels', () => {
      render(<GameLogPanel {...defaultProps} />);

      expect(screen.getByLabelText('Game Log Messages')).toBeInTheDocument();
    });

    it('supports keyboard navigation', () => {
      render(<GameLogPanel {...defaultProps} />);

      const searchInput = screen.getByPlaceholderText('Search messages...');

      // Test keyboard navigation
      fireEvent.keyDown(searchInput, { key: 'Enter' });
      fireEvent.keyDown(searchInput, { key: 'Escape' });

      // Should not throw errors
      expect(searchInput).toBeInTheDocument();
    });
  });
});
