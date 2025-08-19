import { describe, expect, it } from 'vitest';
import {
  ErrorTypes,
  formatErrorForDisplay,
  getErrorDetails,
  getErrorMessage,
  getErrorSeverity,
  getErrorType,
  isAuthenticationError,
  isErrorResponse,
  isErrorType,
  isNetworkError,
  isValidationError,
  type SSEErrorResponse,
  type StandardErrorResponse,
  type WebSocketErrorResponse,
} from './errorHandler';

describe('errorHandler', () => {
  describe('isErrorResponse', () => {
    it('should identify API error responses', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
          user_friendly: 'Please check your input',
          severity: 'medium',
        },
      };
      expect(isErrorResponse(apiError)).toBe(true);
    });

    it('should identify WebSocket error responses', () => {
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
        user_friendly: 'Unable to connect to server',
      };
      expect(isErrorResponse(wsError)).toBe(true);
    });

    it('should identify SSE error responses', () => {
      const sseError: SSEErrorResponse = {
        type: 'error',
        error_type: 'sse_error',
        message: 'SSE connection failed',
        user_friendly: 'Real-time connection lost',
      };
      expect(isErrorResponse(sseError)).toBe(true);
    });

    it('should reject non-error responses', () => {
      expect(isErrorResponse(null)).toBe(false);
      expect(isErrorResponse(undefined)).toBe(false);
      expect(isErrorResponse('string')).toBe(false);
      expect(isErrorResponse({ success: true })).toBe(false);
      expect(isErrorResponse({ error: 'not an object' })).toBe(false);
    });
  });

  describe('getErrorMessage', () => {
    it('should extract user-friendly message from API error', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Technical error message',
          user_friendly: 'User-friendly message',
        },
      };
      expect(getErrorMessage(apiError)).toBe('User-friendly message');
    });

    it('should fall back to technical message if no user-friendly message', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Technical error message',
        },
      };
      expect(getErrorMessage(apiError)).toBe('Technical error message');
    });

    it('should extract message from WebSocket error', () => {
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
        user_friendly: 'Unable to connect',
      };
      expect(getErrorMessage(wsError)).toBe('Unable to connect');
    });

    it('should handle string errors', () => {
      expect(getErrorMessage('Simple error message')).toBe('Simple error message');
    });

    it('should handle generic error objects', () => {
      expect(getErrorMessage({ message: 'Generic error' })).toBe('Generic error');
      expect(getErrorMessage({ detail: 'Detail error' })).toBe('Detail error');
      expect(getErrorMessage({ error: 'Error field' })).toBe('Error field');
    });

    it('should return default message for unknown errors', () => {
      expect(getErrorMessage({})).toBe('An unknown error occurred');
      expect(getErrorMessage(null)).toBe('An unknown error occurred');
    });
  });

  describe('getErrorType', () => {
    it('should extract type from API error', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };
      expect(getErrorType(apiError)).toBe('validation_error');
    });

    it('should extract type from WebSocket error', () => {
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
      };
      expect(getErrorType(wsError)).toBe('connection_error');
    });

    it('should return unknown_error for non-error responses', () => {
      expect(getErrorType({})).toBe('unknown_error');
      expect(getErrorType(null)).toBe('unknown_error');
    });
  });

  describe('getErrorDetails', () => {
    it('should extract details from API error', () => {
      const details = { field: 'username', reason: 'required' };
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
          details,
        },
      };
      expect(getErrorDetails(apiError)).toEqual(details);
    });

    it('should extract details from WebSocket error', () => {
      const details = { retry_after: 30 };
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
        details,
      };
      expect(getErrorDetails(wsError)).toEqual(details);
    });

    it('should return empty object for errors without details', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };
      expect(getErrorDetails(apiError)).toEqual({});
    });
  });

  describe('getErrorSeverity', () => {
    it('should extract severity from API error', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
          severity: 'high',
        },
      };
      expect(getErrorSeverity(apiError)).toBe('high');
    });

    it('should return medium as default severity', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };
      expect(getErrorSeverity(apiError)).toBe('medium');
    });

    it('should return medium for non-API errors', () => {
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
      };
      expect(getErrorSeverity(wsError)).toBe('medium');
    });
  });

  describe('formatErrorForDisplay', () => {
    it('should format API error for display', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Technical message',
          user_friendly: 'User message',
          severity: 'high',
          details: { field: 'username' },
        },
      };
      const result = formatErrorForDisplay(apiError);
      expect(result).toEqual({
        message: 'User message',
        type: 'validation_error',
        severity: 'high',
        details: { field: 'username' },
      });
    });

    it('should format WebSocket error for display', () => {
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
        user_friendly: 'Unable to connect',
        details: { retry_after: 30 },
      };
      const result = formatErrorForDisplay(wsError);
      expect(result).toEqual({
        message: 'Unable to connect',
        type: 'connection_error',
        severity: 'medium',
        details: { retry_after: 30 },
      });
    });
  });

  describe('ErrorTypes', () => {
    it('should contain all expected error types', () => {
      expect(ErrorTypes.AUTHENTICATION_FAILED).toBe('authentication_failed');
      expect(ErrorTypes.VALIDATION_ERROR).toBe('validation_error');
      expect(ErrorTypes.NETWORK_ERROR).toBe('network_error');
      expect(ErrorTypes.SYSTEM_ERROR).toBe('system_error');
    });
  });

  describe('isErrorType', () => {
    it('should check if error is of specific type', () => {
      const apiError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };
      expect(isErrorType(apiError, 'validation_error')).toBe(true);
      expect(isErrorType(apiError, 'authentication_failed')).toBe(false);
    });
  });

  describe('isNetworkError', () => {
    it('should identify network errors', () => {
      const networkError: StandardErrorResponse = {
        error: {
          type: 'network_error',
          message: 'Network failed',
        },
      };
      const connectionError: StandardErrorResponse = {
        error: {
          type: 'connection_error',
          message: 'Connection failed',
        },
      };
      const validationError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };

      expect(isNetworkError(networkError)).toBe(true);
      expect(isNetworkError(connectionError)).toBe(true);
      expect(isNetworkError(validationError)).toBe(false);
    });
  });

  describe('isAuthenticationError', () => {
    it('should identify authentication errors', () => {
      const authError: StandardErrorResponse = {
        error: {
          type: 'authentication_failed',
          message: 'Auth failed',
        },
      };
      const tokenError: StandardErrorResponse = {
        error: {
          type: 'invalid_token',
          message: 'Invalid token',
        },
      };
      const validationError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };

      expect(isAuthenticationError(authError)).toBe(true);
      expect(isAuthenticationError(tokenError)).toBe(true);
      expect(isAuthenticationError(validationError)).toBe(false);
    });
  });

  describe('isValidationError', () => {
    it('should identify validation errors', () => {
      const validationError: StandardErrorResponse = {
        error: {
          type: 'validation_error',
          message: 'Invalid input',
        },
      };
      const invalidInputError: StandardErrorResponse = {
        error: {
          type: 'invalid_input',
          message: 'Invalid input',
        },
      };
      const networkError: StandardErrorResponse = {
        error: {
          type: 'network_error',
          message: 'Network failed',
        },
      };

      expect(isValidationError(validationError)).toBe(true);
      expect(isValidationError(invalidInputError)).toBe(true);
      expect(isValidationError(networkError)).toBe(false);
    });
  });
});
