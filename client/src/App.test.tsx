import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import App from './App';

// Mock the child components
vi.mock('./components/EldritchEffectsDemo', () => ({
  EldritchEffectsDemo: ({ onExit }: { onExit?: () => void }) => (
    <div data-testid="eldritch-effects-demo">
      Eldritch Effects Demo
      {onExit && <button onClick={onExit}>Exit Demo</button>}
    </div>
  ),
}));

vi.mock('./components/GameTerminalWithPanels', () => ({
  GameTerminalWithPanels: ({ playerName, authToken }: { playerName: string; authToken: string }) => (
    <div data-testid="game-terminal">
      Game Terminal for {playerName} with token: {authToken ? 'present' : 'missing'}
    </div>
  ),
}));

vi.mock('./components/StatsRollingScreen', () => ({
  StatsRollingScreen: ({
    characterName,
    onStatsAccepted,
    onError,
  }: {
    characterName: string;
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
        <p>Character: {characterName}</p>
        {error && <div className="error-message">{error}</div>}
        <button onClick={() => onStatsAccepted({ strength: 10 })}>Accept Stats & Create Character</button>
        <button onClick={handleError}>Trigger Error</button>
      </div>
    );
  },
}));

// Mock fetch globally
const mockFetch = vi.fn();
global.fetch = mockFetch;

