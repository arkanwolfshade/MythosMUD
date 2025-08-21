import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import App from './App';

// Mock the child components
vi.mock('./components/EldritchEffectsDemo', () => ({
  EldritchEffectsDemo: () => <div data-testid="eldritch-effects-demo">Eldritch Effects Demo</div>,
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
        Stats Rolling for {characterName}
        {error && <div className="error-message">{error}</div>}
        <button onClick={() => onStatsAccepted({ strength: 10 })}>Accept Stats</button>
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

    it('should handle successful login', async () => {
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
        expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();
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
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();
      });
    });

    it('should handle stats acceptance', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          access_token: 'mock-token',
          has_character: false,
          character_name: '',
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();
      });

      // Accept stats
      const acceptButton = screen.getByText('Accept Stats');
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
      mockFetch.mockResolvedValue(mockResponse);

      render(<App />);

      // Login with new user
      const usernameInput = screen.getByPlaceholderText('Username');
      const passwordInput = screen.getByPlaceholderText('Password');
      const loginButton = screen.getByText('Enter the Void');

      fireEvent.change(usernameInput, { target: { value: 'newuser' } });
      fireEvent.change(passwordInput, { target: { value: 'newpass' } });
      fireEvent.click(loginButton);

      await waitFor(() => {
        expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();
      });

      // Trigger error - this should call onError which sets the error state
      const errorButton = screen.getByText('Trigger Error');
      fireEvent.click(errorButton);

      // The error should appear in the login form since we're back to the login state
      await waitFor(() => {
        expect(screen.getByText('Stats error')).toBeInTheDocument();
      });
    });
  });

  describe('Demo Mode', () => {
    it('should show demo mode when demo button is clicked', () => {
      render(<App />);

      const demoButton = screen.getByText('View Eldritch Effects Demo');
      fireEvent.click(demoButton);

      expect(screen.getByTestId('eldritch-effects-demo')).toBeInTheDocument();
      expect(screen.getByText('Exit Demo')).toBeInTheDocument();
    });

    it('should exit demo mode when exit button is clicked', () => {
      render(<App />);

      // Enter demo mode
      const demoButton = screen.getByText('View Eldritch Effects Demo');
      fireEvent.click(demoButton);

      expect(screen.getByTestId('eldritch-effects-demo')).toBeInTheDocument();

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
    it('should show loading state during login', async () => {
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
      mockFetch.mockImplementation(() => new Promise(resolve => setTimeout(() => resolve(mockResponse), 100)));

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
        expect(screen.getByTestId('stats-rolling-screen')).toBeInTheDocument();
      });
    });
  });
});
