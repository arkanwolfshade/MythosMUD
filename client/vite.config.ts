import react from '@vitejs/plugin-react';
import path from 'path';
import type { Plugin } from 'vite';
import { defineConfig } from 'vite';

// Plugin to ensure Authorization header is forwarded for /professions proxy
const professionsProxyPlugin = (): Plugin => ({
  name: 'professions-proxy-auth',
  configureServer(server) {
    // Add middleware BEFORE proxy to capture Authorization header
    server.middlewares.use('/professions', (req, _res, next) => {
      // Log incoming request headers for debugging
      const authHeader = req.headers.authorization || req.headers.Authorization;
      if (authHeader) {
        // Ensure the header is preserved in the request object
        req.headers.authorization = authHeader as string;
        req.headers.Authorization = authHeader as string;
        console.log('[Vite Plugin] /professions middleware - Authorization header found:', {
          hasAuth: !!authHeader,
          authPreview: authHeader.toString().substring(0, 30),
        });
      } else {
        console.log('[Vite Plugin] /professions middleware - NO Authorization header');
      }
      next();
    });
  },
});

// TODO: Implement AST-based console removal plugin to selectively remove
// console.debug, console.log, console.info, console.trace while preserving
// console.error and console.warn for production error logging.
// Previous regex-based approach was disabled due to breaking complex expressions.

// https://vite.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [
    react(),
    professionsProxyPlugin(),
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
      '/professions': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
        configure: (proxy, _options) => {
          // Access the http-proxy instance to ensure Authorization header is forwarded
          proxy.on('proxyReq', (proxyReq, req) => {
            // Get Authorization header (check both cases)
            const authHeader = req.headers.authorization || req.headers.Authorization;

            // Explicitly set the Authorization header on the proxy request
            if (authHeader) {
              proxyReq.setHeader('Authorization', authHeader as string);
              console.log('[Vite Proxy] /professions proxyReq - Setting Authorization header', {
                url: req.url,
                method: req.method,
                authPreview: (authHeader as string).substring(0, 30),
              });
            } else {
              console.log('[Vite Proxy] /professions proxyReq - NO Authorization header found', {
                url: req.url,
                method: req.method,
                allHeaders: Object.keys(req.headers),
                headerValues: Object.entries(req.headers).map(([k, v]) => [
                  k,
                  typeof v === 'string' ? v.substring(0, 30) : String(v),
                ]),
              });
            }
          });
        },
      },
    },
  },
}));
