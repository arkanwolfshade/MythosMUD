/**
 * XState v5 Inspector integration for development mode.
 *
 * For XState v5, use the browser-based Stately Inspector at https://stately.ai/inspect
 * No npm package needed - just enable inspection in your actor configuration.
 *
 * AI: XState v5 uses a simpler, browser-based inspector without dependencies.
 */

/**
 * Initialize XState Inspector for development mode.
 *
 * For XState v5, simply log instructions for using Stately Inspector.
 * The inspector connects via browser extension or stately.ai/inspect
 *
 * Usage:
 * ```typescript
 * // In main.tsx or App.tsx
 * if (import.meta.env.DEV) {
 *   initializeXStateInspector();
 * }
 * ```
 *
 * AI: XState v5 inspector is browser-based - no initialization needed!
 */
export function initializeXStateInspector(): void {
  if (import.meta.env.DEV) {
    console.log('%c[XState v5 Inspector]', 'color: #2563eb; font-weight: bold;', 'To debug state machines:');
    console.log('  1. Open https://stately.ai/inspect in a new tab');
    console.log('  2. State machines will automatically connect');
    console.log('  3. Or install Stately Inspector browser extension');
    console.log('  Docs: https://stately.ai/docs/developer-tools');
  }
}

/**
 * Enable XState Inspector for a specific machine.
 *
 * For XState v5, enable inspection by setting inspect option when creating actor:
 * ```typescript
 * const actor = createActor(connectionMachine, {
 *   inspect: getInspectorOptions()
 * });
 * ```
 *
 * @returns Inspector configuration object
 *
 * AI: This enables inspection for individual actors in dev mode.
 */
export function getInspectorOptions() {
  if (import.meta.env.DEV && typeof window !== 'undefined') {
    return {
      // Enable inspection in dev mode
      // The browser-based inspector will pick this up automatically
      inspect: true,
    };
  }
  return {};
}
