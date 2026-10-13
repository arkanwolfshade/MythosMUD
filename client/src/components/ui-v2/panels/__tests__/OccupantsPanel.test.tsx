/**
 * Tests for OccupantsPanel component.
 */

import '@testing-library/jest-dom/vitest';
import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import type { Room } from '../../types';
import { OccupantsPanel } from '../OccupantsPanel';

describe('OccupantsPanel', () => {
  it('should render "No other players present" when room is null', () => {
    render(<OccupantsPanel room={null} />);
    expect(screen.getByText('No other players present')).toBeInTheDocument();
  });

  it('should render "No other players present" when room has no occupants', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: [],
      npcs: [],
      occupants: [],
    };

    render(<OccupantsPanel room={room} />);
    expect(screen.getByText('No other players present')).toBeInTheDocument();
  });

  it('should render players when available', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: ['Player1', 'Player2'],
      npcs: [],
      occupants: ['Player1', 'Player2'],
    };

    render(<OccupantsPanel room={room} />);
    expect(screen.getByText('Player1')).toBeInTheDocument();
    expect(screen.getByText('Player2')).toBeInTheDocument();
    expect(screen.getByTestId('occupants-other-players')).toHaveAttribute('data-names', 'Player1\nPlayer2');
  });

  it('should render NPCs when available', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: [],
      npcs: [
        { name: 'NPC1', disposition: 'shopkeeper' },
        { name: 'NPC2', disposition: 'aggressive_mob' },
      ],
      occupants: ['NPC1', 'NPC2'],
    };

    render(<OccupantsPanel room={room} />);
    expect(screen.getByText('NPC1')).toBeInTheDocument();
    expect(screen.getByText('NPC2')).toBeInTheDocument();
  });

  it('styles each NPC by its disposition through the npc.* category', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: [],
      npcs: [
        { name: 'Merchant', disposition: 'shopkeeper' },
        { name: 'Elder', disposition: 'quest_giver' },
        { name: 'Rat', disposition: 'aggressive_mob' },
        { name: 'Pigeon', disposition: 'passive_mob' },
      ],
    };

    render(<OccupantsPanel room={room} />);

    for (const [name, disposition] of [
      ['Merchant', 'shopkeeper'],
      ['Elder', 'quest_giver'],
      ['Rat', 'aggressive_mob'],
      ['Pigeon', 'passive_mob'],
    ]) {
      const row = screen.getByText(name);
      expect(row).toHaveAttribute('data-disposition', disposition);
      expect(row).toHaveClass('cat', 'cat-npc', `cat-npc-${disposition}`);
    }
  });

  it('keeps two same-named NPCs as separate rows, each with its own disposition', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      npcs: [
        { name: 'Rat', disposition: 'passive_mob' },
        { name: 'Rat', disposition: 'aggressive_mob' },
      ],
    };

    render(<OccupantsPanel room={room} />);

    const rows = screen.getAllByText('Rat');
    expect(rows.map(row => row.getAttribute('data-disposition'))).toEqual(['passive_mob', 'aggressive_mob']);
  });

  it('should render both players and NPCs', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: ['Player1'],
      npcs: [{ name: 'NPC1', disposition: 'passive_mob' }],
      occupants: ['Player1', 'NPC1'],
    };

    render(<OccupantsPanel room={room} />);
    expect(screen.getByText('Player1')).toBeInTheDocument();
    expect(screen.getByText('NPC1')).toBeInTheDocument();
  });
});
