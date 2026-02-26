/**
 * Map API client for MythosMUD.
 *
 * Single place for calling ASCII map and minimap endpoints. Used by
 * AsciiMinimap and AsciiMapViewer so URL construction, fetch, and
 * response validation live in one layer.
 */

import type { AsciiMapApiResponse } from '../utils/apiTypeGuards';
import { isAsciiMapApiResponse } from '../utils/apiTypeGuards';
import { getVersionedApiBaseUrl } from '../utils/config';

export interface FetchAsciiMinimapParams {
  plane: string;
  zone: string;
  subZone?: string;
  currentRoomId?: string;
  size?: number;
  baseUrl?: string;
  authToken?: string;
}

export interface FetchAsciiMapParams {
  plane: string;
  zone: string;
  subZone?: string;
  currentRoomId?: string;
  viewportX?: number;
  viewportY?: number;
  viewportWidth?: number;
  viewportHeight?: number;
  baseUrl?: string;
  authToken?: string;
}

function buildMapUrl(baseUrl: string, path: string, params: Record<string, string | number | undefined>): string {
  const base = baseUrl && baseUrl.trim() !== '' ? baseUrl : getVersionedApiBaseUrl();
  const fullPath = `${base.replace(/\/$/, '')}${path}`;
  const url = /^https?:\/\//i.test(base) ? new URL(fullPath) : new URL(fullPath, window.location.origin);
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== '') {
      url.searchParams.set(key, String(value));
    }
  }
  return url.toString();
}

function buildHeaders(authToken?: string): HeadersInit {
  const headers: HeadersInit = {
    'Content-Type': 'application/json',
  };
  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`;
  }
  return headers;
}

/**
 * Fetch ASCII minimap HTML from the server.
 *
 * @returns Validated response with map_html
 * @throws Error on non-OK response or invalid response shape
 */
export async function fetchAsciiMinimap(params: FetchAsciiMinimapParams): Promise<AsciiMapApiResponse> {
  const { plane, zone, subZone, currentRoomId, size = 5, baseUrl = '', authToken } = params;

  const url = buildMapUrl(baseUrl, '/api/maps/ascii/minimap', {
    plane,
    zone,
    sub_zone: subZone,
    current_room_id: currentRoomId,
    size,
  });

  const response = await fetch(url, { headers: buildHeaders(authToken) });

  if (!response.ok) {
    throw new Error(`Failed to fetch minimap: ${response.statusText}`);
  }

  const raw: unknown = await response.json();
  if (!isAsciiMapApiResponse(raw)) {
    throw new Error('Invalid minimap response from server');
  }

  return raw;
}

/**
 * Fetch full ASCII map HTML from the server.
 *
 * @returns Validated response with map_html and optional viewport
 * @throws Error on non-OK response or invalid response shape
 */
export async function fetchAsciiMap(params: FetchAsciiMapParams): Promise<AsciiMapApiResponse> {
  const {
    plane,
    zone,
    subZone,
    currentRoomId,
    viewportX = 0,
    viewportY = 0,
    viewportWidth = 80,
    viewportHeight = 24,
    baseUrl = '',
    authToken,
  } = params;

  const url = buildMapUrl(baseUrl, '/api/maps/ascii', {
    plane,
    zone,
    sub_zone: subZone,
    current_room_id: currentRoomId,
    viewport_x: viewportX,
    viewport_y: viewportY,
    viewport_width: viewportWidth,
    viewport_height: viewportHeight,
  });

  const response = await fetch(url, { headers: buildHeaders(authToken) });

  if (!response.ok) {
    throw new Error(`Failed to fetch map: ${response.statusText}`);
  }

  const raw: unknown = await response.json();
  if (!isAsciiMapApiResponse(raw)) {
    throw new Error('Invalid map response from server');
  }

  return raw;
}
