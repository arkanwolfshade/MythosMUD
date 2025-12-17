/**
 * Tests for RoomEditModal component.
 */

import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { Room } from '../../../stores/gameStore';
import { RoomEditModal } from '../RoomEditModal';

describe('RoomEditModal', () => {
  const mockRoom: Room = {
    id: 'room1',
    name: 'Test Room',
    description: 'A test room',
    plane: 'earth',
    zone: 'arkhamcity',
    sub_zone: 'campus',
    environment: 'indoors',
    exits: {},
  };

  const mockOnUpdate = vi.fn();
  const mockOnClose = vi.fn();

  const defaultProps = {
    isOpen: true,
    onClose: mockOnClose,
    room: mockRoom,
    onUpdate: mockOnUpdate,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render when open', () => {
    render(<RoomEditModal {...defaultProps} />);
    expect(screen.getByText(/edit room/i)).toBeInTheDocument();
  });

  it('should not render when closed', () => {
    render(<RoomEditModal {...defaultProps} isOpen={false} />);
    expect(screen.queryByText(/edit room/i)).not.toBeInTheDocument();
  });

  it('should display room name in form', () => {
    render(<RoomEditModal {...defaultProps} />);
    const nameInput = screen.getByDisplayValue('Test Room') as HTMLInputElement;
    expect(nameInput).toBeInTheDocument();
  });

  it('should display room description in form', () => {
    render(<RoomEditModal {...defaultProps} />);
    const descInput = screen.getByDisplayValue('A test room') as HTMLTextAreaElement;
    expect(descInput).toBeInTheDocument();
  });

  it('should allow editing room name', () => {
    render(<RoomEditModal {...defaultProps} />);
    const nameInput = screen.getByDisplayValue('Test Room') as HTMLInputElement;
    fireEvent.change(nameInput, { target: { value: 'Updated Room' } });
    expect(nameInput.value).toBe('Updated Room');
  });

  it('should allow switching tabs', () => {
    render(<RoomEditModal {...defaultProps} />);
    const locationTab = screen.getByText(/location/i);
    fireEvent.click(locationTab);
    expect(screen.getByText(/location/i)).toBeInTheDocument();
  });

  it('should call onUpdate when form is submitted', async () => {
    render(<RoomEditModal {...defaultProps} />);

    const nameInput = screen.getByDisplayValue('Test Room') as HTMLInputElement;
    fireEvent.change(nameInput, { target: { value: 'Updated Room' } });

    const saveButton = screen.getByText(/update room/i);
    fireEvent.click(saveButton);

    await waitFor(() => {
      expect(mockOnUpdate).toHaveBeenCalled();
    });
  });

  it('should call onClose when cancel button is clicked', () => {
    render(<RoomEditModal {...defaultProps} />);
    const cancelButton = screen.getByText(/cancel/i);
    fireEvent.click(cancelButton);
    expect(mockOnClose).toHaveBeenCalledTimes(1);
  });

  it('should reset form when room changes', () => {
    const { rerender } = render(<RoomEditModal {...defaultProps} />);

    const nameInput = screen.getByDisplayValue('Test Room') as HTMLInputElement;
    fireEvent.change(nameInput, { target: { value: 'Changed' } });

    const newRoom: Room = {
      ...mockRoom,
      name: 'New Room',
    };

    rerender(<RoomEditModal {...defaultProps} room={newRoom} />);

    const updatedNameInput = screen.getByDisplayValue('New Room') as HTMLInputElement;
    expect(updatedNameInput).toBeInTheDocument();
  });
});
