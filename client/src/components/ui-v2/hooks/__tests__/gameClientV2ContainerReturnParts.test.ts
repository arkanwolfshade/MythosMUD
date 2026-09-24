import { describe, expect, it, vi } from 'vitest';
import {
  buildHandlerPublicFields,
  buildNetPublicFields,
  buildSliceAndPropsPublicFields,
} from '../gameClientV2ContainerReturnParts';
import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from '../gameClientV2ContainerTypes';
import type { GameClientV2NetworkPhase } from '../useGameClientV2ContainerNetworkPhase';

function buildSlice(gameState: Record<string, unknown> = {}): GameClientV2MergedSlice {
  return { gameState } as unknown as GameClientV2MergedSlice;
}

describe('buildSliceAndPropsPublicFields', () => {
  it('applies defaults when optional death/delirium/lucidity/logout fields are absent', () => {
    const props = { playerName: 'ArkanWolfshade', authToken: 'tok' } as GameClientV2ContainerProps;
    const result = buildSliceAndPropsPublicFields(props, buildSlice());

    expect(result.isLoggingOut).toBe(false);
    expect(result.lucidityStatus).toBeNull();
    expect(result.isDead).toBe(false);
    expect(result.deathLocation).toBe('Unknown Location');
    expect(result.isDelirious).toBe(false);
    expect(result.deliriumLocation).toBe('Unknown Location');
  });

  it('passes through real values instead of defaulting when present', () => {
    const props = { playerName: 'ArkanWolfshade', authToken: 'tok', isLoggingOut: true } as GameClientV2ContainerProps;
    const slice = buildSlice({
      lucidityStatus: { current: 5, max: 10 },
      isDead: true,
      deathLocation: 'The Attic',
      isDelirious: true,
      deliriumLocation: 'The Cellar',
    });

    const result = buildSliceAndPropsPublicFields(props, slice);

    expect(result.isLoggingOut).toBe(true);
    expect(result.lucidityStatus).toEqual({ current: 5, max: 10 });
    expect(result.isDead).toBe(true);
    expect(result.deathLocation).toBe('The Attic');
    expect(result.isDelirious).toBe(true);
    expect(result.deliriumLocation).toBe('The Cellar');
  });
});

describe('buildNetPublicFields', () => {
  it('passes network phase fields through unchanged', () => {
    const net = {
      sendMessage: vi.fn(),
      isConnected: true,
      isConnecting: false,
      error: null,
      reconnectAttempts: 2,
    } as unknown as GameClientV2NetworkPhase;

    expect(buildNetPublicFields(net)).toEqual(net);
  });
});

describe('buildHandlerPublicFields', () => {
  it('passes handlers and active effects through unchanged', () => {
    const handleLogout = vi.fn();
    const handleCommandSubmit = vi.fn();
    const handleChatMessage = vi.fn();
    const handleClearMessages = vi.fn();
    const handleClearHistory = vi.fn();
    const handleRespawn = vi.fn();
    const handleDeliriumRespawn = vi.fn();
    const activeEffects = [{ name: 'eldritch-glow' }] as never;

    const result = buildHandlerPublicFields(
      handleLogout,
      handleCommandSubmit,
      handleChatMessage,
      handleClearMessages,
      handleClearHistory,
      handleRespawn,
      handleDeliriumRespawn,
      activeEffects
    );

    expect(result).toEqual({
      handleLogout,
      handleCommandSubmit,
      handleChatMessage,
      handleClearMessages,
      handleClearHistory,
      handleRespawn,
      handleDeliriumRespawn,
      activeEffects,
    });
  });
});
