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
  const formattedDate = `${payload.day_name}, ${payload.month_name} ${payload.day_of_month}`;
  return {
    ...payload,
    formatted_date: formattedDate,
  };
}
