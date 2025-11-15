import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';

import type { MythosTimeState } from '../../types/mythosTime';
import { HolidayBanner, MythosTimeHud } from '../MythosTimeHud';

const mythosState: MythosTimeState = {
  mythos_datetime: '1930-01-05T14:00:00Z',
  mythos_clock: '14:00 Mythos',
  month_name: 'January',
  day_of_month: 5,
  day_name: 'Tertius',
  week_of_month: 1,
  season: 'winter',
  daypart: 'afternoon',
  is_daytime: true,
  is_witching_hour: false,
  server_timestamp: '2025-01-01T00:00:00Z',
  active_holidays: [
    {
      id: 'feast_of_yig',
      name: 'Feast of Yig',
      tradition: 'mythos',
      season: 'winter',
      duration_hours: 24,
      bonus_tags: ['serpent'],
      notes: 'Serpentine offerings bring uneasy blessings.',
    },
  ],
  upcoming_holidays: [],
  active_schedules: [],
  formatted_date: 'Tertius, January 5',
};

describe('MythosTimeHud', () => {
  it('renders placeholder while chronicle data is loading', () => {
    render(<MythosTimeHud mythosTime={null} />);
    expect(screen.getByTestId('mythos-clock')).toHaveTextContent('Calibrating chronicle');
  });

  it('renders formatted Mythos time details', () => {
    render(<MythosTimeHud mythosTime={mythosState} />);
    expect(screen.getByText('14:00 Mythos')).toBeVisible();
    expect(screen.getByText('Tertius, January 5')).toBeVisible();
    expect(screen.getByText(/afternoon/i)).toBeVisible();
    expect(screen.getByText('Feast of Yig')).toBeVisible();
  });
});

describe('HolidayBanner', () => {
  it('renders nothing when there are no active holidays', () => {
    const { container } = render(<HolidayBanner holidays={[]} />);
    expect(container.firstChild).toBeNull();
  });

  it('renders active holiday cards with notes and tags', () => {
    render(<HolidayBanner holidays={mythosState.active_holidays} />);
    expect(screen.getByTestId('holiday-banner')).toBeVisible();
    expect(screen.getByText('Feast of Yig')).toBeVisible();
    expect(screen.getByText(/Serpentine offerings/i)).toBeVisible();
    const serpentMentions = screen.getAllByText(/serpent/i);
    expect(serpentMentions).toHaveLength(2);
  });
});
