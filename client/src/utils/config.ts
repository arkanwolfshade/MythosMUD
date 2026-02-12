/**
 * Configuration utilities for MythosMUD client
 * Centralizes environment variable access and provides defaults
 */

/**
 * Get the API base URL from environment variables
 * Falls back to relative URLs for production (same origin)
 * Falls back to same-origin (empty string) in development so the Vite proxy is used (LAN-friendly)
 *
 * @returns API base URL string
 */
export function getApiBaseUrl(): string {
  // Use VITE_API_URL if provided
  if (import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL;
  }

  // In production, use relative URLs (same origin)
  if (import.meta.env.PROD) {
    return '';
  }

  // Development: use same origin so requests go through Vite proxy. This allows LAN clients
  // (e.g. http://<host-ip>:5173) to reach the API via the proxy; absolute localhost:54731
  // would point at the client machine and fail from another PC.
  return '';
}

/**
 * Get the API base URL (exported constant for convenience)
 */
export const API_BASE_URL = getApiBaseUrl();

/**
 * Get the versioned API base URL for v1 endpoints (base + /v1).
 * Use for all REST and WebSocket API calls so the client targets /v1/... paths.
 *
 * @returns Versioned API base string (e.g. '' -> '/v1', 'http://host:54731' -> 'http://host:54731/v1')
 */
export function getVersionedApiBaseUrl(): string {
  const base = getApiBaseUrl();
  return base ? `${base}/v1` : '/v1';
}

/** Versioned API base for v1 endpoints (use for all API fetch/WS URLs). */
export const API_V1_BASE = getVersionedApiBaseUrl();
