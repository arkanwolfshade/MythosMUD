import { describe, expect, it } from 'vitest';
import {
  buildMythosTimeState,
  formatMythosTime12Hour,
  formatMythosDateTime12Hour,
  DAYPART_MESSAGES,
} from '../mythosTime';
import type { MythosTimePayload } from '../../types/mythosTime';

describe('MythosTime Utilities', () => {
  describe('buildMythosTimeState', () => {
    it('should build state with formatted date', () => {
      // Arrange
      const payload: MythosTimePayload = {
        month_name: 'September',
        day_of_month: 21,
        clock: '14:00',
        daypart: 'afternoon',
        active_holidays: [],
      };

      // Act
      const state = buildMythosTimeState(payload);

      // Assert
      expect(state.formatted_date).toBe('September 21');
      expect(state.month_name).toBe('September');
      expect(state.day_of_month).toBe(21);
    });

    it('should append active holidays to formatted date', () => {
      // Arrange
      const payload: MythosTimePayload = {
        month_name: 'October',
        day_of_month: 31,
        clock: '20:00',
        daypart: 'night',
        active_holidays: [
          { name: 'Halloween', description: 'Spooky day' },
          { name: 'All Hallows Eve', description: 'Another spooky day' },
        ],
      };

      // Act
      const state = buildMythosTimeState(payload);

      // Assert
      expect(state.formatted_date).toBe('October 31 - Halloween, All Hallows Eve');
    });

    it('should handle empty active holidays array', () => {
      // Arrange
      const payload: MythosTimePayload = {
        month_name: 'January',
        day_of_month: 1,
        clock: '00:00',
        daypart: 'witching',
        active_holidays: [],
      };

      // Act
      const state = buildMythosTimeState(payload);

      // Assert
      expect(state.formatted_date).toBe('January 1');
    });

    it('should preserve all payload properties', () => {
      // Arrange
      const payload: MythosTimePayload = {
        month_name: 'March',
        day_of_month: 15,
        clock: '12:00',
        daypart: 'midday',
        active_holidays: [],
      };

      // Act
      const state = buildMythosTimeState(payload);

      // Assert
      expect(state.clock).toBe('12:00');
      expect(state.daypart).toBe('midday');
    });
  });

  describe('formatMythosTime12Hour', () => {
    it('should convert 24-hour format to 12-hour AM format', () => {
      // Arrange
      const clockString = '09:30 Mythos';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('9:30 AM');
    });

    it('should convert 24-hour format to 12-hour PM format', () => {
      // Arrange
      const clockString = '14:45 Mythos';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('2:45 PM');
    });

    it('should handle midnight (00:00)', () => {
      // Arrange
      const clockString = '00:00 Mythos';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('12:00 AM');
    });

    it('should handle noon (12:00)', () => {
      // Arrange
      const clockString = '12:00 Mythos';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('12:00 PM');
    });

    it('should handle 23:59', () => {
      // Arrange
      const clockString = '23:59 Mythos';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('11:59 PM');
    });

    it('should handle clock string without Mythos suffix', () => {
      // Arrange
      const clockString = '15:30';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('3:30 PM');
    });

    it('should return default for undefined input', () => {
      // Act
      const formatted = formatMythosTime12Hour(undefined);

      // Assert
      expect(formatted).toBe('--:-- --');
    });

    it('should return default for empty string', () => {
      // Act
      const formatted = formatMythosTime12Hour('');

      // Assert
      expect(formatted).toBe('--:-- --');
    });

    it('should handle invalid format gracefully', () => {
      // Arrange
      const clockString = 'invalid format';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('invalid format'); // Returns as-is after removing Mythos
    });

    it('should handle single digit hours', () => {
      // Arrange
      const clockString = '5:30 Mythos';

      // Act
      const formatted = formatMythosTime12Hour(clockString);

      // Assert
      expect(formatted).toBe('5:30 AM');
    });
  });

  describe('formatMythosDateTime12Hour', () => {
    it('should convert ISO datetime to 12-hour format', () => {
      // Arrange
      const datetimeString = '2024-01-15T14:30:00Z';

      // Act
      const formatted = formatMythosDateTime12Hour(datetimeString);

      // Assert
      expect(formatted).toBe('2:30 PM');
    });

    it('should handle midnight in ISO format', () => {
      // Arrange
      const datetimeString = '2024-01-15T00:00:00Z';

      // Act
      const formatted = formatMythosDateTime12Hour(datetimeString);

      // Assert
      expect(formatted).toBe('12:00 AM');
    });

    it('should handle noon in ISO format', () => {
      // Arrange
      const datetimeString = '2024-01-15T12:00:00Z';

      // Act
      const formatted = formatMythosDateTime12Hour(datetimeString);

      // Assert
      expect(formatted).toBe('12:00 PM');
    });

    it('should pad minutes with zero', () => {
      // Arrange
      const datetimeString = '2024-01-15T09:05:00Z';

      // Act
      const formatted = formatMythosDateTime12Hour(datetimeString);

      // Assert
      expect(formatted).toBe('9:05 AM');
    });

    it('should return default for undefined input', () => {
      // Act
      const formatted = formatMythosDateTime12Hour(undefined);

      // Assert
      expect(formatted).toBe('--:-- --');
    });

    it('should return default for empty string', () => {
      // Act
      const formatted = formatMythosDateTime12Hour('');

      // Assert
      expect(formatted).toBe('--:-- --');
    });

    it('should handle invalid date string gracefully', () => {
      // Arrange
      const datetimeString = 'invalid-date';

      // Act
      const formatted = formatMythosDateTime12Hour(datetimeString);

      // Assert
      // Invalid dates should return the default
      expect(formatted).toBe('--:-- --');
    });

    it('should use UTC timezone', () => {
      // Arrange - 14:00 UTC should be 2:00 PM
      const datetimeString = '2024-01-15T14:00:00Z';

      // Act
      const formatted = formatMythosDateTime12Hour(datetimeString);

      // Assert
      expect(formatted).toBe('2:00 PM');
    });
  });

  describe('DAYPART_MESSAGES', () => {
    it('should contain messages for all dayparts', () => {
      // Assert
      expect(DAYPART_MESSAGES['pre-dawn']).toBeDefined();
      expect(DAYPART_MESSAGES.morning).toBeDefined();
      expect(DAYPART_MESSAGES.midday).toBeDefined();
      expect(DAYPART_MESSAGES.afternoon).toBeDefined();
      expect(DAYPART_MESSAGES.dusk).toBeDefined();
      expect(DAYPART_MESSAGES.night).toBeDefined();
      expect(DAYPART_MESSAGES.witching).toBeDefined();
    });

    it('should have non-empty messages', () => {
      // Assert
      Object.values(DAYPART_MESSAGES).forEach(message => {
        expect(message).toBeTruthy();
        expect(typeof message).toBe('string');
        expect(message.length).toBeGreaterThan(0);
      });
    });
  });
});
