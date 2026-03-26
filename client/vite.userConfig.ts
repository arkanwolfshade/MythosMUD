/// <reference types="vitest/config" />
/**
 * Main Vite user config object (merged plugins, resolve, build, server, test).
 * Split from vite.config.ts for static analysis (Lizard mis-counts nested object literals).
 */
import react from '@vitejs/plugin-react';
import path from 'path';
import type { UserConfig } from 'vite';

import { configureForwardAuthorization } from './vite.proxyAuthorization.js';
import { vitestTestOptions } from './vite.vitestOptions.js';

export function createViteUserConfig(mode: string): UserConfig {
  return {
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
    // Vite 8 transforms TS/JSX with Oxc; top-level `esbuild` is deprecated and triggers a
    // warning when merged with plugin-provided `oxc` options.
    oxc: {
      target: 'es2020',
    },
    build: {
      // Source maps: false for production (smaller bundles), true for dev
      sourcemap: mode === 'development',
      // Vite 8 default; Oxc minifier drops debugger in production by default
      minify: 'oxc',
      // Target modern browsers
      target: 'es2020',
      // Chunk size warning threshold (KB, pre-gzip). vendor-icons is lucide-react alone (~610KB+ minified)
      // because EldritchIcon uses `import * as LucideIcons` (full library for dynamic iconMap lookup).
      // Raised from 600 when lucide minor updates pushed vendor-icons just over the old limit.
      chunkSizeWarningLimit: 700,
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
          configure: configureForwardAuthorization,
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
          configure: configureForwardAuthorization,
        },
      },
    },
    test: vitestTestOptions,
  };
}
