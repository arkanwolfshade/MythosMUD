/// <reference types="vitest/config" />
/**
 * MythosMUD client Vite config (intentionally non-minimal per project needs).
 *
 * - Proxy: `/v1`, `/api`, `/auth`, `/game`, `/professions` forward to the local game server
 *   (see server.port); required for dev against FastAPI/WebSocket.
 * - build.rollupOptions.manualChunks: splits lucide-react, react-grid-layout, and reactflow to
 *   avoid one giant vendor chunk and reduce circular shared-dep issues.
 * - server.warmup: pre-transforms `main.tsx` and `App.tsx` for faster cold start.
 * - oxc + es2020: aligns with Vite 8 defaults for TS/JSX transform.
 *
 * Implementation lives in vite.userConfig.ts so this entry stays small for static analysis.
 */
// TODO: Implement AST-based console removal plugin to selectively remove
// console.debug, console.log, console.info, console.trace while preserving
// console.error and console.warn for production error logging.
// Previous regex-based approach was disabled due to breaking complex expressions.

// https://vite.dev/config/
import { defineConfig } from 'vite';

import { createViteUserConfig } from './vite.userConfig.js';

export default defineConfig(({ mode }) => createViteUserConfig(mode));
