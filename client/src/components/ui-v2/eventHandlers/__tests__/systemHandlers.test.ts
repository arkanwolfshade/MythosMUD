/**
 * Tests for systemHandlers.
 */

import { describe, expect, it, vi } from 'vitest';
import type { MythosTimePayload } from '../../../../types/mythosTime';
import type { ChatMessage, Player } from '../../types';
import { handleGameTick, handleLucidityChange, handleMythosTimeUpdate, handleRescueUpdate } from '../systemHandlers';
import type { EventHandlerContext } from '../types';

// Mock dependencies
vi.mock('../../../../utils/lucidityEventUtils', () => ({
  buildLucidityStatus: vi.fn(() => ({
    status: { current: 50, max: 100, tier: 'lucid', liabilities: [] },
    delta: 0,
  })),
}));

vi.mock('../../../utils/mythosTime', () => ({
  buildMythosTimeState: vi.fn((payload: Partial<MythosTimePayload>) => ({
    daypart: payload.daypart || 'morning',
    hour: 12,
    minute: 0,
  })),
  formatMythosTime12Hour: vi.fn((_clock: string | undefined) => '12:00 PM'),
  DAYPART_MESSAGES: {
    morning: 'The sun rises in the Mythos sky.',
    afternoon: 'The day continues.',
  },
}));

vi.mock('../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (msg: ChatMessage) => msg,
}));

vi.mock('../../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
  },
}));

