/**
 * Tests for EdgeDetailsPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { EdgeDetailsPanel } from '../EdgeDetailsPanel';
import type { ExitEdgeData } from '../types';

describe('EdgeDetailsPanel', () => {
  const mockEdge = {
    id: 'edge1',
    source: 'room1',
    target: 'room2',
    data: {
      direction: 'north',
      sourceRoomId: 'room1',
      targetRoomId: 'room2',
      flags: [],
    } as ExitEdgeData,
  };

  const defaultProps = {
    edge: mockEdge,
    onClose: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render edge details', () => {
    render(<EdgeDetailsPanel {...defaultProps} />);
    expect(screen.getByText('Exit Details')).toBeInTheDocument();
    expect(screen.getByText('edge1')).toBeInTheDocument();
    expect(screen.getByText('north')).toBeInTheDocument();
  });

  it('should display source and target room names', () => {
    render(<EdgeDetailsPanel {...defaultProps} sourceRoomName="Room 1" targetRoomName="Room 2" />);
    expect(screen.getByText('Room 1')).toBeInTheDocument();
    expect(screen.getByText('Room 2')).toBeInTheDocument();
  });

  it('should use edge source/target when room names not provided', () => {
    render(<EdgeDetailsPanel {...defaultProps} />);
    expect(screen.getByText('room1')).toBeInTheDocument();
    expect(screen.getByText('room2')).toBeInTheDocument();
  });

  it('should display flags when present', () => {
    const edgeWithFlags = {
      ...mockEdge,
      data: {
        ...mockEdge.data,
        flags: ['hidden', 'locked'],
      },
    };
    render(<EdgeDetailsPanel {...defaultProps} edge={edgeWithFlags} />);
    expect(screen.getByText('hidden')).toBeInTheDocument();
    expect(screen.getByText('locked')).toBeInTheDocument();
  });

  it('should display description when present', () => {
    const edgeWithDescription = {
      ...mockEdge,
      data: {
        ...mockEdge.data,
        description: 'A secret passage',
      },
    };
    render(<EdgeDetailsPanel {...defaultProps} edge={edgeWithDescription} />);
    expect(screen.getByText('A secret passage')).toBeInTheDocument();
  });

  it('should call onClose when close button is clicked', () => {
    const onClose = vi.fn();
    render(<EdgeDetailsPanel {...defaultProps} onClose={onClose} />);
    const closeButton = screen.getByLabelText('Close panel');
    fireEvent.click(closeButton);
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should render admin buttons when isAdmin is true', () => {
    const onDelete = vi.fn();
    const onEdit = vi.fn();
    render(<EdgeDetailsPanel {...defaultProps} isAdmin={true} onDelete={onDelete} onEdit={onEdit} />);
    expect(screen.getByText('Edit Exit')).toBeInTheDocument();
    expect(screen.getByText('Delete Exit')).toBeInTheDocument();
  });

  it('should not render admin buttons when isAdmin is false', () => {
    render(<EdgeDetailsPanel {...defaultProps} isAdmin={false} />);
    expect(screen.queryByText('Edit Exit')).not.toBeInTheDocument();
    expect(screen.queryByText('Delete Exit')).not.toBeInTheDocument();
  });

  it('should show delete confirmation when delete is clicked', () => {
    const onDelete = vi.fn();
    render(<EdgeDetailsPanel {...defaultProps} isAdmin={true} onDelete={onDelete} />);
    const deleteButton = screen.getByText('Delete Exit');
    fireEvent.click(deleteButton);
    expect(screen.getByText(/are you sure/i)).toBeInTheDocument();
  });

  it('should call onDelete when delete is confirmed', () => {
    const onDelete = vi.fn();
    const onClose = vi.fn();
    render(<EdgeDetailsPanel {...defaultProps} isAdmin={true} onDelete={onDelete} onClose={onClose} />);
    const deleteButton = screen.getByText('Delete Exit');
    fireEvent.click(deleteButton);
    const confirmButton = screen.getByText('Confirm Delete');
    fireEvent.click(confirmButton);
    expect(onDelete).toHaveBeenCalledWith('edge1');
    expect(onClose).toHaveBeenCalled();
  });

  it('should cancel delete confirmation', () => {
    const onDelete = vi.fn();
    render(<EdgeDetailsPanel {...defaultProps} isAdmin={true} onDelete={onDelete} />);
    const deleteButton = screen.getByText('Delete Exit');
    fireEvent.click(deleteButton);
    const cancelButton = screen.getByText('Cancel');
    fireEvent.click(cancelButton);
    expect(onDelete).not.toHaveBeenCalled();
    expect(screen.queryByText(/are you sure/i)).not.toBeInTheDocument();
  });

  it('should call onEdit when edit button is clicked', () => {
    const onEdit = vi.fn();
    const onClose = vi.fn();
    render(<EdgeDetailsPanel {...defaultProps} isAdmin={true} onEdit={onEdit} onClose={onClose} />);
    const editButton = screen.getByText('Edit Exit');
    fireEvent.click(editButton);
    expect(onEdit).toHaveBeenCalledWith('edge1');
    expect(onClose).toHaveBeenCalled();
  });
});
