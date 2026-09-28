/**
 * Tests for CorpseOverlay component (#711): visibility, grace-period lock, live countdown.
 */

import '@testing-library/jest-dom/vitest';
import { act, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { RoomContainerSummary } from '../../types';
import { CorpseOverlay } from '../CorpseOverlay';

function corpse(overrides: Partial<RoomContainerSummary> = {}): RoomContainerSummary {
  return {
    container_id: 'corpse-1',
    source_type: 'corpse',
    owner_id: 'owner-1',
    decay_at: new Date(Date.now() + 3600_000).toISOString(),
    metadata: {
      grace_period_start: new Date().toISOString(),
      grace_period_seconds: 300,
    },
    ...overrides,
  };
}

describe('CorpseOverlay', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it('renders nothing when there are no corpses in the room', () => {
    const { container } = render(<CorpseOverlay roomContainers={[]} playerId="owner-1" onOpen={vi.fn()} />);
    expect(container).toBeEmptyDOMElement();
  });

  it('ignores non-corpse containers', () => {
    const { container } = render(
      <CorpseOverlay
        roomContainers={[{ container_id: 'c1', source_type: 'environment' }]}
        playerId="owner-1"
        onOpen={vi.fn()}
      />
    );
    expect(container).toBeEmptyDOMElement();
  });

  it('shows the owner Open enabled during grace period', () => {
    render(<CorpseOverlay roomContainers={[corpse()]} playerId="owner-1" onOpen={vi.fn()} />);
    expect(screen.getByText(/grace period:/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Open' })).toBeEnabled();
  });

  it('disables Open for a non-owner during grace period', () => {
    render(<CorpseOverlay roomContainers={[corpse()]} playerId="someone-else" onOpen={vi.fn()} />);
    expect(screen.getByText(/only the owner can access/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Open' })).toBeDisabled();
  });

  it('allows any player to open once the grace period has ended', () => {
    const expired = corpse({
      metadata: { grace_period_start: new Date(Date.now() - 400_000).toISOString(), grace_period_seconds: 300 },
    });
    render(<CorpseOverlay roomContainers={[expired]} playerId="someone-else" onOpen={vi.fn()} />);
    expect(screen.getByText(/grace period ended/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Open' })).toBeEnabled();
  });

  it('distinguishes a still-in-grace corpse from an expired one', () => {
    // E2E needs this to tell "the corpse I just made" from stale ones left by earlier specs:
    // an expired corpse is openable by anybody and sorts first, but holds none of our items.
    const fresh = corpse({ container_id: 'corpse-fresh' });
    const expired = corpse({
      container_id: 'corpse-expired',
      metadata: { grace_period_start: new Date(Date.now() - 400_000).toISOString(), grace_period_seconds: 300 },
    });
    render(<CorpseOverlay roomContainers={[expired, fresh]} playerId="owner-1" onOpen={vi.fn()} />);

    const byId = Object.fromEntries(
      screen.getAllByTestId('corpse-card').map(c => [c.getAttribute('data-container-id'), c])
    );
    expect(byId['corpse-fresh']?.getAttribute('data-grace-active')).toBe('true');
    expect(byId['corpse-expired']?.getAttribute('data-grace-active')).toBe('false');
    // Both are openable by the owner, so data-openable alone cannot separate them.
    expect(byId['corpse-fresh']?.getAttribute('data-openable')).toBe('true');
    expect(byId['corpse-expired']?.getAttribute('data-openable')).toBe('true');
  });

  it('calls onOpen with the container id', () => {
    const onOpen = vi.fn();
    render(<CorpseOverlay roomContainers={[corpse()]} playerId="owner-1" onOpen={onOpen} />);
    fireEvent.click(screen.getByRole('button', { name: 'Open' }));
    expect(onOpen).toHaveBeenCalledWith('corpse-1');
  });

  it('ticks the countdown, and the non-owner lock lifts once grace period elapses', () => {
    const c = corpse({
      metadata: { grace_period_start: new Date(Date.now() - 299_500).toISOString(), grace_period_seconds: 300 },
    });
    render(<CorpseOverlay roomContainers={[c]} playerId="someone-else" onOpen={vi.fn()} />);
    expect(screen.getByRole('button', { name: 'Open' })).toBeDisabled();
    act(() => {
      vi.advanceTimersByTime(2000);
    });
    expect(screen.getByText(/grace period ended/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Open' })).toBeEnabled();
  });
  it('marks each card with its container id and whether this player may open it', () => {
    // E2E scopes to these attributes: a room can hold several corpses whose cards render
    // identical text and Open buttons, so tests need to say which card they mean.
    const mine = corpse({ container_id: 'corpse-mine' });
    const theirs = corpse({ container_id: 'corpse-theirs', owner_id: 'someone-else' });
    render(<CorpseOverlay roomContainers={[mine, theirs]} playerId="owner-1" onOpen={vi.fn()} />);

    const cards = screen.getAllByTestId('corpse-card');
    expect(cards).toHaveLength(2);
    const byId = Object.fromEntries(cards.map(c => [c.getAttribute('data-container-id'), c]));
    expect(byId['corpse-mine']?.getAttribute('data-openable')).toBe('true');
    expect(byId['corpse-theirs']?.getAttribute('data-openable')).toBe('false');
  });
});
