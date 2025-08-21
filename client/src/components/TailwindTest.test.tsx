import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { describe, expect, it, vi } from 'vitest';
import { TailwindTest } from './TailwindTest';

// Mock the child components
vi.mock('./ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, variant, size }: { name: string; variant: string; size: number }) => (
    <div data-testid={`eldritch-icon-${name}`} className={`variant-${variant} size-${size}`}>
      Icon: {name}
    </div>
  ),
  MythosIcons: {
    connection: 'connection',
    disconnected: 'disconnected',
    connecting: 'connecting',
    look: 'look',
    chat: 'chat',
    attack: 'attack',
    inventory: 'inventory',
    character: 'character',
    room: 'room',
    eldritch: 'eldritch',
    horror: 'horror',
    help: 'help',
  },
}));

vi.mock('./ui/MythosPanel', () => ({
  MythosPanel: ({
    title,
    subtitle,
    children,
    variant,
    size,
  }: {
    title: string;
    subtitle?: string;
    children: React.ReactNode;
    variant?: string;
    size?: string;
    _showEldritchBorder?: boolean;
  }) => (
    <div data-testid="mythos-panel" className={`variant-${variant} size-${size}`}>
      <h2>{title}</h2>
      {subtitle && <h3>{subtitle}</h3>}
      {children}
    </div>
  ),
}));

vi.mock('./ui/TerminalButton', () => ({
  TerminalButton: ({
    variant,
    size,
    disabled,
    children,
  }: {
    variant?: string;
    size?: string;
    disabled?: boolean;
    children: React.ReactNode;
  }) => (
    <button data-testid="terminal-button" className={`variant-${variant} size-${size}`} disabled={disabled}>
      {children}
    </button>
  ),
}));

vi.mock('./ui/TerminalCard', () => ({
  TerminalCard: ({ title, variant, children }: { title: string; variant?: string; children: React.ReactNode }) => (
    <div data-testid="terminal-card" className={`variant-${variant}`}>
      <h3>{title}</h3>
      {children}
    </div>
  ),
}));

vi.mock('./ui/TerminalInput', () => ({
  TerminalInput: ({
    value,
    onChange,
    placeholder,
    type,
    disabled,
    size,
  }: {
    value: string;
    onChange: (value: string) => void;
    placeholder?: string;
    type?: string;
    disabled?: boolean;
    size?: string;
  }) => (
    <input
      data-testid="terminal-input"
      value={value}
      onChange={e => onChange(e.target.value)}
      placeholder={placeholder}
      type={type}
      disabled={disabled}
      className={`size-${size}`}
    />
  ),
}));

describe('TailwindTest', () => {
  describe('Initial Rendering', () => {
    it('should render the main title and description', () => {
      render(<TailwindTest />);

      expect(screen.getByText('MythosMUD Interface')).toBeInTheDocument();
      expect(screen.getByText('Enhanced TailwindCSS Components with Eldritch Aesthetics')).toBeInTheDocument();
    });

    it('should render all panel sections', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Enhanced Terminal Components')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Icons')).toBeInTheDocument();
      expect(screen.getByText('Color Palette & Typography')).toBeInTheDocument();
      expect(screen.getByText('Animations & Effects')).toBeInTheDocument();
    });

    it('should render panel variants', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Default Panel')).toBeInTheDocument();
      expect(screen.getByText('Elevated Panel')).toBeInTheDocument();
      expect(screen.getByText('Outlined Panel')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Panel')).toBeInTheDocument();
    });
  });

  describe('Button Components', () => {
    it('should render buttons with different variants and sizes', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Small Primary')).toBeInTheDocument();
      expect(screen.getByText('Medium Secondary')).toBeInTheDocument();
      expect(screen.getByText('Large Danger')).toBeInTheDocument();
      expect(screen.getByText('Disabled Button')).toBeInTheDocument();
    });

    it('should render interactive buttons', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Hover Me')).toBeInTheDocument();
      expect(screen.getByText('Focus Me')).toBeInTheDocument();
    });
  });

  describe('Input Components', () => {
    it('should render input fields with different configurations', () => {
      render(<TailwindTest />);

      const inputs = screen.getAllByTestId('terminal-input');
      expect(inputs).toHaveLength(3);

      expect(screen.getByPlaceholderText('Enter command...')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Disabled input')).toBeInTheDocument();
    });

    it('should handle input value changes', () => {
      render(<TailwindTest />);

      const commandInput = screen.getByPlaceholderText('Enter command...');
      fireEvent.change(commandInput, { target: { value: 'test command' } });

      expect(commandInput).toHaveValue('test command');
    });

    it('should handle password input changes', () => {
      render(<TailwindTest />);

      const passwordInput = screen.getByPlaceholderText('Password');
      fireEvent.change(passwordInput, { target: { value: 'secret123' } });

      expect(passwordInput).toHaveValue('secret123');
    });
  });

  describe('Icon Components', () => {
    it('should render eldritch icons', () => {
      render(<TailwindTest />);

      expect(screen.getByTestId('eldritch-icon-connection')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-disconnected')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-connecting')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-look')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-chat')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-attack')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-inventory')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-character')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-room')).toBeInTheDocument();
      // Use getAllByTestId for eldritch icon since there are multiple instances
      const eldritchIcons = screen.getAllByTestId('eldritch-icon-eldritch');
      expect(eldritchIcons).toHaveLength(2);
      expect(screen.getByTestId('eldritch-icon-horror')).toBeInTheDocument();
      expect(screen.getByTestId('eldritch-icon-help')).toBeInTheDocument();
    });
  });

  describe('Typography and Colors', () => {
    it('should render typography examples', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Heading 1')).toBeInTheDocument();
      expect(screen.getByText('Heading 2')).toBeInTheDocument();
      expect(screen.getByText('Heading 3')).toBeInTheDocument();
      expect(
        screen.getByText('Regular text in the MythosMUD terminal style. The font should be Courier New (monospace).')
      ).toBeInTheDocument();
      expect(screen.getByText('Secondary text with a slightly different color for hierarchy.')).toBeInTheDocument();
      expect(screen.getByText('Error text in red for warnings and alerts.')).toBeInTheDocument();
      expect(screen.getByText('Warning text in orange for cautions.')).toBeInTheDocument();
      expect(screen.getByText('Success text in green for confirmations.')).toBeInTheDocument();
    });

    it('should render color palette', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Primary')).toBeInTheDocument();
      expect(screen.getByText('Secondary')).toBeInTheDocument();
      expect(screen.getByText('Surface')).toBeInTheDocument();
      expect(screen.getByText('Background')).toBeInTheDocument();
      expect(screen.getByText('#00ff00')).toBeInTheDocument();
      expect(screen.getByText('#ff9800')).toBeInTheDocument();
      expect(screen.getByText('#1a1a1a')).toBeInTheDocument();
      expect(screen.getByText('#0a0a0a')).toBeInTheDocument();
    });
  });

  describe('Legacy Components', () => {
    it('should render legacy TerminalCard component', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Legacy TerminalCard Component')).toBeInTheDocument();
      expect(
        screen.getByText(
          'This is the original TerminalCard component for comparison. The new MythosPanel provides enhanced styling and eldritch elements.'
        )
      ).toBeInTheDocument();
    });
  });

  describe('Animation and Effects', () => {
    it('should render animation showcase', () => {
      render(<TailwindTest />);

      expect(screen.getByText('Shimmer Animation')).toBeInTheDocument();
      expect(screen.getByText('The shimmer animation should be visible on the green bar above.')).toBeInTheDocument();
      expect(screen.getByText('Interactive Elements')).toBeInTheDocument();
    });
  });
});
