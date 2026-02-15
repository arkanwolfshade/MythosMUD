/// <reference types="vitest/config" />
import react from '@vitejs/plugin-react';
import path from 'path';
import { defineConfig } from 'vite';

// TODO: Implement AST-based console removal plugin to selectively remove
// console.debug, console.log, console.info, console.trace while preserving
// console.error and console.warn for production error logging.
// Previous regex-based approach was disabled due to breaking complex expressions.

// https://vite.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [
    react(),
    // Note: Console removal plugin is disabled due to regex limitations
    // For production, prefer using console.error/warn for logging
    // TODO: Implement AST-based console removal to preserve console.error/warn
    // ...(mode === 'production' ? [removeConsolePlugin()] : []),
  ],

  // Path alias: Only '@' is used in the codebase (in test files)
  // Per Vite best practices, minimize path aliases - prefer explicit relative imports
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },

  // Client code uses import.meta.env (Vite); no define for process.env.NODE_ENV needed.
  esbuild: {
    // Target modern browsers for optimal bundle size
    target: 'es2020',
    // Remove debugger statements in production
    // Note: Console removal is disabled - prefer console.error/warn for production logging
    // TODO: Implement proper AST-based console removal to selectively remove console methods
    ...(mode === 'production' && {
      drop: ['debugger'],
      // Use legalComments to remove comments in production
      legalComments: 'none',
    }),
  },
  build: {
    // Source maps: false for production (smaller bundles), true for dev
    sourcemap: mode === 'development',
    // Minify using esbuild (faster than terser)
    minify: 'esbuild',
    // Target modern browsers
    target: 'es2020',
    // Chunk size warning threshold (600KB)
    // Increased from 500KB to accommodate large single-package chunks like lucide-react (icon library)
    // which cannot be split further. All chunks are already properly separated by functionality.
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        // Manual chunk splitting for optimal bundle sizes
        // Strategy: Split large, self-contained libraries into separate chunks.
        // All other node_modules go into a single vendor chunk to avoid circular
        // chunk dependencies (vendor-react <-> vendor) from shared deps (e.g. scheduler).
        manualChunks: id => {
          if (id.includes('node_modules')) {
            if (id.includes('lucide-react')) return 'vendor-icons';
            if (id.includes('react-grid-layout')) return 'vendor-grid-layout';
            if (id.includes('reactflow')) return 'vendor-reactflow';
            return 'vendor';
          }
        },
        // Optimize chunk file names for better caching
        chunkFileNames: 'assets/js/[name]-[hash].js',
        entryFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]',
      },
    },
  },
  server: {
    host: true, // Listen on 0.0.0.0 so dev server is reachable from LAN (e.g. http://<machine-ip>:5173)
    port: parseInt(process.env.PORT || '5173'),
    warmup: {
      clientFiles: ['./src/main.tsx', './src/App.tsx'],
    },
    proxy: {
      // Versioned API: all /v1/* requests go to the backend (including /v1/professions)
      '/v1': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: false,
        ws: true,
        configure: proxy => {
          proxy.on('proxyReq', (proxyReq, req) => {
            // Explicitly forward Authorization header
            const authHeader = req.headers.authorization || req.headers.Authorization;
            if (authHeader) {
              proxyReq.setHeader('Authorization', authHeader as string);
            }
          });
        },
      },
      '/api': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
        ws: true,
      },
      '/auth': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
      },
      '/game': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
      },
      '/professions': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
        configure: (proxy, _options) => {
          // Ensure Authorization header is forwarded
          proxy.on('proxyReq', (proxyReq, req) => {
            const authHeader = req.headers.authorization || req.headers.Authorization;
            if (authHeader) {
              proxyReq.setHeader('Authorization', authHeader as string);
            }
          });
        },
      },
    },
  },
  test: {
    environment: 'happy-dom',
    globals: true,
    setupFiles: ['./src/test/setup.ts'],
    exclude: [
      'tests/**/*',
      'node_modules/**/*',
      '**/*.spec.tsx',
      '**/components/__tests__/game-log-panel.test.tsx',
      '**/App.integration.test.tsx',
      '**/__tests__/CharacterCreationNavigation.test.tsx',
      '**/__tests__/App.logout.test.tsx',
      '**/__tests__/ProfessionPersistence.test.tsx',
      '**/__tests__/StatRollingWithProfessionRequirements.test.tsx',
      '**/__tests__/LogoutFlow.integration.test.tsx',
      '**/components/__tests__/LogoutFlow.integration.test.tsx',
    ],
    pool: 'threads',
    coverage: {
      provider: 'v8',
      enabled: true,
      clean: false,
      include: ['src/**/*.{ts,tsx}'],
      exclude: [
        'src/**/*.test.{ts,tsx}',
        'src/test/**/*',
        'src/**/*.d.ts',
        'src/main.tsx',
        'src/vite-env.d.ts',
        'tests/**/*',
      ],
      thresholds: {
        statements: 70,
        branches: 69,
        functions: 70,
        lines: 70,
        'src/utils/security.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/utils/errorHandler.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/utils/logoutHandler.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/hooks/useGameConnection.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/hooks/useWebSocketConnection.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/hooks/useSessionManagement.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/stores/sessionStore.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/stores/connectionStore.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/stores/gameStore.ts': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/stores/commandStore.ts': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/stores/containerStore.ts': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/stores/stateNormalization.ts': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/hooks/useGameTerminal.ts': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/hooks/useConnectionStateMachine.ts': { statements: 85, branches: 85, functions: 80, lines: 85 },
        'src/contexts/GameTerminalContext.tsx': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/contexts/PanelContext.tsx': { statements: 85, branches: 85, functions: 85, lines: 85 },
        'src/components/ui-v2/eventHandlers/messageHandlers.ts': {
          statements: 90,
          branches: 90,
          functions: 90,
          lines: 90,
        },
        'src/components/ui-v2/eventHandlers/playerHandlers.ts': {
          statements: 90,
          branches: 90,
          functions: 90,
          lines: 90,
        },
        'src/components/ui-v2/eventHandlers/roomHandlers.ts': {
          statements: 90,
          branches: 90,
          functions: 90,
          lines: 90,
        },
        'src/components/ui-v2/eventHandlers/systemHandlers.ts': {
          statements: 90,
          branches: 90,
          functions: 90,
          lines: 90,
        },
        'src/components/ui-v2/eventHandlers/combatHandlers.ts': {
          statements: 90,
          branches: 90,
          functions: 90,
          lines: 90,
        },
        'src/components/ui-v2/utils/stateUpdateUtils.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/components/ui-v2/utils/messageUtils.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/components/ui-v2/utils/roomMergeUtils.ts': { statements: 90, branches: 90, functions: 90, lines: 90 },
        'src/components/ui-v2/hooks/useEventProcessing.ts': { statements: 90, branches: 85, functions: 90, lines: 90 },
      },
      reporter: ['text', 'html', 'json'],
      reportsDirectory: './coverage',
    },
  },
}));
