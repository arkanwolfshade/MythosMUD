import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { MinimapInlineBody } from '../GameClientV2MinimapSection';
import type { Room } from '../types';

vi.mock('../../map/AsciiMinimap', () => ({
  AsciiMinimap: () => <div data-testid="ascii-minimap" />,
}));

const room: Room = {
  id: 'earth_arkhamcity_sanitarium_room_foyer_001',
  name: 'Main Foyer',
  description: '',
  exits: {},
};

describe('MinimapInlineBody (#909)', () => {
  it('labels the map with the room name, keeping the id as the tooltip', () => {
    render(<MinimapInlineBody room={room} authToken="t" />);
    const label = screen.getByText('Main Foyer');
    expect(label).toHaveAttribute('title', room.id);
    expect(screen.queryByText(room.id)).toBeNull();
  });

  it('falls back to the room id when the name is empty', () => {
    render(<MinimapInlineBody room={{ ...room, name: '' }} authToken="t" />);
    expect(screen.getByText(room.id)).toBeInTheDocument();
  });
});
