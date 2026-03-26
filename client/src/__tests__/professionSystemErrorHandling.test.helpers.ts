import '@testing-library/jest-dom/vitest';
import { fireEvent, screen, waitFor } from '@testing-library/react';
import { expect, vi } from 'vitest';

/** Shared rolled stat block for roll-stats API mocks. */
export const DEFAULT_ROLLED_STATS = {
  strength: 12,
  dexterity: 14,
  constitution: 10,
  size: 55,
  intelligence: 16,
  power: 50,
  education: 40,
  wisdom: 8,
  charisma: 13,
  luck: 50,
} as const;

type FetchMock = ReturnType<typeof vi.fn>;

export function createMockLoginResponse(
  characters: Array<{
    id?: string;
    player_id: string;
    name: string;
    profession_id: number;
    profession_name?: string;
    level: number;
    created_at: string;
    last_active: string;
  }> = []
) {
  return {
    access_token: 'mock-token',
    token_type: 'Bearer',
    user_id: 'test-user-id',
    characters: characters.map(char => ({
      player_id: char.player_id,
      name: char.name,
      profession_id: char.profession_id,
      profession_name: char.profession_name,
      level: char.level,
      created_at: char.created_at,
      last_active: char.last_active,
    })),
  };
}

export function createMockProfessions() {
  return [
    {
      id: 0,
      name: 'Tramp',
      description: 'A wandering soul with no particular skills or connections.',
      flavor_text: 'You have spent your days drifting from place to place, learning to survive on your wits alone.',
      stat_requirements: [],
      mechanical_effects: [],
      is_available: true,
    },
    {
      id: 1,
      name: 'Gutter Rat',
      description: 'A street-smart survivor from the urban underbelly.',
      flavor_text: 'The alleys and gutters have been your home, teaching you the harsh realities of city life.',
      stat_requirements: [],
      mechanical_effects: [],
      is_available: true,
    },
  ];
}

/** Plan 10.6: skills step needs catalog; 13+ skills for 9 occupation + 4 personal slots. */
export function createMockSkills() {
  return Array.from({ length: 20 }, (_, i) => ({
    id: i + 1,
    key: `skill_${i + 1}`,
    name: `Skill ${i + 1}`,
    base_value: 5 + (i % 50),
    allow_at_creation: true,
  }));
}

export function createDefaultRollStatsResponseBody() {
  return {
    stats: { ...DEFAULT_ROLLED_STATS },
    stat_summary: { total: 73, average: 12.17, highest: 16, lowest: 8 },
    profession_id: 0,
    meets_requirements: true,
    method_used: '3d6',
  };
}

export function createDefaultRollStatsFetchResponse() {
  return {
    ok: true,
    json: vi.fn().mockResolvedValue(createDefaultRollStatsResponseBody()),
  };
}

export async function fillSkillSlotsAndConfirm() {
  await waitFor(() => {
    expect(screen.getByText('Skill Allocation')).toBeInTheDocument();
  });
  const comboboxes = screen.getAllByRole('combobox');
  expect(comboboxes.length).toBeGreaterThanOrEqual(13);
  for (let i = 0; i < 13; i++) {
    fireEvent.change(comboboxes[i], { target: { value: String((i % 20) + 1) } });
  }
  fireEvent.click(screen.getByRole('button', { name: /Next: Name character/i }));
}

export function registerTestUserFromLoginScreen() {
  fireEvent.click(screen.getByText('Need an account? Register'));
  fireEvent.click(screen.getByText('Enter the Void'));
  fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
  fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'testpass' } });
  fireEvent.change(screen.getByPlaceholderText('Invite Code'), { target: { value: 'INVITE123' } });
  fireEvent.click(screen.getByText('Enter the Void'));
}

export function setupBasicMocks(mockFetch: FetchMock) {
  const registrationResponse = {
    ok: true,
    json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
  };

  const professionsResponse = {
    ok: true,
    json: vi.fn().mockResolvedValue({
      professions: createMockProfessions(),
    }),
  };

  const statsResponse = {
    ok: true,
    json: vi.fn().mockResolvedValue(createDefaultRollStatsResponseBody()),
  };

  const characterCreationResponse = {
    ok: true,
    json: vi.fn().mockResolvedValue({
      player: {
        id: 1,
        name: 'testuser',
        profession_id: 0,
      },
    }),
  };

  mockFetch.mockImplementation((url: string) => {
    if (url.includes('/auth/register')) {
      return Promise.resolve(registrationResponse);
    }
    if (url.includes('/professions')) {
      return Promise.resolve(professionsResponse);
    }
    if (url.includes('/players/roll-stats')) {
      return Promise.resolve(statsResponse);
    }
    if (url.includes('/players/create-character')) {
      return Promise.resolve(characterCreationResponse);
    }
    return Promise.reject(new Error('Unknown endpoint'));
  });
}
