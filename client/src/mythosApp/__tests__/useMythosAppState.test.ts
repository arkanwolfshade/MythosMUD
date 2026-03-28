import { renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { useMythosAppState } from '../useMythosAppState';

const hoisted = vi.hoisted(() => ({
  memoryStart: vi.fn(),
  memoryStop: vi.fn(),
  restoreSessionMock: vi.fn(),
  authFormMock: vi.fn(),
}));

vi.mock('../../utils/memoryMonitor.js', () => ({
  memoryMonitor: {
    start: hoisted.memoryStart,
    stop: hoisted.memoryStop,
  },
}));

vi.mock('../useAuthSessionRestore.js', () => ({
  useAuthSessionRestore: (...args: unknown[]) => hoisted.restoreSessionMock(...args),
}));

vi.mock('../useMythosAuthForm.js', () => ({
  useMythosAuthForm: (...args: unknown[]) => hoisted.authFormMock(...args),
}));

describe('useMythosAppState', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    hoisted.authFormMock.mockReturnValue({
      handleLoginClick: vi.fn(async () => undefined),
      handleRegisterClick: vi.fn(async () => undefined),
    });
  });

  it('starts and stops memory monitor with lifecycle', () => {
    const { unmount } = renderHook(() => useMythosAppState());

    expect(hoisted.memoryStart).toHaveBeenCalledTimes(1);

    unmount();

    expect(hoisted.memoryStop).toHaveBeenCalledTimes(1);
  });

  it('wires auth session restore and auth form handlers', () => {
    const { result } = renderHook(() => useMythosAppState());

    expect(hoisted.restoreSessionMock).toHaveBeenCalled();
    expect(hoisted.authFormMock).toHaveBeenCalled();
    expect(typeof result.current.handleLoginClick).toBe('function');
    expect(typeof result.current.handleRegisterClick).toBe('function');
  });
});
