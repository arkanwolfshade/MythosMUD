/**
 * @jest-environment jsdom
 */

import '@testing-library/jest-dom';
import { act, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { GameTerminalWithPanels } from '../GameTerminalWithPanels';
import { useGameConnection } from '../../hooks/useGameConnectionRefactored';
import type { UseGameConnectionOptions } from '../../hooks/useGameConnectionRefactored';
vi.mock('../../hooks/useGameConnectionRefactored');

type GameConnectionEvent = Parameters<NonNullable<UseGameConnectionOptions['onEvent']>>[0];

describe('GameTerminalWithPanels Mythos Time', () => {
  const mockUseGameConnection = vi.mocked(useGameConnection);
  let onEvent: ((event: GameConnectionEvent) => void) | null = null;
  const originalFetch = global.fetch;

  beforeEach(() => {
    onEvent = null;
    vi.resetAllMocks();

    mockUseGameConnection.mockImplementation(({ onEvent: eventHandler }) => {
      onEvent = eventHandler ?? null;
      return {
        isConnected: true,
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        connect: vi.fn(),
        disconnect: vi.fn(),
        sendCommand: vi.fn(),
      } as unknown as ReturnType<typeof useGameConnection>;
    });
  });

  afterEach(() => {
    global.fetch = originalFetch;
  });

  it('updates Mythos HUD state when mythos_time_update events are received', async () => {
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        mythos_datetime: '1930-01-05T10:00:00Z',
        mythos_clock: '10:00 Mythos',
        month_name: 'January',
        day_of_month: 5,
        day_name: 'Tertius',
        week_of_month: 1,
        season: 'winter',
        daypart: 'morning',
        is_daytime: true,
        is_witching_hour: false,
        server_timestamp: '2025-11-15T03:00:00Z',
        active_holidays: [],
        upcoming_holidays: [],
        active_schedules: [],
      }),
    }) as unknown as typeof fetch;

    render(<GameTerminalWithPanels playerName="Tester" authToken="token" />);

    expect(onEvent).toBeTruthy();

    const eventPayload: GameConnectionEvent = {
      event_type: 'mythos_time_update',
      sequence_number: 1,
      timestamp: new Date().toISOString(),
      data: {
        mythos_datetime: '1930-01-05T23:00:00Z',
        mythos_clock: '23:00 Mythos',
        month_name: 'January',
        day_of_month: 5,
        day_name: 'Tertius',
        week_of_month: 1,
        season: 'winter',
        daypart: 'witching',
        is_daytime: false,
        is_witching_hour: true,
        server_timestamp: new Date().toISOString(),
        active_holidays: [
          {
            id: 'witching_observance',
            name: 'Witching Observance',
            tradition: 'mythos',
            season: 'winter',
            duration_hours: 24,
            bonus_tags: ['mystic'],
            notes: 'Whispers cling to every threshold.',
          },
        ],
        upcoming_holidays: [],
        active_schedules: [],
      },
    };

    await act(async () => {
      onEvent?.(eventPayload);
    });

    await waitFor(() => expect(screen.getByText(/\[Time]/i)).toBeVisible());
  });
});
