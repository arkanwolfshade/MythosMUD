import type { MythosAppViewModel } from './mythosAppViewModel.js';
import type { useMythosAppActions } from './useMythosAppActions.ts';
import type { useMythosAppState } from './useMythosAppState.ts';

type AppState = ReturnType<typeof useMythosAppState>;
type AppActions = ReturnType<typeof useMythosAppActions>;

function buildStateViewModel(state: AppState) {
  return {
    showDemo: state.showDemo,
    setShowDemo: state.setShowDemo,
    isAuthenticated: state.isAuthenticated,
    characters: state.characters,
    showCharacterSelection: state.showCharacterSelection,
    creationStep: state.creationStep,
    pendingStats: state.pendingStats,
    selectedProfession: state.selectedProfession,
    pendingSkillsPayload: state.pendingSkillsPayload,
    showMotd: state.showMotd,
    playerName: state.playerName,
    setPlayerName: state.setPlayerName,
    password: state.password,
    setPassword: state.setPassword,
    inviteCode: state.inviteCode,
    setInviteCode: state.setInviteCode,
    error: state.error,
    isSubmitting: state.isSubmitting,
    isRegistering: state.isRegistering,
    isLoggingOut: state.isLoggingOut,
    usernameInputRef: state.usernameInputRef,
    authToken: state.authToken,
    selectedCharacterName: state.selectedCharacterName,
    selectedCharacterId: state.selectedCharacterId,
    handleLoginClick: state.handleLoginClick,
    handleRegisterClick: state.handleRegisterClick,
    setError: state.setError,
    setCreationStep: state.setCreationStep,
    setPendingSkillsPayload: state.setPendingSkillsPayload,
    setAuthToken: state.setAuthToken,
    setIsAuthenticated: state.setIsAuthenticated,
    setCharacters: state.setCharacters,
    setSelectedCharacterName: state.setSelectedCharacterName,
    setSelectedCharacterId: state.setSelectedCharacterId,
  };
}

function buildActionViewModel(actions: AppActions) {
  return {
    handleKeyDown: actions.handleKeyDown,
    toggleMode: actions.toggleMode,
    handleCharacterSelected: actions.handleCharacterSelected,
    handleCreateCharacter: actions.handleCreateCharacter,
    handleDeleteCharacter: actions.handleDeleteCharacter,
    handleStatsAccepted: actions.handleStatsAccepted,
    handleStatsError: actions.handleStatsError,
    handleStatsRollingBack: actions.handleStatsRollingBack,
    handleProfessionSelected: actions.handleProfessionSelected,
    handleProfessionSelectionError: actions.handleProfessionSelectionError,
    handleProfessionSelectionBack: actions.handleProfessionSelectionBack,
    handleCreationComplete: actions.handleCreationComplete,
    handleMotdContinue: actions.handleMotdContinue,
    handleMotdReturnToLogin: actions.handleMotdReturnToLogin,
    handleLogout: actions.handleLogout,
    handleDisconnectCallback: actions.handleDisconnectCallback,
  };
}

export function buildMythosAppViewModel(state: AppState, actions: AppActions): MythosAppViewModel {
  return {
    ...buildStateViewModel(state),
    ...buildActionViewModel(actions),
  };
}
