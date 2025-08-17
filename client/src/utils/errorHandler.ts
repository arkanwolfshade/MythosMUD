/**
 * Standardized error handling utilities for MythosMUD client.
 *
 * This module provides utilities to handle the standardized error format
 * returned by the MythosMUD server across all communication channels.
 */

export interface StandardErrorResponse {
  error: {
    type: string;
    message: string;
    user_friendly?: string;
    details?: Record<string, unknown>;
    severity?: string;
    timestamp?: string;
  };
}

export interface WebSocketErrorResponse {
  type: 'error';
  error_type: string;
  message: string;
  user_friendly?: string;
  details?: Record<string, unknown>;
}

export interface SSEErrorResponse {
  type: 'error';
  error_type: string;
  message: string;
  user_friendly?: string;
  details?: Record<string, unknown>;
}

export type ErrorResponse = StandardErrorResponse | WebSocketErrorResponse | SSEErrorResponse;

/**
 * Check if a response is a standardized error response.
 */
export function isErrorResponse(response: unknown): response is ErrorResponse {
  if (!response || typeof response !== 'object') {
    return false;
  }

  const obj = response as Record<string, unknown>;

  // Check for API error format
  if (obj.error && typeof obj.error === 'object') {
    const errorObj = obj.error as Record<string, unknown>;
    return typeof errorObj.type === 'string' && typeof errorObj.message === 'string';
  }

  // Check for WebSocket/SSE error format
  if (obj.type === 'error' && typeof obj.error_type === 'string' && typeof obj.message === 'string') {
    return true;
  }

  return false;
}

/**
 * Extract user-friendly error message from any error response format.
 */
export function getErrorMessage(response: unknown): string {
  if (isErrorResponse(response)) {
    // API error format
    if ('error' in response && response.error) {
      return response.error.user_friendly || response.error.message;
    }

    // WebSocket/SSE error format
    if ('type' in response && response.type === 'error') {
      return response.user_friendly || response.message;
    }
  }

  // Fallback for non-standardized errors
  if (typeof response === 'string') {
    return response;
  }

  if (response && typeof response === 'object') {
    const obj = response as Record<string, unknown>;
    return (
      (typeof obj.message === 'string' ? obj.message : '') ||
      (typeof obj.detail === 'string' ? obj.detail : '') ||
      (typeof obj.error === 'string' ? obj.error : '') ||
      'An unknown error occurred'
    );
  }

  return 'An unknown error occurred';
}

/**
 * Extract error type from any error response format.
 */
export function getErrorType(response: unknown): string {
  if (isErrorResponse(response)) {
    // API error format
    if ('error' in response && response.error) {
      return response.error.type;
    }

    // WebSocket/SSE error format
    if ('type' in response && response.type === 'error') {
      return response.error_type;
    }
  }

  return 'unknown_error';
}

/**
 * Extract error details from any error response format.
 */
export function getErrorDetails(response: unknown): Record<string, unknown> {
  if (isErrorResponse(response)) {
    // API error format
    if ('error' in response && response.error) {
      return response.error.details || {};
    }

    // WebSocket/SSE error format
    if ('type' in response && response.type === 'error') {
      return response.details || {};
    }
  }

  return {};
}

/**
 * Get error severity from any error response format.
 */
export function getErrorSeverity(response: unknown): string {
  if (isErrorResponse(response)) {
    // API error format
    if ('error' in response && response.error) {
      return response.error.severity || 'medium';
    }
  }

  return 'medium';
}

/**
 * Format error for display to users.
 */
export function formatErrorForDisplay(response: unknown): {
  message: string;
  type: string;
  severity: string;
  details: Record<string, unknown>;
} {
  return {
    message: getErrorMessage(response),
    type: getErrorType(response),
    severity: getErrorSeverity(response),
    details: getErrorDetails(response),
  };
}

/**
 * Common error types for client-side handling.
 */
export const ErrorTypes = {
  // Authentication
  AUTHENTICATION_FAILED: 'authentication_failed',
  AUTHORIZATION_DENIED: 'authorization_denied',
  INVALID_TOKEN: 'invalid_token',
  TOKEN_EXPIRED: 'token_expired',

  // Validation
  VALIDATION_ERROR: 'validation_error',
  INVALID_INPUT: 'invalid_input',
  MISSING_REQUIRED_FIELD: 'missing_required_field',
  INVALID_FORMAT: 'invalid_format',

  // Resources
  RESOURCE_NOT_FOUND: 'resource_not_found',
  RESOURCE_ALREADY_EXISTS: 'resource_already_exists',
  RESOURCE_CONFLICT: 'resource_conflict',

  // Game Logic
  GAME_LOGIC_ERROR: 'game_logic_error',
  INVALID_COMMAND: 'invalid_command',
  INVALID_MOVEMENT: 'invalid_movement',
  PLAYER_NOT_IN_ROOM: 'player_not_in_room',

  // Network
  NETWORK_ERROR: 'network_error',
  CONNECTION_ERROR: 'connection_error',
  TIMEOUT_ERROR: 'timeout_error',

  // Real-time
  WEBSOCKET_ERROR: 'websocket_error',
  SSE_ERROR: 'sse_error',
  MESSAGE_PROCESSING_ERROR: 'message_processing_error',

  // System
  SYSTEM_ERROR: 'system_error',
  INTERNAL_ERROR: 'internal_error',
} as const;

/**
 * Check if an error is a specific type.
 */
export function isErrorType(response: unknown, errorType: string): boolean {
  return getErrorType(response) === errorType;
}

/**
 * Check if an error is a network-related error.
 */
export function isNetworkError(response: unknown): boolean {
  const errorType = getErrorType(response);
  const networkErrorTypes = [
    ErrorTypes.NETWORK_ERROR,
    ErrorTypes.CONNECTION_ERROR,
    ErrorTypes.TIMEOUT_ERROR,
    ErrorTypes.WEBSOCKET_ERROR,
    ErrorTypes.SSE_ERROR,
  ] as const;
  return networkErrorTypes.includes(errorType as (typeof networkErrorTypes)[number]);
}

/**
 * Check if an error is an authentication error.
 */
export function isAuthenticationError(response: unknown): boolean {
  const errorType = getErrorType(response);
  const authErrorTypes = [
    ErrorTypes.AUTHENTICATION_FAILED,
    ErrorTypes.AUTHORIZATION_DENIED,
    ErrorTypes.INVALID_TOKEN,
    ErrorTypes.TOKEN_EXPIRED,
  ] as const;
  return authErrorTypes.includes(errorType as (typeof authErrorTypes)[number]);
}

/**
 * Check if an error is a validation error.
 */
export function isValidationError(response: unknown): boolean {
  const errorType = getErrorType(response);
  const validationErrorTypes = [
    ErrorTypes.VALIDATION_ERROR,
    ErrorTypes.INVALID_INPUT,
    ErrorTypes.MISSING_REQUIRED_FIELD,
    ErrorTypes.INVALID_FORMAT,
  ] as const;
  return validationErrorTypes.includes(errorType as (typeof validationErrorTypes)[number]);
}
