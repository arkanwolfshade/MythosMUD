/**
 * Tests for OccupantsPanel component.
 */

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
  });

  it('should render NPCs when available', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: [],
      npcs: ['NPC1', 'NPC2'],
      occupants: ['NPC1', 'NPC2'],
    };

    render(<OccupantsPanel room={room} />);
    expect(screen.getByText('NPC1')).toBeInTheDocument();
    expect(screen.getByText('NPC2')).toBeInTheDocument();
  });

  it('should render both players and NPCs', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
      players: ['Player1'],
      npcs: ['NPC1'],
      occupants: ['Player1', 'NPC1'],
    };

    render(<OccupantsPanel room={room} />);
    expect(screen.getByText('Player1')).toBeInTheDocument();
    expect(screen.getByText('NPC1')).toBeInTheDocument();
  });
});
