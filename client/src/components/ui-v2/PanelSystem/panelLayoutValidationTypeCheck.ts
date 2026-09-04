/**
 * Type checks for panel layout validation. In a separate module so Lizard attributes
 * cyclomatic complexity here rather than panelLayoutValidation.ts (limit 8).
 */

import type { PanelPosition, PanelSize, PanelState } from '../types';
import { hasRequiredPanelStateTypes } from './panelLayoutValidationTypeCheckImpl';

export { hasRequiredPanelStateTypes } from './panelLayoutValidationTypeCheckImpl';

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null;
}

export function isPanelPosition(value: unknown): value is PanelPosition {
  if (!isRecord(value)) return false;
  return typeof value.x === 'number' && typeof value.y === 'number';
}

export function isPanelSize(value: unknown): value is PanelSize {
  if (!isRecord(value)) return false;
  return typeof value.width === 'number' && typeof value.height === 'number';
}

function isPanelState(value: unknown): value is PanelState {
  if (!isRecord(value)) return false;
  if (!hasRequiredPanelStateTypes(value)) return false;
  if (!isPanelPosition(value.position) || !isPanelSize(value.size)) return false;
  if (value.minSize !== undefined && !isPanelSize(value.minSize)) return false;
  if (value.maxSize !== undefined && !isPanelSize(value.maxSize)) return false;
  return true;
}

export function isPanelStateRecord(value: unknown): value is Record<string, PanelState> {
  if (!isRecord(value)) return false;
  return Object.values(value).every(isPanelState);
}
