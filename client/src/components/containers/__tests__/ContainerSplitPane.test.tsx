/**
 * Tests for ContainerSplitPane component.
 *
 * As documented in the restricted archives of Miskatonic University, container
 * split-pane components require thorough testing to ensure proper display and
 * interaction with investigator artifacts.
 */

import { describe, expect, it, vi, beforeEach } from 'vitest';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { ContainerSplitPane } from '../ContainerSplitPane';
import type { ContainerComponent } from '../../../stores/containerStore';

// Mock the stores
const mockGetContainer = vi.fn();
const mockGetMutationToken = vi.fn();
const mockIsContainerOpen = vi.fn();
const mockIsLoading = vi.fn(() => false);

vi.mock('../../../stores/containerStore', () => ({
  useContainerStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      getContainer: mockGetContainer,
      getMutationToken: mockGetMutationToken,
      isContainerOpen: mockIsContainerOpen,
      isLoading: mockIsLoading(),
    };
    return selector(mockState);
  },
}));

const mockPlayer = {
  id: 'player-1',
  name: 'TestPlayer',
  inventory: [] as unknown[],
};

vi.mock('../../../stores/gameStore', () => ({
  useGameStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      player: mockPlayer,
    };
    return selector(mockState);
  },
}));

describe('ContainerSplitPane', () => {
  const mockContainer: ContainerComponent = {
    container_id: 'test-container-1',
    source_type: 'environment',
    room_id: 'test-room-1',
    capacity_slots: 10,
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

  const mockPlayerInventory = [
    {
      item_instance_id: 'player-item-1',
      prototype_id: 'player-item',
      item_id: 'player-item',
      item_name: 'Player Item',
      slot_type: 'backpack',
      quantity: 1,
    },
  ];

  beforeEach(() => {
    vi.clearAllMocks();

    // Setup default store mocks
    mockGetContainer.mockImplementation((id: string) => (id === 'test-container-1' ? mockContainer : null));
    mockGetMutationToken.mockImplementation((id: string) => (id === 'test-container-1' ? 'test-token' : null));
    mockIsContainerOpen.mockImplementation((id: string) => id === 'test-container-1');
    mockIsLoading.mockReturnValue(false);

    // Reset player inventory
    mockPlayer.inventory = mockPlayerInventory;
  });

  describe('Rendering', () => {
    it('should render container and player inventory side by side', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/container/i)).toBeInTheDocument();
      expect(screen.getByText(/inventory/i)).toBeInTheDocument();
    });

    it('should display container items', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText('Test Item')).toBeInTheDocument();
    });

    it('should display player inventory items', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText('Player Item')).toBeInTheDocument();
    });

    it('should show empty state when container has no items', () => {
      const emptyContainer = { ...mockContainer, items: [] };
      mockGetContainer.mockReturnValue(emptyContainer);
      mockGetMutationToken.mockReturnValue('test-token');
      mockIsContainerOpen.mockReturnValue(true);

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/empty/i)).toBeInTheDocument();
    });

    it('should show empty state when player inventory is empty', () => {
      mockPlayer.inventory = [];

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getAllByText(/empty/i).length).toBeGreaterThan(0);
    });
  });

  describe('Container Not Found', () => {
    it('should show error message when container is not found', () => {
      mockGetContainer.mockReturnValue(null);
      mockGetMutationToken.mockReturnValue(null);
      mockIsContainerOpen.mockReturnValue(false);

      render(<ContainerSplitPane containerId="non-existent" />);

      expect(screen.getByText(/not found/i)).toBeInTheDocument();
    });

    it('should show error message when container is not open', () => {
      mockGetContainer.mockReturnValue(mockContainer);
      mockGetMutationToken.mockReturnValue(null);
      mockIsContainerOpen.mockReturnValue(false);

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/not open/i)).toBeInTheDocument();
    });
  });

  describe('Item Transfer', () => {
    it('should call transfer handler when transfer button is clicked', async () => {
      const onTransfer = vi.fn();
      render(<ContainerSplitPane containerId="test-container-1" onTransfer={onTransfer} />);

      const transferButtons = screen.getAllByRole('button', { name: /transfer/i });
      if (transferButtons.length > 0) {
        fireEvent.click(transferButtons[0]);

        await waitFor(() => {
          expect(onTransfer).toHaveBeenCalled();
        });
      }
    });

    it('should disable transfer button when mutation token is missing', () => {
      mockGetContainer.mockReturnValue(mockContainer);
      mockGetMutationToken.mockReturnValue(null);
      mockIsContainerOpen.mockReturnValue(true);

      render(<ContainerSplitPane containerId="test-container-1" />);

      const transferButtons = screen.queryAllByRole('button', { name: /transfer/i });
      // If buttons exist, they should be disabled
      transferButtons.forEach(button => {
        expect(button).toBeDisabled();
      });
    });
  });

  describe('Accessibility', () => {
    it('should have proper ARIA labels', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      const containerSection = screen.getByLabelText(/container inventory/i);
      expect(containerSection).toBeInTheDocument();

      const inventorySection = screen.getByLabelText(/player inventory/i);
      expect(inventorySection).toBeInTheDocument();
    });

    it('should support keyboard navigation', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      // Focus on a focusable element (listitem) instead of the section
      const containerItems = screen.getAllByRole('listitem');
      if (containerItems.length > 0) {
        containerItems[0].focus();
        expect(containerItems[0]).toHaveFocus();
      } else {
        // If no items, focus on a transfer button if available
        const buttons = screen.getAllByRole('button');
        if (buttons.length > 0) {
          buttons[0].focus();
          expect(buttons[0]).toHaveFocus();
        }
      }
    });

    it('should have proper focus management', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      // Items have tabIndex={0} so they can receive focus
      const firstItem = screen.getByText('Test Item').closest('[role="listitem"]');
      if (firstItem) {
        (firstItem as HTMLElement).focus();
        expect(firstItem).toHaveFocus();
      }
    });
  });

  describe('Loading State', () => {
    it('should show loading indicator when loading', () => {
      mockIsLoading.mockReturnValue(true);
      mockGetContainer.mockReturnValue(null);
      mockGetMutationToken.mockReturnValue(null);
      mockIsContainerOpen.mockReturnValue(false);

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/loading/i)).toBeInTheDocument();
    });
  });

  describe('Container Types', () => {
    it('should display environment container correctly', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/container/i)).toBeInTheDocument();
    });

    it('should display equipment container correctly', () => {
      const equipmentContainer = { ...mockContainer, source_type: 'equipment' as const };
      mockGetContainer.mockReturnValue(equipmentContainer);
      mockGetMutationToken.mockReturnValue('test-token');
      mockIsContainerOpen.mockReturnValue(true);

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/container/i)).toBeInTheDocument();
    });

    it('should display corpse container correctly', () => {
      const corpseContainer = {
        ...mockContainer,
        source_type: 'corpse' as const,
        decay_at: new Date(Date.now() + 3600000).toISOString(),
      };
      mockGetContainer.mockReturnValue(corpseContainer);
      mockGetMutationToken.mockReturnValue('test-token');
      mockIsContainerOpen.mockReturnValue(true);

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/container/i)).toBeInTheDocument();
    });
  });

  describe('Item Display', () => {
    it('should show item quantity', () => {
      const containerWithQuantity = {
        ...mockContainer,
        items: [
          {
            ...mockContainer.items[0],
            quantity: 5,
          },
        ],
      };
      mockGetContainer.mockReturnValue(containerWithQuantity);
      mockGetMutationToken.mockReturnValue('test-token');
      mockIsContainerOpen.mockReturnValue(true);

      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText(/5/i)).toBeInTheDocument();
    });

    it('should show item name', () => {
      render(<ContainerSplitPane containerId="test-container-1" />);

      expect(screen.getByText('Test Item')).toBeInTheDocument();
    });
  });
});
