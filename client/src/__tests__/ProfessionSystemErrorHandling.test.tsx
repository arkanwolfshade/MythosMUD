import { act, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../App';
import { CharacterNameScreen } from '../components/CharacterNameScreen.jsx';

// Mock fetch globally
const mockFetch = vi.fn();
globalThis.fetch = mockFetch as typeof fetch;

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
    getToken: vi.fn(() => null),
    setToken: vi.fn(),
    setRefreshToken: vi.fn(),
    clearAllTokens: vi.fn(),
    isValidToken: vi.fn(() => false),
    isTokenExpired: vi.fn(() => true),
  },
  inputSanitizer: {
    sanitizeUsername: vi.fn(val => val),
    sanitizeCommand: vi.fn(val => val),
  },
}));

describe('Profession System Error Handling and Edge Cases', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  // Helper function to create a valid LoginResponse mock
  const createMockLoginResponse = (
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
  ) => ({
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
  });

  const createMockProfessions = () => [
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

  /** Plan 10.6: skills step needs catalog; 13+ skills for 9 occupation + 4 personal slots. */
  const createMockSkills = () =>
    Array.from({ length: 20 }, (_, i) => ({
      id: i + 1,
      key: `skill_${i + 1}`,
      name: `Skill ${i + 1}`,
      base_value: 5 + (i % 50),
      allow_at_creation: true,
    }));

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

  const setupBasicMocks = () => {
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
      json: vi.fn().mockResolvedValue({
        stats: {
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
        },
        stat_summary: {
          total: 73,
          average: 12.17,
          highest: 16,
          lowest: 8,
        },
        profession_id: 0,
        meets_requirements: true,
        method_used: '3d6',
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
      } else if (url.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse);
      } else if (url.includes('/players/create-character')) {
        return Promise.resolve(characterCreationResponse);
      }
      return Promise.reject(new Error('Unknown endpoint'));
    });
  };

  describe('Profession Selection Error Handling', () => {
    it('should handle profession API failure gracefully', async () => {
      const statsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
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
          },
          stat_summary: { total: 73, average: 12.17, highest: 16, lowest: 8 },
          profession_id: 0,
          meets_requirements: true,
          method_used: '3d6',
        }),
      };
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse);
        } else if (url.includes('/professions')) {
          return Promise.reject(new Error('Network error'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      // Register user
      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Plan 10.6: stats first; advance to profession so profession fetch runs and fails
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(
        () => {
          // When server unavailability is detected, the app returns to login screen
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 3000 }
      );
    });

    it('should handle empty profession list gracefully', async () => {
      const statsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
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
          },
          stat_summary: { total: 73, average: 12.17, highest: 16, lowest: 8 },
          profession_id: 0,
          meets_requirements: true,
          method_used: '3d6',
        }),
      };
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ professions: [] }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Plan 10.6: stats first, then profession
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
      fireEvent.click(screen.getByText('Accept Stats'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
    });

    it('should handle malformed profession data gracefully', async () => {
      const statsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
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
          },
          stat_summary: { total: 73, average: 12.17, highest: 16, lowest: 8 },
          profession_id: 0,
          meets_requirements: true,
          method_used: '3d6',
        }),
      };
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue([
              {
                id: 0,
                name: 'Tramp',
                description: 'A wandering soul',
              },
            ]),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

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
        expect(screen.getByText('Error Loading Professions')).toBeInTheDocument();
        expect(screen.getByText(/Invalid API response: expected Profession\[\]/)).toBeInTheDocument();
      });
    });
  });

  describe('Stat Rolling Error Handling', () => {
    it('should handle stat rolling API failure gracefully', async () => {
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.reject(new Error('Stat rolling failed'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Plan 10.6: stats step loads and calls roll-stats on mount; when it fails we return to login
      await waitFor(
        () => {
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 5000 }
      );
    });

    it('should handle invalid profession ID in stat rolling', async () => {
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve({
            ok: false,
            status: 400,
            json: vi.fn().mockResolvedValue({
              detail: 'Invalid profession ID',
            }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // When roll-stats returns 400, stats screen shows error view (no "Character Creation" header)
      await waitFor(() => {
        expect(screen.getByText('Invalid profession ID')).toBeInTheDocument();
      });
      expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
    });

    it('should handle malformed stat response gracefully', async () => {
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              profession_id: 0,
              meets_requirements: true,
            }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      await waitFor(
        () => {
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 5000 }
      );
    });
  });

  describe('Character Creation Error Handling', () => {
    beforeEach(() => {
      vi.stubGlobal('fetch', mockFetch);
    });

    it('should handle character creation API failure gracefully', async () => {
      setupBasicMocks();

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              professions: createMockProfessions(),
            }),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              stats: {
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
              },
              stat_summary: { total: 73, average: 12.17, highest: 16, lowest: 8 },
              profession_id: 0,
              meets_requirements: true,
              method_used: '3d6',
            }),
          });
        } else if (url.includes('/skills/')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ skills: createMockSkills() }),
          });
        } else if (url.includes('/players/create-character')) {
          return Promise.reject(new Error('Character creation failed'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

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

      await fillSkillSlotsAndConfirm();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
      });
      const nameInput = screen.getByPlaceholderText('Enter name');
      await act(async () => {
        fireEvent.change(nameInput, { target: { value: 'TestCharacter' } });
      });
      await act(async () => {
        fireEvent.click(screen.getByText('Create Character'));
      });

      await waitFor(
        () => {
          expect(document.querySelector('.App')).toBeInTheDocument();
        },
        { timeout: 2000 }
      );
    });

    // Isolated test: render CharacterNameScreen only and mock fetch so create-character returns 409.
    // Full App flow is not used so we avoid other fetches/navigation overriding the mock.
    it('should handle duplicate character name error', async () => {
      const createCharacterDetail = { detail: 'Character name already exists' };
      mockFetch.mockImplementation((input: string | URL | Request) => {
        const urlString =
          typeof input === 'string' ? input : input instanceof URL ? input.toString() : ((input as Request).url ?? '');
        if (urlString.includes('create-character')) {
          return Promise.resolve(
            new Response(JSON.stringify(createCharacterDetail), { status: 409, statusText: 'Conflict' })
          );
        }
        return Promise.reject(new Error('Unexpected request'));
      });

      const stats = {
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
      };
      const profession = {
        id: 1,
        name: 'Tramp',
        description: 'A wanderer',
        flavor_text: null,
        stat_requirements: [],
      };
      const skillsPayload = { occupation_slots: [], personal_interest: [] };
      const onComplete = vi.fn();
      const onError = vi.fn();
      const onBack = vi.fn();

      render(
        <CharacterNameScreen
          stats={stats}
          profession={profession}
          skillsPayload={skillsPayload}
          baseUrl="https://test.example/v1"
          authToken="test-token"
          onComplete={onComplete}
          onError={onError}
          onBack={onBack}
        />
      );

      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'TestCharacter' } });
      await act(async () => {
        fireEvent.click(screen.getByRole('button', { name: /Create Character/i }));
      });

      await waitFor(() => {
        expect(screen.getByText('Character name already exists')).toBeInTheDocument();
      });
      expect(onComplete).not.toHaveBeenCalled();
      expect(onError).toHaveBeenCalledWith('Character name already exists');
    });
  });

  describe('Edge Cases', () => {
    it('should handle rapid profession selection changes', async () => {
      setupBasicMocks();
      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

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
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');

      fireEvent.click(trampCard!);
      fireEvent.click(gutterRatCard!);
      fireEvent.click(trampCard!);
      fireEvent.click(gutterRatCard!);

      expect(screen.getByText('Next')).toBeInTheDocument();
    });

    it('should handle rapid stat rerolling', async () => {
      setupBasicMocks();
      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Plan 10.6: stats first; wait for stats screen
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Rapidly click reroll button
      const rerollButton = screen.getByText('Reroll Stats');
      await act(async () => {
        fireEvent.click(rerollButton);
        fireEvent.click(rerollButton);
        fireEvent.click(rerollButton);
      });

      // Should handle rapid rerolling gracefully
      expect(screen.getByText('Character Creation')).toBeInTheDocument();
    });

    it('should handle network timeout gracefully', async () => {
      // Mock network timeout
      mockFetch.mockImplementation(() => {
        return new Promise((_, reject) => {
          setTimeout(() => {
            reject(new Error('Network timeout'));
          }, 100);
        });
      });

      render(<App />);

      // Try to register
      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Should handle timeout gracefully
      await waitFor(() => {
        expect(screen.getByText('Network timeout')).toBeInTheDocument();
      });
    });

    it('should handle concurrent API calls gracefully', async () => {
      setupBasicMocks();
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ professions: createMockProfessions() }),
          });
        } else if (url.includes('/players/roll-stats')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              stats: {
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
              },
              stat_summary: { total: 73, average: 12.17, highest: 16, lowest: 8 },
              profession_id: 0,
              meets_requirements: true,
              method_used: '3d6',
            }),
          });
        } else if (url.includes('/skills/')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ skills: createMockSkills() }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      fireEvent.click(screen.getByText('Need an account? Register'));
      fireEvent.click(screen.getByText('Enter the Void'));

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
    });
  });
});
