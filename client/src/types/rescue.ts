/** Rescue phases the banner shows (#713). `delirium` is deliberately absent: it has its own interstitial. */
export type RescueStatusKind = 'channeling' | 'success' | 'failed' | 'interrupted' | 'rescued' | 'sanitarium';

/** Which side of the rescue the server sent this event to. */
export type RescueRole = 'rescuer' | 'target';

export interface RescueStatus {
  status: RescueStatusKind;
  role: RescueRole;
  rescuerName?: string;
  targetName?: string;
  /** The server's line for this event; already worded for `role`. */
  message?: string;
  /** channeling only: server-decided channel length, animated locally by the banner. */
  etaSeconds?: number;
  /** sequence_number of the rescue_update that set this. Identity for the banner's expiry timer. */
  seq: number;
}

/** How long a terminal status stays on screen; channeling is bounded by its ETA plus this. */
export const RESCUE_TERMINAL_DISPLAY_MS = 5000;
