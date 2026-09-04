import { afterEach, beforeEach, vi } from 'vitest';

import { fetchSpy } from './app.test.mocks';
import { createMockLoginResponse, createMockProfessions } from './professionSystemErrorHandling.test.helpers';

export { createMockLoginResponse, createMockProfessions, fetchSpy };

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

export function createMockJsonResponse(body: unknown, ok = true, status = 200) {
  return {
    ok,
    status,
    json: vi.fn().mockResolvedValue(body),
  };
}

export function createMockProfessionsFetchResponse() {
  return createMockJsonResponse({ professions: createMockProfessions() });
}

export function mockFetchForAuthAndProfessions(authPath: 'login' | 'register', authResponseBody: unknown): void {
  const authResponse = createMockJsonResponse(authResponseBody);
  const professionsResponse = createMockProfessionsFetchResponse();

  fetchSpy.mockImplementation((url: string | URL | Request) => {
    const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
    if (urlString.includes(`/auth/${authPath}`)) {
      return Promise.resolve(authResponse as unknown as Response);
    }
    if (urlString.includes('/professions')) {
      return Promise.resolve(professionsResponse as unknown as Response);
    }
    return Promise.reject(new Error(`Unexpected URL: ${urlString}`));
  });
}
