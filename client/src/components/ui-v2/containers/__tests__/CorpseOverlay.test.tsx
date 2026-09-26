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
});
