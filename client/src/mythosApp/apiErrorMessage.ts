import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { isObject } from './guards.js';

export function errorMessageFromApiBody(rawData: unknown, fallback: string): string {
  if (isErrorResponse(rawData)) {
    return getErrorMessage(rawData);
  }
  if (!isObject(rawData)) {
    return fallback;
  }
  const errorData = rawData;
  if (typeof errorData.detail === 'object' && errorData.detail !== null && 'message' in errorData.detail) {
    return String((errorData.detail as Record<string, unknown>).message);
  }
  if (typeof errorData.detail === 'string') {
    return errorData.detail;
  }
  return fallback;
}
