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
  panelFound: boolean;
  panelNames: string | null;
  hasLinkdead: boolean;
}

/** Raw presence payload as received over the WebSocket, before projection into GameState. */
export interface PresenceEvent {
  eventType: string;
  sequence: number | null;
  roomId: string | null;
  players: string[] | null;
  npcs: string[] | null;
  count: number | null;
}

export interface GameUiDiagnostics {
  isGameUiLoaded: boolean;
  hasVisibleCommandInput: boolean;
  hasVisibleGameInfoPanel: boolean;
  hasVisibleLoginForm: boolean;
  hasBodyGameUiIndicators: boolean;
  bodySnippet: string;
}

export function isGameUiLoadedInBrowser(): boolean;
export function captureGameUiDiagnosticsInBrowser(): GameUiDiagnostics;
export function hasConnectedStatusInBrowser(): boolean;
export function hasRoomSubscriptionInBrowser(): boolean;
export function hasExpectedOccupantCountInBrowser(expected: number): boolean;
export function hasOtherPlayerNamesInBrowser(names: string[]): boolean;
export function isDisconnectedBannerVisibleInBrowser(): boolean;
export function captureOccupantsSnapshotInBrowser(): OccupantsSnapshot;
export function installPresenceRecorderInBrowser(): void;
export function getPresenceEventsInBrowser(): PresenceEvent[];
