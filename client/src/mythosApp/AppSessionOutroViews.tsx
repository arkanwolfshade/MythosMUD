import { Suspense, type ReactElement } from 'react';
import { secureTokenStorage } from '../utils/security.js';
import { GameClientV2Container, LoadingFallback, MotdInterstitialScreen } from './appLazyScreens.js';
import type { MythosAppViewModel } from './mythosAppViewModel.js';

export function AppSessionOutroViews(vm: MythosAppViewModel): ReactElement | null {
  if (vm.showMotd) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <MotdInterstitialScreen onContinue={vm.handleMotdContinue} onReturnToLogin={vm.handleMotdReturnToLogin} />
        </Suspense>
      </div>
    );
  }

  const finalAuthToken = vm.authToken || secureTokenStorage.getToken() || '';

  if (!finalAuthToken) {
    vm.setIsAuthenticated(false);
    vm.setCharacters([]);
    vm.setSelectedCharacterName('');
    vm.setSelectedCharacterId('');
    vm.setError('Session expired. Please log in again.');
    return null;
  }

  if (!vm.authToken && finalAuthToken) {
    vm.setAuthToken(finalAuthToken);
  }

  return (
    <div className="App">
      <Suspense fallback={<LoadingFallback />}>
        <GameClientV2Container
          playerName={vm.selectedCharacterName || vm.playerName}
          authToken={finalAuthToken}
          characterId={vm.selectedCharacterId}
          onLogout={vm.handleLogout}
          isLoggingOut={vm.isLoggingOut}
          onDisconnect={vm.handleDisconnectCallback}
        />
      </Suspense>
    </div>
  );
}
