/**
 * Tests for GameInfoPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../types';
import { GameInfoPanel } from '../GameInfoPanel';

describe('GameInfoPanel', () => {
  const mockOnClearMessages = vi.fn();
  const mockOnDownloadLogs = vi.fn();

  const mockMessages: ChatMessage[] = [
    {
      text: 'System message',
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: 'system',
      channel: 'system',
      type: 'system',
    },
    {
      text: 'Combat message',
      timestamp: new Date().toISOString(),
      isHtml: false,
      messageType: 'combat',
      channel: 'game',
      type: 'system',
    },
  ];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render game info panel', () => {
    render(<GameInfoPanel messages={mockMessages} />);
    expect(screen.getByText('System message')).toBeInTheDocument();
  });

  it('should display all messages by default', () => {
    render(<GameInfoPanel messages={mockMessages} />);
    expect(screen.getByText('System message')).toBeInTheDocument();
    expect(screen.getByText('Combat message')).toBeInTheDocument();
  });

  it('renders a complete-HTML message as real markup, not escaped text (help output)', () => {
    const help: ChatMessage[] = [
      {
        text: '<div class="help-entry"><p><strong>LOOK</strong></p></div>',
        timestamp: new Date().toISOString(),
        isHtml: true,
        isCompleteHtml: true,
        messageType: 'system',
        channel: 'game',
        type: 'system',
      },
    ];

    const { container } = render(<GameInfoPanel messages={help} />);

    expect(container.querySelector('.help-entry strong')?.textContent).toBe('LOOK');
    expect(screen.queryByText(/<strong>/)).not.toBeInTheDocument();
  });

  it('still treats isHtml text that is not marked complete as ANSI text, escaping its markup', () => {
    const ansiText: ChatMessage[] = [
      {
        text: '<strong>LOOK</strong>',
        timestamp: new Date().toISOString(),
        isHtml: true,
        messageType: 'system',
        channel: 'game',
        type: 'system',
      },
    ];

    const { container } = render(<GameInfoPanel messages={ansiText} />);

    expect(container.querySelector('strong')).toBeNull();
    expect(screen.getByText(/<strong>LOOK<\/strong>/)).toBeInTheDocument();
  });

  it('should call onClearMessages when clear button is clicked', () => {
    render(<GameInfoPanel messages={mockMessages} onClearMessages={mockOnClearMessages} />);

    const clearLogButton = screen.getByRole('button', { name: /clear log/i });
    fireEvent.click(clearLogButton);

    expect(mockOnClearMessages).toHaveBeenCalled();
  });

  it('should call onDownloadLogs when download button is clicked', () => {
    render(<GameInfoPanel messages={mockMessages} onDownloadLogs={mockOnDownloadLogs} />);

    const downloadButton = screen.getByRole('button', { name: /download/i });
    fireEvent.click(downloadButton);

    expect(mockOnDownloadLogs).toHaveBeenCalled();
  });

  it('should handle empty messages array', () => {
    render(<GameInfoPanel messages={[]} />);
    // Should render without errors
    expect(screen.queryByText('System message')).not.toBeInTheDocument();
  });

  it('should filter messages by type', () => {
    render(<GameInfoPanel messages={mockMessages} />);

    const filterSelect = screen.getByRole('combobox');
    fireEvent.change(filterSelect, { target: { value: 'system' } });

    expect(screen.getByText('System message')).toBeInTheDocument();
    expect(screen.queryByText('Combat message')).not.toBeInTheDocument();
  });

  it('should filter messages by search query', () => {
    render(<GameInfoPanel messages={mockMessages} />);

    const searchInput = screen.getByPlaceholderText(/search/i);
    fireEvent.change(searchInput, { target: { value: 'System' } });

    expect(screen.getByText('System message')).toBeInTheDocument();
    expect(screen.queryByText('Combat message')).not.toBeInTheDocument();
  });

  it('should show combat header affordances when inCombat is true', () => {
    render(<GameInfoPanel messages={mockMessages} inCombat />);
    expect(screen.getByTestId('game-info-combat-indicator')).toBeInTheDocument();
    expect(screen.getByTestId('game-info-combat-label')).toHaveTextContent('In combat');
  });

  it('should show local and say chat in Game Info for multiplayer E2E', () => {
    const chatMessages: ChatMessage[] = [
      {
        text: 'ArkanWolfshade (local): Hello',
        timestamp: new Date().toISOString(),
        isHtml: false,
        messageType: 'chat',
        channel: 'local',
        type: 'say',
      },
      {
        text: 'ArkanWolfshade says: Hi',
        timestamp: new Date().toISOString(),
        isHtml: false,
        messageType: 'chat',
        channel: 'say',
        type: 'say',
      },
      {
        text: 'Global channel line',
        timestamp: new Date().toISOString(),
        isHtml: false,
        messageType: 'chat',
        channel: 'global',
        type: 'say',
      },
    ];
    render(<GameInfoPanel messages={chatMessages} />);
    expect(screen.getByText('ArkanWolfshade (local): Hello')).toBeInTheDocument();
    expect(screen.getByText('ArkanWolfshade says: Hi')).toBeInTheDocument();
    expect(screen.queryByText('Global channel line')).not.toBeInTheDocument();
  });
});
