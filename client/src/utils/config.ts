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
