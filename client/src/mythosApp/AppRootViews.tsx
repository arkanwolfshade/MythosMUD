import { Suspense } from 'react';
import { MythosLoginForm } from './MythosLoginForm.js';
import { AppCreationFlowViews } from './AppCreationFlowViews.js';
import { AppDemoView } from './AppDemoView.js';
import { AppSessionOutroViews } from './AppSessionOutroViews.js';
import '../App.css';
import { API_V1_BASE } from '../utils/config.js';
import { CharacterSelectionScreen, LoadingFallback } from './appLazyScreens.js';
import type { MythosAppViewModel } from './mythosAppViewModel.js';

export type { MythosAppViewModel } from './mythosAppViewModel.js';

export function AppRootViews(vm: MythosAppViewModel) {
  if (vm.showDemo) {
    return AppDemoView(vm);
  }

  if (!vm.isAuthenticated) {
    return (
      <div className="App">
        <MythosLoginForm
          usernameInputRef={vm.usernameInputRef}
          playerName={vm.playerName}
          setPlayerName={vm.setPlayerName}
          password={vm.password}
          setPassword={vm.setPassword}
          inviteCode={vm.inviteCode}
          setInviteCode={vm.setInviteCode}
          isRegistering={vm.isRegistering}
          error={vm.error}
          isSubmitting={vm.isSubmitting}
          handleKeyDown={vm.handleKeyDown}
          handleLoginClick={vm.handleLoginClick}
          handleRegisterClick={vm.handleRegisterClick}
          toggleMode={vm.toggleMode}
          setShowDemo={vm.setShowDemo}
        />
      </div>
    );
  }

  if (vm.isAuthenticated && vm.showCharacterSelection && vm.characters.length > 0) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <CharacterSelectionScreen
            characters={vm.characters}
            onCharacterSelected={vm.handleCharacterSelected}
            onCreateCharacter={vm.handleCreateCharacter}
            onDeleteCharacter={vm.handleDeleteCharacter}
            onError={vm.setError}
            baseUrl={API_V1_BASE}
            authToken={vm.authToken}
          />
        </Suspense>
      </div>
    );
  }

  if (vm.isAuthenticated && vm.creationStep !== null) {
    return AppCreationFlowViews(vm);
  }

  return AppSessionOutroViews(vm);
}
