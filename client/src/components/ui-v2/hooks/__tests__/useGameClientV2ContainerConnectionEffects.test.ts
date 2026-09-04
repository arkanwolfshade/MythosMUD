import { renderHook } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { useGameClientV2ContainerConnectionEffects } from '../useGameClientV2ContainerConnectionEffects';
import type { GameClientV2MergedSlice } from '../gameClientV2ContainerTypes';

vi.mock('../emptyOccupantsDiagnostics', () => ({
  runEmptyOccupantsReportIfNeeded: vi.fn(),
}));

function buildSlice(roomId: string | null): GameClientV2MergedSlice {
  return {
    gameState: {
      player: { name: 'ArkanWolfshade' },
      room: roomId ? { id: roomId, name: roomId, description: '', exits: {} } : null,
    },
  } as unknown as GameClientV2MergedSlice;
}

function buildRefs() {
  return {
    sendCommandRef: { current: null },
    roomFirstSetAtRef: { current: null as number | null },
    reportedRoomIdsRef: { current: new Set<string>() },
  } as unknown as Parameters<typeof useGameClientV2ContainerConnectionEffects>[1];
}

describe('useGameClientV2ContainerConnectionEffects settle window (#776)', () => {
  it('sets roomFirstSetAt on the first room and resets it on a room change', () => {
    const refs = buildRefs();
    const { rerender } = renderHook(
      ({ slice }) =>
        useGameClientV2ContainerConnectionEffects(slice, refs, true, vi.fn(), vi.fn().mockResolvedValue(true)),
      { initialProps: { slice: buildSlice('room1') } }
    );

    expect(refs.roomFirstSetAtRef.current).not.toBeNull();

    // Force a distinct Date.now() so the reset is observable rather than coincidentally equal
    // (two renders in the same test can land in the same millisecond).
    vi.spyOn(Date, 'now').mockReturnValue(123456789);
    rerender({ slice: buildSlice('room2') });
    vi.restoreAllMocks();

    expect(refs.roomFirstSetAtRef.current).toBe(123456789);
  });

  it('clears roomFirstSetAt when the room becomes null', () => {
    const refs = buildRefs();
    const { rerender } = renderHook(
      ({ slice }) =>
        useGameClientV2ContainerConnectionEffects(slice, refs, true, vi.fn(), vi.fn().mockResolvedValue(true)),
      { initialProps: { slice: buildSlice('room1') } }
    );

    expect(refs.roomFirstSetAtRef.current).not.toBeNull();

    rerender({ slice: buildSlice(null) });

    expect(refs.roomFirstSetAtRef.current).toBeNull();
  });

  it('does not reset roomFirstSetAt on a re-render with the same room id', () => {
    const refs = buildRefs();
    const { rerender } = renderHook(
      ({ slice }) =>
        useGameClientV2ContainerConnectionEffects(slice, refs, true, vi.fn(), vi.fn().mockResolvedValue(true)),
      { initialProps: { slice: buildSlice('room1') } }
    );

    const firstRoomSetAt = refs.roomFirstSetAtRef.current;
    rerender({ slice: buildSlice('room1') });

    expect(refs.roomFirstSetAtRef.current).toBe(firstRoomSetAt);
  });
});
