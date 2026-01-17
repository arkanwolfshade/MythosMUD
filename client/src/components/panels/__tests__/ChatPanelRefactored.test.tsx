import { fireEvent, render, screen, within } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { DEFAULT_CHANNEL } from '../../../config/channels';
import { ChatMessage } from '../../../stores/gameStore';
import { ChatPanelRefactored } from '../ChatPanelRefactored';

// Mock the chat sub-components
// Mock individual files to match the component's import paths
vi.mock('../chat/ChatStatistics.tsx', () => ({
  ChatStatistics: ({
    selectedChannel,
    currentChannelMessages,
    unreadCounts,
  }: {
    selectedChannel: string;
    currentChannelMessages: number;
    unreadCounts: Record<string, number>;
  }) => (
    <div data-testid="chat-statistics">
      <span>Channel: {selectedChannel}</span>
      <span>Messages: {currentChannelMessages}</span>
      <span>Unread: {Object.values(unreadCounts).reduce((a: number, b: number) => a + b, 0)}</span>
    </div>
  ),
}));

vi.mock('../chat/ChatHeader.tsx', () => ({
  ChatHeader: ({ onClearMessages, onDownloadLogs }: { onClearMessages?: () => void; onDownloadLogs?: () => void }) => (
    <div data-testid="chat-header">
      <button onClick={onClearMessages}>Clear Messages</button>
      <button onClick={onDownloadLogs}>Download Logs</button>
    </div>
  ),
}));

vi.mock('../chat/ChannelSelectorSection.tsx', () => ({
  ChannelSelectorSection: ({
    selectedChannel,
    onChannelSelect,
    disabled,
  }: {
    selectedChannel: string;
    onChannelSelect: (channel: string) => void;
    disabled?: boolean;
  }) => (
    <div data-testid="channel-selector">
      <button
        onClick={() => {
          onChannelSelect('local');
        }}
        disabled={disabled}
        className={selectedChannel === 'local' ? 'selected' : ''}
      >
        Local
      </button>
      <button
        onClick={() => {
          onChannelSelect('global');
        }}
        disabled={disabled}
        className={selectedChannel === 'global' ? 'selected' : ''}
      >
        Global
      </button>
    </div>
  ),
}));

vi.mock('../chat/ChannelActivityIndicators.tsx', () => ({
  ChannelActivityIndicators: ({
    selectedChannel: _selectedChannel,
    unreadCounts,
    onChannelSelect,
  }: {
    selectedChannel: string;
    unreadCounts: Record<string, number>;
    onChannelSelect: (channel: string) => void;
  }) => (
    <div data-testid="activity-indicators">
      {Object.entries(unreadCounts).map(([channel, count]) => (
        <span
          key={channel}
          onClick={() => {
            onChannelSelect(channel);
          }}
        >
          {channel}: {count}
        </span>
      ))}
    </div>
  ),
}));

vi.mock('../chat/ChatHistoryToggle.tsx', () => ({
  ChatHistoryToggle: ({
    showChatHistory,
    onToggleHistory,
    chatFilter,
    onFilterChange,
    currentChannelMessages,
  }: {
    showChatHistory: boolean;
    onToggleHistory: () => void;
    chatFilter: string;
    onFilterChange: (filter: string) => void;
    currentChannelMessages: number;
  }) => (
    <div data-testid="chat-history-toggle">
      <button
        onClick={() => {
          onToggleHistory();
        }}
      >
        {showChatHistory ? 'Hide' : 'Show'} History
      </button>
      <select
        value={chatFilter}
        onChange={e => {
          onFilterChange(e.target.value);
        }}
      >
        <option value="current">Current</option>
        <option value="all">All</option>
      </select>
      <span>Messages: {currentChannelMessages}</span>
    </div>
  ),
}));

vi.mock('../chat/ChatMessagesList.tsx', () => ({
  ChatMessagesList: ({ messages }: { messages: ChatMessage[] }) => (
    <div data-testid="chat-messages-list">
      {messages.map((message: { text: string }, index: number) => (
        <div key={index} data-testid={`message-${index}`}>
          {message.text}
        </div>
      ))}
    </div>
  ),
}));

