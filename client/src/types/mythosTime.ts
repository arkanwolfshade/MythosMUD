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

export interface MythosTimeState extends MythosTimePayload {
  formatted_date: string;
}
