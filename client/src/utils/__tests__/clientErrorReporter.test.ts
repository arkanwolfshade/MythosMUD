/**
 * Tests for clientErrorReporter.
 */

import { describe, expect, it, vi } from 'vitest';
import { OCCUPANTS_PANEL_EMPTY_PLAYERS, reportClientError } from '../clientErrorReporter';

describe('clientErrorReporter', () => {
  it('should export OCCUPANTS_PANEL_EMPTY_PLAYERS constant', () => {
    expect(OCCUPANTS_PANEL_EMPTY_PLAYERS).toBe('occupants_panel_empty_players');
  });

  it('should send error report without context', () => {
    const sendMessage = vi.fn().mockReturnValue(true);
    const result = reportClientError(sendMessage, OCCUPANTS_PANEL_EMPTY_PLAYERS, 'Players list empty');

    expect(result).toBe(true);
    expect(sendMessage).toHaveBeenCalledWith('client_error_report', {
      error_type: OCCUPANTS_PANEL_EMPTY_PLAYERS,
      message: 'Players list empty',
    });
  });

  it('should send error report with context when provided and non-empty', () => {
    const sendMessage = vi.fn().mockReturnValue(true);
    const context = { room_id: 'room1', player_count: 0 };
    const result = reportClientError(sendMessage, OCCUPANTS_PANEL_EMPTY_PLAYERS, 'Players list empty', context);

    expect(result).toBe(true);
    expect(sendMessage).toHaveBeenCalledWith('client_error_report', {
      error_type: OCCUPANTS_PANEL_EMPTY_PLAYERS,
      message: 'Players list empty',
      context,
    });
  });

  it('should not include context when context is empty object', () => {
    const sendMessage = vi.fn().mockReturnValue(true);
    reportClientError(sendMessage, OCCUPANTS_PANEL_EMPTY_PLAYERS, 'Players list empty', {});

    expect(sendMessage).toHaveBeenCalledWith('client_error_report', {
      error_type: OCCUPANTS_PANEL_EMPTY_PLAYERS,
      message: 'Players list empty',
    });
  });

  it('should return false when sendMessage returns false', () => {
    const sendMessage = vi.fn().mockReturnValue(false);
    const result = reportClientError(sendMessage, OCCUPANTS_PANEL_EMPTY_PLAYERS, 'Test');

    expect(result).toBe(false);
  });
});
