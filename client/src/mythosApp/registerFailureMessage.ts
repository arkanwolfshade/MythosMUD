import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { isObject } from './guards.js';

function formatValidationErrors(validationErrors: Array<Record<string, unknown>>): {
  passwordMessages: string[];
  otherMessages: string;
} {
  const passwordErrors = validationErrors.filter(err => {
    const loc = err.loc;
    if (Array.isArray(loc)) {
      const fieldPath = loc.map(String).join('.').toLowerCase();
      return fieldPath.includes('password');
    }
    return false;
  });

  if (passwordErrors.length > 0) {
    const passwordMessages = passwordErrors.map(err => {
      const msg = String(err.msg || err.message || 'Validation error');
      if (msg.includes('at least') || msg.includes('8 characters')) {
        return 'Password must be at least 8 characters long';
      }
      if (msg.includes('exceed') || msg.includes('1024')) {
        return 'Password must not exceed 1024 characters';
      }
      if (msg.includes('empty')) {
        return 'Password cannot be empty';
      }
      return msg;
    });
    return {
      passwordMessages,
      otherMessages: '',
    };
  }

  const errorMessages = validationErrors
    .map(err => {
      const loc = err.loc ? (Array.isArray(err.loc) ? err.loc.join('.') : String(err.loc)) : '';
      const msg = err.msg || err.message || 'Validation error';
      const fieldName = loc.split('.').pop()?.replace('_', ' ') || 'field';
      return `${fieldName}: ${msg}`;
    })
    .join('; ');
  return { passwordMessages: [], otherMessages: errorMessages };
}

function messageFromValidationDetail(detail: unknown, fallbackMessage: string): string | null {
  if (Array.isArray(detail)) {
    const validationErrors = detail as Array<Record<string, unknown>>;
    const { passwordMessages, otherMessages } = formatValidationErrors(validationErrors);
    if (passwordMessages.length > 0) {
      return `${passwordMessages.join('. ')}. Password requirements: at least 8 characters, maximum 1024 characters.`;
    }
    return otherMessages || fallbackMessage;
  }

  if (typeof detail === 'string') {
    return detail;
  }

  return null;
}

function messageFromNestedError(errorValue: unknown): string | null {
  if (isObject(errorValue) && 'message' in errorValue) {
    return String((errorValue as Record<string, unknown>).message);
  }
  return null;
}

export function registerFailureMessage(status: number, rawData: unknown, defaultMessage: string): string {
  if (isErrorResponse(rawData)) {
    return getErrorMessage(rawData);
  }
  if (!isObject(rawData)) {
    return defaultMessage;
  }
  const data = rawData;

  if (status === 422) {
    return messageFromValidationDetail(data.detail, defaultMessage) ?? defaultMessage;
  }

  const nestedErrorMessage = messageFromNestedError(data.error);
  if (nestedErrorMessage) {
    return nestedErrorMessage;
  }
  if (typeof data.detail === 'string') {
    return data.detail;
  }

  return defaultMessage;
}
