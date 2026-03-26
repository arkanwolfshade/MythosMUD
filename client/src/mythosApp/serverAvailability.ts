import { isObject } from './guards.js';

const CONNECTION_ERROR_SUBSTRINGS = [
  'failed to fetch',
  'network error',
  'network request failed',
  'connection refused',
  'connection reset',
  'connection closed',
  'connection timeout',
  'err_connection_refused',
  'err_connection_reset',
  'err_connection_aborted',
] as const;

export function isServerUnavailable(error: unknown, response: Response | null): boolean {
  if (!response) {
    if (!(error instanceof Error)) {
      return true;
    }
    const errorMessage = error.message.toLowerCase();
    return CONNECTION_ERROR_SUBSTRINGS.some(err => errorMessage.includes(err));
  }

  if (response.status >= 500 && response.status < 600) {
    return true;
  }

  if (error instanceof Error) {
    const errorMessage = error.message.toLowerCase();
    return CONNECTION_ERROR_SUBSTRINGS.some(err => errorMessage.includes(err));
  }

  return false;
}

/** Patterns used when a string error from a child screen should force return-to-login. */
export const SERVER_UNAVAILABLE_ERROR_SUBSTRINGS = [
  'failed to fetch',
  'network error',
  'network request failed',
  'connection refused',
  'connection reset',
  'connection closed',
  'connection timeout',
  'server is unavailable',
  'service unavailable',
  'bad gateway',
  'gateway timeout',
  'failed to connect to server',
] as const;

export function stringIndicatesServerUnavailable(message: string): boolean {
  const lower = message.toLowerCase();
  return SERVER_UNAVAILABLE_ERROR_SUBSTRINGS.some(p => lower.includes(p));
}

export function errorDetailString(rawData: unknown): string {
  if (!isObject(rawData)) {
    return 'Unknown error';
  }
  const detail = rawData.detail;
  return typeof detail === 'string' ? detail : 'Unknown error';
}
