import type { MythosAppViewModel } from './mythosAppViewModel.js';
import { buildMythosAppViewModel } from './mythosAppViewModelFactory.ts';
import { useMythosAppActions } from './useMythosAppActions.ts';
import { useMythosAppState } from './useMythosAppState.ts';

export function useMythosApp(): MythosAppViewModel {
  const state = useMythosAppState();
  const actions = useMythosAppActions(state);
  return buildMythosAppViewModel(state, actions);
}
