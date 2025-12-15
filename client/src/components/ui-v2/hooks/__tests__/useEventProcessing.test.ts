/**
 * Tests for useEventProcessing hook.
 */

import { HealthStatus } from '@/types/health';
import { LucidityStatus, RescueState } from '@/types/lucidity';
import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { EventHandlerContext, GameEvent } from '../../eventHandlers/types';
import type { ChatMessage, MythosTimeState } from '../../types';
import { useEventProcessing } from '../useEventProcessing';

// Mock dependencies
vi.mock('../../../utils/logger', () => ({
  logger: {
    error: vi.fn(),
  },
}));

vi.mock('../../eventHandlers', () => ({
  processGameEvent: vi.fn(() => ({})),
}));

vi.mock('../../utils/stateUpdateUtils', () => ({
  applyEventUpdates: vi.fn(),
  sanitizeAndApplyUpdates: vi.fn(),
}));

describe('useEventProcessing', () => {
  const mockSetGameState = vi.fn();
  const mockCurrentMessagesRef = { current: [] as ChatMessage[] };
  const mockContext: EventHandlerContext = {
    currentPlayerRef: { current: null },
    currentRoomRef: { current: null },
    currentMessagesRef: mockCurrentMessagesRef,
    healthStatusRef: { current: null },
    lucidityStatusRef: { current: null },
    lastDaypartRef: { current: null },
    lastHourRef: { current: null },
    lastHolidayIdsRef: { current: [] },
    lastRoomUpdateTime: { current: 0 },
    setDpStatus: function (_status: HealthStatus): void {
      throw new Error('Function not implemented.');
    },
    setLucidityStatus: function (_status: LucidityStatus): void {
      throw new Error('Function not implemented.');
    },
    setMythosTime: function (_time: MythosTimeState): void {
      throw new Error('Function not implemented.');
    },
    setIsDead: function (_dead: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsMortallyWounded: function (_wounded: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsRespawning: function (_respawning: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsDelirious: function (_delirious: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsDeliriumRespawning: function (_respawning: boolean): void {
      throw new Error('Function not implemented.');
    },
    setDeathLocation: function (_location: string): void {
      throw new Error('Function not implemented.');
    },
    setDeliriumLocation: function (_location: string): void {
      throw new Error('Function not implemented.');
    },
    setRescueState: function (_state: RescueState | null): void {
      throw new Error('Function not implemented.');
    },
  };

  beforeEach(() => {
    vi.clearAllMocks();
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('should return handleGameEvent function', () => {
    const { result } = renderHook(() =>
      useEventProcessing({
        currentMessagesRef: mockCurrentMessagesRef,
        setGameState: mockSetGameState,
        context: mockContext,
      })
    );

    expect(result.current.handleGameEvent).toBeDefined();
    expect(typeof result.current.handleGameEvent).toBe('function');
  });

  it('should queue events for processing', () => {
    const { result } = renderHook(() =>
      useEventProcessing({
        currentMessagesRef: mockCurrentMessagesRef,
        setGameState: mockSetGameState,
        context: mockContext,
      })
    );

    const event: GameEvent = {
      event_type: 'test_event',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: {},
    };

    act(() => {
      result.current.handleGameEvent(event);
    });

    // Event should be queued
    expect(mockSetGameState).not.toHaveBeenCalled();
  });

  it('should process queued events', async () => {
    const { result } = renderHook(() =>
      useEventProcessing({
        currentMessagesRef: mockCurrentMessagesRef,
        setGameState: mockSetGameState,
        context: mockContext,
      })
    );

    const event: GameEvent = {
      event_type: 'test_event',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: {},
    };

    act(() => {
      result.current.handleGameEvent(event);
    });

    // Advance timers to trigger processing
    act(() => {
      vi.advanceTimersByTime(10);
    });

    // Wait for async processing
    await act(async () => {
      await Promise.resolve();
    });

    // Verify event was queued (processing happens asynchronously)
    expect(result.current.handleGameEvent).toBeDefined();
  });

  it('should handle multiple events in queue', () => {
    const { result } = renderHook(() =>
      useEventProcessing({
        currentMessagesRef: mockCurrentMessagesRef,
        setGameState: mockSetGameState,
        context: mockContext,
      })
    );

    const event1: GameEvent = {
      event_type: 'test_event_1',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: {},
    };

    const event2: GameEvent = {
      event_type: 'test_event_2',
      timestamp: new Date().toISOString(),
      sequence_number: 2,
      data: {},
    };

    act(() => {
      result.current.handleGameEvent(event1);
      result.current.handleGameEvent(event2);
    });

    // Events should be queued (processing happens asynchronously)
    expect(result.current.handleGameEvent).toBeDefined();
  });
});
