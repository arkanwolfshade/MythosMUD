// Vitest config is merged into vite.config.ts (shared plugins and resolve).
// Re-export so scripts that reference vitest.config.ts still resolve.
export { default } from './vite.config';
