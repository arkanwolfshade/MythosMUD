/**
 * Shared test utilities for messageHandlers tests.
 */

import { HealthStatus } from '@/types/health';
import { LucidityStatus, RescueState } from '@/types/lucidity';
import { vi } from 'vitest';
import type { MythosTimeState } from '../../types';
import type { EventHandlerContext } from '../types';

// Mock dependencies
vi.mock('../../../utils/logger', () => ({
  logger: {
    error: vi.fn(),
  },
}));

vi.mock('../../../utils/messageTypeUtils', () => ({
  determineMessageType: vi.fn(() => 'system'),
}));

vi.mock('../../../utils/statusParser', () => ({
  parseStatusResponse: vi.fn(() => ({})),
  convertToPlayerInterface: vi.fn(() => ({ id: 'player1', name: 'Player' })),
}));

vi.mock('../../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (message: unknown) => message,
}));

/**
 * Create a mock context for event handlers.
 */
export const createMockContext = (overrides: Partial<EventHandlerContext> = {}): EventHandlerContext => ({
  currentPlayerRef: { current: null },
  currentRoomRef: { current: null },
  currentMessagesRef: { current: [] },
  healthStatusRef: { current: null },
  lucidityStatusRef: { current: null },
  lastDaypartRef: { current: null },
  lastHourRef: { current: null },
  lastQuarterHourRef: { current: null },
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
  ...overrides,
});

/**
 * Create a mock appendMessage function.
 */
export const createMockAppendMessage = () => vi.fn();
