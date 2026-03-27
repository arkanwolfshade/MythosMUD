/**
 * Clamp persisted panel layouts into the current viewport so a layout saved on a
 * larger display is migrated instead of discarded (see PanelManager init).
 */

import type { PanelState } from '../types';

export const PANEL_VIEWPORT_PADDING = 40;

/** Same bounds check as the former inline helper in PanelManager. */
export function layoutFitsViewport(
  panels: Record<string, PanelState>,
  viewportWidth: number,
  viewportHeight: number,
  padding: number = PANEL_VIEWPORT_PADDING
): boolean {
  const maxRight = viewportWidth - padding;
  const maxBottom = viewportHeight - padding;
  return Object.values(panels).every(
    p =>
      p.position.x >= -padding &&
      p.position.y >= 0 &&
      p.position.x + p.size.width <= maxRight &&
      p.position.y + p.size.height <= maxBottom
  );
}

/**
 * Adjust position and size so every panel fits within padded viewport bounds.
 * Preserves minSize / minHeight when the viewport allows.
 */
export function clampPanelLayoutToViewport(
  panels: Record<string, PanelState>,
  viewportWidth: number,
  viewportHeight: number,
  padding: number = PANEL_VIEWPORT_PADDING
): Record<string, PanelState> {
  const result: Record<string, PanelState> = {};
  for (const [id, panel] of Object.entries(panels)) {
    result[id] = clampSinglePanel(panel, viewportWidth, viewportHeight, padding);
  }
  return result;
}

function applyOptionalContentMinHeight(height: number, maxHFit: number, contentMinH: number | undefined): number {
  if (contentMinH == null || height >= contentMinH || maxHFit < contentMinH) {
    return height;
  }
  return Math.min(contentMinH, maxHFit);
}

function clampDimensionsToViewport(
  panel: PanelState,
  maxWFit: number,
  maxHFit: number
): { width: number; height: number } {
  const minW = panel.minSize?.width ?? 200;
  const minH = panel.minSize?.height ?? 150;

  let w = Math.min(panel.size.width, maxWFit);
  let h = Math.min(panel.size.height, maxHFit);

  w = Math.max(w, Math.min(minW, maxWFit));
  h = Math.max(h, Math.min(minH, maxHFit));
  h = applyOptionalContentMinHeight(h, maxHFit, panel.minHeight);

  return { width: w, height: h };
}

function clampTopLeftWithinBounds(
  x: number,
  y: number,
  width: number,
  height: number,
  minX: number,
  minY: number,
  maxRight: number,
  maxBottom: number
): { x: number; y: number; width: number; height: number } {
  let w = width;
  let h = height;
  const cx = Math.max(minX, Math.min(x, maxRight - w));
  const cy = Math.max(minY, Math.min(y, maxBottom - h));

  if (cx + w > maxRight) {
    w = Math.max(1, maxRight - cx);
  }
  if (cy + h > maxBottom) {
    h = Math.max(1, maxBottom - cy);
  }

  return { x: cx, y: cy, width: w, height: h };
}

function clampSinglePanel(
  panel: PanelState,
  viewportWidth: number,
  viewportHeight: number,
  padding: number
): PanelState {
  const maxRight = viewportWidth - padding;
  const maxBottom = viewportHeight - padding;
  const minX = -padding;
  const minY = 0;

  const maxWFit = maxRight - minX;
  const maxHFit = maxBottom - minY;

  const dims = clampDimensionsToViewport(panel, maxWFit, maxHFit);
  const rect = clampTopLeftWithinBounds(
    panel.position.x,
    panel.position.y,
    dims.width,
    dims.height,
    minX,
    minY,
    maxRight,
    maxBottom
  );

  return {
    ...panel,
    position: { x: rect.x, y: rect.y },
    size: { width: rect.width, height: rect.height },
  };
}
