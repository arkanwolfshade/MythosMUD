import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ProfessionCard } from './ProfessionCard';

describe('ProfessionCard', () => {
  const mockProfession = {
    id: 0,
    name: 'Tramp',
    description: 'A wandering soul with no particular skills or connections.',
    flavor_text: 'You have spent your days drifting from place to place, learning to survive on your wits alone.',
    stat_requirements: {},
    mechanical_effects: {},
    is_available: true,
  };

  const mockProfessionWithRequirements = {
    id: 2,
    name: 'Scholar',
    description: 'A learned individual with high intelligence.',
    flavor_text: 'Your mind is your greatest weapon.',
    stat_requirements: { intelligence: 14, wisdom: 12 },
    mechanical_effects: {},
    is_available: true,
  };

  describe('Rendering', () => {
    it('should render profession name and description', () => {
      const onSelect = vi.fn();
      render(<ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />);

      expect(screen.getByText('Tramp')).toBeInTheDocument();
      expect(screen.getByText('A wandering soul with no particular skills or connections.')).toBeInTheDocument();
    });

    it('should render flavor text', () => {
      const onSelect = vi.fn();
      render(<ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />);

      expect(
        screen.getByText(
          'You have spent your days drifting from place to place, learning to survive on your wits alone.'
        )
      ).toBeInTheDocument();
    });

    it('should show "No requirements" when profession has no stat requirements', () => {
      const onSelect = vi.fn();
      render(<ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />);

      expect(screen.getByText('No requirements')).toBeInTheDocument();
    });

    it('should show stat requirements when present', () => {
      const onSelect = vi.fn();
      render(<ProfessionCard profession={mockProfessionWithRequirements} isSelected={false} onSelect={onSelect} />);

      expect(screen.getByText('Minimum: Intelligence 14, Wisdom 12')).toBeInTheDocument();
    });

    it('should highlight stat requirements', () => {
      const onSelect = vi.fn();
      render(<ProfessionCard profession={mockProfessionWithRequirements} isSelected={false} onSelect={onSelect} />);

      const requirementsElement = screen.getByText('Minimum: Intelligence 14, Wisdom 12');
      expect(requirementsElement).toHaveClass('stat-requirements');
    });
  });

  describe('Selection State', () => {
    it('should apply selected class when isSelected is true', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={true} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');
      expect(card).toHaveClass('selected');
    });

    it('should not apply selected class when isSelected is false', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');
      expect(card).not.toHaveClass('selected');
    });
  });

  describe('Interaction', () => {
    it('should call onSelect when card is clicked', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');
      fireEvent.click(card!);

      expect(onSelect).toHaveBeenCalledWith(mockProfession);
    });

    it('should call onSelect when card is clicked even if already selected', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={true} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');
      fireEvent.click(card!);

      expect(onSelect).toHaveBeenCalledWith(mockProfession);
    });
  });

  describe('Accessibility', () => {
    it('should have proper ARIA attributes', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');
      expect(card).toHaveAttribute('role', 'button');
      expect(card).toHaveAttribute('tabindex', '0');
      expect(card).toHaveAttribute('aria-pressed', 'false');
    });

    it('should update aria-pressed when selected', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={true} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');
      expect(card).toHaveAttribute('aria-pressed', 'true');
    });

    it('should handle keyboard navigation', () => {
      const onSelect = vi.fn();
      const { container } = render(
        <ProfessionCard profession={mockProfession} isSelected={false} onSelect={onSelect} />
      );

      const card = container.querySelector('.profession-card');

      // Test Enter key
      fireEvent.keyDown(card!, { key: 'Enter' });
      expect(onSelect).toHaveBeenCalledWith(mockProfession);

      // Test Space key
      fireEvent.keyDown(card!, { key: ' ' });
      expect(onSelect).toHaveBeenCalledTimes(2);
    });
  });
});
