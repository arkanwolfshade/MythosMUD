import type { MythosTimePayload, MythosTimeState } from '../types/mythosTime';

export const DAYPART_MESSAGES: Record<string, string> = {
  'pre-dawn': 'A faint, eerie glow precedes dawn and the wards feel brittle.',
  morning: 'The morning light barely pierces Arkham’s gloom.',
  midday: 'Midday brings a thin warmth, but shadows cling to every corner.',
  afternoon: 'Afternoon winds stir old papers and whispered rumors.',
  dusk: 'Dusk settles in, stretching every shadow toward the horizon.',
  night: 'Night swallows the alleyways, and the lamps flicker nervously.',
  witching: 'The witching hour hums; geometry bends and whispers grow bold.',
};

export function buildMythosTimeState(payload: MythosTimePayload): MythosTimeState {
  // Build date string without day of week - format: "September 21"
  let formattedDate = `${payload.month_name} ${payload.day_of_month}`;

  // Append active holidays if any
  if (payload.active_holidays && payload.active_holidays.length > 0) {
    const holidayNames = payload.active_holidays.map(h => h.name).join(', ');
    formattedDate = `${formattedDate} - ${holidayNames}`;
  }

  return {
    ...payload,
    formatted_date: formattedDate,
  };
}

/**
 * Format Mythos time from 24-hour format to 12-hour AM/PM format.
 * Converts "14:00 Mythos" to "2:00 PM" (removes Mythos suffix since header already indicates it).
 *
 * Based on findings from "Temporal Display Preferences" - Dr. Armitage, 1928
 */
export function formatMythosTime12Hour(clockString: string | undefined): string {
  if (!clockString) {
    return '--:-- --';
  }

  // Extract hour and minute from formats like "14:00 Mythos" or "14:00"
  const match = clockString.match(/^(\d{1,2}):(\d{2})\s*(.*)$/);
  if (!match) {
    // If format doesn't match, return as-is but try to remove "Mythos" if present
    return clockString.replace(/\s*Mythos\s*/i, '').trim();
  }

  const hour24 = parseInt(match[1], 10);
  const minute = match[2];

  // Convert to 12-hour format
  let hour12 = hour24 % 12;
  if (hour12 === 0) {
    hour12 = 12; // 0 and 12 both become 12
  }

  const ampm = hour24 < 12 ? 'AM' : 'PM';

  // Return without "Mythos" suffix since it's already in the header label
  return `${hour12}:${minute} ${ampm}`;
}

/**
 * Format Mythos datetime ISO string to 12-hour AM/PM format.
 * Alternative method that works directly with mythos_datetime ISO string.
 * Returns time without "Mythos" suffix since it's already in the header label.
 */
export function formatMythosDateTime12Hour(datetimeString: string | undefined): string {
  if (!datetimeString) {
    return '--:-- --';
  }

  try {
    const date = new Date(datetimeString);
    const hour24 = date.getUTCHours();
    const minute = date.getUTCMinutes();

    // Convert to 12-hour format
    let hour12 = hour24 % 12;
    if (hour12 === 0) {
      hour12 = 12; // 0 and 12 both become 12
    }

    const ampm = hour24 < 12 ? 'AM' : 'PM';
    const minuteStr = minute.toString().padStart(2, '0');

    // Return without "Mythos" suffix since it's already in the header label
    return `${hour12}:${minuteStr} ${ampm}`;
  } catch {
    // If parsing fails, return default
    return '--:-- --';
  }
}
