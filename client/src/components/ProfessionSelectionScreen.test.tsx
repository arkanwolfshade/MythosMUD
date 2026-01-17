import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ProfessionSelectionScreen } from './ProfessionSelectionScreen';

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

describe('ProfessionSelectionScreen', () => {
  const defaultProps = {
    characterName: 'TestCharacter',
    onProfessionSelected: vi.fn(),
    onError: vi.fn(),
    onBack: vi.fn(),
    baseUrl: 'http://localhost:54731',
    authToken: 'mock-token',
  };

  const mockProfessions = [
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

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Initial Rendering', () => {
    it('should render with character name and profession selection title', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
        expect(screen.getByText(`Welcome, ${defaultProps.characterName}`)).toBeInTheDocument();
      });
    });

    it('should display profession cards with names and descriptions', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Tramp')).toBeInTheDocument();
        expect(screen.getByText('A wandering soul with no particular skills or connections.')).toBeInTheDocument();
        expect(screen.getByText('Gutter Rat')).toBeInTheDocument();
        expect(screen.getByText('A street-smart survivor from the urban underbelly.')).toBeInTheDocument();
      });
    });

    it('should display "No requirements" for MVP professions', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const noRequirementsElements = screen.getAllByText('No requirements');
        expect(noRequirementsElements).toHaveLength(2);
      });
    });

    it('should have disabled Next button initially', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const nextButton = screen.getByText('Next');
        expect(nextButton).toBeDisabled();
      });
    });

    it('should have enabled Back button', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const backButton = screen.getByText('Back');
        expect(backButton).not.toBeDisabled();
      });
    });
  });

  describe('Profession Selection', () => {
    it('should enable Next button when a profession is selected', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const trampCard = screen.getByText('Tramp').closest('.profession-card');
        expect(trampCard).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      await waitFor(() => {
        const nextButton = screen.getByText('Next');
        expect(nextButton).not.toBeDisabled();
      });
    });

    it('should highlight selected profession card', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const trampCard = screen.getByText('Tramp').closest('.profession-card');
        expect(trampCard).toBeInTheDocument();
      });

      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      await waitFor(() => {
        expect(trampCard).toHaveClass('selected');
      });
    });

    it('should allow switching between professions', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const trampCard = screen.getByText('Tramp').closest('.profession-card');
        const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
        expect(trampCard).toBeInTheDocument();
        expect(gutterRatCard).toBeInTheDocument();
      });

      // Select Tramp first
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      await waitFor(() => {
        expect(trampCard).toHaveClass('selected');
      });

      // Then select Gutter Rat
      const gutterRatCard = screen.getByText('Gutter Rat').closest('.profession-card');
      fireEvent.click(gutterRatCard!);

      await waitFor(() => {
        expect(trampCard).not.toHaveClass('selected');
        expect(gutterRatCard).toHaveClass('selected');
      });
    });
  });

  describe('Navigation', () => {
    it('should call onBack when Back button is clicked', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const backButton = screen.getByText('Back');
        expect(backButton).toBeInTheDocument();
      });

      const backButton = screen.getByText('Back');
      fireEvent.click(backButton);

      expect(defaultProps.onBack).toHaveBeenCalledTimes(1);
    });

    it('should call onProfessionSelected when Next button is clicked with selected profession', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const trampCard = screen.getByText('Tramp').closest('.profession-card');
        expect(trampCard).toBeInTheDocument();
      });

      // Select a profession
      const trampCard = screen.getByText('Tramp').closest('.profession-card');
      fireEvent.click(trampCard!);

      await waitFor(() => {
        const nextButton = screen.getByText('Next');
        expect(nextButton).not.toBeDisabled();
      });

      // Click Next
      const nextButton = screen.getByText('Next');
      fireEvent.click(nextButton);

      expect(defaultProps.onProfessionSelected).toHaveBeenCalledWith(mockProfessions[0]);
    });
  });

  describe('API Integration', () => {
    it('should fetch professions on component mount', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(mockFetch).toHaveBeenCalledWith(
          `${defaultProps.baseUrl}/professions`,
          expect.objectContaining({
            headers: expect.objectContaining({
              Authorization: `Bearer ${defaultProps.authToken}`,
            }),
          })
        );
      });
    });

    it('should handle API errors gracefully', async () => {
      const mockResponse = {
        ok: false,
        status: 500,
        json: vi.fn().mockResolvedValue({ detail: 'Internal server error' }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(defaultProps.onError).toHaveBeenCalledWith('Failed to load professions: Internal server error');
      });
    });

    it('should handle network errors', async () => {
      mockFetch.mockRejectedValue(new Error('Network error'));

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(defaultProps.onError).toHaveBeenCalledWith('Failed to load professions: Network error');
      });
    });
  });

  describe('Loading States', () => {
    it('should show loading state while fetching professions', () => {
      // Don't resolve the fetch immediately
      mockFetch.mockImplementation(() => new Promise(() => {}));

      render(<ProfessionSelectionScreen {...defaultProps} />);

      expect(screen.getByText('Loading professions...')).toBeInTheDocument();
    });

    it('should hide loading state after professions are loaded', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: mockProfessions,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.queryByText('Loading professions...')).not.toBeInTheDocument();
        expect(screen.getByText('Choose Your Profession')).toBeInTheDocument();
      });
    });
  });

  describe('Professions with Requirements', () => {
    const professionsWithRequirements = [
      {
        id: 2,
        name: 'Scholar',
        description: 'A learned individual with high intelligence.',
        flavor_text: 'Your mind is your greatest weapon.',
        stat_requirements: [
          { stat: 'intelligence', minimum: 14 },
          { stat: 'wisdom', minimum: 12 },
        ],
        mechanical_effects: [],
        is_available: true,
      },
    ];

    it('should display stat requirements when present', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: professionsWithRequirements,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        expect(screen.getByText('Minimum: Intelligence 14, Wisdom 12')).toBeInTheDocument();
      });
    });

    it('should highlight stat requirements', async () => {
      const mockResponse = {
        ok: true,
        json: vi.fn().mockResolvedValue({
          professions: professionsWithRequirements,
        }),
      };
      mockFetch.mockResolvedValue(mockResponse);

      render(<ProfessionSelectionScreen {...defaultProps} />);

      await waitFor(() => {
        const requirementsElement = screen.getByText('Minimum: Intelligence 14, Wisdom 12');
        expect(requirementsElement).toHaveClass('stat-requirements');
      });
    });
  });
});
