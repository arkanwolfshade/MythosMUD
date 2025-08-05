import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: parseInt(process.env.PORT || '5173'),
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, ''),
      },
      '/events': {
        target: 'http://127.0.0.1:54731',
        changeOrigin: true,
        ws: true,
      },
      '/ws': {
        target: 'ws://127.0.0.1:54731',
        changeOrigin: true,
        ws: true,
      },
    },
  },
});
