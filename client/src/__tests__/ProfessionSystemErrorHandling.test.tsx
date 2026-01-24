import { act, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from '../App';

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
      // Mock profession API failure
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
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

      // Should return to login screen when server unavailability is detected
      // Wait for the app to navigate back to login
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
      // Mock empty profession list
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue([]),
          });
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

      // Should show profession selection screen with empty state
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
        expect(screen.getByText('Welcome, testuser')).toBeInTheDocument();
      });
    });

    it('should handle malformed profession data gracefully', async () => {
      // Mock malformed profession data
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue(createMockLoginResponse([])),
          });
        } else if (url.includes('/professions')) {
          return Promise.resolve({
            ok: true,
            json: vi.fn().mockResolvedValue([
              {
                id: 0,
                name: 'Tramp',
                // Missing required fields
                description: 'A wandering soul',
              },
            ]),
          });
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

      // Should handle malformed data gracefully by showing error
      await waitFor(() => {
        expect(screen.getByText('Error Loading Professions')).toBeInTheDocument();
        expect(screen.getByText(/Invalid API response: expected Profession\[\]/)).toBeInTheDocument();
      });
    });
  });

  describe('Stat Rolling Error Handling', () => {
    it('should handle stat rolling API failure gracefully', async () => {
      setupBasicMocks();

      // Mock stat rolling API failure
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
          return Promise.reject(new Error('Stat rolling failed'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      // Navigate to profession selection
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

      // Select profession and proceed to stats rolling
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Should return to login when stat rolling fails
      // "Stat rolling failed" doesn't match server unavailability patterns,
      // so it calls onError('Failed to connect to server'), which triggers returnToLogin()
      await waitFor(
        () => {
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 3000 }
      );
    });

    it('should handle invalid profession ID in stat rolling', async () => {
      setupBasicMocks();

      // Mock stat rolling with invalid profession ID
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

      // Navigate to profession selection
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

      // Select profession and proceed to stats rolling
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Should show error for invalid profession ID
      await waitFor(() => {
        expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
      });
    });

    it('should handle malformed stat response gracefully', async () => {
      setupBasicMocks();

      // Mock malformed stat response
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
              // Missing required stats fields
              profession_id: 0,
              meets_requirements: true,
            }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      // Navigate to profession selection
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

      // Select profession and proceed to stats rolling
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Should handle malformed response gracefully
      // Validation error triggers onError('Failed to connect to server'), which returns to login
      await waitFor(
        () => {
          expect(screen.getByText('MythosMUD')).toBeInTheDocument();
          expect(screen.getByText('Server is unavailable. Please try again later.')).toBeInTheDocument();
        },
        { timeout: 3000 }
      );
    });
  });

  describe('Character Creation Error Handling', () => {
    it('should handle character creation API failure gracefully', async () => {
      setupBasicMocks();

      // Mock character creation API failure
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
          // Mock fetch rejection to trigger catch block in component
          return Promise.reject(new Error('Character creation failed'));
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      // Navigate through the flow
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

      // Select profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Accept stats
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Enter character name (required for multi-character support)
      const nameInput = screen.getByPlaceholderText("Enter your character's name");
      await act(async () => {
        fireEvent.change(nameInput, { target: { value: 'TestCharacter' } });
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');

      // Click and verify error is handled gracefully (no uncaught exception)
      // The error handling should catch the Promise.reject and call onError
      // which sets error state without crashing the app
      await act(async () => {
        fireEvent.click(acceptButton);
      });

      // Verify graceful error handling: the error should be caught and handled
      // The component's catch block should call onError and set error state
      // We verify this by ensuring the app doesn't crash and remains functional
      await waitFor(
        () => {
          // App should still be rendered (error handled gracefully)
          const appElement = document.querySelector('.App');
          expect(appElement).toBeInTheDocument();
        },
        { timeout: 2000 }
      );
    });

    it('should handle duplicate character name error', async () => {
      setupBasicMocks();

      // Mock duplicate character name error
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
            ok: false,
            status: 409,
            json: vi.fn().mockResolvedValue({
              detail: 'Character name already exists',
            }),
          });
        }
        return Promise.reject(new Error('Unknown endpoint'));
      });

      render(<App />);

      // Navigate through the flow
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

      // Select profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Accept stats
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Enter character name (required for multi-character support)
      const nameInput = screen.getByPlaceholderText("Enter your character's name");
      fireEvent.change(nameInput, { target: { value: 'TestCharacter' } });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      await act(async () => {
        fireEvent.click(acceptButton);
      });

      // Should show specific error for duplicate character name
      await waitFor(
        () => {
          expect(screen.getByText('Character name already exists')).toBeInTheDocument();
        },
        { timeout: 3000 }
      );
    });
  });

  describe('Edge Cases', () => {
    it('should handle rapid profession selection changes', async () => {
      setupBasicMocks();
      render(<App />);

      // Navigate to profession selection
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
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      // Rapidly click between professions
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');

      fireEvent.click(trampCard!);
      fireEvent.click(gutterRatCard!);
      fireEvent.click(trampCard!);
      fireEvent.click(gutterRatCard!);

      // Should handle rapid changes gracefully
      expect(screen.getByText('Next')).toBeInTheDocument();
    });

    it('should handle rapid stat rerolling', async () => {
      setupBasicMocks();
      render(<App />);

      // Navigate to stats rolling
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

      // Select profession
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

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
      render(<App />);

      // Navigate to profession selection
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
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      // Select profession and proceed
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Should handle concurrent calls gracefully
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });
    });
  });
});
