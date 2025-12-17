/**
 * Tests for csrfProtection module.
 */

import { beforeEach, describe, expect, it, vi } from 'vitest';
import { csrfProtection } from '../security';
import { setupSecurityMocks } from './security.test-utils';

describe('CSRF Protection', () => {
  beforeEach(() => {
    setupSecurityMocks();
  });

  it('should generate CSRF token', () => {
    const token = csrfProtection.generateToken();

    expect(token).toBeDefined();
    expect(typeof token).toBe('string');
    expect(token.length).toBeGreaterThan(0);
  });

  it('should validate CSRF token', () => {
    const token = csrfProtection.generateToken();

    expect(csrfProtection.validateToken(token)).toBe(true);
    expect(csrfProtection.validateToken('invalid-token')).toBe(false);
  });

  it('should add CSRF token to request headers', () => {
    const headers = csrfProtection.addTokenToHeaders({});

    expect(headers['X-CSRF-Token']).toBeDefined();
    expect(typeof headers['X-CSRF-Token']).toBe('string');
    expect(headers['X-CSRF-Token'].length).toBeGreaterThan(0);
  });

  it('should add CSRF token to existing headers', () => {
    const existingHeaders = { 'Content-Type': 'application/json', Authorization: 'Bearer token' };
    const headers = csrfProtection.addTokenToHeaders(existingHeaders);

    expect(headers['X-CSRF-Token']).toBeDefined();
    expect(headers['Content-Type']).toBe('application/json');
    expect(headers['Authorization']).toBe('Bearer token');
  });

  it('should validate null and empty string tokens', () => {
    expect(csrfProtection.validateToken(null as unknown as string)).toBe(false);
    expect(csrfProtection.validateToken(undefined as unknown as string)).toBe(false);
    expect(csrfProtection.validateToken('')).toBe(false);
  });

  it('should handle CSRF token expiry', () => {
    const token = csrfProtection.generateToken(1);

    expect(csrfProtection.validateToken(token)).toBe(true);

    vi.useFakeTimers();
    vi.advanceTimersByTime(2000);

    expect(csrfProtection.validateToken(token)).toBe(false);

    vi.useRealTimers();
  });

  it('should generate token with custom expiry', () => {
    const token = csrfProtection.generateToken(7200);
    expect(token).toBeDefined();
    expect(typeof token).toBe('string');
  });

  it('should handle validation of non-existent token', () => {
    expect(csrfProtection.validateToken('non-existent-token-xyz')).toBe(false);
  });

  it('should clean up expired tokens when generating new token', () => {
    vi.useFakeTimers();

    const token1 = csrfProtection.generateToken(1);
    expect(csrfProtection.validateToken(token1)).toBe(true);

    vi.advanceTimersByTime(2000);

    const token2 = csrfProtection.generateToken(3600);

    expect(csrfProtection.validateToken(token1)).toBe(false);
    expect(csrfProtection.validateToken(token2)).toBe(true);

    vi.useRealTimers();
  });

  it('should handle token validation when token is exactly expired', () => {
    vi.useFakeTimers();

    const token = csrfProtection.generateToken(1);
    expect(csrfProtection.validateToken(token)).toBe(true);

    vi.advanceTimersByTime(1001);

    expect(csrfProtection.validateToken(token)).toBe(false);
    expect(csrfProtection.validateToken(token)).toBe(false);

    vi.useRealTimers();
  });
});
