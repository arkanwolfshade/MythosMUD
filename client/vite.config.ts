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

  define: {
    // Remove debug code in production builds
    ...(mode === 'production' && {
      'process.env.NODE_ENV': '"production"',
    }),
  },
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
    // Chunk size warning threshold (500KB)
    chunkSizeWarningLimit: 500,
    rollupOptions: {
      output: {
        // Manual chunk splitting for optimal bundle sizes
        manualChunks: id => {
          // Vendor chunks - separate large dependencies
          if (id.includes('node_modules')) {
            // React and React-DOM together (often used together)
            if (id.includes('react') || id.includes('react-dom')) {
              return 'vendor-react';
            }
            // XState is a large state management library
            if (id.includes('xstate')) {
              return 'vendor-xstate';
            }
            // React Grid Layout is a large component library
            if (id.includes('react-grid-layout')) {
              return 'vendor-grid-layout';
            }
            // Zustand is smaller but still worth separating
            if (id.includes('zustand')) {
              return 'vendor-zustand';
            }
            // All other node_modules go into vendor chunk
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
    port: parseInt(process.env.PORT || '5173'),
    proxy: {
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
    },
  },
}));
