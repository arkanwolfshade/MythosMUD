/**
 * Tests for InventoryPanel component (#711).
 */

import '@testing-library/jest-dom/vitest';
import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { InventoryStack, RoomContainerSummary } from '../../types';
import { InventoryPanel } from '../InventoryPanel';

function item(overrides: Partial<InventoryStack> = {}): InventoryStack {
  return {
    item_instance_id: 'inst-1',
    prototype_id: 'torch',
    item_id: 'torch',
    item_name: 'Torch',
    slot_type: 'inventory',
    quantity: 1,
    ...overrides,
  };
}

describe('InventoryPanel', () => {
  it('shows an empty-state message with nothing carried, equipped, or in the room', () => {
    render(
      <InventoryPanel
        inventory={[]}
        equipped={{}}
        roomContainers={[]}
        onSendCommand={vi.fn()}
        onOpenContainer={vi.fn()}
      />
    );
    expect(screen.getByText(/carrying nothing/i)).toBeInTheDocument();
  });

  it('lists carried items and sends drop/equip commands', () => {
    const onSendCommand = vi.fn();
    render(
      <InventoryPanel
        inventory={[item()]}
        equipped={{}}
        roomContainers={[]}
        onSendCommand={onSendCommand}
        onOpenContainer={vi.fn()}
      />
    );
    expect(screen.getByText('Torch')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Equip' }));
    expect(onSendCommand).toHaveBeenCalledWith('equip inst-1');
    fireEvent.click(screen.getByRole('button', { name: 'Drop' }));
    expect(onSendCommand).toHaveBeenCalledWith('drop inst-1');
  });

  it('offers Equip for every carried item -- the server validates equippability', () => {
    render(
      <InventoryPanel
        inventory={[item({ slot_type: 'backpack' })]}
        equipped={{}}
        roomContainers={[]}
        onSendCommand={vi.fn()}
        onOpenContainer={vi.fn()}
      />
    );
    expect(screen.getByRole('button', { name: 'Equip' })).toBeInTheDocument();
  });

  it('lists equipped items and sends unequip by slot', () => {
    const onSendCommand = vi.fn();
    render(
      <InventoryPanel
        inventory={[]}
        equipped={{ main_hand: item({ item_name: 'Sword', slot_type: 'main_hand' }) }}
        roomContainers={[]}
        onSendCommand={onSendCommand}
        onOpenContainer={vi.fn()}
      />
    );
    expect(screen.getByText('Sword')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Unequip' }));
    expect(onSendCommand).toHaveBeenCalledWith('unequip main_hand');
  });

  it('offers Open for a worn container and calls onOpenContainer with its instance id', () => {
    const onOpenContainer = vi.fn();
    render(
      <InventoryPanel
        inventory={[]}
        equipped={{
          back: item({
            item_name: 'Backpack',
            slot_type: 'back',
            inner_container: { capacity_slots: 10, items: [] },
          }),
        }}
        roomContainers={[]}
        onSendCommand={vi.fn()}
        onOpenContainer={onOpenContainer}
      />
    );
    fireEvent.click(screen.getByRole('button', { name: 'Open' }));
    expect(onOpenContainer).toHaveBeenCalledWith('inst-1');
  });

  it('lists room containers (corpses) and opens them by id', () => {
    const onOpenContainer = vi.fn();
    const corpse: RoomContainerSummary = { container_id: 'corpse-1', source_type: 'corpse' };
    render(
      <InventoryPanel
        inventory={[]}
        equipped={{}}
        roomContainers={[corpse]}
        onSendCommand={vi.fn()}
        onOpenContainer={onOpenContainer}
      />
    );
    expect(screen.getByText('Corpse')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Open' }));
    expect(onOpenContainer).toHaveBeenCalledWith('corpse-1');
  });
});
