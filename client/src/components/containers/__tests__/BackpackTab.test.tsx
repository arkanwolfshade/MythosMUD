/**
 * Tests for BackpackTab component.
 *
 * As documented in the restricted archives of Miskatonic University, backpack
 * tab components require thorough testing to ensure proper display and interaction
 * with wearable container items.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { ContainerComponent, InventoryStack } from '../../../stores/containerStore';
import { BackpackTab } from '../BackpackTab';

// Mock the stores. BackpackTab subscribes to openContainers and derives wearable list in useMemo.
let mockOpenContainers: Record<string, ContainerComponent> = {};
const mockSelectContainer = vi.fn();
const mockDeselectContainer = vi.fn();
const mockSelectedContainerId = vi.fn();

vi.mock('../../../stores/containerStore', () => ({
  useContainerStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      openContainers: mockOpenContainers,
      selectContainer: mockSelectContainer,
      deselectContainer: mockDeselectContainer,
      selectedContainerId: mockSelectedContainerId(),
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

describe('BackpackTab', () => {
  const mockWearableContainer: ContainerComponent = {
    container_id: 'backpack-1',
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
    metadata: {
      item_id: 'backpack',
      item_name: 'Leather Backpack',
    },
  };

  const mockPlayerInventory: InventoryStack[] = [
    {
      item_instance_id: 'backpack-item-1',
      prototype_id: 'backpack',
      item_id: 'backpack',
      item_name: 'Leather Backpack',
      slot_type: 'backpack',
      quantity: 1,
      inner_container: {
        capacity_slots: 5,
        items: [],
      },
    },
  ];

  beforeEach(() => {
    vi.clearAllMocks();
    mockOpenContainers = { 'backpack-1': mockWearableContainer };
    mockSelectedContainerId.mockReturnValue(null);
    mockPlayer.inventory = mockPlayerInventory;
  });

  describe('Rendering', () => {
    it('should render backpack tab when player has wearable container', () => {
      render(<BackpackTab />);

      expect(screen.getByText(/backpack/i)).toBeInTheDocument();
    });

    it('should not render when player has no wearable containers', () => {
      mockOpenContainers = {};
      mockPlayer.inventory = [];

      const { container } = render(<BackpackTab />);
      expect(container.firstChild).toBeNull();
    });

    it('should show container name in tab', () => {
      render(<BackpackTab />);

      expect(screen.getByText(/leather backpack/i)).toBeInTheDocument();
    });

    it('should show item count in tab', () => {
      render(<BackpackTab />);

      expect(screen.getByText(/1/i)).toBeInTheDocument();
    });

    it('should show capacity in tab', () => {
      render(<BackpackTab />);

      expect(screen.getByText(/5/i)).toBeInTheDocument();
    });
  });

  describe('Selection', () => {
    it('should highlight tab when container is selected', () => {
      mockSelectedContainerId.mockReturnValue('backpack-1');

      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      expect(tab).toHaveClass(/active|selected|primary/i);
    });

    it('should call selectContainer when tab is clicked', () => {
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      fireEvent.click(tab);

      expect(mockSelectContainer).toHaveBeenCalledWith('backpack-1');
    });

    it('should deselect when clicking selected tab', () => {
      mockSelectedContainerId.mockReturnValue('backpack-1');

      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      fireEvent.click(tab);

      expect(mockDeselectContainer).toHaveBeenCalled();
      expect(mockSelectContainer).not.toHaveBeenCalled();
    });
  });

  describe('Multiple Containers', () => {
    it('should render multiple tabs for multiple containers', () => {
      const container2: ContainerComponent = {
        container_id: 'backpack-2',
        source_type: 'equipment',
        entity_id: 'player-1',
        capacity_slots: 10,
        lock_state: 'unlocked',
        items: [],
        allowed_roles: [],
        metadata: {
          item_id: 'bandolier',
          item_name: 'Leather Bandolier',
        },
      };

      mockOpenContainers = {
        'backpack-1': mockWearableContainer,
        'backpack-2': container2,
      };

      render(<BackpackTab />);

      expect(screen.getByText(/leather backpack/i)).toBeInTheDocument();
      expect(screen.getByText(/leather bandolier/i)).toBeInTheDocument();
    });

    it('should allow selecting different containers', () => {
      const container2: ContainerComponent = {
        container_id: 'backpack-2',
        source_type: 'equipment',
        entity_id: 'player-1',
        capacity_slots: 10,
        lock_state: 'unlocked',
        items: [],
        allowed_roles: [],
        metadata: {
          item_id: 'bandolier',
          item_name: 'Leather Bandolier',
        },
      };

      mockOpenContainers = {
        'backpack-1': mockWearableContainer,
        'backpack-2': container2,
      };

      render(<BackpackTab />);

      const bandolierTab = screen.getByRole('tab', { name: /leather bandolier/i });
      fireEvent.click(bandolierTab);

      expect(mockSelectContainer).toHaveBeenCalledWith('backpack-2');
    });
  });

  describe('Accessibility', () => {
    it('should have proper ARIA labels', () => {
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      expect(tab).toHaveAttribute('aria-label');
    });

    it('should support keyboard navigation', () => {
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      tab.focus();
      expect(tab).toHaveFocus();
    });

    it('should activate on Enter key press', () => {
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      fireEvent.keyDown(tab, { key: 'Enter', code: 'Enter' });

      expect(mockSelectContainer).toHaveBeenCalled();
    });

    it('should activate on Space key press', () => {
      render(<BackpackTab />);

      const tab = screen.getByRole('tab', { name: /leather backpack/i });
      fireEvent.keyDown(tab, { key: ' ', code: 'Space' });

      expect(mockSelectContainer).toHaveBeenCalled();
    });
  });

  describe('Empty State', () => {
    it('should show empty indicator when container has no items', () => {
      const emptyContainer = { ...mockWearableContainer, items: [] };
      mockOpenContainers = { 'backpack-1': emptyContainer };

      render(<BackpackTab />);

      expect(screen.getByText(/0/i)).toBeInTheDocument();
    });
  });

  describe('Container Metadata', () => {
    it('should display container name from metadata', () => {
      render(<BackpackTab />);

      expect(screen.getByText(/leather backpack/i)).toBeInTheDocument();
    });

    it('should fallback to item_id if item_name not in metadata', () => {
      const containerWithoutName = {
        ...mockWearableContainer,
        metadata: {
          item_id: 'backpack',
        },
      };
      mockOpenContainers = { 'backpack-1': containerWithoutName };

      render(<BackpackTab />);

      expect(screen.getByText(/backpack/i)).toBeInTheDocument();
    });
  });
});
