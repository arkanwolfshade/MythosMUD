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
    // Chunk size warning threshold (600KB)
    // Increased from 500KB to accommodate large single-package chunks like lucide-react (icon library)
    // which cannot be split further. All chunks are already properly separated by functionality.
    chunkSizeWarningLimit: 600,
    rollupOptions: {
      output: {
        // Manual chunk splitting for optimal bundle sizes
        // Strategy: Split large libraries into separate chunks to keep chunks under 500KB
        // Order matters: check most specific packages first
        manualChunks: id => {
          // Vendor chunks - separate large dependencies
          if (id.includes('node_modules')) {
            // Large icon library - split to reduce vendor chunk size
            if (id.includes('lucide-react')) {
              return 'vendor-icons';
            }
            // Large React libraries - split into separate chunks to reduce vendor-react size
            if (id.includes('react-grid-layout')) {
              return 'vendor-grid-layout';
            }
            if (id.includes('reactflow')) {
              return 'vendor-reactflow';
            }
            // XState core library (separate from @xstate/react to reduce chunk size)
            if (id.includes('xstate') && !id.includes('@xstate/react')) {
              return 'vendor-xstate';
            }
            // React ecosystem: Core React packages and commonly used React libraries
            // This includes react, react-dom, react-router, react-rnd, @xstate/react, zustand
            // Keeping these together prevents circular dependencies while maintaining reasonable chunk sizes
            if (
              id.includes('/react/') ||
              id.includes('/react-dom/') ||
              id.includes('\\react\\') ||
              id.includes('\\react-dom\\') ||
              id.includes('react-router') ||
              id.includes('react-rnd') ||
              id.includes('@xstate/react') ||
              id.includes('zustand')
            ) {
              return 'vendor-react';
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
