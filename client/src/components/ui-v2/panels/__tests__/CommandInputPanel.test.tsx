/**
 * Tests for CommandInputPanel component.
 */

import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { CommandInputPanel } from '../CommandInputPanel';

describe('CommandInputPanel', () => {
  const mockOnSendCommand = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render command input panel', () => {
    render(<CommandInputPanel onSendCommand={mockOnSendCommand} isConnected={true} />);
    expect(screen.getByPlaceholderText(/Enter game command/i)).toBeInTheDocument();
  });

  it('should call onSendCommand when form is submitted', async () => {
    render(<CommandInputPanel onSendCommand={mockOnSendCommand} isConnected={true} />);

    const input = screen.getByPlaceholderText(/Enter game command/i);
    fireEvent.change(input, { target: { value: 'look' } });
    fireEvent.submit(input.closest('form')!);

    await waitFor(() => {
      expect(mockOnSendCommand).toHaveBeenCalledWith('look');
    });
  });

  it('should not send empty commands', () => {
    render(<CommandInputPanel onSendCommand={mockOnSendCommand} isConnected={true} />);

    const input = screen.getByPlaceholderText(/Enter game command/i);
    fireEvent.change(input, { target: { value: '   ' } });
    fireEvent.submit(input.closest('form')!);

    expect(mockOnSendCommand).not.toHaveBeenCalled();
  });

  it('should not send commands when disabled', () => {
    render(<CommandInputPanel onSendCommand={mockOnSendCommand} disabled={true} isConnected={true} />);

    const input = screen.getByPlaceholderText(/Enter game command/i);
    fireEvent.change(input, { target: { value: 'look' } });
    fireEvent.submit(input.closest('form')!);

    expect(mockOnSendCommand).not.toHaveBeenCalled();
  });

  it('should not send commands when not connected', () => {
    render(<CommandInputPanel onSendCommand={mockOnSendCommand} isConnected={false} />);

    const input = screen.getByPlaceholderText(/Enter game command/i);
    expect(input).toBeDisabled();
    
    fireEvent.change(input, { target: { value: 'look' } });
    fireEvent.submit(input.closest('form')!);

    // Input is disabled, so command should not be sent
    expect(mockOnSendCommand).not.toHaveBeenCalled();
  });

  it('should use custom placeholder when provided', () => {
    render(
      <CommandInputPanel
        onSendCommand={mockOnSendCommand}
        placeholder="Custom placeholder"
        isConnected={true}
      />
    );
    expect(screen.getByPlaceholderText('Custom placeholder')).toBeInTheDocument();
  });

  it('should trim whitespace from commands', async () => {
    render(<CommandInputPanel onSendCommand={mockOnSendCommand} isConnected={true} />);

    const input = screen.getByPlaceholderText(/Enter game command/i);
    fireEvent.change(input, { target: { value: '  look  ' } });
    fireEvent.submit(input.closest('form')!);

    await waitFor(() => {
      expect(mockOnSendCommand).toHaveBeenCalledWith('look');
    });
  });
});
