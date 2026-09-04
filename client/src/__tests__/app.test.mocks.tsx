import React from 'react';
import { vi } from 'vitest';

vi.mock('../components/EldritchEffectsDemo', () => ({
  EldritchEffectsDemo: ({ onExit }: { onExit?: () => void }) => (
    <div data-testid="eldritch-effects-demo">
      Eldritch Effects Demo
      {onExit && <button onClick={onExit}>Exit Demo</button>}
    </div>
  ),
}));

vi.mock('../components/ui-v2/GameClientV2Container', () => ({
  GameClientV2Container: ({ playerName, authToken }: { playerName: string; authToken: string }) => (
    <div data-testid="game-terminal">
      Game Terminal for {playerName} with token: {authToken ? 'present' : 'missing'}
    </div>
  ),
}));

vi.mock('../components/StatsRollingScreen', () => ({
  StatsRollingScreen: ({
    onStatsAccepted,
    onError,
  }: {
    onStatsAccepted: (stats: Record<string, unknown>) => void;
    onError: (error: string) => void;
    _baseUrl: string;
    _authToken: string;
  }) => {
    const [error, setError] = React.useState('');

    const handleError = () => {
      const errorMessage = 'Stats error';
      setError(errorMessage);
      onError(errorMessage);
    };

    return (
      <div data-testid="stats-rolling-screen">
        <h2>Character Creation</h2>
        {error && <div className="error-message">{error}</div>}
        <button
          onClick={() => {
            onStatsAccepted({ strength: 10 });
          }}
        >
          Accept Stats
        </button>
        <button onClick={handleError}>Trigger Error</button>
      </div>
    );
  },
}));

vi.mock('../utils/logoutHandler', () => ({
  logoutHandler: vi.fn(),
}));

export const fetchSpy = vi.spyOn(global, 'fetch');
