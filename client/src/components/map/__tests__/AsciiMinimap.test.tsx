import { render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { fetchAsciiMinimap } from '../../../api/maps';
import { AsciiMinimap } from '../AsciiMinimap';

vi.mock('../../../api/maps', () => ({ fetchAsciiMinimap: vi.fn() }));

type MinimapResponse = Awaited<ReturnType<typeof fetchAsciiMinimap>>;

function renderMinimap() {
  render(
    <AsciiMinimap
      plane="earth"
      zone="arkhamcity"
      subZone="first_exposure"
      currentRoomId="instance_e4857769-81a3-40dd-bf65-b1811a1904ee_earth_arkhamcity_first_exposure_room_vault_of_the_owner_001"
      variant="inline"
    />
  );
}

describe('AsciiMinimap', () => {
  beforeEach(() => {
    vi.mocked(fetchAsciiMinimap).mockReset();
  });

  it('says so when the server has no map for the location, instead of leaving the panel blank (#1108)', async () => {
    vi.mocked(fetchAsciiMinimap).mockResolvedValue({ map_html: '' } as unknown as MinimapResponse);

    renderMinimap();

    expect(await screen.findByText('No map for this location')).toBeInTheDocument();
  });

  it('renders the map the server sends', async () => {
    vi.mocked(fetchAsciiMinimap).mockResolvedValue({ map_html: '<pre>[@]</pre>' } as unknown as MinimapResponse);

    renderMinimap();

    expect(await screen.findByText('[@]')).toBeInTheDocument();
    expect(screen.queryByText('No map for this location')).not.toBeInTheDocument();
  });

  it('shows the error marker when the request fails', async () => {
    vi.mocked(fetchAsciiMinimap).mockRejectedValue(new Error('boom'));

    renderMinimap();

    expect(await screen.findByText('Map Error')).toBeInTheDocument();
    expect(screen.queryByText('No map for this location')).not.toBeInTheDocument();
  });
});
