import { lazy } from 'react';

export const EldritchEffectsDemo = lazy(() =>
  import('../components/EldritchEffectsDemo.tsx').then(m => ({ default: m.EldritchEffectsDemo }))
);
export const GameClientV2Container = lazy(() =>
  import('../components/ui-v2/GameClientV2Container.tsx').then(m => ({ default: m.GameClientV2Container }))
);
export const MotdInterstitialScreen = lazy(() =>
  import('../components/MotdInterstitialScreen.tsx').then(m => ({ default: m.MotdInterstitialScreen }))
);
export const ProfessionSelectionScreen = lazy(() =>
  import('../components/ProfessionSelectionScreen.tsx').then(m => ({ default: m.ProfessionSelectionScreen }))
);
export const StatsRollingScreen = lazy(() =>
  import('../components/StatsRollingScreen.tsx').then(m => ({ default: m.StatsRollingScreen }))
);
export const CharacterSelectionScreen = lazy(() =>
  import('../components/CharacterSelectionScreen.tsx').then(m => ({ default: m.CharacterSelectionScreen }))
);
export const SkillAssignmentScreen = lazy(() =>
  import('../components/SkillAssignmentScreen.tsx').then(m => ({ default: m.SkillAssignmentScreen }))
);
export const CharacterNameScreen = lazy(() =>
  import('../components/CharacterNameScreen.tsx').then(m => ({ default: m.CharacterNameScreen }))
);

export function LoadingFallback() {
  return (
    <div className="App flex items-center justify-center min-h-screen bg-mythos-terminal-background">
      <div className="text-mythos-terminal-text font-mono">Loading...</div>
    </div>
  );
}
