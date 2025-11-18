/**
 * Configuration utilities for MythosMUD client
 * Centralizes environment variable access and provides defaults
 */

/**
 * Get the API base URL from environment variables
 * Falls back to relative URLs for production (same origin)
 * Falls back to localhost:54731 for development
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

  // Development default
  return 'http://localhost:54731';
}

/**
 * Get the API base URL (exported constant for convenience)
 */
export const API_BASE_URL = getApiBaseUrl();
