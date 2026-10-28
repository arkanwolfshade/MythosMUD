// Projects a rescue_update payload into the banner's RescueStatus (#713).

import type { RescueRole, RescueStatus, RescueStatusKind } from '../../../types/rescue';

const BANNER_STATUSES: ReadonlySet<string> = new Set<RescueStatusKind>([
  'channeling',
  'success',
  'failed',
  'interrupted',
  'rescued',
  'sanitarium',
]);

const optionalString = (value: unknown): string | undefined => (typeof value === 'string' ? value : undefined);

/**
 * Returns null for statuses the banner does not show (e.g. `delirium`, which has its own modal).
 * The server sets `role` on every rescue_update; an absent or unknown role is treated as the
 * target, which is the only side the trigger-originated events (sanitarium, natural exit) go to.
 */
export function toRescueStatus(data: Record<string, unknown>, seq: number): RescueStatus | null {
  const status = data.status;
  if (typeof status !== 'string' || !BANNER_STATUSES.has(status)) return null;
  const role: RescueRole = data.role === 'rescuer' ? 'rescuer' : 'target';
  return {
    status: status as RescueStatusKind,
    role,
    rescuerName: optionalString(data.rescuer_name),
    targetName: optionalString(data.target_name),
    message: optionalString(data.message),
    etaSeconds: typeof data.eta_seconds === 'number' ? data.eta_seconds : undefined,
    seq,
  };
}
