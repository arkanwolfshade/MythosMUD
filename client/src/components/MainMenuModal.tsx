/**
 * Main Menu Modal component.
 *
 * A modal dialog accessible via ESC key that provides access to
 * map, logout, and a Settings sub-menu (UI preferences, layout reset).
 *
 * As documented in the Pnakotic Manuscripts, proper access control
 * interfaces are essential for maintaining the integrity of our
 * eldritch architecture.
 */

import React, { useEffect, useState } from 'react';
import { createPortal } from 'react-dom';
import { SettingsToggles } from './SettingsToggles';

export interface MainMenuModalProps {
  /** Whether the modal is open */
  isOpen: boolean;
  /** Callback when modal should close */
  onClose: () => void;
  /** @deprecated Callback when map button is clicked (for in-page modal) - no longer used, always opens in new tab */
  onMapClick?: () => void;
  /** Callback when logout button is clicked */
  onLogoutClick: () => void;
  /** Callback for Settings > Reset UI Layout; the button is hidden when omitted */
  onResetLayoutClick?: () => void;
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

type MenuView = 'main' | 'settings';

const PRIMARY_BUTTON_CLASS =
  'w-full px-4 py-3 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 transition-colors text-left font-medium';
const NEUTRAL_BUTTON_CLASS =
  'w-full px-4 py-3 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface transition-colors text-left font-medium';

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

/** ESC steps back one level (Settings -> Main Menu) and closes the menu from the top level. */
function useMenuEscape(view: MenuView, setView: (view: MenuView) => void, onClose: () => void): void {
  useEffect(() => {
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key !== 'Escape') return;
      if (view === 'settings') setView('main');
      else onClose();
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [view, setView, onClose]);
}

type MainMenuViewProps = Pick<MainMenuModalProps, 'onClose' | 'onLogoutClick' | 'currentRoom' | 'playerId'> & {
  onSettingsClick: () => void;
};

function MainMenuView(props: MainMenuViewProps) {
  const { onClose, onLogoutClick, currentRoom, playerId, onSettingsClick } = props;

  const openInNewTab = (url: string) => {
    window.open(url, '_blank');
    onClose();
  };

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
    openInNewTab(query ? `/map?${query}` : '/map');
  };

  return (
    <div className="space-y-3">
      {/* Map Button */}
      <button onClick={handleMapClick} className={PRIMARY_BUTTON_CLASS} style={{ pointerEvents: 'auto' }} type="button">
        Map (New Tab)
      </button>

      {/* Skills (New Tab) - plan 10.7 V1 */}
      <button
        onClick={() => openInNewTab(playerId ? `/skills?playerId=${encodeURIComponent(playerId)}` : '/skills')}
        className={PRIMARY_BUTTON_CLASS}
        style={{ pointerEvents: 'auto' }}
        type="button"
      >
        Skills (New Tab)
      </button>

      <button
        onClick={() => openInNewTab('/catalog')}
        className={PRIMARY_BUTTON_CLASS}
        style={{ pointerEvents: 'auto' }}
        type="button"
      >
        Catalog (New Tab)
      </button>

      <button
        onClick={() => openInNewTab('/manual')}
        className={PRIMARY_BUTTON_CLASS}
        style={{ pointerEvents: 'auto' }}
        type="button"
      >
        Manual (New Tab)
      </button>

      <button
        onClick={() => openInNewTab('/admin/content/dialogue')}
        className={PRIMARY_BUTTON_CLASS}
        style={{ pointerEvents: 'auto' }}
        type="button"
      >
        Content Tools — Dialogue (New Tab)
      </button>

      <button
        onClick={onSettingsClick}
        className={NEUTRAL_BUTTON_CLASS}
        style={{ pointerEvents: 'auto' }}
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
  );
}

type SettingsViewProps = Pick<MainMenuModalProps, 'onClose' | 'onResetLayoutClick'> & { onBack: () => void };

function SettingsView({ onClose, onResetLayoutClick, onBack }: SettingsViewProps) {
  return (
    <div className="space-y-3">
      <button onClick={onBack} className={NEUTRAL_BUTTON_CLASS} style={{ pointerEvents: 'auto' }} type="button">
        ← Back
      </button>

      {onResetLayoutClick ? (
        <button
          onClick={() => {
            onResetLayoutClick();
            onClose();
          }}
          className={NEUTRAL_BUTTON_CLASS}
          style={{ pointerEvents: 'auto' }}
          type="button"
        >
          Reset UI Layout
        </button>
      ) : null}

      <SettingsToggles />
    </div>
  );
}

/** The open dialog. Mounted only while the menu is open, so `view` resets to 'main' on every open. */
function MainMenuDialog(props: Omit<MainMenuModalProps, 'isOpen'>) {
  const { onClose, onLogoutClick, onResetLayoutClick, currentRoom, playerId } = props;
  const [view, setView] = useState<MenuView>('main');
  useMenuEscape(view, setView, onClose);

  return (
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
        className="relative z-10 bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-md max-h-[90vh] overflow-y-auto shadow-xl"
        role="dialog"
        aria-modal="true"
        aria-labelledby="main-menu-title"
        style={{ pointerEvents: 'auto' }}
      >
        <div className="flex items-center justify-between mb-6">
          <h2 id="main-menu-title" className="text-2xl font-bold text-mythos-terminal-text">
            {view === 'main' ? 'Main Menu' : 'Settings'}
          </h2>
          <button
            type="button"
            onClick={onClose}
            className="text-mythos-terminal-text hover:text-mythos-terminal-error text-2xl leading-none"
            aria-label="Close menu"
          >
            ×
          </button>
        </div>

        {view === 'main' ? (
          <MainMenuView
            onClose={onClose}
            onLogoutClick={onLogoutClick}
            currentRoom={currentRoom}
            playerId={playerId}
            onSettingsClick={() => setView('settings')}
          />
        ) : (
          <SettingsView onClose={onClose} onResetLayoutClick={onResetLayoutClick} onBack={() => setView('main')} />
        )}

        <div className="mt-6 text-xs text-mythos-terminal-text/50 text-center">
          {view === 'main' ? 'Press ESC to close' : 'Press ESC to go back'}
        </div>
      </div>
    </div>
  );
}

/**
 * Main Menu Modal component.
 */
export const MainMenuModal: React.FC<MainMenuModalProps> = props => {
  const { isOpen, ...dialogProps } = props;

  // Prevent body scroll and disable pointer events on game content when modal is open
  useLockGameContainer(isOpen);

  if (!isOpen) return null;

  // Render modal in a portal to ensure it's always on top
  return createPortal(<MainMenuDialog {...dialogProps} />, document.body);
};
