/**
 * #626: AsciiMapViewer noise-replacement behavior under deranged-tier hallucination.
 */

import { render, screen, waitFor } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { AsciiMapViewer } from '../AsciiMapViewer';

vi.mock('../../../api/maps', () => ({
  fetchAsciiMap: vi.fn().mockResolvedValue({ map_html: '<div class="ascii-map">real map</div>' }),
}));

describe('AsciiMapViewer #626 hallucination', () => {
  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('renders noise instead of loading/real map when hallucinating', async () => {
    render(
      <AsciiMapViewer
        plane="earth"
        zone="arkhamcity"
        currentRoomId="room1"
        hallucinate={true}
        seed={7}
        viewportWidth={20}
        viewportHeight={5}
      />
    );

    expect(screen.queryByText('Loading map...')).not.toBeInTheDocument();
    expect(screen.queryByText('real map')).not.toBeInTheDocument();
  });

  it('never shows the real map content even after the (irrelevant) fetch resolves', async () => {
    render(<AsciiMapViewer plane="earth" zone="arkhamcity" currentRoomId="room1" hallucinate={true} seed={7} />);
    await new Promise(resolve => setTimeout(resolve, 0));
    expect(screen.queryByText('real map')).not.toBeInTheDocument();
  });

  it('shows the real map when not hallucinating', async () => {
    render(<AsciiMapViewer plane="earth" zone="arkhamcity" currentRoomId="room1" hallucinate={false} />);
    await waitFor(() => expect(screen.getByText('real map')).toBeInTheDocument());
  });
});
