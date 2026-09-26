/**
 * Resolve initial panel layout from localStorage vs defaults (viewport clamp + metadata merge).
 */

import type { PanelState } from '../types';
import { clampPanelLayoutToViewport, layoutFitsViewport } from './panelLayoutClamp';
import { loadPanelLayout, savePanelLayout } from './panelLayoutValidation';

/** Copy optional panel metadata (opaque, minHeight) from default into stored, and add any
 * default panel id missing from a returning user's saved layout (e.g. a panel added since they
 * last saved -- without this, a new panel id never appears for existing users, see #711). */
export function mergePanelMetadataFromDefault(
  stored: Record<string, PanelState>,
  defaultPanels: Record<string, PanelState>
): Record<string, PanelState> {
  const result = { ...stored };
  for (const id of Object.keys(result)) {
    const def = defaultPanels[id];
    if (!def) continue;
    const patch: Partial<PanelState> = {};
    if (def.opaque !== undefined) patch.opaque = def.opaque;
    if (def.minHeight !== undefined) patch.minHeight = def.minHeight;
    if (Object.keys(patch).length > 0) {
      result[id] = { ...result[id], ...patch };
    }
  }
  for (const id of Object.keys(defaultPanels)) {
    if (!(id in result)) {
      result[id] = defaultPanels[id];
    }
  }
  return result;
}

export function resolveInitialPanelLayout(
  defaultPanels: Record<string, PanelState>,
  viewportWidth: number,
  viewportHeight: number
): Record<string, PanelState> {
  const stored = loadPanelLayout();
  if (!stored) {
    return defaultPanels;
  }
  if (layoutFitsViewport(stored, viewportWidth, viewportHeight)) {
    return mergePanelMetadataFromDefault(stored, defaultPanels);
  }
  const clamped = clampPanelLayoutToViewport(stored, viewportWidth, viewportHeight);
  const merged = mergePanelMetadataFromDefault(clamped, defaultPanels);
  savePanelLayout(merged);
  return merged;
}
