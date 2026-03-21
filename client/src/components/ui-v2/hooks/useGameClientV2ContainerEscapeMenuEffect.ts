// Escape toggles main menu (unless dead or map).

import { useEffect } from 'react';

import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';

export function useGameClientV2ContainerEscapeMenuEffect(slice: GameClientV2MergedSlice): void {
  const { isDead, showMap, setIsMainMenuOpen } = slice;

  useEffect(() => {
    if (isDead || showMap) return;
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setIsMainMenuOpen(prev => !prev);
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [isDead, showMap, setIsMainMenuOpen]);
}
