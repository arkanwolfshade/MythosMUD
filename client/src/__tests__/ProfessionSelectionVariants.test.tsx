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

describe('Profession Selection - Different Profession Choices', () => {
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
      return Promise.reject(new Error('Unexpected URL'));
    });
  };

  it('should allow selection of Tramp profession (no requirements)', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // Select Tramp profession
    const trampCard = screen.getByText('Tramp').closest('.profession-card');
    fireEvent.click(trampCard!);

    await waitFor(() => {
      expect(trampCard).toHaveClass('selected');
      // Check that the selected card shows "No requirements"
      const selectedCard = screen.getByRole('button', { pressed: true });
      expect(selectedCard).toHaveTextContent('No requirements');
    });

    // Should be able to proceed
    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();
  });

  it('should allow selection of Gutter Rat profession (no requirements)', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // Select Gutter Rat profession
    const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
    fireEvent.click(gutterRatCard!);

    await waitFor(() => {
      expect(gutterRatCard).toHaveClass('selected');
      // Check that the selected card shows "No requirements"
      const selectedCard = screen.getByRole('button', { pressed: true });
      expect(selectedCard).toHaveTextContent('No requirements');
    });

    // Should be able to proceed
    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();
  });

  it('should show stat requirements for Scholar profession', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // Select Scholar profession
    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);

    await waitFor(() => {
      expect(scholarCard).toHaveClass('selected');
      expect(screen.getByText('Minimum: Intelligence 14, Wisdom 12')).toBeInTheDocument();
    });

    // Should be able to proceed
    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();
  });

  it('should show stat requirements for Soldier profession', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // Select Soldier profession
    const soldierCard = screen.getByText('Soldier').closest('.profession-card');
    fireEvent.click(soldierCard!);

    await waitFor(() => {
      expect(soldierCard).toHaveClass('selected');
      expect(screen.getByText('Minimum: Strength 13, Constitution 12')).toBeInTheDocument();
    });

    // Should be able to proceed
    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();
  });

  it('should show stat requirements for Detective profession', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // Select Detective profession
    const detectiveCard = screen.getByText('Detective').closest('.profession-card');
    fireEvent.click(detectiveCard!);

    await waitFor(() => {
      expect(detectiveCard).toHaveClass('selected');
      expect(screen.getByText('Minimum: Intelligence 12, Wisdom 13, Dexterity 11')).toBeInTheDocument();
    });

    // Should be able to proceed
    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();
  });

  it('should allow switching between different professions', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // First select Tramp
    const trampCard = screen.getByText('Tramp').closest('.profession-card');
    fireEvent.click(trampCard!);

    await waitFor(() => {
      expect(trampCard).toHaveClass('selected');
      // Check that the selected card shows "No requirements"
      const selectedCard = screen.getByRole('button', { pressed: true });
      expect(selectedCard).toHaveTextContent('No requirements');
    });

    // Then switch to Scholar
    const scholarCard = screen.getByText('Scholar').closest('.profession-card');
    fireEvent.click(scholarCard!);

    await waitFor(() => {
      expect(trampCard).not.toHaveClass('selected');
      expect(scholarCard).toHaveClass('selected');
      expect(screen.getByText('Minimum: Intelligence 14, Wisdom 12')).toBeInTheDocument();
    });

    // Then switch to Soldier
    const soldierCard = screen.getByText('Soldier').closest('.profession-card');
    fireEvent.click(soldierCard!);

    await waitFor(() => {
      expect(scholarCard).not.toHaveClass('selected');
      expect(soldierCard).toHaveClass('selected');
      expect(screen.getByText('Minimum: Strength 13, Constitution 12')).toBeInTheDocument();
    });

    // Should be able to proceed with any selection
    const nextButton = screen.getByText('Next');
    expect(nextButton).not.toBeDisabled();
  });

  it('should display all profession descriptions and flavor text', async () => {
    setupBasicMocks();
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

    // Should show profession selection
    await waitFor(() => {
      expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
    });

    // Check that all professions are displayed with their descriptions
    expect(screen.getByText('Tramp')).toBeInTheDocument();
    expect(screen.getByText('A wandering soul with no particular skills or connections.')).toBeInTheDocument();
    expect(
      screen.getByText('You have spent your days drifting from place to place, learning to survive on your wits alone.')
    ).toBeInTheDocument();

    expect(screen.getByText('Gutter Rat')).toBeInTheDocument();
    expect(screen.getByText('A street-smart survivor from the urban underbelly.')).toBeInTheDocument();
    expect(
      screen.getByText('The alleys and gutters have been your home, teaching you the harsh realities of city life.')
    ).toBeInTheDocument();

    expect(screen.getByText('Scholar')).toBeInTheDocument();
    expect(screen.getByText('A learned individual with high intelligence and wisdom.')).toBeInTheDocument();
    expect(
      screen.getByText('Your mind is your greatest weapon, filled with knowledge of the arcane and mundane.')
    ).toBeInTheDocument();

    expect(screen.getByText('Soldier')).toBeInTheDocument();
    expect(screen.getByText('A disciplined warrior with combat training.')).toBeInTheDocument();
    expect(screen.getByText('You have served in conflicts and know the art of war and survival.')).toBeInTheDocument();

    expect(screen.getByText('Detective')).toBeInTheDocument();
    expect(screen.getByText('A sharp-eyed investigator with keen perception.')).toBeInTheDocument();
    expect(
      screen.getByText('You have a talent for noticing details others miss and solving mysteries.')
    ).toBeInTheDocument();
  });
});
