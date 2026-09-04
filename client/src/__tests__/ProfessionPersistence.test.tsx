import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../App';

// Mock fetch globally using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(global, 'fetch');

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

// Un-skipped: runs with mocked fetch; full E2E remains in Playwright.
describe('Profession Choice Persistence to Database', () => {
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
  ];

  const setupBasicMocks = () => {
    const registrationResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        access_token: 'mock-token',
        token_type: 'Bearer',
        user_id: 'test-user-id',
        characters: [],
      }),
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

    const createMockSkills = () =>
      Array.from({ length: 20 }, (_, i) => ({
        id: i + 1,
        key: `skill_${i + 1}`,
        name: `Skill ${i + 1}`,
        base_value: 5 + (i % 50),
        allow_at_creation: true,
      }));

    const charactersListResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue([
        {
          player_id: 'char-1',
          name: 'testuser',
          profession_id: 0,
          level: 1,
          created_at: new Date().toISOString(),
          last_active: new Date().toISOString(),
        },
      ]),
    };

    fetchSpy.mockImplementation((url: string | URL | Request) => {
      const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
      if (urlString.includes('/auth/register')) {
        return Promise.resolve(registrationResponse as unknown as Response);
      } else if (urlString.includes('/professions')) {
        return Promise.resolve(professionsResponse as unknown as Response);
      } else if (urlString.includes('/players/roll-stats')) {
        return Promise.resolve(statsResponse as unknown as Response);
      } else if (urlString.includes('/skills/')) {
        return Promise.resolve({
          ok: true,
          json: vi.fn().mockResolvedValue({ skills: createMockSkills() }),
        } as unknown as Response);
      } else if (urlString.includes('/players/create-character')) {
        return Promise.resolve(characterCreationResponse as unknown as Response);
      } else if (urlString.includes('/players/characters') && !urlString.includes('create-character')) {
        return Promise.resolve(charactersListResponse as unknown as Response);
      }
      return Promise.reject(new Error('Unknown endpoint'));
    });
  };

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

  describe('Profession Persistence Verification', () => {
    it('should persist Tramp profession choice to database', async () => {
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
      fireEvent.click(trampCard!);
      fireEvent.click(screen.getByText('Next'));

      await fillSkillSlotsAndConfirm();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
      });
      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
      fireEvent.click(screen.getByText('Create Character'));

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/players/create-character'),
          expect.objectContaining({
            method: 'POST',
            headers: expect.objectContaining({
              'Content-Type': 'application/json',
            }),
            body: expect.stringContaining('"profession_id":0'),
          })
        );
      });

      // Verify that the response includes the correct profession_id
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should persist Gutter Rat profession choice to database', async () => {
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

      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);
      fireEvent.click(screen.getByText('Next'));

      await fillSkillSlotsAndConfirm();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
      });
      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
      fireEvent.click(screen.getByText('Create Character'));

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/players/create-character'),
          expect.objectContaining({
            method: 'POST',
            headers: expect.objectContaining({
              'Content-Type': 'application/json',
            }),
            body: expect.stringContaining('"profession_id":1'),
          })
        );
      });

      // Verify that the response includes the correct profession_id
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should persist profession choice when switching between professions', async () => {
      setupBasicMocks();
      render(<App />);

      // Navigate through the complete character creation flow
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
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);
      fireEvent.click(screen.getByText('Next'));

      await fillSkillSlotsAndConfirm();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
      });
      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
      fireEvent.click(screen.getByText('Create Character'));

      // Verify that the character creation API was called with the correct profession_id (Gutter Rat)
      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/players/create-character'),
          expect.objectContaining({
            method: 'POST',
            headers: expect.objectContaining({
              'Content-Type': 'application/json',
            }),
            body: expect.stringContaining('"profession_id":1'),
          })
        );
      });

      // Verify that the response includes the correct profession_id
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should persist profession choice when navigating back and forth', async () => {
      setupBasicMocks();
      render(<App />);

      // Navigate through the complete character creation flow
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
      fireEvent.click(screen.getByText('Back'));

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);
      fireEvent.click(screen.getByText('Next'));

      await fillSkillSlotsAndConfirm();

      await waitFor(() => {
        expect(screen.getByPlaceholderText('Enter name')).toBeInTheDocument();
      });
      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
      fireEvent.click(screen.getByText('Create Character'));

      // Verify that the character creation API was called with the correct profession_id (Gutter Rat)
      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/players/create-character'),
          expect.objectContaining({
            method: 'POST',
            headers: expect.objectContaining({
              'Content-Type': 'application/json',
            }),
            body: expect.stringContaining('"profession_id":1'),
          })
        );
      });

      // Verify that the response includes the correct profession_id
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should handle profession persistence with different stat rolling methods', async () => {
      setupBasicMocks();
      render(<App />);

      // Navigate through the complete character creation flow
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

      const rerollButton = screen.getByText('Reroll Stats');
      fireEvent.click(rerollButton);
      fireEvent.click(rerollButton);
      fireEvent.click(rerollButton);

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
      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
      fireEvent.click(screen.getByText('Create Character'));

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/players/create-character'),
          expect.objectContaining({
            method: 'POST',
            headers: expect.objectContaining({
              'Content-Type': 'application/json',
            }),
            body: expect.stringContaining('"profession_id":0'),
          })
        );
      });

      // Verify that the response includes the correct profession_id
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should persist profession choice with malformed profession data', async () => {
      const createMockSkills = () =>
        Array.from({ length: 20 }, (_, i) => ({
          id: i + 1,
          key: `skill_${i + 1}`,
          name: `Skill ${i + 1}`,
          base_value: 5 + (i % 50),
          allow_at_creation: true,
        }));

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              access_token: 'mock-token',
              token_type: 'Bearer',
              user_id: 'test-user-id',
              characters: [],
            }),
          } as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              professions: [
                {
                  id: 0,
                  name: 'Tramp',
                  description: 'A wandering soul',
                  // Missing required fields
                },
              ],
            }),
          } as unknown as Response);
        } else if (urlString.includes('/players/roll-stats')) {
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
          } as unknown as Response);
        } else if (urlString.includes('/skills/')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({ skills: createMockSkills() }),
          } as unknown as Response);
        } else if (urlString.includes('/players/create-character')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue({
              player: {
                id: 1,
                name: 'testuser',
                profession_id: 0,
              },
            }),
          } as unknown as Response);
        } else if (urlString.includes('/players/characters') && !urlString.includes('create-character')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue([
              {
                player_id: 'char-1',
                name: 'testuser',
                profession_id: 0,
                level: 1,
                created_at: new Date().toISOString(),
                last_active: new Date().toISOString(),
              },
            ]),
          } as unknown as Response);
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
      fireEvent.change(screen.getByPlaceholderText('Enter name'), { target: { value: 'testuser' } });
      fireEvent.click(screen.getByText('Create Character'));

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(fetchSpy).toHaveBeenCalledWith(
          expect.stringContaining('/players/create-character'),
          expect.objectContaining({
            method: 'POST',
            headers: expect.objectContaining({
              'Content-Type': 'application/json',
            }),
            body: expect.stringContaining('"profession_id":0'),
          })
        );
      });

      // Verify that the response includes the correct profession_id
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });
  });
});
