/**
 * XState Inspector integration for development mode.
 *
 * Enables visual debugging of state machines in browser DevTools.
 * Only active in development mode to avoid performance impact in production.
 *
 * AI: Visual FSM debugging is invaluable for understanding complex state transitions.
 */

import { inspect } from '@xstate/inspect';

/**
 * Initialize XState Inspector for development mode.
 *
 * Opens a visual inspector in a popup window where you can:
 * - See all active state machines
 * - View current states and context
 * - Track state transitions in real-time
 * - Send events manually for testing
 *
 * Usage:
 * ```typescript
 * // In main.tsx or App.tsx
 * if (import.meta.env.DEV) {
 *   initializeXStateInspector();
 * }
 * ```
 *
 * AI: Call once at app startup in development mode only.
 */
export function initializeXStateInspector(): void {
  if (import.meta.env.DEV) {
    try {
      inspect({
        // Use iframe instead of popup for better dev experience
        iframe: false,
        // URL for the inspector (defaults to https://stately.ai/viz)
        url: 'https://stately.ai/viz?inspect',
      });

      console.log('[XState Inspector] Initialized - Open https://stately.ai/viz?inspect to view state machines');
    } catch (error) {
      console.warn('[XState Inspector] Failed to initialize:', error);
    }
  }
}

/**
 * Enable XState Inspector for a specific machine.
 *
 * Add this option when creating a machine actor:
 * ```typescript
 * const actor = createActor(connectionMachine, {
 *   inspect: getInspectorOptions()
 * });
 * ```
 *
 * @returns Inspector configuration object
 *
 * AI: This connects individual machines to the global inspector.
 */
export function getInspectorOptions() {
  if (import.meta.env.DEV) {
    return {
      inspect: true,
    };
  }
  return {};
}
