import react from '@vitejs/plugin-react';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./src/test/setup.ts'],
    exclude: ['tests/**/*', '**/*.spec.ts', '**/*.spec.tsx', 'node_modules/**/*'],
    pool: 'threads',
    maxConcurrency: 1,
    poolOptions: {
      threads: {
        singleThread: true,
        maxThreads: 1,
        minThreads: 1,
      },
    },
    coverage: {
      provider: 'v8',
      enabled: true,
      include: ['src/**/*.{ts,tsx}'],
      exclude: [
        'src/**/*.test.{ts,tsx}',
        'src/**/*.spec.{ts,tsx}',
        'src/test/**/*',
        'src/**/*.d.ts',
        'src/main.tsx',
        'src/vite-env.d.ts',
        'tests/**/*',
        '**/*.spec.ts',
      ],
      thresholds: {
        // Tiered Coverage Strategy:
        // - Critical code (security, auth, data handling): 98%
        // - Core business logic (game state, connections, stores): 85%+
        // - UI components (behavior-focused): 70-80%
        // - Utilities (important ones): 60-70%
        //
        // Global threshold is set to 70% as a minimum baseline.
        // Per-file thresholds below enforce category-specific requirements.
        // Note: Vitest requires exact file paths (not globs) for per-file thresholds.
        statements: 70,
        branches: 65,
        functions: 70,
        lines: 70,
        // Critical code: security, authentication, data handling → 95% (security.ts adjusted from 98%)
        'src/utils/security.ts': {
          statements: 95,
          branches: 95,
          functions: 95,
          lines: 95,
        },
        'src/utils/errorHandler.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        'src/utils/logoutHandler.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        'src/hooks/useGameConnection.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        'src/hooks/useSSEConnection.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        'src/hooks/useWebSocketConnection.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        'src/stores/sessionStore.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        'src/stores/connectionStore.ts': {
          statements: 98,
          branches: 98,
          functions: 98,
          lines: 98,
        },
        // Core business logic: game state, connections, stores → 85%+
        'src/stores/gameStore.ts': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/stores/commandStore.ts': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/stores/containerStore.ts': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/stores/stateNormalization.ts': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/hooks/useGameTerminal.ts': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/hooks/useConnectionStateMachine.ts': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/contexts/GameTerminalContext.tsx': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        'src/contexts/PanelContext.tsx': {
          statements: 85,
          branches: 85,
          functions: 85,
          lines: 85,
        },
        // Note: UI components (src/components/**/*.tsx, src/pages/**/*.tsx)
        // and utilities (src/utils/**/*.ts, src/types/**/*.ts, src/config/**/*.ts)
        // use the global 70% threshold above.
        // See docs/TEST_COVERAGE_STRATEGY.md for detailed category-specific targets.
      },
      reporter: ['text', 'html', 'json'],
      reportsDirectory: './coverage',
    },
  },
});
