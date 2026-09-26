/**
 * Tests for ContainerTransferModal (#711): rendering, transfer/loot-all/close calls, error surfacing.
 */

import '@testing-library/jest-dom/vitest';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { ContainerApiError } from '../../../../api/containers';
import * as containersApi from '../../../../api/containers';
import type { ContainerSnapshot, InventoryStack } from '../../types';
import type { OpenContainerState } from '../../utils/stateUpdateUtils';
import { ContainerTransferModal, ContainerTransferModals } from '../ContainerTransferModal';

vi.mock('../../../../api/containers', async () => {
  const actual = await vi.importActual<typeof containersApi>('../../../../api/containers');
  return {
    ...actual,
    transferItem: vi.fn(),
    lootAll: vi.fn(),
    closeContainer: vi.fn(),
  };
});

function stack(overrides: Partial<InventoryStack> = {}): InventoryStack {
  return {
    item_instance_id: 'inst-1',
    prototype_id: 'coin',
    item_id: 'coin',
    item_name: 'Coin',
    slot_type: 'inventory',
    quantity: 3,
    ...overrides,
  };
}

function containerState(overrides: Partial<ContainerSnapshot> = {}): OpenContainerState {
  const container: ContainerSnapshot = {
    container_id: 'c1',
    source_type: 'environment',
    lock_state: 'unlocked',
    capacity_slots: 10,
    allowed_roles: [],
    items: [stack()],
    metadata: {},
    ...overrides,
  };
  return { container, mutationToken: 'tok-1' };
}

describe('ContainerTransferModal', () => {
  afterEach(() => {
    vi.clearAllMocks();
  });

  it('renders container and player inventory columns', () => {
    render(
      <ContainerTransferModal
        containerId="c1"
        state={containerState()}
        playerInventory={[stack({ item_instance_id: 'inst-2', item_name: 'Torch', quantity: 1 })]}
        authToken="tok"
        onClose={vi.fn()}
      />
    );
    expect(screen.getByText('Coin')).toBeInTheDocument();
    expect(screen.getByText('Torch')).toBeInTheDocument();
    expect(screen.getAllByRole('button', { name: 'Transfer' })).toHaveLength(2);
  });

  it('transfers a container item to the player with the default (full stack) quantity', async () => {
    render(
      <ContainerTransferModal
        containerId="c1"
        state={containerState()}
        playerInventory={[]}
        authToken="tok"
        onClose={vi.fn()}
      />
    );
    fireEvent.click(screen.getByRole('button', { name: 'Transfer' }));
    await waitFor(() =>
      expect(containersApi.transferItem).toHaveBeenCalledWith('tok', {
        containerId: 'c1',
        mutationToken: 'tok-1',
        direction: 'to_player',
        stack: { item_id: 'coin', item_instance_id: 'inst-1' },
        quantity: 3,
      })
    );
  });

  it('transfers a chosen quantity when the stepper is changed', async () => {
    render(
      <ContainerTransferModal
        containerId="c1"
        state={containerState()}
        playerInventory={[]}
        authToken="tok"
        onClose={vi.fn()}
      />
    );
    fireEvent.change(screen.getByLabelText(/quantity for coin/i), { target: { value: '2' } });
    fireEvent.click(screen.getByRole('button', { name: 'Transfer' }));
    await waitFor(() =>
      expect(containersApi.transferItem).toHaveBeenCalledWith(
        'tok',
        expect.objectContaining({ quantity: 2, direction: 'to_player' })
      )
    );
  });

  it('loots all container items', async () => {
    render(
      <ContainerTransferModal
        containerId="c1"
        state={containerState()}
        playerInventory={[]}
        authToken="tok"
        onClose={vi.fn()}
      />
    );
    fireEvent.click(screen.getByRole('button', { name: 'Loot all' }));
    await waitFor(() => expect(containersApi.lootAll).toHaveBeenCalledWith('tok', 'c1', 'tok-1'));
  });

  it('closes the container and notifies the parent', async () => {
    const onClose = vi.fn();
    vi.mocked(containersApi.closeContainer).mockResolvedValue(undefined);
    render(
      <ContainerTransferModal
        containerId="c1"
        state={containerState()}
        playerInventory={[]}
        authToken="tok"
        onClose={onClose}
      />
    );
    fireEvent.click(screen.getAllByLabelText('Close modal')[0]);
    await waitFor(() => expect(containersApi.closeContainer).toHaveBeenCalledWith('tok', 'c1', 'tok-1'));
    await waitFor(() => expect(onClose).toHaveBeenCalledWith('c1'));
  });

  it('surfaces an API error (e.g. capacity) without throwing', async () => {
    vi.mocked(containersApi.transferItem).mockRejectedValue(new ContainerApiError('Container is full', 409));
    render(
      <ContainerTransferModal
        containerId="c1"
        state={containerState()}
        playerInventory={[]}
        authToken="tok"
        onClose={vi.fn()}
      />
    );
    fireEvent.click(screen.getByRole('button', { name: 'Transfer' }));
    expect(await screen.findByRole('alert')).toHaveTextContent('Container is full');
  });
});

describe('ContainerTransferModals', () => {
  it('renders nothing when no containers are open', () => {
    const { container } = render(
      <ContainerTransferModals openContainers={undefined} playerInventory={[]} authToken="tok" onClose={vi.fn()} />
    );
    expect(container).toBeEmptyDOMElement();
  });

  it('renders one modal per open container', () => {
    render(
      <ContainerTransferModals
        openContainers={{ c1: containerState(), c2: containerState({ container_id: 'c2' }) }}
        playerInventory={[]}
        authToken="tok"
        onClose={vi.fn()}
      />
    );
    expect(screen.getAllByRole('dialog')).toHaveLength(2);
  });
});
