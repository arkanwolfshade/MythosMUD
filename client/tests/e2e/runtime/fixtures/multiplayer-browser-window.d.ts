export {};

declare global {
  interface Window {
    __mythosE2eIsGameUiLoaded?: () => boolean;
    __mythosE2eCaptureGameUiDiagnostics?: () => {
      isGameUiLoaded: boolean;
      hasVisibleCommandInput: boolean;
      hasVisibleGameInfoPanel: boolean;
      hasVisibleLoginForm: boolean;
      hasBodyGameUiIndicators: boolean;
      bodySnippet: string;
    };
    __mythosE2eHasConnectedStatus?: () => boolean;
    __mythosE2eHasRoomSubscription?: () => boolean;
    __mythosE2eHasExpectedOccupantCount?: (expected: number) => boolean;
    __mythosE2eHasOtherPlayerNames?: (names: string[]) => boolean;
    __mythosE2eIsDisconnectedBannerVisible?: () => boolean;
    __mythosE2eCaptureOccupantsSnapshot?: () => import('./multiplayer-browser-helpers').OccupantsSnapshot;
  }
}
