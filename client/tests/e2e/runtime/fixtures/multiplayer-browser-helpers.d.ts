/**
 * TypeScript surface for browser-side Playwright helpers.
 * Implementation lives in multiplayer-browser-helpers.js (plain JS for Lizard parsing).
 */

export interface OccupantsSnapshot {
  hasOccupantsMatch: boolean;
  occupantsCount: number | null;
  hasPlayersMatch: boolean;
  playersCount: number | null;
  occupantsSnippet: string;
  hasLinkdead: boolean;
}

export function isGameUiLoadedInBrowser(): boolean;
export function hasConnectedStatusInBrowser(): boolean;
export function hasRoomSubscriptionInBrowser(): boolean;
export function hasExpectedOccupantCountInBrowser(expected: number): boolean;
export function hasOtherPlayerNamesInBrowser(names: string[]): boolean;
export function isDisconnectedBannerVisibleInBrowser(): boolean;
export function captureOccupantsSnapshotInBrowser(): OccupantsSnapshot;
