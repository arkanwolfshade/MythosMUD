/** Shared configuration for DI migration validation E2E tests. */

export const BASE_URL = 'http://127.0.0.1:5173';
export const SERVER_URL = 'http://localhost:54768';
/** Versioned API base for v1 endpoints (use for all direct API requests in E2E). */
export const SERVER_API_V1 = `${SERVER_URL}/v1`;
export const TEST_USERNAME = 'ArkanWolfshade';
export const TEST_PASSWORD = 'Cthulhu1';
export const ADMIN_USERNAME = 'ArkanWolfshade';

/** Resolved relative to each spec under tests/e2e/di-migration/ (same dir as legacy monolith). */
export const AUTH_STORAGE_PATH = '../.auth/user-auth.json';
export const ADMIN_STORAGE_PATH = '../.auth/admin-auth.json';
