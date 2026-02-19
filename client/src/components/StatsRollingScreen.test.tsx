import { act, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { StatsRollingScreen } from './StatsRollingScreen';

// Mock fetch globally
const mockFetch = vi.fn();
vi.stubGlobal('fetch', mockFetch);

// Mock the logger
vi.mock('../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
  },
}));

describe('StatsRollingScreen', () => {
  const defaultProps = {
    onStatsAccepted: vi.fn(),
    onError: vi.fn(),
    baseUrl: 'http://localhost:54731/v1',
    authToken: 'mock-token',
  };

  // Helper function to create a valid StatsRollResponse mock
  const createMockStatsResponse = (stats: {
    strength: number;
    dexterity: number;
    constitution: number;
    size: number;
    intelligence: number;
    power: number;
    education: number;
    charisma: number;
    luck: number;
    wisdom?: number;
  }) => {
    const allStats = {
      ...stats,
      wisdom: stats.wisdom ?? 50, // Default wisdom if not provided
    };
    const statValues = Object.values(allStats);
    const total = statValues.reduce((sum, val) => sum + val, 0);
    const average = total / statValues.length;
    const highest = Math.max(...statValues);
    const lowest = Math.min(...statValues);

    return {
      stats: allStats,
      stat_summary: {
        total,
        average,
        highest,
        lowest,
      },
      profession_id: 1,
      meets_requirements: true,
      method_used: '3d6',
    };
  };

  beforeEach(() => {
    vi.clearAllMocks();
    vi.stubGlobal('fetch', mockFetch);
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Stats Rerolling', () => {
    const rerollStatsData = createMockStatsResponse({
      strength: 60,
      dexterity: 70,
      constitution: 50,
      size: 55,
      intelligence: 80,
      power: 65,
      education: 40,
      charisma: 65,
      luck: 50,
    });
    const rerollResponseLike = {
      ok: true,
      json: () => Promise.resolve(rerollStatsData),
    };

    beforeEach(() => {
      vi.stubGlobal('fetch', mockFetch);
      mockFetch.mockImplementation(() => Promise.resolve(rerollResponseLike as unknown as Response));
    });

    it('should allow rerolling stats', async () => {
      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        expect(screen.getByText('Reroll Stats')).toBeInTheDocument();
      });

      const rerollButton = screen.getByText('Reroll Stats');
      await act(async () => {
        fireEvent.click(rerollButton);
      });

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledTimes(2);
      });
    });
  });

  describe('Initial Rendering', () => {
    it('should render stats and accept button', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockStatsResponse({
            strength: 60,
            dexterity: 70,
            constitution: 50,
            size: 55,
            intelligence: 80,
            power: 65,
            education: 40,
            charisma: 65,
            luck: 50,
          })
        ),
      };
      mockFetch.mockResolvedValue(mockResponse);

      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        expect(screen.getByText('Character Creation')).toBeInTheDocument();
        expect(screen.getByText('Accept Stats')).toBeInTheDocument();
      });
    });

    it('should show loading state initially', async () => {
      // Create a promise that we can control to delay the fetch response
      let resolveFetch: (value: Response) => void;
      const fetchPromise = new Promise<Response>(resolve => {
        resolveFetch = resolve;
      });

      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockStatsResponse({
            strength: 60,
            dexterity: 70,
            constitution: 50,
            size: 55,
            intelligence: 80,
            power: 65,
            education: 40,
            charisma: 65,
            luck: 50,
          })
        ),
      } as unknown as Response;

      // Mock fetch to return our controlled promise
      mockFetch.mockReturnValue(fetchPromise);

      // Render without waiting for async operations to complete
      render(<StatsRollingScreen {...defaultProps} />);

      // Check loading state immediately (before fetch completes)
      expect(screen.getByText("Rolling your character's stats...")).toBeInTheDocument();

      // Now resolve the fetch to clean up and prevent hanging
      await act(async () => {
        resolveFetch(mockResponse);
        await fetchPromise;
      });
      // Wait for state updates to complete using vi.waitFor
      await vi.waitFor(
        () => {
          expect(screen.queryByText("Rolling your character's stats...")).not.toBeInTheDocument();
        },
        { timeout: 1000 }
      );
    });
  });

  describe('Stats Rolling', () => {
    it('should roll stats on mount when authToken is available', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockStatsResponse({
            strength: 60,
            dexterity: 70,
            constitution: 50,
            size: 55,
            intelligence: 80,
            power: 65,
            education: 40,
            charisma: 65,
            luck: 50,
          })
        ),
      };
      mockFetch.mockResolvedValue(mockResponse);

      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith('http://localhost:54731/v1/api/players/roll-stats', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer mock-token',
          },
          body: JSON.stringify({ method: '3d6' }),
        });
      });

      await waitFor(() => {
        // Use within to scope queries to each stat-item to avoid conflicts with duplicate values
        const strengthItem = screen.getByText('Strength:').closest('.stat-item');
        expect(strengthItem).not.toBeNull();
        expect(within(strengthItem as HTMLElement).getByText('60')).toBeInTheDocument();

        const dexterityItem = screen.getByText('Dexterity:').closest('.stat-item');
        expect(dexterityItem).not.toBeNull();
        expect(within(dexterityItem as HTMLElement).getByText('70')).toBeInTheDocument();

        const constitutionItem = screen.getByText('Constitution:').closest('.stat-item');
        expect(constitutionItem).not.toBeNull();
        expect(within(constitutionItem as HTMLElement).getByText('50')).toBeInTheDocument();

        const sizeItem = screen.getByText('Size:').closest('.stat-item');
        expect(sizeItem).not.toBeNull();
        expect(within(sizeItem as HTMLElement).getByText('55')).toBeInTheDocument();

        const intelligenceItem = screen.getByText('Intelligence:').closest('.stat-item');
        expect(intelligenceItem).not.toBeNull();
        expect(within(intelligenceItem as HTMLElement).getByText('80')).toBeInTheDocument();

        const powerItem = screen.getByText('Power:').closest('.stat-item');
        expect(powerItem).not.toBeNull();
        expect(within(powerItem as HTMLElement).getByText('65')).toBeInTheDocument();

        const educationItem = screen.getByText('Education:').closest('.stat-item');
        expect(educationItem).not.toBeNull();
        expect(within(educationItem as HTMLElement).getByText('40')).toBeInTheDocument();

        const charismaItem = screen.getByText('Charisma:').closest('.stat-item');
        expect(charismaItem).not.toBeNull();
        expect(within(charismaItem as HTMLElement).getByText('65')).toBeInTheDocument();

        const luckItem = screen.getByText('Luck:').closest('.stat-item');
        expect(luckItem).not.toBeNull();
        expect(within(luckItem as HTMLElement).getByText('50')).toBeInTheDocument();
      });
    });

    it('should handle successful stats rolling', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockStatsResponse({
            strength: 75,
            dexterity: 60,
            constitution: 70,
            size: 55,
            intelligence: 50,
            power: 50,
            education: 65,
            charisma: 55,
            luck: 50,
          })
        ),
      };
      mockFetch.mockResolvedValue(mockResponse);

      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        // Use within to scope queries to each stat-item to avoid conflicts with duplicate values
        const strengthItem = screen.getByText('Strength:').closest('.stat-item');
        expect(strengthItem).not.toBeNull();
        expect(within(strengthItem as HTMLElement).getByText('75')).toBeInTheDocument();

        const dexterityItem = screen.getByText('Dexterity:').closest('.stat-item');
        expect(dexterityItem).not.toBeNull();
        expect(within(dexterityItem as HTMLElement).getByText('60')).toBeInTheDocument();

        const constitutionItem = screen.getByText('Constitution:').closest('.stat-item');
        expect(constitutionItem).not.toBeNull();
        expect(within(constitutionItem as HTMLElement).getByText('70')).toBeInTheDocument();

        const sizeItem = screen.getByText('Size:').closest('.stat-item');
        expect(sizeItem).not.toBeNull();
        expect(within(sizeItem as HTMLElement).getByText('55')).toBeInTheDocument();

        const intelligenceItem = screen.getByText('Intelligence:').closest('.stat-item');
        expect(intelligenceItem).not.toBeNull();
        expect(within(intelligenceItem as HTMLElement).getByText('50')).toBeInTheDocument();

        const powerItem = screen.getByText('Power:').closest('.stat-item');
        expect(powerItem).not.toBeNull();
        expect(within(powerItem as HTMLElement).getByText('50')).toBeInTheDocument();

        const educationItem = screen.getByText('Education:').closest('.stat-item');
        expect(educationItem).not.toBeNull();
        expect(within(educationItem as HTMLElement).getByText('65')).toBeInTheDocument();

        const charismaItem = screen.getByText('Charisma:').closest('.stat-item');
        expect(charismaItem).not.toBeNull();
        expect(within(charismaItem as HTMLElement).getByText('55')).toBeInTheDocument();

        const luckItem = screen.getByText('Luck:').closest('.stat-item');
        expect(luckItem).not.toBeNull();
        expect(within(luckItem as HTMLElement).getByText('50')).toBeInTheDocument();
      });

      expect(screen.getByText('Accept Stats')).toBeInTheDocument();
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

      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
      });
    });

    it('should handle network error', async () => {
      mockFetch.mockRejectedValue(new Error('Network error'));

      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        expect(screen.getByText('Failed to load stats. Please try again.')).toBeInTheDocument();
      });

      expect(defaultProps.onError).toHaveBeenCalledWith('Server is unavailable. Please try again later.');
    });
  });

  describe('Stats Acceptance', () => {
    it('should call onStatsAccepted when stats are accepted', async () => {
      // Mock the initial stats rolling
      const mockStatsResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue(
          createMockStatsResponse({
            strength: 60,
            dexterity: 70,
            constitution: 50,
            size: 55,
            intelligence: 80,
            power: 65,
            education: 40,
            charisma: 65,
            luck: 50,
          })
        ),
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

      await act(async () => {
        render(<StatsRollingScreen {...defaultProps} />);
      });

      await waitFor(() => {
        expect(screen.getByText('Accept Stats')).toBeInTheDocument();
      });

      const acceptButton = screen.getByText('Accept Stats');
      await act(async () => {
        fireEvent.click(acceptButton);
      });

      await waitFor(() => {
        expect(defaultProps.onStatsAccepted).toHaveBeenCalledWith({
          strength: 60,
          dexterity: 70,
          constitution: 50,
          size: 55,
          intelligence: 80,
          power: 65,
          education: 40,
          wisdom: 50,
          charisma: 65,
          luck: 50,
        });
      });
    });
  });
});
