/**
 * #626: AsciiMinimap noise-replacement behavior under deranged-tier hallucination.
 */

import { render, screen, waitFor } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { AsciiMinimap } from '../AsciiMinimap';

vi.mock('../../../api/maps', () => ({
  fetchAsciiMinimap: vi.fn().mockResolvedValue({ map_html: '<div class="ascii-map">real map</div>' }),
}));

describe('AsciiMinimap #626 hallucination', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('renders churning noise instead of fetching/showing the real map when hallucinate is true', async () => {
    const { fetchAsciiMinimap } = await import('../../../api/maps');
    render(
      <AsciiMinimap
        plane="earth"
        zone="arkhamcity"
        currentRoomId="room1"
        size={5}
        variant="inline"
        hallucinate={true}
        seed={42}
      />
    );

    expect(screen.queryByText('real map')).not.toBeInTheDocument();
    expect(fetchAsciiMinimap).not.toHaveBeenCalled();
  });

  it('fetches and shows the real map when not hallucinating', async () => {
    render(
      <AsciiMinimap
        plane="earth"
        zone="arkhamcity"
        currentRoomId="room1"
        size={5}
        variant="inline"
        hallucinate={false}
      />
    );

    await waitFor(() => expect(screen.getByText('real map')).toBeInTheDocument());
  });
});
