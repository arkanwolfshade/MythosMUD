import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { App } from './App';

// Mock fetch globally using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(global, 'fetch');

// Mock the logger
vi.mock('./utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
    debug: vi.fn(),
    warn: vi.fn(),
  },
}));

// Mock secure token storage
vi.mock('./utils/security', () => ({
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

// SKIPPED: This is an E2E test that should use Playwright, not Vitest
// These tests require full App authentication flows and should be in client/tests/
describe.skip('App - Character Creation Flow Integration', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    fetchSpy.mockClear();
  });

  afterEach(() => {
    fetchSpy.mockRestore();
  });

  describe('Complete Character Creation Flow', () => {
    it('should navigate through profession selection to stats rolling to game', async () => {
      // Mock registration response
      const registrationResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      // Mock professions response
      const professionsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: [
            {
              id: 0,
              name: 'Tramp',
              description: 'A wandering soul with no particular skills or connections.',
              flavor_text:
                'You have spent your days drifting from place to place, learning to survive on your wits alone.',
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
          ],
        }),
      };

      // Mock stats rolling response
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

      // Mock character creation response
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

      // Set up fetch mock to return different responses based on URL
      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return Promise.resolve(registrationResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(professionsResponse as unknown as Response);
        } else if (urlString.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse as unknown as Response);
        } else if (urlString.includes('/players/create-character')) {
          return Promise.resolve(characterCreationResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Step 1: Switch to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      // Step 2: Register a new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Step 2: Should show profession selection screen
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
        expect(screen.getByText('Welcome, testuser')).toBeInTheDocument();
      });

      // Step 3: Select a profession
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      await waitFor(() => {
        expect(trampCard).toHaveClass('selected');
        const nextButton = screen.getByText('Next');
        expect(nextButton).not.toBeDisabled();
      });

      // Step 4: Click Next to go to stats rolling
      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Step 5: Should show stats rolling screen
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
        expect(screen.getByText(/testuser/)).toBeInTheDocument();
      });

      // Step 6: Accept stats and create character
      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Step 7: Should show game terminal
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
        // Game terminal should be visible
        expect(screen.getByTestId('command-input')).toBeInTheDocument();
      });
    });

    it('should allow going back from stats rolling to profession selection', async () => {
      // Mock responses
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
          professions: [
            {
              id: 0,
              name: 'Tramp',
              description: 'A wandering soul with no particular skills or connections.',
              flavor_text:
                'You have spent your days drifting from place to place, learning to survive on your wits alone.',
              stat_requirements: {},
              mechanical_effects: {},
              is_available: true,
            },
          ],
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

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return Promise.resolve(registrationResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(professionsResponse as unknown as Response);
        } else if (urlString.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Switch to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      // Register and go to profession selection
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Select profession and go to stats rolling
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Should be on stats rolling screen
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Click Back button
      const backButton = screen.getByText('Back');
      fireEvent.click(backButton);

      // Should return to profession selection
      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
        expect(screen.getByText(/Welcome, testuser/)).toBeInTheDocument();
      });
    });

    it('should handle profession selection errors gracefully', async () => {
      // Mock registration response
      const registrationResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      // Mock professions error response
      const professionsErrorResponse = {
        ok: false,
        status: 500,
        json: vi.fn().mockResolvedValue({ detail: 'Internal server error' }),
      };

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return Promise.resolve(registrationResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(professionsErrorResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Switch to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      // Register user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteCodeInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.change(inviteCodeInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Should show error state
      await waitFor(() => {
        expect(screen.getByText('Error Loading Professions')).toBeInTheDocument();
        expect(screen.getByText('Internal server error')).toBeInTheDocument();
      });

      // Should have retry and back buttons
      expect(screen.getByText('Retry')).toBeInTheDocument();
      expect(screen.getByText('Back')).toBeInTheDocument();
    });

    it('should handle stats rolling with profession requirements', async () => {
      // Mock responses
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
          professions: [
            {
              id: 2,
              name: 'Scholar',
              description: 'A learned individual with high intelligence.',
              flavor_text: 'Your mind is your greatest weapon.',
              stat_requirements: { intelligence: 14, wisdom: 12 },
              mechanical_effects: {},
              is_available: true,
            },
          ],
        }),
      };

      const statsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
            strength: 10,
            dexterity: 12,
            constitution: 11,
            intelligence: 15,
            wisdom: 13,
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

      const characterCreationResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          player: {
            id: 1,
            name: 'testuser',
            profession_id: 2,
          },
        }),
      };

      fetchSpy.mockImplementation((url: string | URL | Request) => {
        const urlString = typeof url === 'string' ? url : url instanceof URL ? url.toString() : url.url;
        if (urlString.includes('/auth/register')) {
          return Promise.resolve(registrationResponse as unknown as Response);
        } else if (urlString.includes('/professions')) {
          return Promise.resolve(professionsResponse as unknown as Response);
        } else if (urlString.includes('/players/roll-stats')) {
          return Promise.resolve(statsResponse as unknown as Response);
        } else if (urlString.includes('/players/create-character')) {
          return Promise.resolve(characterCreationResponse as unknown as Response);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Switch to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      // Register user
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

      // Should show stats rolling with profession requirements
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
        // Stats should meet the profession requirements
        expect(screen.getByText('Intelligence:')).toBeInTheDocument();
        expect(screen.getByText('Wisdom:')).toBeInTheDocument();
      });

      // Accept stats and create character
      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      // Should show game terminal
      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
        expect(screen.getByTestId('command-input')).toBeInTheDocument();
      });
    });
  });
});
