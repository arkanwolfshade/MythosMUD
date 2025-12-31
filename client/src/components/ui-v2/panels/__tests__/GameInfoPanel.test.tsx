/**
 * Tests for GameInfoPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { GameInfoPanel } from '../GameInfoPanel';
import type { ChatMessage } from '../../types';

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
});
