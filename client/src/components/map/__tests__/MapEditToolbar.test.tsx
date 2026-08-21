/**
 * Tests for MapEditToolbar component.
 */

import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { MapEditToolbar } from '../MapEditToolbar';

describe('MapEditToolbar', () => {
  const defaultProps = {
    hasUnsavedChanges: true,
    canUndo: false,
    canRedo: false,
    onUndo: vi.fn(),
    onRedo: vi.fn(),
    onSave: vi.fn(async () => {}),
    onReset: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    // jsdom does not implement window.confirm/alert, so there is nothing for vi.spyOn to wrap --
    // assign stub functions directly instead.
    window.confirm = vi.fn(() => true);
    window.alert = vi.fn();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('should call onSave after the user confirms', async () => {
    const onSave = vi.fn(async () => {});
    render(<MapEditToolbar {...defaultProps} onSave={onSave} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(onSave).toHaveBeenCalledTimes(1);
    });
  });

  it('should not call onSave if the user cancels the confirmation', () => {
    window.confirm = vi.fn(() => false);
    const onSave = vi.fn(async () => {});
    render(<MapEditToolbar {...defaultProps} onSave={onSave} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    expect(onSave).not.toHaveBeenCalled();
  });

  it('should surface the specific error message when save fails (#627)', async () => {
    const onSave = vi.fn(async () => {
      throw new Error('Failed to create exit north from room room1: Exit already exists');
    });
    render(<MapEditToolbar {...defaultProps} onSave={onSave} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(window.alert).toHaveBeenCalledWith('Failed to create exit north from room room1: Exit already exists');
    });
  });

  it('should fall back to a generic message when the thrown value is not an Error', async () => {
    const onSave = vi.fn(async () => {
      throw 'not an Error instance';
    });
    render(<MapEditToolbar {...defaultProps} onSave={onSave} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(window.alert).toHaveBeenCalledWith('Failed to save changes. Please try again.');
    });
  });

  it('should call onSaveFailed to trigger a refetch after a failed save (#627)', async () => {
    const onSaveFailed = vi.fn();
    const onSave = vi.fn(async () => {
      throw new Error('boom');
    });
    render(<MapEditToolbar {...defaultProps} onSave={onSave} onSaveFailed={onSaveFailed} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(onSaveFailed).toHaveBeenCalledTimes(1);
    });
  });

  it('should not call onSaveFailed after a successful save', async () => {
    const onSaveFailed = vi.fn();
    const onSave = vi.fn(async () => {});
    render(<MapEditToolbar {...defaultProps} onSave={onSave} onSaveFailed={onSaveFailed} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(onSave).toHaveBeenCalled();
    });
    expect(onSaveFailed).not.toHaveBeenCalled();
  });

  it('should tolerate a missing onSaveFailed prop', async () => {
    const onSave = vi.fn(async () => {
      throw new Error('boom');
    });
    render(<MapEditToolbar {...defaultProps} onSave={onSave} />);

    fireEvent.click(screen.getByRole('button', { name: /save/i }));

    await waitFor(() => {
      expect(window.alert).toHaveBeenCalled();
    });
  });

  it('should disable save when there are no unsaved changes', () => {
    render(<MapEditToolbar {...defaultProps} hasUnsavedChanges={false} />);
    expect(screen.getByRole('button', { name: /save/i })).toBeDisabled();
  });

  it('should call onUndo/onRedo/onReset', () => {
    const onUndo = vi.fn();
    const onRedo = vi.fn();
    const onReset = vi.fn();
    render(
      <MapEditToolbar
        {...defaultProps}
        canUndo={true}
        canRedo={true}
        onUndo={onUndo}
        onRedo={onRedo}
        onReset={onReset}
      />
    );

    fireEvent.click(screen.getByText(/undo/i));
    fireEvent.click(screen.getByText(/redo/i));
    fireEvent.click(screen.getByText(/reset/i));

    expect(onUndo).toHaveBeenCalledTimes(1);
    expect(onRedo).toHaveBeenCalledTimes(1);
    expect(onReset).toHaveBeenCalledTimes(1);
  });
});
