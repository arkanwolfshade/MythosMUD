import { fireEvent, render, screen, waitFor, act } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { StatsRollingScreen } from './StatsRollingScreen';

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

describe('StatsRollingScreen', () => {
  const defaultProps = {
    characterName: 'TestCharacter',
    onStatsAccepted: vi.fn(),
    onError: vi.fn(),
    baseUrl: 'http://localhost:54731',
    authToken: 'mock-token',
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Initial Rendering', () => {
    it('should render with character name', async () => {
      const mockResponse = {
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
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
        expect(screen.getByText('Character: TestCharacter')).toBeInTheDocument();
      });
    });

    it('should show loading state initially', () => {
      render(<StatsRollingScreen {...defaultProps} />);

      expect(screen.getByText("Rolling your character's stats...")).toBeInTheDocument();
    });
  });

  describe('Stats Rolling', () => {
    it('should roll stats on mount when authToken is available', async () => {
      const mockResponse = {
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
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith('http://localhost:54731/players/roll-stats', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer mock-token',
          },
          body: JSON.stringify({ method: '3d6' }),
        });
      });

      await waitFor(() => {
        expect(screen.getByText('12')).toBeInTheDocument();
        expect(screen.getByText('14')).toBeInTheDocument();
        expect(screen.getByText('10')).toBeInTheDocument();
        expect(screen.getByText('16')).toBeInTheDocument();
        expect(screen.getByText('8')).toBeInTheDocument();
        expect(screen.getByText('13')).toBeInTheDocument();
      });
    });

    it('should handle successful stats rolling', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          stats: {
            strength: 15,
            dexterity: 12,
            constitution: 14,
            intelligence: 10,
            wisdom: 13,
            charisma: 11,
          },
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('15')).toBeInTheDocument();
        expect(screen.getByText('12')).toBeInTheDocument();
        expect(screen.getByText('14')).toBeInTheDocument();
        expect(screen.getByText('10')).toBeInTheDocument();
        expect(screen.getByText('13')).toBeInTheDocument();
        expect(screen.getByText('11')).toBeInTheDocument();
      });

      expect(screen.getByText('Accept Stats & Create Character')).toBeInTheDocument();
      expect(screen.getByText('Reroll Stats')).toBeInTheDocument();
    });

    it('should handle stats rolling failure', async () => {
      const mockResponse = {
        ok: false,
        status: 500,
        json: vi.fn().mockResolvedValue({
          detail: 'Internal server error',
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
      });
    });

    it('should handle network error', async () => {
      mockFetch.mockRejectedValue(new Error('Network error'));

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
      });

      expect(defaultProps.onError).toHaveBeenCalledWith('Failed to connect to server');
    });
  });

  describe('Stats Acceptance', () => {
    it('should call onStatsAccepted when stats are accepted', async () => {
      // Mock the initial stats rolling
      const mockStatsResponse = {
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
        }),
      };

      // Mock the character creation API call
      const mockCreateResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          player: { id: 'test-player-id' },
        }),
      };

      // Mock fetch to return different responses for different calls
      mockFetch
        .mockResolvedValueOnce(mockStatsResponse) // First call for stats rolling
        .mockResolvedValueOnce(mockCreateResponse); // Second call for character creation

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Accept Stats & Create Character')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats & Create Character');
      await act(async () => {
        fireEvent.click(acceptButton);
      });

      await waitFor(() => {
        expect(defaultProps.onStatsAccepted).toHaveBeenCalledWith({
          strength: 12,
          dexterity: 14,
          constitution: 10,
          intelligence: 16,
          wisdom: 8,
          charisma: 13,
        });
      });
    });
  });

  describe('Stats Rerolling', () => {
    it('should allow rerolling stats', async () => {
      const mockResponse = {
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
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<StatsRollingScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Reroll Stats')).toBeInTheDocument();
      });

      const rerollButton = screen.getByText('Reroll Stats');
      await act(async () => {
        fireEvent.click(rerollButton);
      });

      // Should make another API call
      expect(mockFetch).toHaveBeenCalledTimes(2);
    });
  });
});
