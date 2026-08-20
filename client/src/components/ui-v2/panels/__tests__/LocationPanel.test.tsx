import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { LocationPanel } from '../LocationPanel';
import type { Room } from '../../types';

describe('LocationPanel', () => {
  describe('rendering', () => {
    it('should render "No location information available" when room is null', () => {
      render(<LocationPanel room={null} />);
      expect(screen.getByText('No location information available')).toBeInTheDocument();
    });

    it('should render location hierarchy when room is provided', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'arkham_city',
        sub_zone: 'university_library',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/Arkham City/)).toBeInTheDocument();
      expect(screen.getByText(/University Library/)).toBeInTheDocument();
      expect(screen.getByText(/Test Room/)).toBeInTheDocument();
    });

    it('should render exits when room has exits', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'arkham',
        sub_zone: 'city',
        exits: {
          north: 'room2',
          south: 'room3',
        },
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/Exits:/)).toBeInTheDocument();
      expect(screen.getByText(/North/)).toBeInTheDocument();
      expect(screen.getByText(/South/)).toBeInTheDocument();
    });

    it('should not render exits section when room has no exits', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      expect(screen.queryByText(/Exits:/)).not.toBeInTheDocument();
    });

    it('should filter out null exits', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        exits: {
          north: 'room2',
          south: null as unknown as string,
        },
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/North/)).toBeInTheDocument();
      expect(screen.queryByText(/South/)).not.toBeInTheDocument();
    });
  });

  describe('#626 deranged-tier direction hallucination', () => {
    const room: Room = {
      id: 'room1',
      name: 'Test Room',
      description: 'A test room',
      exits: { north: 'room2', east: 'room3' },
    };

    it('shows real exits for non-deranged tiers', () => {
      for (const tier of ['lucid', 'uneasy', 'fractured', 'catatonic'] as const) {
        const { unmount } = render(<LocationPanel room={room} tier={tier} playerId="player-1" />);
        expect(screen.getByText(/North/)).toBeInTheDocument();
        expect(screen.getByText(/East/)).toBeInTheDocument();
        unmount();
      }
    });

    it('shows real exits when deranged but no playerId is available', () => {
      render(<LocationPanel room={room} tier="deranged" />);
      expect(screen.getByText(/North/)).toBeInTheDocument();
      expect(screen.getByText(/East/)).toBeInTheDocument();
    });

    it('shows a hallucinated exit list when deranged with a playerId', () => {
      render(<LocationPanel room={room} tier="deranged" playerId="player-1" />);
      const exitsLine = screen.getByText(/Exits:/).parentElement;
      expect(exitsLine?.textContent).toMatch(/Exits:/);
    });

    it('is stable across re-renders for the same room+player', () => {
      const { rerender } = render(<LocationPanel room={room} tier="deranged" playerId="player-1" />);
      const first = screen.getByText(/Exits:/).parentElement?.textContent;
      rerender(<LocationPanel room={room} tier="deranged" playerId="player-1" />);
      const second = screen.getByText(/Exits:/).parentElement?.textContent;
      expect(second).toBe(first);
    });

    it('differs between two players standing in the same room', () => {
      const { unmount } = render(<LocationPanel room={room} tier="deranged" playerId="player-1" />);
      const first = screen.getByText(/Exits:/).parentElement?.textContent;
      unmount();
      render(<LocationPanel room={room} tier="deranged" playerId="player-2" />);
      const second = screen.getByText(/Exits:/).parentElement?.textContent;
      expect(second).not.toBe(first);
    });
  });

  describe('formatLocationName', () => {
    it('should format underscore-separated names', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'arkham_city',
        sub_zone: 'university_library',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/Arkham City/)).toBeInTheDocument();
      expect(screen.getByText(/University Library/)).toBeInTheDocument();
    });

    it('should format camelCase names', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'arkhamCity',
        sub_zone: 'universityLibrary',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/Arkham City/)).toBeInTheDocument();
      expect(screen.getByText(/University Library/)).toBeInTheDocument();
    });

    it('should use known patterns for common locations', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'arkhamcity',
        sub_zone: 'universitylibrary',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/Arkham City/)).toBeInTheDocument();
      expect(screen.getByText(/University Library/)).toBeInTheDocument();
    });

    it('should handle "Unknown" location', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'Unknown',
        sub_zone: 'Unknown',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      const locationText = screen.getByText(/Unknown/);
      expect(locationText).toBeInTheDocument();
    });

    it('should capitalize first letter for simple names', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'A test room',
        zone: 'arkham',
        sub_zone: 'city',
        exits: {},
      };

      render(<LocationPanel room={room} />);
      expect(screen.getByText(/Arkham/)).toBeInTheDocument();
      expect(screen.getByText(/City/)).toBeInTheDocument();
    });
  });
});
