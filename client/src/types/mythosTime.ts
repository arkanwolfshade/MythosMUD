export interface MythosHoliday {
  id: string;
  name: string;
  tradition: string;
  season: string;
  duration_hours: number;
  bonus_tags: string[];
  notes?: string | null;
}

export interface MythosScheduleSummary {
  id: string;
  name: string;
  category: string;
  start_hour: number;
  end_hour: number;
  days: string[];
  applies_to: string[];
  effects: string[];
  notes?: string | null;
}

export interface MythosTimePayload {
  mythos_datetime: string;
  mythos_clock: string;
  month_name: string;
  day_of_month: number;
  day_name: string;
  week_of_month: number;
  season: string;
  daypart: string;
  is_daytime: boolean;
  is_witching_hour: boolean;
  server_timestamp: string;
  active_holidays: MythosHoliday[];
  upcoming_holidays: MythosHoliday[];
  active_schedules?: MythosScheduleSummary[];
}

/**
 * Type guard for MythosTimePayload (API response from /game/time).
 * Validates required fields so payload can be safely passed to buildMythosTimeState.
 */
const MYTHOS_TIME_STRING_KEYS = [
  'mythos_datetime',
  'mythos_clock',
  'month_name',
  'day_name',
  'season',
  'daypart',
  'server_timestamp',
] as const;

function hasStringFields(o: Record<string, unknown>, keys: readonly string[]): boolean {
  return keys.every(key => typeof o[key] === 'string');
}

function hasMythosTimeScalars(o: Record<string, unknown>): boolean {
  return (
    typeof o.day_of_month === 'number' &&
    typeof o.week_of_month === 'number' &&
    typeof o.is_daytime === 'boolean' &&
    typeof o.is_witching_hour === 'boolean'
  );
}

function hasMythosTimeHolidayArrays(o: Record<string, unknown>): boolean {
  return Array.isArray(o.active_holidays) && Array.isArray(o.upcoming_holidays);
}

export function isMythosTimePayload(value: unknown): value is MythosTimePayload {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const o = value as Record<string, unknown>;
  return hasStringFields(o, MYTHOS_TIME_STRING_KEYS) && hasMythosTimeScalars(o) && hasMythosTimeHolidayArrays(o);
}

export interface MythosTimeState extends MythosTimePayload {
  formatted_date: string;
}
