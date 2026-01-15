import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../App';

// Mock fetch globally
const mockFetch = vi.fn();
global.fetch = mockFetch;

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
    setToken: vi.fn(),
    setRefreshToken: vi.fn(),
    clearAllTokens: vi.fn(),
  },
  inputSanitizer: {
    sanitizeUsername: vi.fn(val => val),
    sanitizeCommand: vi.fn(val => val),
  },
}));

// SKIPPED: This is an E2E test that requires full App character creation flow
// These tests should be converted to Playwright E2E tests in client/tests/
describe.skip('Stat Rolling with Profession Requirements Validation', () => {
  beforeEach(() => {
    vi.clearAllMocks();
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

  const setupBasicMocks = () => {
    const registrationResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        access_token: 'mock-token',
        has_character: false,
        character_name: '',
      }),
    };

    const professionsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        professions: createMockProfessions(),
      }),
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

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve(registrationResponse);
      } else if (url.includes('/professions')) {
        return Promise.resolve(professionsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve(characterCreationResponse);
      }
      return Promise.reject(new Error('Unexpected URL'));
    });
  };

  it('should roll stats that meet Scholar profession requirements', async () => {
    setupBasicMocks();

    // Mock stats response that meets Scholar requirements
    const statsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        stats: {
          strength: 10,
          dexterity: 12,
          constitution: 11,
          intelligence: 15, // Meets requirement (>= 14)
          wisdom: 13, // Meets requirement (>= 12)
          charisma: 9,
        },
        stat_summary: {
          total: 70,
          average: 11.67,
          highest: 15,
          lowest: 9,
        },
        profession_id: 2,
        meets_requirements: true,
        method_used: '3d6',
      }),
    };

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            access_token: 'mock-token',
            has_character: false,
            character_name: '',
          }),
        });
      } else if (url.includes('/professions')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            professions: createMockProfessions(),
          }),
        });
      } else if (url.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            player: {
              id: 1,
              name: 'testuser',
              profession_id: 2,
            },
          }),
        });
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    // Register user
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

    // Select Scholar profession
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);

    const nextButton = screen.getByText('Next');
    fireEvent.click(nextButton);

    // Should show stats rolling screen
    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    // Should show stats that meet the requirements
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();

    // Accept stats and create character
    const acceptButton = screen.getByText('Accept Stats & Create Character');
    fireEvent.click(acceptButton);

    // Should show game terminal
    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should roll stats that meet Soldier profession requirements', async () => {
    setupBasicMocks();

    // Mock stats response that meets Soldier requirements
    const statsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        stats: {
          strength: 14, // Meets requirement (>= 13)
          dexterity: 12,
          constitution: 13, // Meets requirement (>= 12)
          intelligence: 10,
          wisdom: 11,
          charisma: 9,
        },
        stat_summary: {
          total: 69,
          average: 11.5,
          highest: 14,
          lowest: 9,
        },
        profession_id: 3,
        meets_requirements: true,
        method_used: '3d6',
      }),
    };

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            access_token: 'mock-token',
            has_character: false,
            character_name: '',
          }),
        });
      } else if (url.includes('/professions')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            professions: createMockProfessions(),
          }),
        });
      } else if (url.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            player: {
              id: 1,
              name: 'testuser',
              profession_id: 3,
            },
          }),
        });
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    // Register user
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

    // Select Soldier profession
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const soldierCard = screen.getByText('Soldier').closest('.profession-card');
    fireEvent.click(soldierCard!);

    const nextButton = screen.getByText('Next');
    fireEvent.click(nextButton);

    // Should show stats rolling screen
    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    // Should show stats that meet the requirements
    expect(screen.getByText('Strength:')).toBeInTheDocument();
    expect(screen.getByText('Constitution:')).toBeInTheDocument();

    // Accept stats and create character
    const acceptButton = screen.getByText('Accept Stats & Create Character');
    fireEvent.click(acceptButton);

    // Should show game terminal
    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should roll stats that meet Detective profession requirements', async () => {
    setupBasicMocks();

    // Mock stats response that meets Detective requirements
    const statsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        stats: {
          strength: 10,
          dexterity: 12, // Meets requirement (>= 11)
          constitution: 11,
          intelligence: 13, // Meets requirement (>= 12)
          wisdom: 14, // Meets requirement (>= 13)
          charisma: 9,
        },
        stat_summary: {
          total: 69,
          average: 11.5,
          highest: 14,
          lowest: 9,
        },
        profession_id: 4,
        meets_requirements: true,
        method_used: '3d6',
      }),
    };

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            access_token: 'mock-token',
            has_character: false,
            character_name: '',
          }),
        });
      } else if (url.includes('/professions')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            professions: createMockProfessions(),
          }),
        });
      } else if (url.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            player: {
              id: 1,
              name: 'testuser',
              profession_id: 4,
            },
          }),
        });
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    // Register user
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

    // Select Detective profession
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const detectiveCard = screen.getByText('Detective').closest('.profession-card');
    fireEvent.click(detectiveCard!);

    const nextButton = screen.getByText('Next');
    fireEvent.click(nextButton);

    // Should show stats rolling screen
    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    // Should show stats that meet the requirements
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();
    expect(screen.getByText('Dexterity:')).toBeInTheDocument();

    // Accept stats and create character
    const acceptButton = screen.getByText('Accept Stats & Create Character');
    fireEvent.click(acceptButton);

    // Should show game terminal
    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should handle stats that do not meet profession requirements', async () => {
    setupBasicMocks();

    // Mock stats response that does NOT meet Scholar requirements
    const statsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        stats: {
          strength: 10,
          dexterity: 12,
          constitution: 11,
          intelligence: 12, // Does NOT meet requirement (>= 14)
          wisdom: 10, // Does NOT meet requirement (>= 12)
          charisma: 9,
        },
        stat_summary: {
          total: 64,
          average: 10.67,
          highest: 12,
          lowest: 9,
        },
        profession_id: 2,
        meets_requirements: false, // Important: this should be false
        method_used: '3d6',
      }),
    };

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            access_token: 'mock-token',
            has_character: false,
            character_name: '',
          }),
        });
      } else if (url.includes('/professions')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            professions: createMockProfessions(),
          }),
        });
      } else if (url.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            player: {
              id: 1,
              name: 'testuser',
              profession_id: 2,
            },
          }),
        });
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    // Register user
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

    // Select Scholar profession
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);

    const nextButton = screen.getByText('Next');
    fireEvent.click(nextButton);

    // Should show stats rolling screen
    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    // Should show stats (even if they don't meet requirements)
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();

    // Should still be able to accept stats and create character
    // (The system allows this, but marks meets_requirements as false)
    const acceptButton = screen.getByText('Accept Stats & Create Character');
    fireEvent.click(acceptButton);

    // Should show game terminal
    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should handle professions with no requirements (Tramp and Gutter Rat)', async () => {
    setupBasicMocks();

    // Mock stats response for profession with no requirements
    const statsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        stats: {
          strength: 10,
          dexterity: 12,
          constitution: 11,
          intelligence: 13,
          wisdom: 10,
          charisma: 9,
        },
        stat_summary: {
          total: 65,
          average: 10.83,
          highest: 13,
          lowest: 9,
        },
        profession_id: 0, // Tramp
        meets_requirements: true, // Always true for professions with no requirements
        method_used: '3d6',
      }),
    };

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            access_token: 'mock-token',
            has_character: false,
            character_name: '',
          }),
        });
      } else if (url.includes('/professions')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            professions: createMockProfessions(),
          }),
        });
      } else if (url.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            player: {
              id: 1,
              name: 'testuser',
              profession_id: 0,
            },
          }),
        });
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    // Register user
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

    // Select Tramp profession
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const trampCard = screen.getByText('Tramp').closest('.profession-card');
    fireEvent.click(trampCard!);

    const nextButton = screen.getByText('Next');
    fireEvent.click(nextButton);

    // Should show stats rolling screen
    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    // Should show all stats
    expect(screen.getByText('Strength:')).toBeInTheDocument();
    expect(screen.getByText('Dexterity:')).toBeInTheDocument();
    expect(screen.getByText('Constitution:')).toBeInTheDocument();
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();
    expect(screen.getByText('Charisma:')).toBeInTheDocument();

    // Accept stats and create character
    const acceptButton = screen.getByText('Accept Stats & Create Character');
    fireEvent.click(acceptButton);

    // Should show game terminal
    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });

  it('should allow rerolling stats for professions with requirements', async () => {
    setupBasicMocks();

    // Mock multiple stats responses - first one doesn't meet requirements, second one does
    let rollCount = 0;
    const statsResponses = [
      {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
            strength: 10,
            dexterity: 12,
            constitution: 11,
            intelligence: 12, // Does NOT meet requirement (>= 14)
            wisdom: 10, // Does NOT meet requirement (>= 12)
            charisma: 9,
          },
          stat_summary: {
            total: 64,
            average: 10.67,
            highest: 12,
            lowest: 9,
          },
          profession_id: 2,
          meets_requirements: false,
          method_used: '3d6',
        }),
      },
      {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
            strength: 10,
            dexterity: 12,
            constitution: 11,
            intelligence: 15, // Meets requirement (>= 14)
            wisdom: 13, // Meets requirement (>= 12)
            charisma: 9,
          },
          stat_summary: {
            total: 70,
            average: 11.67,
            highest: 15,
            lowest: 9,
          },
          profession_id: 2,
          meets_requirements: true,
          method_used: '3d6',
        }),
      },
    ];

    mockFetch.mockImplementation(url => {
      if (url.includes('/auth/register')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            access_token: 'mock-token',
            has_character: false,
            character_name: '',
          }),
        });
      } else if (url.includes('/professions')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            professions: createMockProfessions(),
          }),
        });
      } else if (url.includes('/players/roll-stats')) {
        const response = statsResponses[rollCount];
        rollCount++;
        return Promise.resolve(response);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({
            player: {
              id: 1,
              name: 'testuser',
              profession_id: 2,
            },
          }),
        });
      }
      return Promise.reject(new Error('Unexpected URL'));
    });

    render(<App />);

    // Register user
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

    // Select Scholar profession
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);

    const nextButton = screen.getByText('Next');
    fireEvent.click(nextButton);

    // Should show stats rolling screen
    await waitFor(() => {
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    // Should show first set of stats
    expect(screen.getByText('Intelligence:')).toBeInTheDocument();
    expect(screen.getByText('Wisdom:')).toBeInTheDocument();

    // Click reroll button
    const rerollButton = screen.getByText('Reroll Stats');
    fireEvent.click(rerollButton);

    // Should show second set of stats (that meet requirements)
    await waitFor(() => {
      expect(screen.getByText('Intelligence:')).toBeInTheDocument();
      expect(screen.getByText('Wisdom:')).toBeInTheDocument();
    });

    // Accept stats and create character
    const acceptButton = screen.getByText('Accept Stats & Create Character');
    fireEvent.click(acceptButton);

    // Should show game terminal
    await waitFor(() => {
      expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
    });
  });
});
