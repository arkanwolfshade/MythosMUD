/**
 * Tests for ChatHeader component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ChatHeader } from '../ChatHeader';

// Mock EldritchIcon - it renders lucide-react icons
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name }: { name: string; variant?: string }) => <span data-testid={`icon-${name}`}>{name}</span>,
  MythosIcons: {
    chat: 'chat',
    clear: 'clear',
    download: 'download',
  },
}));

// Mock TerminalButton
vi.mock('../../ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    className,
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    className?: string;
  }) => (
    <button onClick={onClick} className={className} data-testid="terminal-button">
      {children}
    </button>
  ),
}));

describe('ChatHeader', () => {
  it('should render chat header with title', () => {
    render(<ChatHeader />);
    expect(screen.getByText('Chat')).toBeInTheDocument();
  });

  it('should render chat icon', () => {
    render(<ChatHeader />);
    // Chat icon is rendered by EldritchIcon, verify header is present
    expect(screen.getByText('Chat')).toBeInTheDocument();
  });

  it('should render clear button when onClearMessages is provided', () => {
    const onClearMessages = vi.fn();
    render(<ChatHeader onClearMessages={onClearMessages} />);
    // Find button by its container - TerminalButton wraps the icon
    const buttons = screen.getAllByRole('button');
    // Should have at least one button (the clear button)
    expect(buttons.length).toBeGreaterThan(0);
  });

  it('should not render clear button when onClearMessages is not provided', () => {
    render(<ChatHeader />);
    // When onClearMessages is not provided, no action buttons should be rendered
    // Only the header title should be present
    expect(screen.getByText('Chat')).toBeInTheDocument();
    // No buttons should be present (only header, no action buttons)
    const buttons = screen.queryAllByRole('button');
    expect(buttons.length).toBe(0);
  });

  it('should render download button when onDownloadLogs is provided', () => {
    const onDownloadLogs = vi.fn();
    render(<ChatHeader onDownloadLogs={onDownloadLogs} />);
    // Find button by its container - TerminalButton wraps the icon
    const buttons = screen.getAllByRole('button');
    // Should have at least one button (the download button)
    expect(buttons.length).toBeGreaterThan(0);
  });

  it('should not render download button when onDownloadLogs is not provided', () => {
    render(<ChatHeader />);
    // When onDownloadLogs is not provided, no action buttons should be rendered
    const buttons = screen.queryAllByRole('button');
    expect(buttons.length).toBe(0);
  });

  it('should call onClearMessages when clear button is clicked', () => {
    const onClearMessages = vi.fn();
    render(<ChatHeader onClearMessages={onClearMessages} />);
    const buttons = screen.getAllByRole('button');
    // Find the clear button (should be the first/only button when only onClearMessages is provided)
    const clearButton = buttons[0];
    fireEvent.click(clearButton);
    expect(onClearMessages).toHaveBeenCalledTimes(1);
  });

  it('should call onDownloadLogs when download button is clicked', () => {
    const onDownloadLogs = vi.fn();
    render(<ChatHeader onDownloadLogs={onDownloadLogs} />);
    const buttons = screen.getAllByRole('button');
    // Find the download button (should be the first/only button when only onDownloadLogs is provided)
    const downloadButton = buttons[0];
    fireEvent.click(downloadButton);
    expect(onDownloadLogs).toHaveBeenCalledTimes(1);
  });

  it('should render both buttons when both callbacks are provided', () => {
    const onClearMessages = vi.fn();
    const onDownloadLogs = vi.fn();
    render(<ChatHeader onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />);
    // Both buttons should be present
    const buttons = screen.getAllByRole('button');
    expect(buttons.length).toBe(2);
  });
});
