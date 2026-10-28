import { afterEach, beforeEach, vi } from 'vitest';

import { fetchSpy } from './app.test.mocks';
import { createMockLoginResponse } from './professionSystemErrorHandling.test.helpers';

export { createMockLoginResponse, fetchSpy };

export function registerAppTestHooks(): void {
  beforeEach(() => {
    vi.clearAllMocks();
    fetchSpy.mockClear();
    localStorage.clear();
  });

  afterEach(() => {
    fetchSpy.mockReset();
  });
}
