/**
 * Main Menu Modal component.
 *
 * A modal dialog accessible via ESC key that provides access to
 * map, logout, and settings (placeholder) functionality.
 *
 * As documented in the Pnakotic Manuscripts, proper access control
 * interfaces are essential for maintaining the integrity of our
 * eldritch architecture.
 */

import React, { useEffect } from 'react';
import { createPortal } from 'react-dom';

export interface MainMenuModalProps {
  /** Whether the modal is open */
  isOpen: boolean;
  /** Callback when modal should close */
  onClose: () => void;
  /** @deprecated Callback when map button is clicked (for in-page modal) - no longer used, always opens in new tab */
  onMapClick?: () => void;
  /** Callback when logout button is clicked */
  onLogoutClick: () => void;
  /** Current room information (if provided, map opens in new tab) */
  currentRoom?: {
    id: string;
    plane?: string;
    zone?: string;
    subZone?: string;
  } | null;
  /** @deprecated Always opens in new tab now */
  openMapInNewTab?: boolean;
}

/**
 * Main Menu Modal component.
 */
export const MainMenuModal: React.FC<MainMenuModalProps> = ({ isOpen, onClose, onLogoutClick, currentRoom }) => {
  const handleMapClick = () => {
    // Always open map in new tab
    if (currentRoom) {
      // Build URL with room parameters
      const params = new URLSearchParams();
      params.set('roomId', currentRoom.id);
      if (currentRoom.plane) params.set('plane', currentRoom.plane);
      if (currentRoom.zone) params.set('zone', currentRoom.zone);
      if (currentRoom.subZone) params.set('subZone', currentRoom.subZone);

      // Open map in new tab
      window.open(`/map?${params.toString()}`, '_blank');
    } else {
      // Fallback: open in new tab without room info
      window.open('/map', '_blank');
    }
    onClose();
  };
  // Handle ESC key to close modal
  useEffect(() => {
    if (!isOpen) return;

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isOpen, onClose]);

  // Prevent body scroll and disable pointer events on game content when modal is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
      // Disable pointer events on the main game container to prevent panel dragging
      const gameContainer = document.querySelector('[data-game-container]');
      if (gameContainer) {
        (gameContainer as HTMLElement).style.pointerEvents = 'none';
      }
    } else {
      document.body.style.overflow = '';
      // Re-enable pointer events on the main game container
      const gameContainer = document.querySelector('[data-game-container]');
      if (gameContainer) {
        (gameContainer as HTMLElement).style.pointerEvents = '';
      }
    }
    return () => {
      document.body.style.overflow = '';
      const gameContainer = document.querySelector('[data-game-container]');
      if (gameContainer) {
        (gameContainer as HTMLElement).style.pointerEvents = '';
      }
    };
  }, [isOpen]);

  if (!isOpen) return null;

  const modalContent = (
    <div
      className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-100"
      onClick={onClose}
      style={{ pointerEvents: 'auto' }}
      data-testid="main-menu-backdrop"
    >
      <div
        className="bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-md shadow-xl"
        role="dialog"
        aria-modal="true"
        aria-labelledby="main-menu-title"
        onClick={e => {
          e.stopPropagation();
        }}
        style={{ pointerEvents: 'auto' }}
      >
        <div className="flex items-center justify-between mb-6">
          <h2 id="main-menu-title" className="text-2xl font-bold text-mythos-terminal-text">
            Main Menu
          </h2>
          <button
            onClick={onClose}
            className="text-mythos-terminal-text hover:text-mythos-terminal-error text-2xl leading-none"
            aria-label="Close menu"
          >
            ×
          </button>
        </div>

        <div className="space-y-3">
          {/* Map Button */}
          <button
            onClick={handleMapClick}
            className="w-full px-4 py-3 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 transition-colors text-left font-medium"
            style={{ pointerEvents: 'auto' }}
            type="button"
          >
            Map (New Tab)
          </button>

          {/* Settings Button (Placeholder - Inactive) */}
          <button
            disabled
            className="w-full px-4 py-3 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text/50 rounded cursor-not-allowed text-left font-medium opacity-50"
            aria-label="Settings (coming soon)"
            type="button"
          >
            Settings
          </button>

          {/* Logout Button */}
          <button
            onClick={() => {
              onLogoutClick();
              onClose();
            }}
            className="w-full px-4 py-3 bg-mythos-terminal-error text-white rounded hover:bg-mythos-terminal-error/80 transition-colors text-left font-medium"
            style={{ pointerEvents: 'auto' }}
            type="button"
          >
            Logout
          </button>
        </div>

        <div className="mt-6 text-xs text-mythos-terminal-text/50 text-center">Press ESC to close</div>
      </div>
    </div>
  );

  // Render modal in a portal to ensure it's always on top
  return createPortal(modalContent, document.body);
};
