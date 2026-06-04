import type { APIResponse, Page } from '@playwright/test';

import { SERVER_API_V1 } from '../constants';

export async function testAPIEndpoint(
  page: Page,
  method: 'GET' | 'POST' | 'DELETE',
  endpoint: string,
  body?: unknown
): Promise<APIResponse> {
  const fetchOptions: { method: string; headers: Record<string, string>; data?: unknown } = {
    method,
    headers: {
      'Content-Type': 'application/json',
    },
  };
  if (body) {
    fetchOptions.data = body;
  }
  return page.request.fetch(`${SERVER_API_V1}${endpoint}`, fetchOptions);
}
