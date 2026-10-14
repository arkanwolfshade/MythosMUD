// Escape opens the main menu (unless dead or map). Once open, MainMenuModal owns Escape: it steps
// back from a sub-menu (Settings) and closes from the top level, so this must not also toggle it.

import { useEffect } from 'react';

import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';

export function useGameClientV2ContainerEscapeMenuEffect(slice: GameClientV2MergedSlice): void {
  const { showMap, isMainMenuOpen, setIsMainMenuOpen } = slice;
  const isDead = slice.gameState.isDead ?? false;

  useEffect(() => {
    if (isDead || showMap || isMainMenuOpen) return;
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setIsMainMenuOpen(true);
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [isDead, showMap, isMainMenuOpen, setIsMainMenuOpen]);
}
