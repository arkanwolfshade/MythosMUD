import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import App from '../App';

// Mock fetch globally
const mockFetch = vi.fn();
global.fetch = mockFetch;

// Mock the logger
vi.mock('../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
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

describe('Profession Choice Persistence to Database', () => {
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

    const statsResponse = {
      ok: true,
      json: vi.fn().mockResolvedValue({
        stats: {
          strength: 12,
          dexterity: 14,
          constitution: 10,
          intelligence: 16,
          wisdom: 8,
          charisma: 13,
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

  describe('Profession Persistence Verification', () => {
    it('should persist Tramp profession choice to database', async () => {
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

      // Select Tramp profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Accept stats and create character
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
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

      // Select Gutter Rat profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Accept stats and create character
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
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

      // Select Tramp profession first
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      // Switch to Gutter Rat profession
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Accept stats and create character
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Verify that the character creation API was called with the correct profession_id (Gutter Rat)
      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
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

      // Select Tramp profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Navigate back to profession selection
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const backButton = screen.getByText('Back');
      fireEvent.click(backButton);

      // Verify we're back at profession selection
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      // Select Gutter Rat profession
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);

      const nextButton2 = screen.getByText('Next');
      fireEvent.click(nextButton2);

      // Accept stats and create character
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Verify that the character creation API was called with the correct profession_id (Gutter Rat)
      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
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

      // Select Tramp profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Reroll stats multiple times
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const rerollButton = screen.getByText('Reroll Stats');
      fireEvent.click(rerollButton);
      fireEvent.click(rerollButton);
      fireEvent.click(rerollButton);

      // Accept stats and create character
      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
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
      // Mock malformed profession data
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
              professions: [
                {
                  id: 0,
                  name: 'Tramp',
                  description: 'A wandering soul',
                  // Missing required fields
                },
              ],
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
                intelligence: 16,
                wisdom: 8,
                charisma: 13,
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
          });
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
        return Promise.reject(new Error('Unknown endpoint'));
      });

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

      // Select profession (even with malformed data)
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Accept stats and create character
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Verify that the character creation API was called with the correct profession_id
      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
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
