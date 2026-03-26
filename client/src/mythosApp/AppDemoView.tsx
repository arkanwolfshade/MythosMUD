import { Suspense, type ReactElement } from 'react';
import { EldritchEffectsDemo, LoadingFallback } from './appLazyScreens.js';
import type { MythosAppViewModel } from './mythosAppViewModel.js';

export function AppDemoView(vm: MythosAppViewModel): ReactElement {
  return (
    <div className="App">
      <Suspense fallback={<LoadingFallback />}>
        <EldritchEffectsDemo
          onExit={() => {
            vm.setShowDemo(false);
          }}
        />
      </Suspense>
    </div>
  );
}
