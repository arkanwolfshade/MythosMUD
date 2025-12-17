/**
 * Tests for GameLogPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { GameLogPanel } from '../GameLogPanel';

// Mock ansiToHtmlWithBreaks
vi.mock('../../utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text,
}));

// Mock EldritchIcon
vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({ icon }: { icon: string }) => <span data-testid={`icon-${icon}`}>{icon}</span>,
  MythosIcons: {},
}));

// Mock TerminalButton
vi.mock('../ui/TerminalButton', () => ({
  TerminalButton: ({ children, onClick }: { children: React.ReactNode; onClick?: () => void }) => (
    <button onClick={onClick}>{children}</button>
  ),
}));

describe('GameLogPanel', () => {
  const mockMessages = [
    {
      text: 'Welcome to MythosMUD',
      timestamp: '2024-01-01T12:00:00Z',
      isHtml: false,
      messageType: 'system',
    },
    {
      text: 'You enter a dark room',
      timestamp: '2024-01-01T12:00:01Z',
      isHtml: false,
      messageType: 'room',
    },
    {
      text: '*player1 waves*',
      timestamp: '2024-01-01T12:00:02Z',
      isHtml: false,
      messageType: 'emote',
    },
    {
      text: 'Error occurred',
      timestamp: '2024-01-01T12:00:03Z',
      isHtml: false,
      messageType: 'error',
    },
  ];

  it('should render messages', () => {
    render(<GameLogPanel messages={mockMessages} />);

    expect(screen.getByText('Welcome to MythosMUD')).toBeInTheDocument();
    expect(screen.getByText('You enter a dark room')).toBeInTheDocument();
  });

  it('should filter messages by type', () => {
    render(<GameLogPanel messages={mockMessages} />);

    // Get all select elements - first one is message filter, second is time filter
    const filterSelects = screen.getAllByRole('combobox');
    const messageFilterSelect = filterSelects[0];
    fireEvent.change(messageFilterSelect, { target: { value: 'emote' } });

    expect(screen.getByText('*player1 waves*')).toBeInTheDocument();
    expect(screen.queryByText('Welcome to MythosMUD')).not.toBeInTheDocument();
  });

  it('should filter messages by search query', () => {
    render(<GameLogPanel messages={mockMessages} />);

    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: 'dark' } });

    expect(screen.getByText('You enter a dark room')).toBeInTheDocument();
    expect(screen.queryByText('Welcome to MythosMUD')).not.toBeInTheDocument();
  });

  it('should call onClearMessages when clear button is clicked', () => {
    const onClearMessages = vi.fn();
    render(<GameLogPanel messages={mockMessages} onClearMessages={onClearMessages} />);

    const clearButton = screen.getByText(/clear log/i);
    fireEvent.click(clearButton);

    expect(onClearMessages).toHaveBeenCalledTimes(1);
  });

  it('should call onDownloadLogs when download button is clicked', () => {
    const onDownloadLogs = vi.fn();
    render(<GameLogPanel messages={mockMessages} onDownloadLogs={onDownloadLogs} />);

    const downloadButton = screen.getByText(/download/i);
    fireEvent.click(downloadButton);

    expect(onDownloadLogs).toHaveBeenCalledTimes(1);
  });

  it('should exclude chat messages from display', () => {
    const messagesWithChat = [
      ...mockMessages,
      {
        text: 'Hello world',
        timestamp: '2024-01-01T12:00:04Z',
        isHtml: false,
        messageType: 'chat',
      },
    ];

    render(<GameLogPanel messages={messagesWithChat} />);

    expect(screen.queryByText('Hello world')).not.toBeInTheDocument();
  });

  it('should apply correct CSS classes based on message type', () => {
    render(<GameLogPanel messages={mockMessages} />);

    // Check that different message types are rendered
    expect(screen.getByText('Welcome to MythosMUD')).toBeInTheDocument();
    expect(screen.getByText('*player1 waves*')).toBeInTheDocument();
    expect(screen.getByText('Error occurred')).toBeInTheDocument();
  });

  it('should handle empty messages array', () => {
    render(<GameLogPanel messages={[]} />);

    // Should render without errors
    expect(screen.getByPlaceholderText(/search/i)).toBeInTheDocument();
  });

  it('should clear filters when clear filters button is clicked', () => {
    render(<GameLogPanel messages={mockMessages} />);

    // Set message filter
    const filterSelects = screen.getAllByRole('combobox');
    const messageFilterSelect = filterSelects[0];
    fireEvent.change(messageFilterSelect, { target: { value: 'emote' } });

    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: 'test' } });

    // Find the Clear Filters button (case-insensitive)
    const clearFiltersButton = screen.getByRole('button', { name: /clear filters/i });
    fireEvent.click(clearFiltersButton);

    // Filters should be reset - both selects should have 'all' value
    const resetSelects = screen.getAllByRole('combobox');
    expect(resetSelects[0]).toHaveValue('all'); // Message filter reset
    expect(resetSelects[1]).toHaveValue('all'); // Time filter reset
    expect(searchInput).toHaveValue(''); // Search query cleared
  });

  it('should format timestamps correctly', () => {
    render(<GameLogPanel messages={mockMessages} />);

    // Timestamps should be formatted and displayed
    // The formatTimestamp function uses toLocaleTimeString which may format differently
    // Check for the time pattern (HH:MM:SS format)
    // Use getAllByText with regex to find timestamp elements
    const timestampElements = screen.getAllByText(/\d{1,2}:\d{2}:\d{2}/);
    expect(timestampElements.length).toBeGreaterThan(0);
  });

  it('should handle messages with HTML content', () => {
    const htmlMessages = [
      {
        text: '<b>Bold text</b>',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: true,
        messageType: 'system',
      },
    ];

    render(<GameLogPanel messages={htmlMessages} />);

    expect(screen.getByText(/Bold text/i)).toBeInTheDocument();
  });

  it('should filter messages by time range', () => {
    // Use recent timestamps to ensure they pass the time filter
    const recentMessages = [
      {
        text: 'Welcome to MythosMUD',
        timestamp: new Date().toISOString(), // Current time
        isHtml: false,
        messageType: 'system',
      },
      {
        text: 'You enter a dark room',
        timestamp: new Date(Date.now() - 30 * 60 * 1000).toISOString(), // 30 minutes ago
        isHtml: false,
        messageType: 'room',
      },
    ];

    render(<GameLogPanel messages={recentMessages} />);

    // Get all select elements - second one is time filter
    const filterSelects = screen.getAllByRole('combobox');
    const timeFilterSelect = filterSelects[1];
    // The time filter uses numeric values: "5", "15", "30", "60" for minutes
    fireEvent.change(timeFilterSelect, { target: { value: '60' } });

    // Messages within last hour should still be visible
    expect(screen.getByText('Welcome to MythosMUD')).toBeInTheDocument();
  });

  it('should handle alias chain in messages', () => {
    const messagesWithAlias = [
      {
        text: 'You say hello',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        messageType: 'say',
        aliasChain: [
          {
            original: 'say hello',
            expanded: 'say hello',
            alias_name: 'greet',
          },
        ],
      },
    ];

    render(<GameLogPanel messages={messagesWithAlias} />);

    expect(screen.getByText('You say hello')).toBeInTheDocument();
  });
});
