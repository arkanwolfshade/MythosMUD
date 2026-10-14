/**
 * Runtime validation for panel layout (localStorage). Type guards live in
 * panelLayoutValidationTypeCheck.ts to keep cyclomatic complexity per file under Lizard limit.
 */

import type { PanelState } from '../types';
import { isPanelStateRecord } from './panelLayoutValidationTypeCheck';

export const PANEL_LAYOUT_STORAGE_KEY = 'mythosmud-ui-v2-panel-layout';

export function loadPanelLayout(): Record<string, PanelState> | null {
  try {
    const stored = localStorage.getItem(PANEL_LAYOUT_STORAGE_KEY);
    if (!stored) return null;
    const parsed: unknown = JSON.parse(stored);
    if (isPanelStateRecord(parsed)) return parsed;
    console.warn('Invalid panel layout in localStorage');
  } catch (error) {
    console.warn('Failed to load panel layout from localStorage', error);
  }
  return null;
}

export function savePanelLayout(panels: Record<string, PanelState>): void {
  try {
    localStorage.setItem(PANEL_LAYOUT_STORAGE_KEY, JSON.stringify(panels));
  } catch (error) {
    console.warn('Failed to save panel layout to localStorage', error);
  }
}
