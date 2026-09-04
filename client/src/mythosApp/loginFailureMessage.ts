import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { isObject } from './guards.js';

export function loginFailureMessage(rawData: unknown, defaultMessage: string): string {
  if (isErrorResponse(rawData)) {
    return getErrorMessage(rawData);
  }
  if (isObject(rawData)) {
    const data = rawData;
    if (typeof data.error === 'object' && data.error !== null && 'message' in data.error) {
      return String((data.error as Record<string, unknown>).message);
    }
    if (typeof data.detail === 'string') {
      return data.detail;
    }
  }
  return defaultMessage;
}
