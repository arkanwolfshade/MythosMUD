/**
 * Tests for CorpseOverlay component.
 *
 * As documented in the restricted archives of Miskatonic University, corpse
 * overlay components require thorough testing to ensure proper display of
 * decay timers and grace period countdowns for fallen investigators.
 */

import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { ContainerComponent } from '../../../stores/containerStore';
import { CorpseOverlay } from '../CorpseOverlay';

// Mock container store state
let mockOpenContainers: Record<string, ContainerComponent> = {};
const mockOpenContainer = vi.fn();

vi.mock('../../../stores/containerStore', () => ({
  useContainerStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      openContainers: mockOpenContainers,
      mutationTokens: {},
      isLoading: false,
      selectedContainerId: null,
      openContainer: mockOpenContainer,
      closeContainer: vi.fn(),
      updateContainer: vi.fn(),
      handleContainerDecayed: vi.fn(),
      selectContainer: vi.fn(),
      deselectContainer: vi.fn(),
      setLoading: vi.fn(),
      reset: vi.fn(),
      getContainer: (id: string) => mockOpenContainers[id] || null,
      getMutationToken: (_id: string) => null,
      getOpenContainerIds: () => Object.keys(mockOpenContainers),
      isContainerOpen: (id: string) => id in mockOpenContainers,
      getWearableContainersForPlayer: vi.fn(),
      getCorpseContainersInRoom: (roomId: string) =>
        Object.values(mockOpenContainers).filter(
          container => container.source_type === 'corpse' && container.room_id === roomId
        ),
    };
    return selector(mockState);
  },
}));

// Mock game store state
let mockPlayer: { id: string; name: string } | null = null;
let mockRoom: { id: string; name: string } | null = null;

vi.mock('../../../stores/gameStore', () => ({
  useGameStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      player: mockPlayer,
      room: mockRoom,
      chatMessages: [],
      gameLog: [],
      isLoading: false,
      lastUpdate: null,
      setPlayer: vi.fn(),
      updatePlayerStats: vi.fn(),
      clearPlayer: vi.fn(),
      setRoom: vi.fn(),
      updateRoomOccupants: vi.fn(),
      clearRoom: vi.fn(),
      addChatMessage: vi.fn(),
      clearChatMessages: vi.fn(),
      addGameLogEntry: vi.fn(),
      clearGameLog: vi.fn(),
      setLoading: vi.fn(),
      updateLastUpdate: vi.fn(),
      reset: vi.fn(),
      getPlayerStats: vi.fn(),
      getRoomOccupantsCount: vi.fn(),
      getRecentChatMessages: vi.fn(),
      getRecentGameLogEntries: vi.fn(),
    };
    return selector(mockState);
  },
}));

// Mock timer functions
vi.useFakeTimers();

