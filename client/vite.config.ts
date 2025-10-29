import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

// https://vite.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [react()],
  define: {
    // Remove debug code in production builds
    ...(mode === 'production' && {
      'process.env.NODE_ENV': '"production"',
    }),
  },
  esbuild: {
    // Remove console.debug calls in production
    ...(mode === 'production' && {
      drop: ['console', 'debugger'],
    }),
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
    },
  },
}));
