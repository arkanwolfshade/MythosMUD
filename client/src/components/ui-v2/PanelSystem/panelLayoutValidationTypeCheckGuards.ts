/**
 * Position/size type guards. Split from panelLayoutValidationTypeCheck.ts so
 * Codacy lizard 1.17.x does not merge them with isPanelState into one CCN blob.
 */

import type { PanelPosition, PanelSize } from '../types';

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

export { isRecord };