describe('CorpseOverlay', () => {
  const createCorpseContainer = (overrides?: Partial<ContainerComponent>): ContainerComponent => {
    const now = new Date();
    const decayAt = new Date(now.getTime() + 60 * 60 * 1000); // 1 hour from now

    return {
      container_id: 'corpse-1',
      source_type: 'corpse',
      owner_id: 'dead-player-1',
      room_id: 'test-room-1',
      capacity_slots: 20,
      lock_state: 'unlocked',
      items: [
        {
          item_instance_id: 'item-1',
          prototype_id: 'test-item',
          item_id: 'test-item',
          item_name: 'Test Item',
          slot_type: 'backpack',
          quantity: 1,
        },
      ],
      allowed_roles: [],
      metadata: {
        grace_period_start: now.toISOString(),
        grace_period_seconds: 300, // 5 minutes
        decay_seconds: 3600, // 1 hour
      },
      decay_at: decayAt.toISOString(),
      ...overrides,
    };
  };

  beforeEach(() => {
    vi.clearAllMocks();
    vi.setSystemTime(new Date('2025-01-01T12:00:00Z'));

    mockPlayer = {
      id: 'player-1',
      name: 'TestPlayer',
    };
    mockRoom = {
      id: 'test-room-1',
      name: 'Test Room',
    };
    mockOpenContainers = {};
  });

  afterEach(() => {
    vi.clearAllTimers();
  });

  describe('Rendering', () => {
    it('should not render when no corpse containers in room', () => {
      mockOpenContainers = {};

      const { container } = render(<CorpseOverlay />);
      expect(container.firstChild).toBeNull();
    });

    it('should render when corpse container is present', () => {
      const corpse = createCorpseContainer();
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      expect(screen.getByText(/corpse/i)).toBeInTheDocument();
    });

    it('should display corpse owner information', () => {
      const corpse = createCorpseContainer({ owner_id: 'dead-player-1' });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      expect(screen.getByText(/dead-player-1/i)).toBeInTheDocument();
    });

    it('should display item count in corpse', () => {
      const corpse = createCorpseContainer({
        items: [
          {
            item_instance_id: 'item-1',
            prototype_id: 'test-item',
            item_id: 'test-item',
            item_name: 'Test Item',
            slot_type: 'backpack',
            quantity: 1,
          },
        ],
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      expect(screen.getByText(/1.*item/i)).toBeInTheDocument();
    });
  });

  describe('Grace Period Countdown', () => {
    it('should display grace period countdown when active', () => {
      const now = new Date('2025-01-01T12:00:00Z');

      const corpse = createCorpseContainer({
        metadata: {
          grace_period_start: now.toISOString(),
          grace_period_seconds: 300,
        },
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      // Use getAllByText since "grace period" appears multiple times
      const gracePeriodTexts = screen.getAllByText(/grace period/i);
      expect(gracePeriodTexts.length).toBeGreaterThan(0);
      // Format is "5m 0s" (not "5 min")
      expect(screen.getByText(/5m/i)).toBeInTheDocument();
    });

    it('should display correct grace period countdown at different time points', () => {
      const baseTime = new Date('2025-01-01T12:00:00Z');

      // Test at initial time: 5 minutes remaining
      vi.setSystemTime(baseTime);
      const corpse1 = createCorpseContainer({
        metadata: {
          grace_period_start: baseTime.toISOString(),
          grace_period_seconds: 300, // 5 minutes
        },
      });
      mockOpenContainers = { [corpse1.container_id]: corpse1 };
      const { unmount } = render(<CorpseOverlay />);

      // Initial: 5 minutes remaining
      expect(screen.getByText(/grace period.*5m/i)).toBeInTheDocument();
      unmount();

      // Test at 1 minute later: 4 minutes remaining
      vi.setSystemTime(new Date(baseTime.getTime() + 60 * 1000));
      const corpse2 = createCorpseContainer({
        metadata: {
          grace_period_start: baseTime.toISOString(),
          grace_period_seconds: 300,
        },
      });
      mockOpenContainers = { [corpse2.container_id]: corpse2 };
      render(<CorpseOverlay />);

      // Should show 4 minutes remaining (or close to it, accounting for formatting)
      // Query for the specific "Grace Period:" text in the countdown div
      const gracePeriodCountdown = screen.getByText(/grace period:\s*\d+m/i);
      expect(gracePeriodCountdown).toBeInTheDocument();
      expect(gracePeriodCountdown.textContent).toMatch(/4m/i);
    });

    it('should show expired grace period message when grace period ends', () => {
      const now = new Date('2025-01-01T12:00:00Z');
      const pastTime = new Date(now.getTime() - 10 * 60 * 1000); // 10 minutes ago

      const corpse = createCorpseContainer({
        metadata: {
          grace_period_start: pastTime.toISOString(),
          grace_period_seconds: 300, // 5 minutes
        },
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      expect(screen.getByText(/grace period.*ended/i)).toBeInTheDocument();
    });
  });

  describe('Decay Countdown', () => {
    it('should display decay countdown timer', () => {
      const now = new Date('2025-01-01T12:00:00Z');
      const decayAt = new Date(now.getTime() + 60 * 60 * 1000); // 1 hour

      const corpse = createCorpseContainer({
        decay_at: decayAt.toISOString(),
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      expect(screen.getByText(/decay/i)).toBeInTheDocument();
      // Format is "1h 0m" (not "1 hour")
      expect(screen.getByText(/1h/i)).toBeInTheDocument();
    });

    it('should display correct decay countdown at different time points', () => {
      const baseTime = new Date('2025-01-01T12:00:00Z');
      const decayAt = new Date(baseTime.getTime() + 60 * 60 * 1000); // 1 hour from base time

      // Test at initial time: 1 hour remaining
      vi.setSystemTime(baseTime);
      const corpse1 = createCorpseContainer({
        decay_at: decayAt.toISOString(),
      });
      mockOpenContainers = { [corpse1.container_id]: corpse1 };
      const { unmount } = render(<CorpseOverlay />);

      // Initial: 1 hour remaining
      expect(screen.getByText(/decays in.*1h/i)).toBeInTheDocument();
      unmount();

      // Test at 30 minutes later: approximately 30 minutes remaining
      vi.setSystemTime(new Date(baseTime.getTime() + 30 * 60 * 1000));
      const corpse2 = createCorpseContainer({
        decay_at: decayAt.toISOString(),
      });
      mockOpenContainers = { [corpse2.container_id]: corpse2 };
      render(<CorpseOverlay />);

      // Should show approximately 30 minutes remaining (allow for small precision differences)
      const decayText = screen.getByText(/decays in/i).textContent;
      expect(decayText).toMatch(/29m|30m/i); // Accept 29m or 30m due to timing precision
    });

    it('should show decayed message when decay time passes', () => {
      const now = new Date('2025-01-01T12:00:00Z');
      const pastDecay = new Date(now.getTime() - 10 * 60 * 1000); // 10 minutes ago

      const corpse = createCorpseContainer({
        decay_at: pastDecay.toISOString(),
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      expect(screen.getByText(/decayed/i)).toBeInTheDocument();
    });
  });

  describe('Multiple Corpses', () => {
    it('should display multiple corpse overlays', () => {
      const corpse1 = createCorpseContainer({ container_id: 'corpse-1', owner_id: 'player-1' });
      const corpse2 = createCorpseContainer({ container_id: 'corpse-2', owner_id: 'player-2' });

      mockOpenContainers = {
        [corpse1.container_id]: corpse1,
        [corpse2.container_id]: corpse2,
      };

      render(<CorpseOverlay />);

      expect(screen.getByText(/player-1/i)).toBeInTheDocument();
      expect(screen.getByText(/player-2/i)).toBeInTheDocument();
    });
  });

  describe('Interaction', () => {
    it('should call openContainer when open button is clicked', () => {
      const corpse = createCorpseContainer({ owner_id: 'player-1' });
      mockOpenContainers = { [corpse.container_id]: corpse };
      mockPlayer = { id: 'player-1', name: 'TestPlayer' };
      // Mock fetch for API call
      const mockFetch = vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          container: corpse,
          mutation_token: 'token-1',
        }),
      });
      global.fetch = mockFetch;
      // Mock localStorage
      const localStorageMock = {
        getItem: vi.fn().mockReturnValue('test-token'),
        setItem: vi.fn(),
        removeItem: vi.fn(),
        clear: vi.fn(),
      };
      Object.defineProperty(window, 'localStorage', { value: localStorageMock });

      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse/i });
      fireEvent.click(openButton);

      expect(mockFetch).toHaveBeenCalled();
    });

    it('should disable open button during grace period for non-owner', () => {
      const corpse = createCorpseContainer({
        owner_id: 'other-player',
        metadata: {
          grace_period_start: new Date().toISOString(),
          grace_period_seconds: 300,
        },
      });
      mockOpenContainers = { [corpse.container_id]: corpse };
      mockPlayer = { id: 'current-player', name: 'TestPlayer' };

      render(<CorpseOverlay />);

      // Button text changes to "Grace Period Active" when disabled
      // Find button by its text content since aria-label takes precedence
      const openButton = screen.getByText(/grace period active/i).closest('button');
      expect(openButton).toBeInTheDocument();
      expect(openButton).toBeDisabled();
    });

    it('should enable open button for corpse owner during grace period', () => {
      const corpse = createCorpseContainer({
        owner_id: 'player-1',
        metadata: {
          grace_period_start: new Date().toISOString(),
          grace_period_seconds: 300,
        },
      });
      mockOpenContainers = { [corpse.container_id]: corpse };
      mockPlayer = { id: 'player-1', name: 'TestPlayer' };

      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse/i });
      expect(openButton).not.toBeDisabled();
    });
  });

  describe('Accessibility', () => {
    it('should have proper ARIA labels', () => {
      const corpse = createCorpseContainer();
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      const overlay = screen.getByRole('region', { name: /corpse/i });
      expect(overlay).toBeInTheDocument();
    });

    it('should support keyboard navigation', () => {
      const corpse = createCorpseContainer({ owner_id: 'player-1' });
      mockOpenContainers = { [corpse.container_id]: corpse };
      mockPlayer = { id: 'player-1', name: 'TestPlayer' };

      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse/i });
      openButton.focus();
      expect(openButton).toHaveFocus();
    });

    it('should activate on Enter key press', async () => {
      // Use real timers for this test since we're testing async behavior
      vi.useRealTimers();

      const corpse = createCorpseContainer({ owner_id: 'player-1' });
      mockOpenContainers = { [corpse.container_id]: corpse };
      mockPlayer = { id: 'player-1', name: 'TestPlayer' };
      // Mock fetch for API call
      const mockFetch = vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          container: corpse,
          mutation_token: 'token-1',
        }),
      });
      global.fetch = mockFetch;
      // Mock localStorage
      const localStorageMock = {
        getItem: vi.fn().mockReturnValue('test-token'),
        setItem: vi.fn(),
        removeItem: vi.fn(),
        clear: vi.fn(),
      };
      Object.defineProperty(window, 'localStorage', { value: localStorageMock });

      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse/i });

      // Use userEvent for more realistic interaction
      const user = userEvent.setup();
      openButton.focus();
      await user.keyboard('{Enter}');

      // Wait for async API call
      await waitFor(
        () => {
          expect(mockFetch).toHaveBeenCalled();
        },
        { timeout: 3000 }
      );

      // Restore fake timers
      vi.useFakeTimers();
    });
  });

  describe('Time Formatting', () => {
    it('should format time remaining correctly', () => {
      const now = new Date('2025-01-01T12:00:00Z');
      const decayAt = new Date(now.getTime() + 90 * 60 * 1000); // 1.5 hours

      const corpse = createCorpseContainer({
        decay_at: decayAt.toISOString(),
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      // Format is "1h 30m" (not "1 hour 30 min")
      expect(screen.getByText(/1h.*30m/i)).toBeInTheDocument();
    });

    it('should show seconds when less than a minute remains', () => {
      const now = new Date('2025-01-01T12:00:00Z');
      const decayAt = new Date(now.getTime() + 30 * 1000); // 30 seconds

      const corpse = createCorpseContainer({
        decay_at: decayAt.toISOString(),
      });
      mockOpenContainers = { [corpse.container_id]: corpse };

      render(<CorpseOverlay />);

      // Format is "30s" (not "30 sec")
      expect(screen.getByText(/30s/i)).toBeInTheDocument();
    });
  });
});
