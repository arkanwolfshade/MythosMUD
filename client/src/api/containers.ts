/**
 * Container REST client (#711): open/transfer/close/loot-all.
 *
 * State does not come from these responses -- it arrives via the container.* websocket events
 * (see eventLog/projectorHandlersContainers.ts). These calls report success/failure only; on
 * success the caller does nothing further and waits for the event.
 */

import { getVersionedApiBaseUrl } from '../utils/config';

export type TransferDirection = 'to_container' | 'to_player';

export class ContainerApiError extends Error {
  readonly status: number;

  constructor(message: string, status: number) {
    super(message);
    this.name = 'ContainerApiError';
    this.status = status;
  }
}

function buildHeaders(authToken: string): HeadersInit {
  return { 'Content-Type': 'application/json', Authorization: `Bearer ${authToken}` };
}

function baseUrl(apiBase?: string): string {
  const base = apiBase && apiBase.trim() !== '' ? apiBase : getVersionedApiBaseUrl();
  return base.replace(/\/$/, '');
}

async function postContainerRequest(
  path: string,
  authToken: string,
  body: Record<string, unknown>,
  apiBase?: string
): Promise<unknown> {
  const response = await fetch(`${baseUrl(apiBase)}/api/containers/${path}`, {
    method: 'POST',
    headers: buildHeaders(authToken),
    body: JSON.stringify(body),
  });
  if (!response.ok) {
    const detail = await response.text().catch(() => '');
    let message = detail;
    try {
      const parsed = JSON.parse(detail) as { detail?: string };
      if (parsed.detail) message = parsed.detail;
    } catch {
      // detail wasn't JSON; use the raw text
    }
    throw new ContainerApiError(message || `Request failed (${response.status})`, response.status);
  }
  return response.status === 204 ? null : response.json();
}

/** Open a container for interaction. Idempotent for the same player; rejects with 409 if another
 * player already holds it (message names the holder). State arrives via container.opened. */
export async function openContainer(authToken: string, containerId: string, apiBase?: string): Promise<void> {
  await postContainerRequest('open', authToken, { container_id: containerId }, apiBase);
}

/** Move a stack between the player's inventory and an open container. State arrives via
 * container.updated and, for to_player, inventory_updated. */
export async function transferItem(
  authToken: string,
  params: {
    containerId: string;
    mutationToken: string;
    direction: TransferDirection;
    stack: Record<string, unknown>;
    quantity: number;
  },
  apiBase?: string
): Promise<void> {
  await postContainerRequest(
    'transfer',
    authToken,
    {
      container_id: params.containerId,
      mutation_token: params.mutationToken,
      direction: params.direction,
      stack: params.stack,
      quantity: params.quantity,
    },
    apiBase
  );
}

/** Close an open container session. State arrives via container.closed. */
export async function closeContainer(
  authToken: string,
  containerId: string,
  mutationToken: string,
  apiBase?: string
): Promise<void> {
  await postContainerRequest('close', authToken, { container_id: containerId, mutation_token: mutationToken }, apiBase);
}

/** Move every eligible item from the container into the player's inventory. State arrives via
 * container.updated and inventory_updated. */
export async function lootAll(
  authToken: string,
  containerId: string,
  mutationToken: string,
  apiBase?: string
): Promise<void> {
  await postContainerRequest(
    'loot-all',
    authToken,
    { container_id: containerId, mutation_token: mutationToken },
    apiBase
  );
}
