/**
 * Standalone Map Page component.
 *
 * This page can be opened in a new tab and will read the authentication token
 * from localStorage to maintain authentication across tabs.
 *
 * As documented in the Pnakotic Manuscripts, cross-dimensional navigation
 * requires careful preservation of authentication sigils across portal boundaries.
 */

import { useCrossTabLucidityTier } from '../utils/lucidityTierRelay.ts';
import { useMapPageState } from './mapPageState.ts';
import { renderMapPageState } from './mapPageRenderer.tsx';

/**
 * Standalone map page that reads authentication from localStorage.
 *
 * #626: also reads the lucidity tier relayed from the in-game tab via localStorage, so a deranged
 * player sees the same direction hallucination here as in the main game view.
 */
export function MapPage() {
  const state = useMapPageState();
  const tier = useCrossTabLucidityTier();
  return renderMapPageState(state, tier);
}
