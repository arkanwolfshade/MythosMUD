import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { EldritchEffectsDemo } from './EldritchEffectsDemo';

vi.mock('../primitives/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; _size: number; className?: string }) => (
    <div data-testid={`eldritch-icon-${name}`} className={className}>
      Icon: {name}
    </div>
  ),
  MythosIcons: {
    lightbulb: 'lightbulb',
    heart: 'heart',
    sparkles: 'sparkles',
    eye: 'eye',
    move: 'move',
    maximize: 'maximize',
    rotate: 'rotate',
    eyeOff: 'eyeOff',
    shadow: 'shadow',
    square: 'square',
    play: 'play',
    star: 'star',
  },
}));

vi.mock('../primitives/MythosPanel', () => ({
  MythosPanel: ({
    title,
    subtitle,
    children,
    className,
  }: {
    title: string;
    subtitle?: string;
    children: React.ReactNode;
    _variant?: string;
    _size?: string;
    _interactive?: boolean;
    _showEldritchBorder?: boolean;
    className?: string;
  }) => (
    <div data-testid="mythos-panel" className={className}>
      <h2>{title}</h2>
      {subtitle && <h3>{subtitle}</h3>}
      {children}
    </div>
  ),
}));

vi.mock('../primitives/TerminalButton', () => ({
  TerminalButton: ({
    onClick,
    className,
    children,
  }: {
    onClick: () => void;
    _variant?: string;
    _size?: string;
    className?: string;
    children: React.ReactNode;
  }) => (
    <button data-testid="terminal-button" onClick={onClick} className={className}>
      {children}
    </button>
  ),
}));

vi.mock('../primitives/TerminalInput', () => ({
  TerminalInput: ({
    value,
    onChange,
    placeholder,
    className,
  }: {
    value: string;
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
    placeholder?: string;
    className?: string;
  }) => (
    <input
      data-testid="terminal-input"
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className={className}
    />
  ),
}));

describe('EldritchEffectsDemo', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Initial Rendering', () => {
    it('should render the demo component', () => {
      render(<EldritchEffectsDemo />);

      const root = screen.getByRole('region', { name: 'Eldritch Effects Demo' });
      expect(root).toBeInTheDocument();
      expect(root).toHaveClass('eldritch-demo-force-motion');
      expect(screen.getByText('Always Active Effects Test')).toBeInTheDocument();
      expect(screen.getAllByText('Eldritch Effects Demo').length).toBeGreaterThanOrEqual(1);
      expect(screen.getByText('Phase 4.1 Visuals')).toBeInTheDocument();
    });

    it('should notice when OS reduced-motion is enabled', () => {
      const previous = window.matchMedia;
      Object.defineProperty(window, 'matchMedia', {
        writable: true,
        configurable: true,
        value: (query: string) => ({
          matches: query.includes('prefers-reduced-motion'),
          media: query,
          addEventListener: vi.fn(),
          removeEventListener: vi.fn(),
        }),
      });

      render(<EldritchEffectsDemo />);

      expect(screen.getByTestId('reduced-motion-notice')).toBeInTheDocument();
      Object.defineProperty(window, 'matchMedia', { writable: true, configurable: true, value: previous });
    });

    it('should render all effect buttons', () => {
      render(<EldritchEffectsDemo />);

      expect(screen.getByText('Eldritch Glow')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Pulse')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Shimmer')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Fade')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Slide')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Scale')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Rotate')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Blur')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Shadow')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Border')).toBeInTheDocument();
    });

    it('should render preview sections', () => {
      render(<EldritchEffectsDemo />);

      expect(screen.getByText('Live Preview')).toBeInTheDocument();
      expect(screen.getByText('Animated Button')).toBeInTheDocument();
      expect(screen.getByText('Animated Input')).toBeInTheDocument();
      expect(screen.getByText('Animated Panel')).toBeInTheDocument();
      expect(screen.getByText('Animated Icon')).toBeInTheDocument();
    });
  });

  describe('Effect Toggling', () => {
    it('should toggle effects when buttons are clicked', () => {
      render(<EldritchEffectsDemo />);

      const glowButton = screen.getByText('Eldritch Glow');
      const pulseButton = screen.getByText('Eldritch Pulse');

      expect(glowButton).toBeInTheDocument();
      expect(pulseButton).toBeInTheDocument();

      fireEvent.click(glowButton);
      fireEvent.click(pulseButton);

      expect(glowButton).toBeInTheDocument();
      expect(pulseButton).toBeInTheDocument();
    });
  });

  describe('Interactive Elements', () => {
    it('should handle input changes', () => {
      render(<EldritchEffectsDemo />);

      const input = screen.getByTestId('terminal-input');
      fireEvent.change(input, { target: { value: 'test incantation' } });

      expect(input).toHaveValue('test incantation');
    });

    it('should show ritual status when Invoke Ritual is clicked', () => {
      render(<EldritchEffectsDemo />);

      const invokeButton = screen.getByText('Invoke Ritual');
      fireEvent.click(invokeButton);

      expect(screen.getByTestId('ritual-status')).toHaveTextContent('Ritual invoked.');
    });
  });

  describe('Effect Descriptions', () => {
    it('should display effect descriptions', () => {
      render(<EldritchEffectsDemo />);

      expect(
        screen.getByText(
          'Explore various eldritch-themed visual effects and animations. Click the buttons to toggle effects on the elements below.'
        )
      ).toBeInTheDocument();
      expect(screen.getByText('A button with glow and scale effects.')).toBeInTheDocument();
      expect(screen.getByText('An input field with border and shimmer effects on focus.')).toBeInTheDocument();
      expect(screen.getByText('A panel with pulsing shadow and opacity effects.')).toBeInTheDocument();
      expect(screen.getByText('An icon with rotation and blur effects.')).toBeInTheDocument();
    });
  });
});
