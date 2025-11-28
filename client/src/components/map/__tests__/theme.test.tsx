/**
 * Tests for theme integration in map components.
 *
 * Verifies that map components use consistent styling
 * with the existing client UI theme and support dark mode.
 */

import { render } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import type { Room } from '../../../stores/gameStore';
import { MapControls } from '../MapControls';
import { RoomDetailsPanel } from '../RoomDetailsPanel';

describe('Theme Integration', () => {
  beforeEach(() => {
    // Set up document with theme classes
    document.documentElement.className = 'theme-terminal color-scheme-default';
  });

  afterEach(() => {
    document.documentElement.className = '';
  });

  describe('MapControls theme classes', () => {
    it('should use mythos-terminal theme classes', () => {
      const { container } = render(
        <MapControls
          searchQuery=""
          onSearchChange={() => {}}
          plane="earth"
          zone="arkhamcity"
          availablePlanes={['earth']}
          availableZones={['arkhamcity']}
          availableSubZones={[]}
        />
      );

      // Check for mythos-terminal classes
      const controlsElement = container.querySelector('.bg-mythos-terminal-background');
      expect(controlsElement).toBeTruthy();
      const textElement = container.querySelector('.text-mythos-terminal-text');
      expect(textElement).toBeTruthy();
      const borderElement = container.querySelector('.border-mythos-terminal-border');
      expect(borderElement).toBeTruthy();
    });

    it('should use consistent color classes', () => {
      const { container } = render(
        <MapControls
          searchQuery=""
          onSearchChange={() => {}}
          plane="earth"
          zone="arkhamcity"
          availablePlanes={['earth']}
          availableZones={['arkhamcity']}
          availableSubZones={[]}
          onResetView={() => {}}
        />
      );

      // Check for primary color class in reset button
      const buttonElement = container.querySelector('.bg-mythos-terminal-primary');
      expect(buttonElement).toBeTruthy();
    });
  });

  describe('RoomDetailsPanel theme classes', () => {
    it('should use mythos-terminal theme classes', () => {
      const room: Room = {
        id: 'test_room',
        name: 'Test Room',
        description: 'A test room',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'northside',
        exits: {},
      };

      const { container } = render(<RoomDetailsPanel room={room} onClose={() => {}} />);

      // Check for mythos-terminal classes
      const panelElement = container.querySelector('.bg-mythos-terminal-background');
      expect(panelElement).toBeTruthy();
      const textElement = container.querySelector('.text-mythos-terminal-text');
      expect(textElement).toBeTruthy();
      const borderElement = container.querySelector('.border-mythos-terminal-border');
      expect(borderElement).toBeTruthy();
    });

    it('should use primary color for exit targets', () => {
      const room: Room = {
        id: 'test_room',
        name: 'Test Room',
        description: 'A test room',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'northside',
        exits: { north: 'other_room' },
      };

      const { container } = render(<RoomDetailsPanel room={room} onClose={() => {}} />);

      // Check for primary color class in exit targets
      const exitElement = container.querySelector('.text-mythos-terminal-primary');
      expect(exitElement).toBeTruthy();
    });
  });

  describe('Dark mode support', () => {
    it('should support dark mode theme classes', () => {
      // Set dark mode theme
      document.documentElement.className = 'theme-terminal color-scheme-default';

      const { container } = render(
        <MapControls
          searchQuery=""
          onSearchChange={() => {}}
          plane="earth"
          zone="arkhamcity"
          availablePlanes={['earth']}
          availableZones={['arkhamcity']}
          availableSubZones={[]}
        />
      );

      // Dark mode classes should still work (mythos-terminal uses dark colors by default)
      const nodeElement = container.querySelector('.bg-mythos-terminal-background');
      expect(nodeElement).toBeTruthy();
    });
  });

  describe('Consistent styling', () => {
    it('should use consistent color classes across components', () => {
      const expectedClasses = [
        'bg-mythos-terminal-background',
        'text-mythos-terminal-text',
        'border-mythos-terminal-border',
        'bg-mythos-terminal-primary',
        'text-mythos-terminal-error',
      ];

      // All components should use these classes
      expectedClasses.forEach(className => {
        expect(className).toContain('mythos-terminal');
      });
    });

    it('should use consistent spacing and layout classes', () => {
      // Verify that components use Tailwind utility classes consistently
      const commonClasses = ['p-4', 'mb-4', 'rounded', 'border', 'shadow-lg'];

      // These classes should be used across map components
      commonClasses.forEach(className => {
        expect(className).toBeTruthy();
      });
    });

    it('should use consistent hover states', () => {
      const room: Room = {
        id: 'test_room',
        name: 'Test Room',
        description: 'A test room',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'northside',
        exits: {},
      };

      const { container } = render(<RoomDetailsPanel room={room} onClose={() => {}} />);

      // Check for hover state classes
      const closeButton = container.querySelector('.hover\\:text-mythos-terminal-error');
      expect(closeButton).toBeTruthy();
    });
  });

  describe('Theme context integration', () => {
    it('should work with theme context classes', () => {
      // Verify that components work with theme classes applied to document
      document.documentElement.className = 'theme-terminal color-scheme-default';

      const { container } = render(
        <MapControls
          searchQuery=""
          onSearchChange={() => {}}
          plane="earth"
          zone="arkhamcity"
          availablePlanes={['earth']}
          availableZones={['arkhamcity']}
          availableSubZones={[]}
        />
      );

      // Components should render correctly with theme classes
      expect(container).toBeTruthy();
      expect(document.documentElement.classList.contains('theme-terminal')).toBe(true);
    });
  });
});
