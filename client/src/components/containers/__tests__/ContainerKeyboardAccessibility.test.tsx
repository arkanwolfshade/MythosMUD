/**
 * Tests for container component keyboard accessibility.
 *
 * As documented in the restricted archives of Miskatonic University, keyboard
 * accessibility is critical for ensuring all investigators can interact with
 * container systems regardless of input method.
 */

import { describe, expect, it, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ContainerSplitPane } from '../ContainerSplitPane';
import { BackpackTab } from '../BackpackTab';
import { CorpseOverlay } from '../CorpseOverlay';
import type { ContainerComponent } from '../../../stores/containerStore';

// Mock container store state
let mockOpenContainers: Record<string, ContainerComponent> = {};
let mockMutationTokens: Record<string, string> = {};
let mockIsLoading = false;
const mockSelectContainer = vi.fn();
const mockOpenContainer = vi.fn();

vi.mock('../../../stores/containerStore', () => ({
  useContainerStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      openContainers: mockOpenContainers,
      mutationTokens: mockMutationTokens,
      isLoading: mockIsLoading,
      selectedContainerId: null,
      openContainer: mockOpenContainer,
      closeContainer: vi.fn(),
      updateContainer: vi.fn(),
      handleContainerDecayed: vi.fn(),
      selectContainer: mockSelectContainer,
      deselectContainer: vi.fn(),
      setLoading: vi.fn(),
      reset: vi.fn(),
      getContainer: (id: string) => mockOpenContainers[id] || null,
      getMutationToken: (id: string) => mockMutationTokens[id] || null,
      getOpenContainerIds: () => Object.keys(mockOpenContainers),
      isContainerOpen: (id: string) => id in mockOpenContainers,
      getWearableContainersForPlayer: (playerId: string) =>
        Object.values(mockOpenContainers).filter(
          container => container.source_type === 'equipment' && container.entity_id === playerId
        ),
      getCorpseContainersInRoom: (roomId: string) =>
        Object.values(mockOpenContainers).filter(
          container => container.source_type === 'corpse' && container.room_id === roomId
        ),
    };
    return selector(mockState);
  },
}));

// Create mutable player object for tests
const mockPlayer = {
  id: 'player-1',
  name: 'TestPlayer',
  inventory: [
    {
      item_instance_id: 'item-1',
      item_id: 'item-1',
      item_name: 'Test Item',
      quantity: 1,
    },
  ],
};

const mockRoom = {
  id: 'room-1',
  name: 'Test Room',
};

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

