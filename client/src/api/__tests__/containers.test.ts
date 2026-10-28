/**
 * Unit tests for container API client (open/transfer/close/loot-all).
 * Guards against regressions in URL building, auth headers, request bodies, and error surfacing.
 */

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { closeContainer, ContainerApiError, lootAll, openContainer, transferItem } from '../containers';

describe('containers API', () => {
  const originalFetch = globalThis.fetch;

  beforeEach(() => {
    globalThis.fetch = vi.fn();
  });

  afterEach(() => {
    globalThis.fetch = originalFetch;
  });

  function okResponse(body: unknown = {}) {
    return { ok: true, status: 200, json: async () => body, text: async () => JSON.stringify(body) } as Response;
  }

  describe('openContainer', () => {
    it('POSTs to /api/containers/open with the container_id and Bearer auth', async () => {
      vi.mocked(fetch).mockResolvedValue(okResponse());
      await openContainer('tok', 'container-1', 'https://api.example.com/v1');

      const [url, init] = (fetch as ReturnType<typeof vi.fn>).mock.calls[0];
      expect(url).toBe('https://api.example.com/v1/api/containers/open');
      expect(init.method).toBe('POST');
      expect(init.headers.Authorization).toBe('Bearer tok');
      expect(JSON.parse(init.body)).toEqual({ container_id: 'container-1' });
    });

    it('throws ContainerApiError with the server detail on a non-ok response', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        status: 409,
        text: async () => JSON.stringify({ detail: 'Ithaqua already has this container open.' }),
      } as Response);

      await expect(openContainer('tok', 'container-1')).rejects.toMatchObject({
        name: 'ContainerApiError',
        status: 409,
        message: 'Ithaqua already has this container open.',
      });
    });

    it('falls back to a generic message when the error body is not JSON', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        status: 500,
        text: async () => '',
      } as Response);

      await expect(openContainer('tok', 'container-1')).rejects.toThrow(/Request failed \(500\)/);
    });
  });

  describe('transferItem', () => {
    it('POSTs mutation_token, direction, stack, and quantity', async () => {
      vi.mocked(fetch).mockResolvedValue(okResponse());
      await transferItem('tok', {
        containerId: 'c1',
        mutationToken: 'mt-1',
        direction: 'to_player',
        stack: { item_id: 'coin', item_instance_id: 'inst-1' },
        quantity: 2,
      });

      const [url, init] = (fetch as ReturnType<typeof vi.fn>).mock.calls[0];
      expect(url).toContain('/api/containers/transfer');
      expect(JSON.parse(init.body)).toEqual({
        container_id: 'c1',
        mutation_token: 'mt-1',
        direction: 'to_player',
        stack: { item_id: 'coin', item_instance_id: 'inst-1' },
        quantity: 2,
      });
    });
  });

  describe('closeContainer', () => {
    it('POSTs container_id and mutation_token', async () => {
      vi.mocked(fetch).mockResolvedValue(okResponse({ status: 'closed' }));
      await closeContainer('tok', 'c1', 'mt-1');

      const [url, init] = (fetch as ReturnType<typeof vi.fn>).mock.calls[0];
      expect(url).toContain('/api/containers/close');
      expect(JSON.parse(init.body)).toEqual({ container_id: 'c1', mutation_token: 'mt-1' });
    });
  });

  describe('lootAll', () => {
    it('POSTs container_id and mutation_token', async () => {
      vi.mocked(fetch).mockResolvedValue(okResponse());
      await lootAll('tok', 'c1', 'mt-1');

      const [url, init] = (fetch as ReturnType<typeof vi.fn>).mock.calls[0];
      expect(url).toContain('/api/containers/loot-all');
      expect(JSON.parse(init.body)).toEqual({ container_id: 'c1', mutation_token: 'mt-1' });
    });
  });

  it('ContainerApiError carries the HTTP status', () => {
    const err = new ContainerApiError('nope', 403);
    expect(err.status).toBe(403);
    expect(err.message).toBe('nope');
  });
});
