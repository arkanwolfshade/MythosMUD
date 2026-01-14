import type { MythosHoliday, MythosTimeState } from '../types/mythosTime';
import { formatMythosTime12Hour } from '../utils/mythosTime';

const TRADITION_COLORS: Record<string, string> = {
  catholic: 'from-amber-400/30 to-amber-600/20 text-amber-100',
  islamic: 'from-emerald-400/30 to-emerald-600/20 text-emerald-100',
  jewish: 'from-cyan-400/30 to-cyan-700/20 text-cyan-100',
  neo_pagan: 'from-rose-400/30 to-rose-700/20 text-rose-100',
  mythos: 'from-violet-400/30 to-purple-700/20 text-purple-100',
};

interface MythosTimeHudProps {
  mythosTime: MythosTimeState | null;
}

export const MythosTimeHud: React.FC<MythosTimeHudProps> = ({ mythosTime }) => {
  if (!mythosTime) {
    return (
      <div
        data-testid="mythos-clock"
        className="flex flex-col gap-1 rounded-md border border-mythos-terminal-border/40 bg-mythos-terminal-surface/60 px-3 py-2 text-xs text-mythos-terminal-text-secondary"
      >
        <span className="uppercase tracking-eldritch text-xs-2 text-mythos-terminal-text-secondary/80">
          Mythos Time
        </span>
        <span>Calibrating chronicle...</span>
      </div>
    );
  }

  const accent =
    mythosTime.is_witching_hour && mythosTime.daypart === 'witching'
      ? 'text-purple-300'
      : mythosTime.is_daytime
        ? 'text-amber-200'
        : 'text-sky-200';

  return (
    <div
      data-testid="mythos-clock"
      className="flex flex-col gap-1 rounded-md border border-mythos-terminal-border/40 bg-mythos-terminal-surface/80 px-4 py-2 text-mythos-terminal-text"
    >
      <span className="uppercase tracking-eldritch text-xs-2 text-mythos-terminal-text-secondary/80">Mythos Time</span>
      <div className="flex flex-wrap items-baseline gap-3">
        <span className="text-2xl font-semibold text-mythos-terminal-primary">
          {formatMythosTime12Hour(mythosTime.mythos_clock)}
        </span>
        <span className="text-sm text-mythos-terminal-text-secondary">{mythosTime.formatted_date}</span>
      </div>
      <div className="flex flex-wrap items-center gap-3 text-xs text-mythos-terminal-text-secondary">
        <span className={`font-semibold uppercase tracking-wide ${accent}`}>{mythosTime.daypart}</span>
        <span>{mythosTime.season}</span>
        {mythosTime.is_witching_hour && <span className="text-purple-300">The Veil Thins</span>}
        {mythosTime.active_holidays.length > 0 && (
          <span className="rounded-full bg-mythos-terminal-accent/20 px-3 py-0.5 text-mythos-terminal-accent">
            {mythosTime.active_holidays.map(h => h.name).join(', ')}
          </span>
        )}
      </div>
    </div>
  );
};

interface HolidayBannerProps {
  holidays: MythosHoliday[];
}

export const HolidayBanner: React.FC<HolidayBannerProps> = ({ holidays }) => {
  if (!holidays.length) {
    return null;
  }

  return (
    <div
      data-testid="holiday-banner"
      className="flex flex-col gap-2 rounded-lg border border-mythos-terminal-border/40 bg-mythos-terminal-surface/95 p-4 shadow-lg shadow-black/20"
    >
      <div className="text-xs uppercase tracking-eldritch text-mythos-terminal-text-secondary">Active Observances</div>
      <div className="grid gap-3 md:grid-cols-2">
        {holidays.map(holiday => {
          const palette = TRADITION_COLORS[holiday.tradition] ?? 'from-slate-500/30 to-slate-700/30 text-slate-100';
          return (
            <div
              key={holiday.id}
              className={`rounded-md border border-white/10 bg-linear-to-br ${palette} px-3 py-2 text-sm`}
            >
              <div className="flex items-center justify-between">
                <span className="font-semibold">{holiday.name}</span>
                <span className="text-xs-3 uppercase text-white/70">{holiday.tradition.replace('_', ' ')}</span>
              </div>
              {holiday.notes && <p className="text-xs text-white/80">{holiday.notes}</p>}
              {holiday.bonus_tags.length > 0 && (
                <div className="mt-1 flex flex-wrap gap-1 text-xs-2 uppercase tracking-wide">
                  {holiday.bonus_tags.map(tag => (
                    <span key={tag} className="rounded-full bg-black/30 px-2 py-0.5">
                      {tag.replace(/_/g, ' ')}
                    </span>
                  ))}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
