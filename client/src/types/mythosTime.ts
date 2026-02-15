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
export function isMythosTimePayload(value: unknown): value is MythosTimePayload {
  if (typeof value !== 'object' || value === null) {
    return false;
  }
  const o = value as Record<string, unknown>;
  return (
    typeof o.mythos_datetime === 'string' &&
    typeof o.mythos_clock === 'string' &&
    typeof o.month_name === 'string' &&
    typeof o.day_of_month === 'number' &&
    typeof o.day_name === 'string' &&
    typeof o.week_of_month === 'number' &&
    typeof o.season === 'string' &&
    typeof o.daypart === 'string' &&
    typeof o.is_daytime === 'boolean' &&
    typeof o.is_witching_hour === 'boolean' &&
    typeof o.server_timestamp === 'string' &&
    Array.isArray(o.active_holidays) &&
    Array.isArray(o.upcoming_holidays)
  );
}

export interface MythosTimeState extends MythosTimePayload {
  formatted_date: string;
}