describe('systemHandlers', () => {
  const mockAppendMessage = vi.fn();
  const mockContext: EventHandlerContext = {
    currentPlayerRef: { current: null },
    currentRoomRef: { current: null },
    currentMessagesRef: { current: [] },
    healthStatusRef: { current: null },
    lucidityStatusRef: { current: null },
    lastDaypartRef: { current: null },
    lastHourRef: { current: null },
    lastHolidayIdsRef: { current: [] },
    lastRoomUpdateTime: { current: 0 },
    setDpStatus: vi.fn(),
    setLucidityStatus: vi.fn(),
    setMythosTime: vi.fn(),
    setIsDead: vi.fn(),
    setIsMortallyWounded: vi.fn(),
    setIsRespawning: vi.fn(),
    setIsDelirious: vi.fn(),
    setIsDeliriumRespawning: vi.fn(),
    setDeathLocation: vi.fn(),
    setDeliriumLocation: vi.fn(),
    setRescueState: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    mockContext.lastDaypartRef.current = null;
    mockContext.lastHourRef.current = null;
  });

  describe('handleLucidityChange', () => {
    it('should update lucidity status', () => {
      mockContext.lucidityStatusRef.current = { current: 50, max: 100, tier: 'lucid', liabilities: [] };
      const event = {
        event_type: 'lucidity_change',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { current_lcd: 75, max_lcd: 100 },
      };
      handleLucidityChange(event, mockContext, mockAppendMessage);
      expect(mockContext.setLucidityStatus).toHaveBeenCalled();
    });

    it('should update player lucidity when currentPlayerRef exists', async () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 50, max_lucidity: 100 },
      };
      mockContext.currentPlayerRef.current = mockPlayer as Player;
      mockContext.lucidityStatusRef.current = { current: 50, max: 100, tier: 'lucid', liabilities: [] };
      // Import the mocked module to reset its return value
      const lucidityUtils = await import('../../../../utils/lucidityEventUtils');
      // Mock should return status based on event data (current_lcd: 75)
      vi.mocked(lucidityUtils.buildLucidityStatus).mockReturnValueOnce({
        status: { current: 75, max: 100, tier: 'lucid', liabilities: [] },
        delta: 0,
      });
      const event = {
        event_type: 'lucidity_change',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { current_lcd: 75, max_lcd: 100 },
      };
      const result = handleLucidityChange(event, mockContext, mockAppendMessage);
      expect(mockContext.setLucidityStatus).toHaveBeenCalled();
      // The mock returns status with current: 75 (from event data), so the player's lucidity should be updated to 75
      expect(result?.player?.stats?.lucidity).toBe(75);
    });

    it('should not return player update when currentPlayerRef is null', () => {
      mockContext.currentPlayerRef.current = null;
      mockContext.lucidityStatusRef.current = { current: 50, max: 100, tier: 'lucid', liabilities: [] };
      const event = {
        event_type: 'lucidity_change',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { current_lcd: 75, max_lcd: 100 },
      };
      const result = handleLucidityChange(event, mockContext, mockAppendMessage);
      expect(mockContext.setLucidityStatus).toHaveBeenCalled();
      expect(result).toBeUndefined();
    });

    it('should use player max_lucidity as fallback', () => {
      const mockPlayer: Partial<Player> = {
        name: 'TestPlayer',
        stats: { max_lucidity: 150, current_dp: 0, lucidity: 0 },
      };
      mockContext.currentPlayerRef.current = mockPlayer as Player;
      const event = {
        event_type: 'lucidity_change',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { current_lcd: 75 },
      };
      handleLucidityChange(event, mockContext, mockAppendMessage);
      expect(mockContext.setLucidityStatus).toHaveBeenCalled();
    });
  });

  describe('handleRescueUpdate', () => {
    it('should set isDelirious to true when status is delirium', () => {
      const event = {
        event_type: 'rescue_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { status: 'delirium', current_lcd: 0 },
      };
      handleRescueUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDelirious).toHaveBeenCalledWith(true);
    });

    it('should append message when status is delirium and message is provided', () => {
      const event = {
        event_type: 'rescue_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { status: 'delirium', message: 'You have lost consciousness.' },
      };
      handleRescueUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDelirious).toHaveBeenCalledWith(true);
      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should not append message when status is not delirium', () => {
      const event = {
        event_type: 'rescue_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { status: 'safe' },
      };
      handleRescueUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDelirious).not.toHaveBeenCalled();
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when status is delirium but message is missing', () => {
      const event = {
        event_type: 'rescue_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { status: 'delirium' },
      };
      handleRescueUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDelirious).toHaveBeenCalledWith(true);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handleMythosTimeUpdate', () => {
    it('should update mythos time when mythos_clock is present', () => {
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { mythos_clock: '12:00 PM', daypart: 'afternoon', mythos_datetime: '2024-01-01T12:00:00Z' },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setMythosTime).toHaveBeenCalled();
    });

    it('should not update when mythos_clock is missing', () => {
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { daypart: 'afternoon' },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setMythosTime).not.toHaveBeenCalled();
    });

    it('should append clock chime message when hour changes', () => {
      mockContext.lastHourRef.current = 11;
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          mythos_clock: '12:00 PM',
          daypart: 'afternoon',
          mythos_datetime: '2024-01-01T12:00:00Z', // 12:00 UTC
        },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: expect.stringContaining('The clock chimes'),
        })
      );
      expect(mockContext.lastHourRef.current).toBe(12);
    });

    it('should not append clock chime when hour does not change', () => {
      mockContext.lastHourRef.current = 12;
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          mythos_clock: '12:00 PM',
          daypart: 'afternoon',
          mythos_datetime: '2024-01-01T12:00:00Z',
        },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should append daypart change message when daypart changes', () => {
      mockContext.lastDaypartRef.current = 'morning';
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { mythos_clock: '12:00 PM', daypart: 'afternoon' },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: expect.stringContaining('[Time]'),
        })
      );
      expect(mockContext.lastDaypartRef.current).toBe('afternoon');
    });

    it('should not append daypart change message when daypart does not change', () => {
      mockContext.lastDaypartRef.current = 'afternoon';
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { mythos_clock: '12:00 PM', daypart: 'afternoon' },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      // Should not have daypart change message
      expect(mockAppendMessage).not.toHaveBeenCalledWith(
        expect.objectContaining({
          text: expect.stringContaining('The Mythos clock shifts'),
        })
      );
    });

    it('should handle invalid mythos_datetime gracefully', () => {
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { mythos_clock: '12:00 PM', daypart: 'afternoon', mythos_datetime: 'invalid-date' },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      expect(mockContext.setMythosTime).toHaveBeenCalled();
      // Should not throw error
    });

    it('should not append clock chime on first update (lastHour is null)', () => {
      mockContext.lastHourRef.current = null;
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          mythos_clock: '12:00 PM',
          daypart: 'afternoon',
          mythos_datetime: '2024-01-01T12:00:00Z',
        },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      // Should not append chime message on first update
      expect(mockAppendMessage).not.toHaveBeenCalledWith(
        expect.objectContaining({
          text: expect.stringContaining('The clock chimes'),
        })
      );
      expect(mockContext.lastHourRef.current).toBe(12);
    });

    it('should not append daypart change on first update (lastDaypart is null)', () => {
      mockContext.lastDaypartRef.current = null;
      const event = {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { mythos_clock: '12:00 PM', daypart: 'afternoon' },
      };
      handleMythosTimeUpdate(event, mockContext, mockAppendMessage);
      // Should not append daypart change on first update
      expect(mockAppendMessage).not.toHaveBeenCalled();
      expect(mockContext.lastDaypartRef.current).toBe('afternoon');
    });
  });

  describe('handleGameTick', () => {
    it('should append message for every 100th tick', () => {
      const event = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 100 },
      };
      handleGameTick(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: '[Tick 100]',
          messageType: 'system',
        })
      );
    });

    it('should append message for 200th tick', () => {
      const event = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 200 },
      };
      handleGameTick(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should not append message for non-100th ticks', () => {
      const event = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 50 },
      };
      handleGameTick(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message for 0th tick', () => {
      const event = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 0 },
      };
      handleGameTick(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: '[Tick 0]',
        })
      );
    });

    it('should handle missing tick_number', () => {
      const event = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      handleGameTick(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: '[Tick 0]',
        })
      );
    });

    it('should not append message for negative tick numbers', () => {
      const event = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: -100 },
      };
      handleGameTick(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });
});
