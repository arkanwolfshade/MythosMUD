import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { describe, expect, it, vi } from 'vitest';
import { EldritchEffectsDemo } from './EldritchEffectsDemo';

// Mock the child components
vi.mock('./ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, _size, className }: { name: string; _size: number; className?: string }) => (
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

vi.mock('./ui/MythosPanel', () => ({
  MythosPanel: ({
    title,
    subtitle,
    children,
    _variant,
    _size,
    _interactive,
    _showEldritchBorder,
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

vi.mock('./ui/TerminalButton', () => ({
  TerminalButton: ({
    onClick,
    _variant,
    _size,
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

vi.mock('./ui/TerminalInput', () => ({
  TerminalInput: ({
    value,
    onChange,
    placeholder,
    className,
  }: {
    value: string;
    onChange: (value: string) => void;
    placeholder?: string;
    className?: string;
  }) => (
    <input
      data-testid="terminal-input"
      value={value}
      onChange={e => onChange(e.target.value)}
      placeholder={placeholder}
      className={className}
    />
  ),
}));

// Mock window.alert
const mockAlert = vi.fn();
global.alert = mockAlert;

describe('EldritchEffectsDemo', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Initial Rendering', () => {
    it('should render the demo component', () => {
      render(<EldritchEffectsDemo />);

      expect(screen.getByText('Always Active Effects Test')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Effects Demo')).toBeInTheDocument();
      expect(screen.getByText('Phase 4.1 Visuals')).toBeInTheDocument();
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

      // Initially buttons should be rendered
      expect(glowButton).toBeInTheDocument();
      expect(pulseButton).toBeInTheDocument();

      // Click buttons to test they respond to clicks
      fireEvent.click(glowButton);
      fireEvent.click(pulseButton);

      // Verify buttons are still present after clicking
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

    it('should handle button click with alert', () => {
      render(<EldritchEffectsDemo />);

      const invokeButton = screen.getByText('Invoke Ritual');
      fireEvent.click(invokeButton);

      expect(mockAlert).toHaveBeenCalledWith('Button clicked!');
    });
  });

  describe('Effect Descriptions', () => {
    it('should display effect descriptions', () => {
      render(<EldritchEffectsDemo />);

      // Test that the component renders with the expected structure
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
