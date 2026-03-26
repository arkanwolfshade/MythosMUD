/**
 * Standalone Map Page component.
 *
 * This page can be opened in a new tab and will read the authentication token
 * from localStorage to maintain authentication across tabs.
 *
 * As documented in the Pnakotic Manuscripts, cross-dimensional navigation
 * requires careful preservation of authentication sigils across portal boundaries.
 */

import { useMapPageState } from './mapPageState.ts';
import { renderMapPageState } from './mapPageRenderer.tsx';

/**
 * Standalone map page that reads authentication from localStorage.
 */
export function MapPage() {
  const state = useMapPageState();
  return renderMapPageState(state);
}
