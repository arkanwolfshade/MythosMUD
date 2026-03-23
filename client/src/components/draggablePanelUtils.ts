import type React from 'react';

export const PANEL_DRAG_BLOCK_SELECTORS = ['button', '[role="button"]', '.terminal-button', 'input', 'select'] as const;

// Helper function to convert relative position (0-1) to absolute pixels
export const relativeToAbsolute = (
  relative: { x: number; y: number },
  viewportWidth: number,
  viewportHeight: number
): { x: number; y: number } => {
  // If values are > 1, treat as absolute pixels; otherwise treat as percentage (0-1)
  const x = relative.x > 1 ? relative.x : relative.x * viewportWidth;
  const y = relative.y > 1 ? relative.y : relative.y * viewportHeight;
  return { x: Math.round(x), y: Math.round(y) };
};

// Helper function to convert relative size (0-1) to absolute pixels
export const relativeSizeToAbsolute = (
  relative: { width: number; height: number },
  viewportWidth: number,
  viewportHeight: number
): { width: number; height: number } => {
  // If values are > 1, treat as absolute pixels; otherwise treat as percentage (0-1)
  const width = relative.width > 1 ? relative.width : relative.width * viewportWidth;
  const height = relative.height > 1 ? relative.height : relative.height * viewportHeight;
  return { width: Math.round(width), height: Math.round(height) };
};

/** True when the event target is a control that must not start a panel drag. */
export function isPanelDragBlockedTarget(target: HTMLElement): boolean {
  for (const selector of PANEL_DRAG_BLOCK_SELECTORS) {
    if (target.closest(selector)) {
      return true;
    }
  }
  return false;
}

export function isMouseEventOnHeader(e: React.MouseEvent, headerEl: HTMLDivElement | null): boolean {
  if (!headerEl) {
    return false;
  }
  return e.target === headerEl || headerEl.contains(e.target as Node);
}
