import react from '@vitejs/plugin-react';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./src/test/setup.ts'],
    exclude: ['tests/**/*', '**/*.spec.ts', '**/*.spec.tsx', 'node_modules/**/*'],
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
        statements: 10,
        branches: 30,
        functions: 60,
        lines: 10,
      },
      reporter: ['text', 'html', 'json'],
      reportsDirectory: './coverage',
    },
  },
});
