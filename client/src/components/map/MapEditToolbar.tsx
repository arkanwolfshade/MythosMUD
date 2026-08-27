/**
 * Map Edit Toolbar component.
 *
 * Provides admin editing controls including undo/redo, save, and reset.
 *
 * As noted in the Cultes des Goules, proper control interfaces are
 * essential for managing dimensional modifications.
 */

import React, { useState, useCallback } from 'react';

export interface MapEditToolbarProps {
  /** Whether there are unsaved changes */
  hasUnsavedChanges: boolean;
  /** Whether undo is available */
  canUndo: boolean;
  /** Whether redo is available */
  canRedo: boolean;
  /** Callback for undo */
  onUndo: () => void;
  /** Callback for redo */
  onRedo: () => void;
  /** Callback for save */
  onSave: () => Promise<void>;
  /** Callback for reset */
  onReset: () => void;
  /**
   * Called after a save fails, so the caller can refetch server state -- a partial save may have
   * landed some writes before failing (see saveMapChanges.ts's sequential delete/create/update
   * ordering), and local optimistic state no longer reflects the truth. See #627.
   */
  onSaveFailed?: () => void;
  /**
   * Callback for admin coordinate recalculation. Omit to hide the button entirely -- ported from
   * the legacy AsciiMapEditor (#693), which was the endpoint's only client.
   */
  onRecalculate?: () => Promise<void>;
}

/**
 * Map Edit Toolbar component.
 */
export const MapEditToolbar: React.FC<MapEditToolbarProps> = ({
  hasUnsavedChanges,
  canUndo,
  canRedo,
  onUndo,
  onRedo,
  onSave,
  onReset,
  onSaveFailed,
  onRecalculate,
}) => {
  const [isSaving, setIsSaving] = useState(false);
  const [isRecalculating, setIsRecalculating] = useState(false);

  const handleSave = useCallback(async () => {
    if (!hasUnsavedChanges) return;

    const confirmed = window.confirm(
      'Are you sure you want to save all changes? This will update the map layout in the database.'
    );

    if (!confirmed) return;

    setIsSaving(true);
    try {
      await onSave();
    } catch (error) {
      console.error('Failed to save:', error);
      const message = error instanceof Error ? error.message : 'Failed to save changes. Please try again.';
      alert(message);
      // A partial save may have landed some writes before failing -- refetch so the UI reflects
      // server truth rather than the optimistic local state.
      onSaveFailed?.();
    } finally {
      setIsSaving(false);
    }
  }, [hasUnsavedChanges, onSave, onSaveFailed]);

  const handleReset = useCallback(() => {
    if (!hasUnsavedChanges) return;

    const confirmed = window.confirm(
      'Are you sure you want to reset all changes? This will discard all unsaved modifications.'
    );

    if (!confirmed) return;

    onReset();
  }, [hasUnsavedChanges, onReset]);

  const handleRecalculate = useCallback(async () => {
    if (!onRecalculate) return;

    setIsRecalculating(true);
    try {
      await onRecalculate();
    } catch (error) {
      console.error('Failed to recalculate coordinates:', error);
      const message = error instanceof Error ? error.message : 'Failed to recalculate coordinates. Please try again.';
      alert(message);
    } finally {
      setIsRecalculating(false);
    }
  }, [onRecalculate]);

  return (
    <div className="flex flex-col gap-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded p-2 shadow-lg">
      {/* Unsaved changes indicator */}
      {hasUnsavedChanges && <div className="text-xs text-yellow-400 mb-2 text-center">⚠ Unsaved changes</div>}

      {/* Undo/Redo buttons */}
      <div className="flex gap-2">
        <button
          onClick={onUndo}
          disabled={!canUndo}
          className="px-3 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm hover:bg-mythos-terminal-surface disabled:opacity-50 disabled:cursor-not-allowed"
          title="Undo (Ctrl+Z)"
        >
          ↶ Undo
        </button>
        <button
          onClick={onRedo}
          disabled={!canRedo}
          className="px-3 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm hover:bg-mythos-terminal-surface disabled:opacity-50 disabled:cursor-not-allowed"
          title="Redo (Ctrl+Y)"
        >
          ↷ Redo
        </button>
      </div>

      {/* Save button */}
      <button
        onClick={handleSave}
        disabled={!hasUnsavedChanges || isSaving}
        className="px-3 py-1 bg-mythos-terminal-primary text-white rounded text-sm hover:bg-mythos-terminal-primary/80 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {isSaving ? 'Saving...' : '💾 Save'}
      </button>

      {/* Reset button */}
      <button
        onClick={handleReset}
        disabled={!hasUnsavedChanges}
        className="px-3 py-1 bg-mythos-terminal-error text-white rounded text-sm hover:bg-mythos-terminal-error/80 disabled:opacity-50 disabled:cursor-not-allowed"
      >
        ↺ Reset
      </button>

      {/* Recalculate coordinates button */}
      {onRecalculate && (
        <button
          onClick={handleRecalculate}
          disabled={isRecalculating}
          className="px-3 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm hover:bg-mythos-terminal-surface disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {isRecalculating ? 'Recalculating...' : '⟳ Recalculate Coordinates'}
        </button>
      )}
    </div>
  );
};
