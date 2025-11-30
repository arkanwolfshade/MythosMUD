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

    it('should fall back to message when WebSocket error has no user_friendly', () => {
      // Test line 73: when user_friendly is missing, should use message
      const wsError = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed message',
      } as WebSocketErrorResponse;
      expect(getErrorMessage(wsError)).toBe('Connection failed message');
    });

    it('should handle SSE error with message but no user_friendly', () => {
      // Test line 73 for SSE format
      const sseError = {
        type: 'error',
        error_type: 'sse_error',
        message: 'SSE connection lost',
      } as SSEErrorResponse;
      expect(getErrorMessage(sseError)).toBe('SSE connection lost');
    });

    it('should handle WebSocket error when isErrorResponse is true but error field check fails', () => {
      // Test line 72: When isErrorResponse returns true but 'error' in response is false
      // This should hit the WebSocket/SSE format branch
      const wsError = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
        user_friendly: 'Unable to connect',
      } as WebSocketErrorResponse;
      // This should match isErrorResponse and then hit line 72 branch
      expect(isErrorResponse(wsError)).toBe(true);
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

    it('should handle WebSocket error type when isErrorResponse is true but error field check fails', () => {
      // Test line 106: When isErrorResponse returns true but 'error' in response is false
      // This should hit the WebSocket/SSE format branch
      const wsError = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
      } as WebSocketErrorResponse;
      // This should match isErrorResponse and then hit line 106 branch
      expect(isErrorResponse(wsError)).toBe(true);
      expect(getErrorType(wsError)).toBe('connection_error');
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

    it('should return empty object when WebSocket error has no details', () => {
      // Test line 126: when details is missing in WebSocket/SSE format
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
      };
      expect(getErrorDetails(wsError)).toEqual({});
    });

    it('should return empty object when SSE error has no details', () => {
      // Test line 126 for SSE format
      const sseError: SSEErrorResponse = {
        type: 'error',
        error_type: 'sse_error',
        message: 'SSE connection lost',
      };
      expect(getErrorDetails(sseError)).toEqual({});
    });

    it('should handle WebSocket error details when isErrorResponse is true but error field check fails', () => {
      // Test line 125: When isErrorResponse returns true but 'error' in response is false
      // This should hit the WebSocket/SSE format branch
      const wsError = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
        details: { retry_after: 30 },
      } as WebSocketErrorResponse;
      // This should match isErrorResponse and then hit line 125 branch
      expect(isErrorResponse(wsError)).toBe(true);
      expect(getErrorDetails(wsError)).toEqual({ retry_after: 30 });
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

    it('should return empty object for non-error responses', () => {
      expect(getErrorDetails({})).toEqual({});
      expect(getErrorDetails(null)).toEqual({});
      expect(getErrorDetails('string')).toEqual({});
      expect(getErrorDetails(123)).toEqual({});
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
      // Test line 137: when isErrorResponse returns true but 'error' in response is false
      // This tests the branch where the response is a WebSocket/SSE error (no error field)
      const wsError: WebSocketErrorResponse = {
        type: 'error',
        error_type: 'connection_error',
        message: 'Connection failed',
      };
      expect(isErrorResponse(wsError)).toBe(true);
      expect(getErrorSeverity(wsError)).toBe('medium');
    });

    it('should return medium when isErrorResponse returns false', () => {
      // Test line 137: the false branch when isErrorResponse returns false
      expect(getErrorSeverity(null)).toBe('medium');
      expect(getErrorSeverity({})).toBe('medium');
      expect(getErrorSeverity('string')).toBe('medium');
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

    it('should identify missing_required_field as validation error', () => {
      const error: StandardErrorResponse = {
        error: {
          type: 'missing_required_field',
          message: 'Field required',
        },
      };
      expect(isValidationError(error)).toBe(true);
    });

    it('should identify invalid_format as validation error', () => {
      const error: StandardErrorResponse = {
        error: {
          type: 'invalid_format',
          message: 'Invalid format',
        },
      };
      expect(isValidationError(error)).toBe(true);
    });
  });

  describe('isErrorResponse - Edge Cases', () => {
    it('should reject objects with error field that is not an object', () => {
      expect(isErrorResponse({ error: 'string' })).toBe(false);
      expect(isErrorResponse({ error: null })).toBe(false);
      expect(isErrorResponse({ error: 123 })).toBe(false);
    });

    it('should reject objects with error object missing type', () => {
      expect(isErrorResponse({ error: { message: 'test' } })).toBe(false);
    });

    it('should reject objects with error object missing message', () => {
      expect(isErrorResponse({ error: { type: 'test' } })).toBe(false);
    });

    it('should reject objects with type=error but missing error_type', () => {
      expect(isErrorResponse({ type: 'error', message: 'test' })).toBe(false);
    });

    it('should reject objects with type=error but missing message', () => {
      expect(isErrorResponse({ type: 'error', error_type: 'test' })).toBe(false);
    });

    it('should reject objects with type=error but error_type is not string', () => {
      expect(isErrorResponse({ type: 'error', error_type: 123, message: 'test' })).toBe(false);
    });

    it('should reject objects with type=error but message is not string', () => {
      expect(isErrorResponse({ type: 'error', error_type: 'test', message: 123 })).toBe(false);
    });
  });

  describe('getErrorMessage - Edge Cases', () => {
    it('should handle error object with empty string message', () => {
      // Empty strings are falsy, so it falls through to default
      expect(getErrorMessage({ message: '' })).toBe('An unknown error occurred');
    });

    it('should handle error object with empty string detail', () => {
      // Empty strings are falsy, so it falls through to default
      expect(getErrorMessage({ detail: '' })).toBe('An unknown error occurred');
    });

    it('should handle error object with empty string error field', () => {
      // Empty strings are falsy, so it falls through to default
      expect(getErrorMessage({ error: '' })).toBe('An unknown error occurred');
    });

    it('should handle error object with all empty fields', () => {
      // All empty strings are falsy, so it falls through to default
      expect(getErrorMessage({ message: '', detail: '', error: '' })).toBe('An unknown error occurred');
    });

    it('should prioritize message over detail and error', () => {
      expect(getErrorMessage({ message: 'message', detail: 'detail', error: 'error' })).toBe('message');
    });

    it('should fall back to detail when message is empty', () => {
      expect(getErrorMessage({ message: '', detail: 'detail', error: 'error' })).toBe('detail');
    });

    it('should fall back to error when message and detail are empty', () => {
      expect(getErrorMessage({ message: '', detail: '', error: 'error' })).toBe('error');
    });
  });
});
