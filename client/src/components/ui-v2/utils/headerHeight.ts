// Single source of truth for HeaderBar's own height and the panel area's top offset, so the
// two can't drift out of sync (root cause of a pre-existing 16px gap when collapsed - #699).
import type { MythosTimeState } from '../../../types/mythosTime';

/** True when the header needs its second (flavor) row: witching hour or an active holiday. */
export function hasFlavorRow(mythosTime: MythosTimeState | null): boolean {
  return Boolean(mythosTime && (mythosTime.is_witching_hour || mythosTime.active_holidays.length > 0));
}

export function headerHeightClass(
  isCollapsed: boolean,
  mythosTime: MythosTimeState | null
): { header: string; padding: string } {
  if (isCollapsed) {
    return { header: 'h-8', padding: 'pt-8' };
  }
  return hasFlavorRow(mythosTime) ? { header: 'h-20', padding: 'pt-20' } : { header: 'h-12', padding: 'pt-12' };
}
