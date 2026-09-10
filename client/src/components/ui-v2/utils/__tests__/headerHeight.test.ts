import { describe, expect, it } from 'vitest';
import type { MythosTimeState } from '../../../../types/mythosTime';
import { hasFlavorRow, headerHeightClass } from '../headerHeight';

describe('headerHeight', () => {
  const baseMythosTime: MythosTimeState = {
    mythos_datetime: '1928-01-01T12:00:00Z',
    mythos_clock: '12:00:00',
    month_name: 'January',
    day_of_month: 1,
    day_name: 'Sunday',
    week_of_month: 1,
    season: 'Winter',
    daypart: 'midday',
    is_daytime: true,
    is_witching_hour: false,
    server_timestamp: '2025-01-01T12:00:00Z',
    active_holidays: [],
    upcoming_holidays: [],
    formatted_date: 'January 1, 1928',
  };

  const witchingMythosTime: MythosTimeState = { ...baseMythosTime, is_witching_hour: true };
  const holidayMythosTime: MythosTimeState = {
    ...baseMythosTime,
    active_holidays: [
      {
        id: 'hol_hallowmas',
        name: 'Hallowmas',
        tradition: 'mythos',
        season: 'autumn',
        duration_hours: 24,
        bonus_tags: [],
        notes: null,
      },
    ],
  };

  describe('hasFlavorRow', () => {
    it('is false when mythos time is null', () => {
      expect(hasFlavorRow(null)).toBe(false);
    });

    it('is false on an ordinary day', () => {
      expect(hasFlavorRow(baseMythosTime)).toBe(false);
    });

    it('is true during witching hour', () => {
      expect(hasFlavorRow(witchingMythosTime)).toBe(true);
    });

    it('is true with an active holiday', () => {
      expect(hasFlavorRow(holidayMythosTime)).toBe(true);
    });
  });

  describe('headerHeightClass', () => {
    it('returns the collapsed height regardless of mythos time', () => {
      expect(headerHeightClass(true, witchingMythosTime)).toEqual({ header: 'h-8', padding: 'pt-8', offset: 'top-8' });
    });

    it('returns the ordinary expanded height with no flavor content', () => {
      expect(headerHeightClass(false, baseMythosTime)).toEqual({
        header: 'h-12',
        padding: 'pt-12',
        offset: 'top-12',
      });
    });

    it('returns the tall expanded height during witching hour', () => {
      expect(headerHeightClass(false, witchingMythosTime)).toEqual({
        header: 'h-20',
        padding: 'pt-20',
        offset: 'top-20',
      });
    });

    it('returns the tall expanded height with an active holiday', () => {
      expect(headerHeightClass(false, holidayMythosTime)).toEqual({
        header: 'h-20',
        padding: 'pt-20',
        offset: 'top-20',
      });
    });

    it('returns the ordinary expanded height when mythos time is null', () => {
      expect(headerHeightClass(false, null)).toEqual({ header: 'h-12', padding: 'pt-12', offset: 'top-12' });
    });
  });
});
