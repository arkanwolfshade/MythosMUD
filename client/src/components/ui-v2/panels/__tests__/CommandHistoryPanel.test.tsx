/**
 * Tests for CommandHistoryPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { CommandHistoryPanel } from '../CommandHistoryPanel';

describe('CommandHistoryPanel', () => {
  const mockOnClearHistory = vi.fn();
  const mockOnSelectCommand = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render command history panel', () => {
    render(<CommandHistoryPanel commandHistory={[]} />);
    expect(screen.getByText('Command History')).toBeInTheDocument();
  });

  it('should display "No commands yet" when history is empty', () => {
    render(<CommandHistoryPanel commandHistory={[]} />);
    expect(screen.getByText('No commands yet')).toBeInTheDocument();
  });

  it('should display command history', () => {
    const history = ['look', 'inventory', 'go north'];
    render(<CommandHistoryPanel commandHistory={history} />);

    expect(screen.getByText('look')).toBeInTheDocument();
    expect(screen.getByText('inventory')).toBeInTheDocument();
    expect(screen.getByText('go north')).toBeInTheDocument();
  });

  it('should display only last 10 commands', () => {
    const history = Array.from({ length: 15 }, (_, i) => `command${i}`);
    render(<CommandHistoryPanel commandHistory={history} />);

    // Should show last 10 commands (indices 5-14)
    expect(screen.getByText('command5')).toBeInTheDocument();
    expect(screen.getByText('command14')).toBeInTheDocument();
    expect(screen.queryByText('command0')).not.toBeInTheDocument();
    expect(screen.queryByText('command4')).not.toBeInTheDocument();
  });

  it('should call onClearHistory when clear button is clicked', () => {
    const history = ['look', 'inventory'];
    render(<CommandHistoryPanel commandHistory={history} onClearHistory={mockOnClearHistory} />);

    const clearButton = screen.getByRole('button', { name: /clear/i });
    fireEvent.click(clearButton);

    expect(mockOnClearHistory).toHaveBeenCalled();
  });

  it('should not show clear button when history is empty', () => {
    render(<CommandHistoryPanel commandHistory={[]} onClearHistory={mockOnClearHistory} />);
    expect(screen.queryByRole('button', { name: /clear/i })).not.toBeInTheDocument();
  });

  it('should call onSelectCommand when command is clicked', () => {
    const history = ['look', 'inventory'];
    render(<CommandHistoryPanel commandHistory={history} onSelectCommand={mockOnSelectCommand} />);

    const commandElement = screen.getByText('look');
    fireEvent.click(commandElement);

    expect(mockOnSelectCommand).toHaveBeenCalledWith('look');
  });

  it('should display commands in reverse order (newest first)', () => {
    const history = ['command1', 'command2', 'command3'];
    render(<CommandHistoryPanel commandHistory={history} />);

    const commands = screen.getAllByText(/command\d/);
    // Commands should be displayed in reverse order
    expect(commands[0].textContent).toBe('command3');
    expect(commands[commands.length - 1].textContent).toBe('command1');
  });
});
