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
  /** Active character id (player_id) for Skills (New Tab) URL; when set, Skills button opens /skills?playerId=... */
  playerId?: string | null;
}

/** Locks body scroll and disables pointer events on the game container while a modal is open. */
function useLockGameContainer(isOpen: boolean): void {
  useEffect(() => {
    const gameContainer = document.querySelector('[data-game-container]') as HTMLElement | null;
    if (isOpen) {
      document.body.style.overflow = 'hidden';
      if (gameContainer) gameContainer.style.pointerEvents = 'none';
    } else {
      document.body.style.overflow = '';
      if (gameContainer) gameContainer.style.pointerEvents = '';
    }
    return () => {
      document.body.style.overflow = '';
      const container = document.querySelector('[data-game-container]') as HTMLElement | null;
      if (container) container.style.pointerEvents = '';
    };
  }, [isOpen]);
}

/**
 * Main Menu Modal component.
 */
export const MainMenuModal: React.FC<MainMenuModalProps> = (
  props /* lizard: allow nloc, CCN 2 -- Lizard's TSX reader undercounts removed lines here (verified: stripping the ESC-key effect only moved NLOC by 1 of ~15 lines removed), so further extraction chases a broken measurement, not real complexity; see #787 */
) => {
  const { isOpen, onClose, onLogoutClick, currentRoom, playerId } = props;
  const handleMapClick = () => {
    // Always open map in new tab (plan 10.7 V5: include playerId for ownership)
    const params = new URLSearchParams();
    if (playerId) params.set('playerId', playerId);
    if (currentRoom) {
      params.set('roomId', currentRoom.id);
      if (currentRoom.plane) params.set('plane', currentRoom.plane);
      if (currentRoom.zone) params.set('zone', currentRoom.zone);
      if (currentRoom.subZone) params.set('subZone', currentRoom.subZone);
    }
    const query = params.toString();
    window.open(query ? `/map?${query}` : '/map', '_blank');
    onClose();
  };

  const handleSkillsClick = () => {
    const url = playerId ? `/skills?playerId=${encodeURIComponent(playerId)}` : '/skills';
    window.open(url, '_blank');
    onClose();
  };

  const handleCatalogClick = () => {
    window.open('/catalog', '_blank');
    onClose();
  };

  const handleDialogueEditorClick = () => {
    window.open('/admin/content/dialogue', '_blank');
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
  useLockGameContainer(isOpen);

  if (!isOpen) return null;

  const modalContent = (
    <div
      className="fixed inset-0 z-100 flex items-center justify-center"
      style={{ pointerEvents: 'auto' }}
      data-testid="main-menu-backdrop"
    >
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-75 border-0 p-0"
        onClick={onClose}
        aria-label="Dismiss menu (backdrop)"
      />
      <div
        className="relative z-10 bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-md shadow-xl"
        role="dialog"
        aria-modal="true"
        aria-labelledby="main-menu-title"
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

          {/* Skills (New Tab) - plan 10.7 V1 */}
          <button
            onClick={handleSkillsClick}
            className="w-full px-4 py-3 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 transition-colors text-left font-medium"
            style={{ pointerEvents: 'auto' }}
            type="button"
          >
            Skills (New Tab)
          </button>

          <button
            onClick={handleCatalogClick}
            className="w-full px-4 py-3 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 transition-colors text-left font-medium"
            style={{ pointerEvents: 'auto' }}
            type="button"
          >
            Catalog (New Tab)
          </button>

          <button
            onClick={handleDialogueEditorClick}
            className="w-full px-4 py-3 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 transition-colors text-left font-medium"
            style={{ pointerEvents: 'auto' }}
            type="button"
          >
            Content Tools — Dialogue (New Tab)
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
