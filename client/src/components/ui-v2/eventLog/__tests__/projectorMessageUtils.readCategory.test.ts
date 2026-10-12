/**
 * readCategory is the one place the client validates a server-assigned category: a valid value passes
 * through, a missing or unknown one falls back to command.output with a once-per-event-type dev warning.
 */
import { afterEach, describe, expect, it, vi } from 'vitest';
import { MESSAGE_CATEGORIES } from '../../../../types/messageCategory';
import { logger } from '../../../../utils/logger';
import { readCategory } from '../projectorMessageUtils';

describe('readCategory', () => {
  afterEach(() => {
    vi.restoreAllMocks();
    vi.unstubAllEnvs();
  });

  it.each(MESSAGE_CATEGORIES)('passes the known category %s through without warning', category => {
    const warn = vi.spyOn(logger, 'warn');
    expect(readCategory({ category }, `valid_${category}`)).toBe(category);
    expect(warn).not.toHaveBeenCalled();
  });

  it('falls back to command.output and warns when the server sent no category', () => {
    const warn = vi.spyOn(logger, 'warn');
    expect(readCategory({}, 'missing_event')).toBe('command.output');
    expect(readCategory(undefined, 'missing_event_undefined_data')).toBe('command.output');
    expect(warn).toHaveBeenCalledTimes(2);
    expect(warn.mock.calls[0][1]).toContain('missing_event');
    expect(warn.mock.calls[0][1]).toContain('no message category');
  });

  it.each([['bogus.kind'], [42], [null], [{ nested: true }]])(
    'falls back to command.output for the unknown value %j',
    value => {
      const warn = vi.spyOn(logger, 'warn');
      expect(readCategory({ category: value }, `unknown_${JSON.stringify(value)}`)).toBe('command.output');
      expect(warn).toHaveBeenCalledTimes(1);
      expect(warn.mock.calls[0][1]).toContain('unknown message category');
    }
  );

  it('warns once per event type, not once per message', () => {
    const warn = vi.spyOn(logger, 'warn');
    readCategory({}, 'repeating_event');
    readCategory({ category: 'nope' }, 'repeating_event');
    readCategory({}, 'repeating_event');
    expect(warn).toHaveBeenCalledTimes(1);
    readCategory({}, 'another_event');
    expect(warn).toHaveBeenCalledTimes(2);
  });

  it('still falls back but stays silent outside development', () => {
    vi.stubEnv('DEV', false);
    const warn = vi.spyOn(logger, 'warn');
    expect(readCategory({}, 'silent_in_production')).toBe('command.output');
    expect(warn).not.toHaveBeenCalled();
  });
});