describe('ChatPanelRefactored', () => {
  const defaultProps = {
    messages: [],
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onDownloadLogs: vi.fn(),
    disabled: false,
    isConnected: true,
    selectedChannel: DEFAULT_CHANNEL,
    onChannelSelect: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Basic Rendering', () => {
    it('should render all sub-components', () => {
      render(<ChatPanelRefactored {...defaultProps} />);

      expect(screen.getByTestId('chat-header')).toBeInTheDocument();
      expect(screen.getByTestId('channel-selector')).toBeInTheDocument();
      expect(screen.getByTestId('activity-indicators')).toBeInTheDocument();
      expect(screen.getByTestId('chat-history-toggle')).toBeInTheDocument();
      expect(screen.getByTestId('chat-messages-list')).toBeInTheDocument();
      expect(screen.getByTestId('chat-statistics')).toBeInTheDocument();
    });

    it('should render with default props', () => {
      render(<ChatPanelRefactored messages={[]} onSendChatMessage={vi.fn()} />);

      expect(screen.getByTestId('chat-header')).toBeInTheDocument();
      expect(screen.getByText('Local')).toBeInTheDocument();
    });
  });

  describe('Channel Management', () => {
    it('should handle channel selection', () => {
      const mockOnChannelSelect = vi.fn();
      render(<ChatPanelRefactored {...defaultProps} selectedChannel="local" onChannelSelect={mockOnChannelSelect} />);

      // Find the Global button in the channel selector (not the activity indicator)
      const channelSelector = screen.getByTestId('channel-selector');
      const globalButton = within(channelSelector).getByText('Global');
      fireEvent.click(globalButton);
      expect(mockOnChannelSelect).toHaveBeenCalledWith('global');
    });

    it('should clear unread counts when switching channels', () => {
      const mockOnChannelSelect = vi.fn();
      const messages = [
        {
          text: 'Hello from global',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'global',
        },
        {
          text: 'Hello from local',
          timestamp: '2024-01-01T10:01:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local',
        },
      ];

      render(
        <ChatPanelRefactored
          {...defaultProps}
          messages={messages}
          selectedChannel="local"
          onChannelSelect={mockOnChannelSelect}
        />
      );

      // Should have unread count for global channel
      expect(screen.getByText('global: 1')).toBeInTheDocument();

      // Switch to global channel
      fireEvent.click(screen.getByText('global: 1'));
      expect(mockOnChannelSelect).toHaveBeenCalledWith('global');
    });
  });

  describe('Message Filtering', () => {
    it('should filter system messages out', () => {
      const messages = [
        {
          text: 'System message',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'system' as const,
        },
        {
          text: 'Chat message',
          timestamp: '2024-01-01T10:01:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local', // Use 'local' to match DEFAULT_CHANNEL
        },
      ];

      render(<ChatPanelRefactored {...defaultProps} messages={messages} />);

      const messageList = screen.getByTestId('chat-messages-list');
      expect(within(messageList).getByText('Chat message')).toBeInTheDocument();
      expect(within(messageList).queryByText('System message')).not.toBeInTheDocument();
    });

    it('should filter messages by current channel', () => {
      const messages = [
        {
          text: 'Local message',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local',
        },
        {
          text: 'Global message',
          timestamp: '2024-01-01T10:01:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'global',
        },
      ];

      render(<ChatPanelRefactored {...defaultProps} messages={messages} selectedChannel="local" />);

      const messageList = screen.getByTestId('chat-messages-list');
      expect(within(messageList).getByText('Local message')).toBeInTheDocument();
      expect(within(messageList).queryByText('Global message')).not.toBeInTheDocument();
    });

    it('should show all messages when filter is set to "all"', () => {
      const messages = [
        {
          text: 'Local message',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local',
        },
        {
          text: 'Global message',
          timestamp: '2024-01-01T10:01:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'global',
        },
      ];

      render(<ChatPanelRefactored {...defaultProps} messages={messages} selectedChannel="local" />);

      // Change filter to "all"
      const historyToggle = screen.getByTestId('chat-history-toggle');
      fireEvent.change(within(historyToggle).getByRole('combobox'), { target: { value: 'all' } });

      const messageList = screen.getByTestId('chat-messages-list');
      expect(within(messageList).getByText('Local message')).toBeInTheDocument();
      expect(within(messageList).getByText('Global message')).toBeInTheDocument();
    });
  });

  describe('Chat History Toggle', () => {
    it('should toggle chat history visibility', () => {
      render(<ChatPanelRefactored {...defaultProps} />);

      const historyToggle = screen.getByTestId('chat-history-toggle');
      const toggleButton = within(historyToggle).getByText('Show History');
      expect(toggleButton).toBeInTheDocument();

      fireEvent.click(toggleButton);
      expect(within(historyToggle).getByText('Hide History')).toBeInTheDocument();

      fireEvent.click(within(historyToggle).getByText('Hide History'));
      expect(within(historyToggle).getByText('Show History')).toBeInTheDocument();
    });

    it('should update filter when changed', () => {
      render(<ChatPanelRefactored {...defaultProps} />);

      const historyToggle = screen.getByTestId('chat-history-toggle');
      const filterSelect = within(historyToggle).getByRole('combobox');
      expect(filterSelect).toHaveValue('current');

      fireEvent.change(filterSelect, { target: { value: 'all' } });
      expect(filterSelect).toHaveValue('all');
    });
  });

  describe('Statistics', () => {
    it('should calculate correct statistics', () => {
      const messages = [
        {
          text: 'Local message 1',
          timestamp: '2024-01-01T10:00:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local',
        },
        {
          text: 'Local message 2',
          timestamp: '2024-01-01T10:01:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'local',
        },
        {
          text: 'Global message',
          timestamp: '2024-01-01T10:02:00Z',
          isHtml: false,
          messageType: 'chat' as const,
          channel: 'global',
        },
      ];

      render(<ChatPanelRefactored {...defaultProps} messages={messages} selectedChannel="local" />);

      // ChatStatistics should be rendered as it's always present in ChatPanelRefactored
      // Check for the statistics section with the expected content
      const statisticsSection = screen.getByTestId('chat-statistics');
      expect(statisticsSection).toBeInTheDocument();
      expect(statisticsSection).toHaveTextContent('Messages: 2');
      expect(statisticsSection).toHaveTextContent('Unread: 1');
    });
  });

  describe('Event Handlers', () => {
    it('should call onClearMessages when clear button is clicked', () => {
      const mockOnClearMessages = vi.fn();
      render(<ChatPanelRefactored {...defaultProps} onClearMessages={mockOnClearMessages} />);

      const chatHeader = screen.getByTestId('chat-header');
      const clearButton = within(chatHeader).getByText('Clear Messages');
      fireEvent.click(clearButton);
      expect(mockOnClearMessages).toHaveBeenCalled();
    });

    it('should call onDownloadLogs when download button is clicked', () => {
      const mockOnDownloadLogs = vi.fn();
      render(<ChatPanelRefactored {...defaultProps} onDownloadLogs={mockOnDownloadLogs} />);

      const chatHeader = screen.getByTestId('chat-header');
      const downloadButton = within(chatHeader).getByText('Download Logs');
      fireEvent.click(downloadButton);
      expect(mockOnDownloadLogs).toHaveBeenCalled();
    });
  });

  describe('Accessibility', () => {
    it('should have proper ARIA labels', () => {
      render(<ChatPanelRefactored {...defaultProps} />);

      const messagesContainer = screen.getByRole('log', { name: 'Chat Messages' });
      expect(messagesContainer).toBeInTheDocument();
      expect(messagesContainer).toHaveAttribute('aria-label', 'Chat Messages');
    });

    it('should have proper disabled state', () => {
      render(<ChatPanelRefactored {...defaultProps} disabled={true} />);

      const channelSelector = screen.getByTestId('channel-selector');
      const localButton = within(channelSelector).getByRole('button', { name: 'Local' });
      expect(localButton).toBeDisabled();
    });
  });
});
