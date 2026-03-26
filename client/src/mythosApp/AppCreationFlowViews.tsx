import { Suspense, type ReactElement } from 'react';
import { API_V1_BASE } from '../utils/config.js';
import type { MythosAppViewModel } from './mythosAppViewModel.js';
import {
  CharacterNameScreen,
  LoadingFallback,
  ProfessionSelectionScreen,
  SkillAssignmentScreen,
  StatsRollingScreen,
} from './appLazyScreens.js';

export function AppCreationFlowViews(vm: MythosAppViewModel): ReactElement | null {
  if (!vm.isAuthenticated || vm.creationStep === null) {
    return null;
  }

  if (vm.creationStep === 'stats') {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <StatsRollingScreen
            onStatsAccepted={vm.handleStatsAccepted}
            onError={vm.handleStatsError}
            onBack={vm.handleStatsRollingBack}
            baseUrl={API_V1_BASE}
            authToken={vm.authToken}
          />
        </Suspense>
      </div>
    );
  }

  if (vm.creationStep === 'profession') {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <ProfessionSelectionScreen
            onProfessionSelected={vm.handleProfessionSelected}
            onError={vm.handleProfessionSelectionError}
            onBack={vm.handleProfessionSelectionBack}
            baseUrl={API_V1_BASE}
            authToken={vm.authToken}
          />
        </Suspense>
      </div>
    );
  }

  if (vm.creationStep === 'skills') {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <SkillAssignmentScreen
            baseUrl={API_V1_BASE}
            authToken={vm.authToken}
            onSkillsConfirmed={payload => {
              vm.setPendingSkillsPayload(payload);
              vm.setCreationStep('name');
            }}
            onBack={() => {
              vm.setCreationStep('profession');
            }}
            onError={vm.handleStatsError}
          />
        </Suspense>
      </div>
    );
  }

  if (vm.creationStep === 'name' && vm.pendingStats && vm.selectedProfession && vm.pendingSkillsPayload) {
    return (
      <div className="App">
        <Suspense fallback={<LoadingFallback />}>
          <CharacterNameScreen
            stats={vm.pendingStats}
            profession={vm.selectedProfession}
            skillsPayload={vm.pendingSkillsPayload}
            baseUrl={API_V1_BASE}
            authToken={vm.authToken}
            onComplete={vm.handleCreationComplete}
            onError={vm.handleStatsError}
            onBack={() => {
              vm.setCreationStep('skills');
            }}
          />
        </Suspense>
      </div>
    );
  }

  if (vm.creationStep === 'name') {
    vm.setCreationStep('skills');
    return null;
  }

  return null;
}
