import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { RoomDescriptionPanel } from '../RoomDescriptionPanel';
import type { Room } from '../../types';

describe('RoomDescriptionPanel', () => {
  describe('rendering', () => {
    it('should render "No room description available" when room is null', () => {
      render(<RoomDescriptionPanel room={null} />);
      expect(screen.getByText('No room description available')).toBeInTheDocument();
    });

    it('should render room description when room is provided', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'This is a test room description.',
        exits: {},
      };

      render(<RoomDescriptionPanel room={room} />);
      expect(screen.getByText('Description')).toBeInTheDocument();
      expect(screen.getByText('This is a test room description.')).toBeInTheDocument();
    });

    it('should format description by trimming whitespace', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: '  This is a test room description.  ',
        exits: {},
      };

      render(<RoomDescriptionPanel room={room} />);
      expect(screen.getByText('This is a test room description.')).toBeInTheDocument();
    });

    it('should handle empty description', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: '',
        exits: {},
      };

      render(<RoomDescriptionPanel room={room} />);
      expect(screen.getByText('No description available')).toBeInTheDocument();
    });

    it('should handle description with multiple spaces', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'This  is   a    test     room',
        exits: {},
      };

      render(<RoomDescriptionPanel room={room} />);
      // Should normalize multiple spaces to single space
      const descriptionElement = screen.getByText(/This is a test room/);
      expect(descriptionElement).toBeInTheDocument();
    });

    it('should handle description with newlines', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'This is a test room.\nWith multiple lines.',
        exits: {},
      };

      render(<RoomDescriptionPanel room={room} />);
      expect(screen.getByText(/This is a test room/)).toBeInTheDocument();
      expect(screen.getByText(/With multiple lines/)).toBeInTheDocument();
    });

    it('should render description with whitespace-pre-wrap class', () => {
      const room: Room = {
        id: 'room1',
        name: 'Test Room',
        description: 'Test description',
        exits: {},
      };

      const { container } = render(<RoomDescriptionPanel room={room} />);
      const descriptionElement = container.querySelector('.whitespace-pre-wrap');
      expect(descriptionElement).toBeInTheDocument();
    });
  });
});
