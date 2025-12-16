/**
 * Tests for EdgeCreationModal component.
 */

import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { EdgeCreationModal } from '../EdgeCreationModal';
import type { EdgeCreationData, EdgeValidationResult } from '../hooks/useMapEditing';
import type { RoomNodeData } from '../types';

describe('EdgeCreationModal', () => {
  const mockNodes = [
    {
      id: 'room1',
      type: 'room',
      position: { x: 0, y: 0 },
      data: { id: 'room1', name: 'Room 1' } as RoomNodeData,
    },
    {
      id: 'room2',
      type: 'room',
      position: { x: 100, y: 100 },
      data: { id: 'room2', name: 'Room 2' } as RoomNodeData,
    },
  ];

  const mockOnCreate = vi.fn();
  const mockOnValidate = vi.fn(() => ({ isValid: true, errors: [], warnings: [] }));
  const mockOnClose = vi.fn();

  const defaultProps = {
    isOpen: true,
    onClose: mockOnClose,
    sourceRoomId: 'room1',
    availableNodes: mockNodes,
    availableDirections: ['north', 'south', 'east', 'west'],
    validation: null,
    onCreate: mockOnCreate,
    onValidate: mockOnValidate,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render when open', () => {
    render(<EdgeCreationModal {...defaultProps} />);
    expect(screen.getByRole('dialog')).toBeInTheDocument();
    expect(screen.getByRole('heading', { name: /create exit/i })).toBeInTheDocument();
  });

  it('should not render when closed', () => {
    const { container } = render(<EdgeCreationModal {...defaultProps} isOpen={false} />);
    expect(container.firstChild).toBeNull();
  });

  it('should call onClose when close button is clicked', () => {
    render(<EdgeCreationModal {...defaultProps} />);
    const closeButton = screen.getByLabelText('Close dialog');
    fireEvent.click(closeButton);
    expect(mockOnClose).toHaveBeenCalledTimes(1);
  });

  it('should display source room', () => {
    render(<EdgeCreationModal {...defaultProps} />);
    expect(screen.getByText(/Room 1/i)).toBeInTheDocument();
  });

  it('should allow selecting target room', () => {
    render(<EdgeCreationModal {...defaultProps} />);
    const targetSelect = screen.getByLabelText(/To Room:/i) as HTMLSelectElement;
    expect(targetSelect).toBeInTheDocument();
  });

  it('should allow selecting direction', () => {
    render(<EdgeCreationModal {...defaultProps} />);
    const directionLabel = screen.getByText(/Direction:/i);
    expect(directionLabel).toBeInTheDocument();
  });

  it('should call onCreate when form is submitted with valid data', async () => {
    const mockOnValidateValid = vi.fn(() => ({ isValid: true, errors: [], warnings: [] }));
    render(
      <EdgeCreationModal
        {...defaultProps}
        onValidate={mockOnValidateValid}
        validation={{ isValid: true, errors: [], warnings: [] }}
      />
    );

    // Fill in form fields
    const targetSelect = screen.getByLabelText(/To Room:/i) as HTMLSelectElement;
    fireEvent.change(targetSelect, { target: { value: 'room2' } });

    // Fill direction
    const directionLabel = screen.getByText(/Direction:/i);
    const directionSelect = directionLabel.parentElement?.querySelector('select') as HTMLSelectElement;
    if (directionSelect) {
      fireEvent.change(directionSelect, { target: { value: 'north' } });
    }
      fireEvent.change(directionSelect, { target: { value: 'north' } });
    // Wait for validation
    await waitFor(() => {
      expect(mockOnValidateValid).toHaveBeenCalled();
    });

    // Submit form
    const submitButton = screen.getByRole('button', { name: /create exit/i });
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(mockOnCreate).toHaveBeenCalled();
    });
  });

  it('should display validation errors', () => {
    const validation: EdgeValidationResult = {
      isValid: false,
      errors: ['Target room is required'],
      warnings: [],
    };

    render(<EdgeCreationModal {...defaultProps} validation={validation} />);
    expect(screen.getByText('Target room is required')).toBeInTheDocument();
  });

  it('should handle edit mode when existingEdge is provided', () => {
    const existingEdge: EdgeCreationData & { edgeId: string } = {
      edgeId: 'edge1',
      sourceRoomId: 'room1',
      targetRoomId: 'room2',
      direction: 'north',
    };

    const mockOnUpdate = vi.fn();
    render(<EdgeCreationModal {...defaultProps} existingEdge={existingEdge} onUpdate={mockOnUpdate} />);
    // In edit mode, title might change or target room should be disabled
    const targetSelect = screen.getByLabelText(/To Room:/i) as HTMLSelectElement;
    expect(targetSelect.disabled).toBe(true);
  });
});
