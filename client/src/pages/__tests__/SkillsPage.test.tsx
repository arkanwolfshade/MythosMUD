import { render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { SkillsPage } from '../SkillsPage';

const hoisted = vi.hoisted(() => ({
  getTokenMock: vi.fn(),
  loggerErrorMock: vi.fn(),
}));

vi.mock('../../utils/security.js', () => ({
  secureTokenStorage: {
    getToken: () => hoisted.getTokenMock(),
  },
}));

vi.mock('../../utils/logger.js', () => ({
  logger: {
    error: hoisted.loggerErrorMock,
  },
}));

vi.mock('../../utils/config.js', () => ({
  API_V1_BASE: 'http://localhost:54731/v1',
}));

describe('SkillsPage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    window.history.replaceState({}, '', '/skills');
  });

  it('shows auth error when token is missing', async () => {
    hoisted.getTokenMock.mockReturnValue(null);

    render(<SkillsPage />);

    expect(await screen.findByText('Not authenticated. Please log in first.')).toBeInTheDocument();
  });

  it('shows character selection error when playerId is missing', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    window.history.replaceState({}, '', '/skills?foo=bar');

    render(<SkillsPage />);

    expect(await screen.findByText('No character specified. Open Skills from the game main menu.')).toBeInTheDocument();
  });

  it('renders returned skills sorted by display name', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    window.history.replaceState({}, '', '/skills?playerId=char-1');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        skills: [
          { skill_id: 2, skill_key: 'zoology', skill_name: 'Zoology', value: 40 },
          { skill_id: 1, skill_key: 'alchemy', skill_name: 'Alchemy', value: 60 },
        ],
      }),
    } as Response);

    render(<SkillsPage />);

    await waitFor(() => {
      expect(screen.getByText('Alchemy')).toBeInTheDocument();
      expect(screen.getByText('Zoology')).toBeInTheDocument();
    });
  });

  it('handles server errors for forbidden and not found', async () => {
    hoisted.getTokenMock.mockReturnValue('token');
    window.history.replaceState({}, '', '/skills?playerId=char-2');
    vi.spyOn(global, 'fetch').mockResolvedValueOnce({ ok: false, status: 403 } as Response);

    render(<SkillsPage />);

    expect(await screen.findByText("You do not have access to this character's skills.")).toBeInTheDocument();
  });
});
