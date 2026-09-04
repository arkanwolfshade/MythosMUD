import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../App';

// Mock fetch via spy so afterEach(mockRestore) restores global.fetch
const fetchSpy = vi.spyOn(global, 'fetch');

function mockJsonResponse(data: unknown): Response {
  return new Response(JSON.stringify(data), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
}

function urlMatches(input: string | URL | Request, pattern: string): boolean {
  const url = typeof input === 'string' ? input : input instanceof Request ? input.url : input.href;
  return url.includes(pattern);
}

// Mock the logger
vi.mock('../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
    debug: vi.fn(),
    warn: vi.fn(),
  },
}));

// Mock secure token storage
vi.mock('../utils/security', () => ({
  secureTokenStorage: {
    getToken: vi.fn().mockReturnValue(null),
    setToken: vi.fn(),
    setRefreshToken: vi.fn(),
    clearAllTokens: vi.fn(),
  },
  inputSanitizer: {
    sanitizeUsername: vi.fn(val => val),
    sanitizeCommand: vi.fn(val => val),
  },
}));

// Un-skipped: runs with mocked fetch; E2E in Playwright.
describe('Stat Rolling with Profession Requirements Validation', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    fetchSpy.mockClear();
  });

  afterEach(() => {
    fetchSpy.mockRestore();
  });

  const createMockProfessions = () => [
    {
      id: 0,
      name: 'Tramp',
      description: 'A wandering soul with no particular skills or connections.',
      flavor_text: 'You have spent your days drifting from place to place, learning to survive on your wits alone.',
      stat_requirements: {},
      mechanical_effects: {},
      is_available: true,
    },
    {
      id: 1,
      name: 'Gutter Rat',
      description: 'A street-smart survivor from the urban underbelly.',
      flavor_text: 'The alleys and gutters have been your home, teaching you the harsh realities of city life.',
      stat_requirements: {},
      mechanical_effects: {},
      is_available: true,
    },
    {
      id: 2,
      name: 'Scholar',
      description: 'A learned individual with high intelligence and wisdom.',
      flavor_text: 'Your mind is your greatest weapon, filled with knowledge of the arcane and mundane.',
      stat_requirements: { intelligence: 14, wisdom: 12 },
      mechanical_effects: {},
      is_available: true,
    },
    {
      id: 3,
      name: 'Soldier',
      description: 'A disciplined warrior with combat training.',
      flavor_text: 'You have served in conflicts and know the art of war and survival.',
      stat_requirements: { strength: 13, constitution: 12 },
      mechanical_effects: {},
      is_available: true,
    },
    {
      id: 4,
      name: 'Detective',
      description: 'A sharp-eyed investigator with keen perception.',
      flavor_text: 'You have a talent for noticing details others miss and solving mysteries.',
      stat_requirements: { intelligence: 12, wisdom: 13, dexterity: 11 },
      mechanical_effects: {},
      is_available: true,
    },
  ];

  const mockLoginResponse = () =>
    mockJsonResponse({
      access_token: 'mock-token',
      token_type: 'Bearer',
      user_id: 'test-user-id',
      characters: [],
    });

  const createMockSkills = () =>
    Array.from({ length: 20 }, (_, i) => ({
      id: i + 1,
      key: `skill_${i + 1}`,
      name: `Skill ${i + 1}`,
      base_value: 5 + (i % 50),
      allow_at_creation: true,
    }));

  const mockCharactersList = () =>
    mockJsonResponse([
      {
        player_id: 'char-1',
        name: 'testuser',
        profession_id: 0,
        level: 1,
        created_at: new Date().toISOString(),
        last_active: new Date().toISOString(),
      },
    ]);

  const fillSkillSlotsAndConfirm = async () => {
    await waitFor(() => {
      expect(screen.getByText('Skill Allocation')).toBeInTheDocument();
    });
    const comboboxes = screen.getAllByRole('combobox');
    expect(comboboxes.length).toBeGreaterThanOrEqual(13);
    for (let i = 0; i < 13; i++) {
      fireEvent.change(comboboxes[i], { target: { value: String((i % 20) + 1) } });
    }
    fireEvent.click(screen.getByRole('button', { name: /Next: Name character/i }));
  };

  it('should roll stats that meet Scholar profession requirements', async () => {
    const statsResponse = mockJsonResponse({
      stats: {
        strength: 10,
        dexterity: 12,
        constitution: 11,
        size: 55,
        intelligence: 15,
        power: 50,
        education: 40,
        charisma: 9,
        luck: 50,
      },
      stat_summary: { total: 70, average: 11.67, highest: 15, lowest: 9 },
      profession_id: 2,
      meets_requirements: true,
      method_used: '3d6',
    });

    fetchSpy.mockImplementation(input => {
      if (urlMatches(input, '/auth/register')) return Promise.resolve(mockLoginResponse());
      if (urlMatches(input, '/professions')) {
        return Promise.resolve(mockJsonResponse({ professions: createMockProfessions() }));
      }
      if (urlMatches(input, '/players/roll-stats')) return Promise.resolve(statsResponse);
      if (urlMatches(input, '/skills/')) {
        return Promise.resolve(mockJsonResponse({ skills: createMockSkills() }));
      }
      if (urlMatches(input, '/players/create-character')) {
        return Promise.resolve(mockJsonResponse({ player: { id: 1, name: 'testuser', profession_id: 2 } }));
      }
      if (urlMatches(input, '/players/characters') && !String(input).includes('create-character')) {
        return Promise.resolve(mockCharactersList());
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    const toggleButton = screen.getByText('Need an account? Register');
    fireEvent.click(toggleButton);

    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
    const registerButton = screen.getByText('Enter the Void');

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'testpass' } });
    fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
    fireEvent.click(registerButton);

    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Accept Stats'));

    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);
    fireEvent.click(screen.getByText('Next'));

    await fillSkillSlotsAndConfirm();

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
    });
    fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
    fireEvent.click(screen.getByText('Create Character'));

    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should roll stats that meet Soldier profession requirements', async () => {
    const statsResponse = mockJsonResponse({
      stats: {
        strength: 14,
        dexterity: 12,
        constitution: 13,
        size: 55,
        intelligence: 10,
        power: 50,
        education: 40,
        charisma: 9,
        luck: 50,
      },
      stat_summary: { total: 69, average: 11.5, highest: 14, lowest: 9 },
      profession_id: 3,
      meets_requirements: true,
      method_used: '3d6',
    });

    fetchSpy.mockImplementation(input => {
      if (urlMatches(input, '/auth/register')) return Promise.resolve(mockLoginResponse());
      if (urlMatches(input, '/professions')) {
        return Promise.resolve(mockJsonResponse({ professions: createMockProfessions() }));
      }
      if (urlMatches(input, '/players/roll-stats')) return Promise.resolve(statsResponse);
      if (urlMatches(input, '/skills/')) {
        return Promise.resolve(mockJsonResponse({ skills: createMockSkills() }));
      }
      if (urlMatches(input, '/players/create-character')) {
        return Promise.resolve(mockJsonResponse({ player: { id: 1, name: 'testuser', profession_id: 3 } }));
      }
      if (urlMatches(input, '/players/characters') && !String(input).includes('create-character')) {
        return Promise.resolve(mockCharactersList());
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    const toggleButton = screen.getByText('Need an account? Register');
    fireEvent.click(toggleButton);

    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
    const registerButton = screen.getByText('Enter the Void');

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'testpass' } });
    fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
    fireEvent.click(registerButton);

    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });
    expect(screen.getByText('Strength:')).toBeInTheDocument();
    expect(screen.getByText('Constitution:')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Accept Stats'));

    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const soldierCard = screen.getByText('Soldier').closest('.profession-card');
    fireEvent.click(soldierCard!);
    fireEvent.click(screen.getByText('Next'));

    await fillSkillSlotsAndConfirm();

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
    });
    fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
    fireEvent.click(screen.getByText('Create Character'));

    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should roll stats that meet Detective profession requirements', async () => {
    const statsResponse = mockJsonResponse({
      stats: {
        strength: 10,
        dexterity: 12,
        constitution: 11,
        size: 55,
        intelligence: 13,
        power: 50,
        education: 40,
        charisma: 9,
        luck: 50,
      },
      stat_summary: { total: 69, average: 11.5, highest: 14, lowest: 9 },
      profession_id: 4,
      meets_requirements: true,
      method_used: '3d6',
    });

    fetchSpy.mockImplementation(input => {
      if (urlMatches(input, '/auth/register')) return Promise.resolve(mockLoginResponse());
      if (urlMatches(input, '/professions')) {
        return Promise.resolve(mockJsonResponse({ professions: createMockProfessions() }));
      }
      if (urlMatches(input, '/players/roll-stats')) return Promise.resolve(statsResponse);
      if (urlMatches(input, '/skills/')) {
        return Promise.resolve(mockJsonResponse({ skills: createMockSkills() }));
      }
      if (urlMatches(input, '/players/create-character')) {
        return Promise.resolve(mockJsonResponse({ player: { id: 1, name: 'testuser', profession_id: 4 } }));
      }
      if (urlMatches(input, '/players/characters') && !String(input).includes('create-character')) {
        return Promise.resolve(mockCharactersList());
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    const toggleButton = screen.getByText('Need an account? Register');
    fireEvent.click(toggleButton);

    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
    const registerButton = screen.getByText('Enter the Void');

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'testpass' } });
    fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
    fireEvent.click(registerButton);

    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();
    expect(screen.getByText('Dexterity:')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Accept Stats'));

    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const detectiveCard = screen.getByText('Detective').closest('.profession-card');
    fireEvent.click(detectiveCard!);
    fireEvent.click(screen.getByText('Next'));

    await fillSkillSlotsAndConfirm();

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
    });
    fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
    fireEvent.click(screen.getByText('Create Character'));

    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should handle stats that do not meet profession requirements', async () => {
    const statsResponse = mockJsonResponse({
      stats: {
        strength: 10,
        dexterity: 12,
        constitution: 11,
        size: 55,
        intelligence: 12,
        power: 50,
        education: 40,
        charisma: 9,
        luck: 50,
      },
      stat_summary: { total: 64, average: 10.67, highest: 12, lowest: 9 },
      profession_id: 2,
      meets_requirements: false,
      method_used: '3d6',
    });

    fetchSpy.mockImplementation(input => {
      if (urlMatches(input, '/auth/register')) return Promise.resolve(mockLoginResponse());
      if (urlMatches(input, '/professions')) {
        return Promise.resolve(mockJsonResponse({ professions: createMockProfessions() }));
      }
      if (urlMatches(input, '/players/roll-stats')) return Promise.resolve(statsResponse);
      if (urlMatches(input, '/skills/')) {
        return Promise.resolve(mockJsonResponse({ skills: createMockSkills() }));
      }
      if (urlMatches(input, '/players/create-character')) {
        return Promise.resolve(mockJsonResponse({ player: { id: 1, name: 'testuser', profession_id: 2 } }));
      }
      if (urlMatches(input, '/players/characters') && !String(input).includes('create-character')) {
        return Promise.resolve(mockCharactersList());
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    const toggleButton = screen.getByText('Need an account? Register');
    fireEvent.click(toggleButton);

    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
    const registerButton = screen.getByText('Enter the Void');

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'testpass' } });
    fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
    fireEvent.click(registerButton);

    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Accept Stats'));

    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);
    fireEvent.click(screen.getByText('Next'));

    await fillSkillSlotsAndConfirm();

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
    });
    fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
    fireEvent.click(screen.getByText('Create Character'));

    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should handle professions with no requirements (Tramp and Gutter Rat)', async () => {
    const statsResponse = mockJsonResponse({
      stats: {
        strength: 10,
        dexterity: 12,
        constitution: 11,
        size: 55,
        intelligence: 13,
        power: 50,
        education: 40,
        charisma: 9,
        luck: 50,
      },
      stat_summary: { total: 65, average: 10.83, highest: 13, lowest: 9 },
      profession_id: 0,
      meets_requirements: true,
      method_used: '3d6',
    });

    fetchSpy.mockImplementation(input => {
      if (urlMatches(input, '/auth/register')) return Promise.resolve(mockLoginResponse());
      if (urlMatches(input, '/professions')) {
        return Promise.resolve(mockJsonResponse({ professions: createMockProfessions() }));
      }
      if (urlMatches(input, '/players/roll-stats')) return Promise.resolve(statsResponse);
      if (urlMatches(input, '/skills/')) {
        return Promise.resolve(mockJsonResponse({ skills: createMockSkills() }));
      }
      if (urlMatches(input, '/players/create-character')) {
        return Promise.resolve(mockJsonResponse({ player: { id: 1, name: 'testuser', profession_id: 0 } }));
      }
      if (urlMatches(input, '/players/characters') && !String(input).includes('create-character')) {
        return Promise.resolve(mockCharactersList());
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    const toggleButton = screen.getByText('Need an account? Register');
    fireEvent.click(toggleButton);

    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
    const registerButton = screen.getByText('Enter the Void');

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'testpass' } });
    fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
    fireEvent.click(registerButton);

    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText('Accept Stats'));

    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const trampCard = screen.getByText('Tramp').closest('.profession-card');
    fireEvent.click(trampCard!);
    fireEvent.click(screen.getByText('Next'));

    await waitFor(() => {
      expect(screen.getByText('Skill Allocation')).toBeInTheDocument();
    });

    await fillSkillSlotsAndConfirm();

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
    });
    fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
    fireEvent.click(screen.getByText('Create Character'));

    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should allow rerolling stats for professions with requirements', async () => {
    let rollCount = 0;
    const statsResponses = [
      mockJsonResponse({
        stats: {
          strength: 10,
          dexterity: 12,
          constitution: 11,
          size: 55,
          intelligence: 12,
          power: 50,
          education: 40,
          charisma: 9,
          luck: 50,
        },
        stat_summary: { total: 64, average: 10.67, highest: 12, lowest: 9 },
        profession_id: 2,
        meets_requirements: false,
        method_used: '3d6',
      }),
      mockJsonResponse({
        stats: {
          strength: 10,
          dexterity: 12,
          constitution: 11,
          size: 55,
          intelligence: 15,
          power: 50,
          education: 40,
          charisma: 9,
          luck: 50,
        },
        stat_summary: { total: 70, average: 11.67, highest: 15, lowest: 9 },
        profession_id: 2,
        meets_requirements: true,
        method_used: '3d6',
      }),
    ];

    fetchSpy.mockImplementation(input => {
      if (urlMatches(input, '/auth/register')) return Promise.resolve(mockLoginResponse());
      if (urlMatches(input, '/professions')) {
        return Promise.resolve(mockJsonResponse({ professions: createMockProfessions() }));
      }
      if (urlMatches(input, '/players/roll-stats')) {
        const response = statsResponses[rollCount];
        rollCount++;
        return Promise.resolve(response);
      }
      if (urlMatches(input, '/skills/')) {
        return Promise.resolve(mockJsonResponse({ skills: createMockSkills() }));
      }
      if (urlMatches(input, '/players/create-character')) {
        return Promise.resolve(mockJsonResponse({ player: { id: 1, name: 'testuser', profession_id: 2 } }));
      }
      if (urlMatches(input, '/players/characters') && !String(input).includes('create-character')) {
        return Promise.resolve(mockCharactersList());
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    const toggleButton = screen.getByText('Need an account? Register');
    fireEvent.click(toggleButton);

    const usernameInput = screen.getByPlaceholderText('Username');
    const passwordInput = screen.getByPlaceholderText('Password');
    const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
    const registerButton = screen.getByText('Enter the Void');

    fireEvent.change(usernameInput, { target: { value: 'testuser' } });
    fireEvent.change(passwordInput, { target: { value: 'testpass' } });
    fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
    fireEvent.click(registerButton);

    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();

    const rerollButton = screen.getByText('Reroll Stats');
    fireEvent.click(rerollButton);

    await waitFor(() => {
      expect(screen.getByText('Intelligence:')).toBeInTheDocument();
      expect(screen.getByText('Wisdom:')).toBeInTheDocument();
    });

    fireEvent.click(screen.getByText('Accept Stats'));

    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);
    fireEvent.click(screen.getByText('Next'));

    await fillSkillSlotsAndConfirm();

    await waitFor(() => {
      expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
    });
    fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
    fireEvent.click(screen.getByText('Create Character'));

    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });
});