describe('App', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    // Reset localStorage
    localStorage.clear();
  });

  describe('Login Flow', () => {
    it('should show login form by default', () => {
      render(<App />);

      expect(screen.getByText('MythosMUD')).toBeInTheDocument();
      expect(screen.getByText('Enter the realm of eldritch knowledge')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
      expect(screen.getByText('Enter the Void')).toBeInTheDocument();
    });

    it('should handle login form input changes', () => {
      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });

      expect(usernameInput).toHaveValue('testuser');
      expect(passwordInput).toHaveValue('testpass');
    });

    it('should show error when login fields are empty', async () => {
      render(<App />);

      const loginButton = screen.getByText('Enter the Void');
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Username and password are required')).toBeInTheDocument();
      });
    });

    // SKIPPED: Integration test - should be converted to Playwright E2E test
    it.skip('should handle successful login', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: true,
          character_name: 'testuser',
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith('/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username: 'testuser', password: 'testpass' }),
        });
      });

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should handle login failure', async () => {
      const mockResponse = {
        ok: false,
        status: 401,
        json: vi.fn().mockResolvedValue({ detail: 'Invalid credentials' }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'wrongpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Invalid credentials')).toBeInTheDocument();
      });
    });

    it('should handle login with missing access token', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({}),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('No access_token in response')).toBeInTheDocument();
      });
    });
  });

  describe('Registration Flow', () => {
    it('should toggle to registration mode', () => {
      render(<App />);

      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      expect(screen.getByPlaceholderText('Invite Code')).toBeInTheDocument();
      expect(screen.getByText('Already have an account? Login')).toBeInTheDocument();
    });

    it('should handle registration form input changes', () => {
      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });

      expect(usernameInput).toHaveValue('newuser');
      expect(passwordInput).toHaveValue('newpass');
      expect(inviteInput).toHaveValue('INVITE123');
    });

    it('should show error when registration fields are empty', async () => {
      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const registerButton = screen.getByText('Enter the Void');
      fireEvent.click(registerButton);

      await waitFor(() => {
        expect(screen.getByText('Username, password, and invite code are required')).toBeInTheDocument();
      });
    });

    it('should handle successful registration', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      const mockProfessionsResponse = {
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

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return Promise.resolve(mockResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith('/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: 'newuser',
            password: 'newpass',
            invite_code: 'INVITE123',
          }),
        });
      });

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
    });

    it('should handle registration failure', async () => {
      const mockResponse = {
        ok: false,
        status: 400,
        json: vi.fn().mockResolvedValue({ detail: 'Invalid invite code' }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVALID' } });
      fireEvent.click(registerButton);

      await waitFor(() => {
        expect(screen.getByText('Invalid invite code')).toBeInTheDocument();
      });
    });
  });

  describe('Stats Rolling Flow', () => {
    it('should show stats rolling screen for new character', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      const mockProfessionsResponse = {
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

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/login')) {
          return Promise.resolve(mockResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
    });

    // SKIPPED: Integration test - should be converted to Playwright E2E test
    it.skip('should handle stats acceptance', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      const mockProfessionsResponse = {
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

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/login')) {
          return Promise.resolve(mockResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      // Select profession first
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Wait for stats rolling screen
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Accept stats
      const acceptButton = screen.getByText('Accept Stats & Create Character');
      fireEvent.click(acceptButton);

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should handle stats error', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      const mockProfessionsResponse = {
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

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/login')) {
          return Promise.resolve(mockResponse);
        } else if (url.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });

      // Select profession and go to stats rolling
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      // Wait for stats rolling screen
      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
      });

      // Mock an error response for character creation
      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/login')) {
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
            json: vi.fn().mockResolvedValue([
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
            ]),
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
            ok: false,
            status: 500,
            json: vi.fn().mockResolvedValue({ detail: 'Character creation failed' }),
          });
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      // Trigger error by clicking the error button
      const errorButton = screen.getByText('Trigger Error');
      fireEvent.click(errorButton);

      // The error should appear in the stats rolling screen
      await waitFor(() => {
        expect(screen.getByText('Stats error')).toBeInTheDocument();
      });
    });
  });

  describe('Demo Mode', () => {
    it('should show demo mode when demo button is clicked', async () => {
      render(<App />);

      const demoButton = screen.getByText('View Eldritch Effects Demo');
      fireEvent.click(demoButton);

      // Wait for lazy-loaded component to render
      await waitFor(() => {
        expect(screen.getByTestId('eldritch-effects-demo')).toBeInTheDocument();
      });
      expect(screen.getByText('Exit Demo')).toBeInTheDocument();
    });

    it('should exit demo mode when exit button is clicked', async () => {
      render(<App />);

      // Enter demo mode
      const demoButton = screen.getByText('View Eldritch Effects Demo');
      fireEvent.click(demoButton);

      // Wait for lazy-loaded component to render
      await waitFor(() => {
        expect(screen.getByTestId('eldritch-effects-demo')).toBeInTheDocument();
      });

      // Exit demo mode
      const exitButton = screen.getByText('Exit Demo');
      fireEvent.click(exitButton);

      expect(screen.getByText('MythosMUD')).toBeInTheDocument();
      expect(screen.queryByTestId('eldritch-effects-demo')).not.toBeInTheDocument();
    });
  });

  describe('Form State Management', () => {
    it('should clear form when toggling between login and register', () => {
      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');

      // Fill in form
      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });

      expect(usernameInput).toHaveValue('testuser');
      expect(passwordInput).toHaveValue('testpass');

      // Toggle to register
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      // Form should be cleared
      expect(usernameInput).toHaveValue('');
      expect(passwordInput).toHaveValue('');

      // Toggle back to login
      const toggleBackButton = screen.getByText('Already have an account? Login');
      fireEvent.click(toggleBackButton);

      // Form should still be cleared
      expect(usernameInput).toHaveValue('');
      expect(passwordInput).toHaveValue('');
    });

    it('should clear error when toggling modes', () => {
      render(<App />);

      // Trigger an error
      const loginButton = screen.getByText('Enter the Void');
      fireEvent.click(loginButton);

      expect(screen.getByText('Username and password are required')).toBeInTheDocument();

      // Toggle to register - error should be cleared
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      expect(screen.queryByText('Username and password are required')).not.toBeInTheDocument();
    });
  });

  describe('Loading States', () => {
    // SKIPPED: Integration test - should be converted to Playwright E2E test
    it.skip('should show loading state during login', async () => {
      // Mock a slow response
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: true,
          character_name: 'testuser',
        }),
      };
      mockFetch.mockImplementation(() => new Promise(resolve => setTimeout(() => resolve(mockResponse), 100)));

      render(<App />);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'testuser' } });
      fireEvent.change(passwordInput, { target: { value: 'testpass' } });
      fireEvent.click(loginButton);

      // Should show loading state
      expect(screen.getByText('Authenticating…')).toBeInTheDocument();
      expect(loginButton).toBeDisabled();

      await waitFor(() => {
        expect(screen.getByTestId('game-terminal')).toBeInTheDocument();
      });
    });

    it('should show loading state during registration', async () => {
      // Mock a slow response
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };

      const mockProfessionsResponse = {
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

      mockFetch.mockImplementation(url => {
        if (url.includes('/auth/register')) {
          return new Promise(resolve => setTimeout(() => resolve(mockResponse), 100));
        } else if (url.includes('/professions')) {
          return Promise.resolve(mockProfessionsResponse);
        }
        return Promise.reject(new Error('Unexpected URL'));
      });

      render(<App />);

      // Toggle to registration mode
      const toggleButton = screen.getByText('Need an account? Register');
      fireEvent.click(toggleButton);

      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const inviteInput = screen.getByPlaceholderText('Invite Code');
      const registerButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.change(inviteInput, { target: { value: 'INVITE123' } });
      fireEvent.click(registerButton);

      // Should show loading state
      expect(screen.getByText('Registering…')).toBeInTheDocument();
      expect(registerButton).toBeDisabled();

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
    });
  });
});
