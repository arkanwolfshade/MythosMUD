import { test, expect, Page } from '@playwright/test';
import { installRealtimeFakes, loginWithRealCredentials } from './utils/mockAuth';

async function captureWebSocket(page: Page): Promise<{ getLast: () => { url: string; protocols: string[] } | null }> {
  await page.addInitScript(() => {
    class CapturingWebSocket {
      url: string;
      protocols: string[];
      readyState = 1;
      onopen: ((ev: unknown) => void) | null = null;
      onmessage: ((ev: { data: string }) => void) | null = null;
      onerror: ((ev: unknown) => void) | null = null;
      onclose: ((ev: unknown) => void) | null = null;
      constructor(url: string, protocols?: string | string[]) {
        this.url = url;
        this.protocols = Array.isArray(protocols) ? protocols : protocols ? [protocols] : [];
        (window as unknown as { __capturedWS: CapturingWebSocket[] }).__capturedWS =
          (window as unknown as { __capturedWS: CapturingWebSocket[] }).__capturedWS || [];
        (window as unknown as { __capturedWS: CapturingWebSocket[] }).__capturedWS.push(this);
        setTimeout(() => this.onopen && this.onopen({}), 0);
      }
      send(_data: string) {}
      close() {}
    }
    (window as unknown as { WebSocket: unknown }).WebSocket = CapturingWebSocket as unknown as typeof WebSocket;
  });

  return {
    getLast: async () =>
      (await page.evaluate(() => {
        const list = (window as unknown as { __capturedWS?: Array<{ url: string; protocols: string[] }> }).__capturedWS;
        return list && list.length ? list[list.length - 1] : null;
      })) as { url: string; protocols: string[] } | null,
  };
}

test('WebSocket connects via relative /api/ws and uses subprotocol token', async ({ page }) => {
  await installRealtimeFakes(page);
  const wsCapture = await captureWebSocket(page);

  // Navigate and login through standard helper (ensures hooks initialize)
  await page.goto('/');
  await loginWithRealCredentials(page, { username: 'testuser', password: 'testpass' });

  // Allow app to initialize realtime connections
  await page.waitForTimeout(200);

  const last = await wsCapture.getLast();
  expect(last).not.toBeNull();
  if (!last) return;

  expect(last.url).toContain('/api/ws');
  expect(last.url).not.toContain('localhost:54731');
  // Expect protocols to contain bearer and a token-like value
  expect(last.protocols[0].toLowerCase()).toBe('bearer');
  expect(last.protocols.length).toBeGreaterThan(1);
});
