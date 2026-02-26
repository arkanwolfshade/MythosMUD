/**
 * Shared constants and helpers for AsciiMapViewer.
 * Kept in a separate file so AsciiMapViewerViews can export only components (fast refresh).
 */

import React from 'react';

export const VIEWPORT_BUTTON_CLASS =
  'px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-border';

export function createViewportKeyHandler(
  setViewportX: React.Dispatch<React.SetStateAction<number>>,
  setViewportY: React.Dispatch<React.SetStateAction<number>>
): (event: KeyboardEvent) => void {
  return (event: KeyboardEvent) => {
    if (event.target instanceof HTMLInputElement || event.target instanceof HTMLTextAreaElement) {
      return;
    }
    switch (event.key) {
      case 'ArrowUp':
        event.preventDefault();
        setViewportY(prev => prev - 1);
        break;
      case 'ArrowDown':
        event.preventDefault();
        setViewportY(prev => prev + 1);
        break;
      case 'ArrowLeft':
        event.preventDefault();
        setViewportX(prev => prev - 1);
        break;
      case 'ArrowRight':
        event.preventDefault();
        setViewportX(prev => prev + 1);
        break;
      case 'Home':
        event.preventDefault();
        setViewportX(0);
        setViewportY(0);
        break;
    }
  };
}