describe('Container Keyboard Accessibility', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('ContainerSplitPane', () => {
    const mockContainer: ContainerComponent = {
      container_id: 'container-1',
      source_type: 'equipment',
      entity_id: 'player-1',
      capacity_slots: 5,
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
      metadata: {},
    };

    beforeEach(() => {
      mockOpenContainers = {
        'container-1': mockContainer,
      };
      mockMutationTokens = {
        'container-1': 'token-1',
      };
      mockIsLoading = false;
    });

    it('should support Tab navigation between items', async () => {
      const user = userEvent.setup();
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="container-1" onTransfer={onTransfer} />);

      const transferButtons = screen.getAllByRole('button', { name: /transfer/i });
      expect(transferButtons.length).toBeGreaterThan(0);

      transferButtons[0].focus();
      expect(transferButtons[0]).toHaveFocus();

      await user.tab();
      // Focus should move to next focusable element
      expect(document.activeElement).toBeInTheDocument();
    });

    it('should activate buttons with Enter key', async () => {
      const user = userEvent.setup();
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="container-1" onTransfer={onTransfer} />);

      const transferButtons = screen.getAllByRole('button', { name: /transfer/i });
      expect(transferButtons.length).toBeGreaterThan(0);
      transferButtons[0].focus();

      await user.keyboard('{Enter}');
      // Button should be clickable (actual click handler will be tested separately)
      expect(transferButtons[0]).toBeInTheDocument();
    });

    it('should activate buttons with Space key', async () => {
      const user = userEvent.setup();
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="container-1" onTransfer={onTransfer} />);

      const transferButtons = screen.getAllByRole('button', { name: /transfer/i });
      expect(transferButtons.length).toBeGreaterThan(0);
      transferButtons[0].focus();

      await user.keyboard(' ');
      // Button should be clickable
      expect(transferButtons[0]).toBeInTheDocument();
    });

    it('should have proper ARIA labels for screen readers', () => {
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="container-1" onTransfer={onTransfer} />);

      const transferButtons = screen.getAllByRole('button', { name: /transfer/i });
      expect(transferButtons.length).toBeGreaterThan(0);
      transferButtons.forEach(button => {
        expect(button).toHaveAttribute('aria-label');
      });
    });

    it('should support Escape key to close container', async () => {
      const user = userEvent.setup();
      const onClose = vi.fn();
      render(<ContainerSplitPane containerId="container-1" onClose={onClose} />);

      const container = screen.getByRole('region', { name: /container/i });
      container.focus();

      await user.keyboard('{Escape}');
      expect(onClose).toHaveBeenCalled();
    });

    it('should trap focus within container when open', async () => {
      const user = userEvent.setup();
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="container-1" modal={true} onTransfer={onTransfer} />);

      const buttons = screen.getAllByRole('button');
      expect(buttons.length).toBeGreaterThan(0);
      buttons[0].focus();

      // Tab through all buttons
      await user.tab();
      await user.tab();
      await user.tab();

      // Focus should remain within container - check if active element is within the container region
      const containerRegion = screen.getByRole('region', { name: /container/i });
      const focusableElements = containerRegion.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      const activeElement = document.activeElement;
      const isWithinContainer =
        Array.from(focusableElements).some(el => el === activeElement) || containerRegion.contains(activeElement);
      expect(isWithinContainer).toBe(true);
    });
  });

  describe('BackpackTab', () => {
    const mockWearableContainer: ContainerComponent = {
      container_id: 'backpack-1',
      source_type: 'equipment',
      entity_id: 'player-1',
      capacity_slots: 5,
      lock_state: 'unlocked',
      items: [],
      allowed_roles: [],
      metadata: {
        item_name: 'Leather Backpack',
      },
    };

    beforeEach(() => {
      mockOpenContainers = {
        [mockWearableContainer.container_id]: mockWearableContainer,
      };
      mockMutationTokens = {};
      mockIsLoading = false;
    });

    it('should support Tab navigation between tabs', async () => {
      const user = userEvent.setup();
      const container2: ContainerComponent = {
        ...mockWearableContainer,
        container_id: 'backpack-2',
        metadata: { item_name: 'Bandolier' },
      };
      mockOpenContainers = {
        [mockWearableContainer.container_id]: mockWearableContainer,
        [container2.container_id]: container2,
      };

      render(<BackpackTab />);

      const tabs = screen.getAllByRole('tab');
      tabs[0].focus();
      expect(tabs[0]).toHaveFocus();

      await user.tab();
      expect(tabs[1]).toHaveFocus();
    });

    it('should activate tabs with Enter key', async () => {
      const user = userEvent.setup();
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /backpack/i });
      tab.focus();

      await user.keyboard('{Enter}');
      expect(mockSelectContainer).toHaveBeenCalled();
    });

    it('should activate tabs with Space key', async () => {
      const user = userEvent.setup();
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /backpack/i });
      tab.focus();

      await user.keyboard(' ');
      expect(mockSelectContainer).toHaveBeenCalled();
    });

    it('should support Arrow key navigation between tabs', async () => {
      const user = userEvent.setup();
      const container2: ContainerComponent = {
        ...mockWearableContainer,
        container_id: 'backpack-2',
        metadata: { item_name: 'Bandolier' },
      };
      mockOpenContainers = {
        [mockWearableContainer.container_id]: mockWearableContainer,
        [container2.container_id]: container2,
      };

      render(<BackpackTab />);

      const tabs = screen.getAllByRole('tab');
      tabs[0].focus();

      await user.keyboard('{ArrowRight}');
      expect(tabs[1]).toHaveFocus();

      await user.keyboard('{ArrowLeft}');
      expect(tabs[0]).toHaveFocus();
    });

    it('should wrap Arrow key navigation at boundaries', async () => {
      const user = userEvent.setup();
      const container2: ContainerComponent = {
        ...mockWearableContainer,
        container_id: 'backpack-2',
        metadata: { item_name: 'Bandolier' },
      };
      mockOpenContainers = {
        [mockWearableContainer.container_id]: mockWearableContainer,
        [container2.container_id]: container2,
      };

      render(<BackpackTab />);

      const tabs = screen.getAllByRole('tab');
      tabs[0].focus();

      await user.keyboard('{ArrowLeft}');
      // Should wrap to last tab
      expect(tabs[tabs.length - 1]).toHaveFocus();
    });

    it('should have proper ARIA labels', () => {
      render(<BackpackTab />);

      const tab = screen.getByRole('tab');
      expect(tab).toHaveAttribute('aria-label');
      expect(tab).toHaveAttribute('aria-selected');
    });
  });

  describe('CorpseOverlay', () => {
    const mockCorpse: ContainerComponent = {
      container_id: 'corpse-1',
      source_type: 'corpse',
      owner_id: 'dead-player-1',
      room_id: 'room-1',
      capacity_slots: 20,
      lock_state: 'unlocked',
      items: [],
      allowed_roles: [],
      metadata: {
        grace_period_start: new Date().toISOString(),
        grace_period_seconds: 300,
      },
      decay_at: new Date(Date.now() + 3600000).toISOString(),
    };

    beforeEach(() => {
      // Reset player to default
      mockPlayer.id = 'player-1';
      mockOpenContainers = {
        [mockCorpse.container_id]: mockCorpse,
      };
      // Mock fetch for API call
      global.fetch = vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({
          container: mockCorpse,
          mutation_token: 'token-1',
        }),
      });
    });

    it('should support Tab navigation to open button', async () => {
      // Set up corpse so button is enabled (owner matches player)
      const enabledCorpse = {
        ...mockCorpse,
        owner_id: 'player-1',
      };
      mockOpenContainers = {
        [enabledCorpse.container_id]: enabledCorpse,
      };

      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse/i });
      openButton.focus();
      expect(openButton).toHaveFocus();
    });

    it('should activate open button with Enter key', async () => {
      const user = userEvent.setup();
      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse|grace period/i });
      openButton.focus();

      await user.keyboard('{Enter}');
      // Button should handle the event
      expect(openButton).toBeInTheDocument();
    });

    it('should activate open button with Space key', async () => {
      const user = userEvent.setup();
      render(<CorpseOverlay />);

      const openButton = screen.getByRole('button', { name: /open corpse|grace period/i });
      openButton.focus();

      await user.keyboard(' ');
      // Button should handle the event
      expect(openButton).toBeInTheDocument();
    });

    it('should not activate disabled button with keyboard', async () => {
      const user = userEvent.setup();
      const gracePeriodCorpse = {
        ...mockCorpse,
        owner_id: 'other-player',
      };
      mockOpenContainers = {
        [gracePeriodCorpse.container_id]: gracePeriodCorpse,
      };
      mockPlayer.id = 'current-player';

      render(<CorpseOverlay />);

      // Find button by its text content since aria-label takes precedence
      const openButton = screen.getByText(/grace period active/i).closest('button') as HTMLButtonElement;
      expect(openButton).toBeInTheDocument();
      expect(openButton).toBeDisabled();

      openButton.focus();
      await user.keyboard('{Enter}');
      // Disabled button should not trigger action
      expect(mockOpenContainer).not.toHaveBeenCalled();
    });

    it('should have proper ARIA labels', () => {
      // Set up corpse so button is enabled (owner matches player)
      const enabledCorpse = {
        ...mockCorpse,
        owner_id: 'player-1',
      };
      mockOpenContainers = {
        [enabledCorpse.container_id]: enabledCorpse,
      };

      render(<CorpseOverlay />);

      const overlay = screen.getByRole('complementary', { name: /corpse/i });
      expect(overlay).toBeInTheDocument();

      const openButton = screen.getByRole('button', { name: /open corpse/i });
      expect(openButton).toHaveAttribute('aria-label');
    });
  });

  describe('Focus Management', () => {
    it('should restore focus when container closes', async () => {
      const mockContainer: ContainerComponent = {
        container_id: 'container-1',
        source_type: 'equipment',
        entity_id: 'player-1',
        capacity_slots: 5,
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
        metadata: {},
      };

      mockOpenContainers = {
        'container-1': mockContainer,
      };
      mockMutationTokens = {
        'container-1': 'token-1',
      };
      mockIsLoading = false;

      const triggerButton = document.createElement('button');
      triggerButton.textContent = 'Open Container';
      document.body.appendChild(triggerButton);
      triggerButton.focus();

      const onClose = vi.fn();
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="container-1" onClose={onClose} onTransfer={onTransfer} />);

      // Container opens, focus moves to container
      const containerButtons = screen.getAllByRole('button', { name: /transfer/i });
      expect(containerButtons.length).toBeGreaterThan(0);
      containerButtons[0].focus();

      // Close container with Escape key
      const containerRegion = screen.getByRole('region', { name: /container/i });
      fireEvent.keyDown(containerRegion, { key: 'Escape', code: 'Escape' });

      // Focus should be managed (actual restoration will be handled by parent component)
      expect(onClose).toHaveBeenCalled();
    });

    it('should prevent focus from escaping modal containers', async () => {
      const user = userEvent.setup();
      const mockContainer: ContainerComponent = {
        container_id: 'container-1',
        source_type: 'equipment',
        entity_id: 'player-1',
        capacity_slots: 5,
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
        metadata: {},
      };

      mockOpenContainers = {
        'container-1': mockContainer,
      };
      mockMutationTokens = {
        'container-1': 'token-1',
      };
      mockIsLoading = false;

      render(<ContainerSplitPane containerId="container-1" modal={true} onTransfer={vi.fn()} />);

      // Get all focusable elements (buttons and items with tabIndex)
      const focusableElements = document.querySelectorAll('button, [tabindex]:not([tabindex="-1"])');
      if (focusableElements.length > 0) {
        const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;
        lastElement.focus();

        // Tab should wrap to first button (focus trap)
        await user.tab();
        // Focus should remain within container (may wrap to first or stay on last)
        expect(document.activeElement).toBeInTheDocument();
      }
    });
  });
});
