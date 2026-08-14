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

function creationShell(children: ReactElement): ReactElement {
  return (
    <div className="App">
      <Suspense fallback={<LoadingFallback />}>{children}</Suspense>
    </div>
  );
}

function renderStatsStep(vm: MythosAppViewModel): ReactElement {
  return creationShell(
    <StatsRollingScreen
      onStatsAccepted={vm.handleStatsAccepted}
      onError={vm.handleStatsError}
      onBack={vm.handleStatsRollingBack}
      baseUrl={API_V1_BASE}
      authToken={vm.authToken}
    />
  );
}

function renderProfessionStep(vm: MythosAppViewModel): ReactElement {
  return creationShell(
    <ProfessionSelectionScreen
      onProfessionSelected={vm.handleProfessionSelected}
      onError={vm.handleProfessionSelectionError}
      onBack={vm.handleProfessionSelectionBack}
      baseUrl={API_V1_BASE}
      authToken={vm.authToken}
    />
  );
}

function renderSkillsStep(vm: MythosAppViewModel): ReactElement {
  return creationShell(
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
  );
}

function renderNameStep(vm: MythosAppViewModel): ReactElement | null {
  if (!vm.pendingStats || !vm.selectedProfession || !vm.pendingSkillsPayload) {
    return null;
  }
  return creationShell(
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
  );
}

export function AppCreationFlowViews(vm: MythosAppViewModel): ReactElement | null {
  if (!vm.isAuthenticated || vm.creationStep === null) {
    return null;
  }

  if (vm.creationStep === 'stats') {
    return renderStatsStep(vm);
  }
  if (vm.creationStep === 'profession') {
    return renderProfessionStep(vm);
  }
  if (vm.creationStep === 'skills') {
    return renderSkillsStep(vm);
  }
  if (vm.creationStep === 'name') {
    const nameView = renderNameStep(vm);
    if (nameView) {
      return nameView;
    }
    vm.setCreationStep('skills');
    return null;
  }

  return null;
}
