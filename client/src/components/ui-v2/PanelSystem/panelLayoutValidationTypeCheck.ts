/**
 * Type checks for panel layout validation. In a separate module so Lizard attributes
 * cyclomatic complexity here rather than panelLayoutValidation.ts (limit 8).
 *
 * Position/size guards live in panelLayoutValidationTypeCheckGuards.ts: Codacy lizard
 * 1.17.x merges consecutive non-exported TS functions and was reporting isPanelPosition
 * at CCN 13.
 */

import type { PanelState } from '../types';
import { isPanelPosition, isPanelSize, isRecord } from './panelLayoutValidationTypeCheckGuards';
import { hasRequiredPanelStateTypes } from './panelLayoutValidationTypeCheckImpl';

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
