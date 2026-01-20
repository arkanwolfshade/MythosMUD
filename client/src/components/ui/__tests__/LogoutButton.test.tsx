import { fireEvent, render, screen } from '@testing-library/react';
import { vi } from 'vitest';
import { LogoutButton } from '../LogoutButton';

// Mock the EldritchIcon component
vi.mock('../EldritchIcon', () => ({
  EldritchIcon: ({
    name,
    size,
    variant,
    className,
  }: {
    name: string;
    size?: number;
    variant?: string;
    className?: string;
  }) => (
    <div data-testid={`icon-${name}`} data-size={size} data-variant={variant} className={className}>
      {name}
    </div>
  ),
  MythosIcons: {
    portal: 'portal',
    exit: 'exit',
  },
}));

describe('LogoutButton', () => {
  const defaultProps = {
    onLogout: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Rendering', () => {
    it('renders the logout button with correct text and icon', () => {
      render(<LogoutButton {...defaultProps} />);

      expect(screen.getByRole('button', { name: /exit the realm/i })).toBeInTheDocument();
      expect(screen.getByText('Exit the Realm')).toBeInTheDocument();
      expect(screen.getByTestId('icon-portal')).toBeInTheDocument();
    });

    it('renders with eldritch styling classes', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveClass('font-mono');
      expect(button).toHaveClass('border');
      expect(button).toHaveClass('rounded');
      expect(button).toHaveClass('transition-eldritch');
      expect(button).toHaveClass('duration-eldritch');
      expect(button).toHaveClass('ease-eldritch');
    });

    it('renders with danger variant styling', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveClass('bg-mythos-terminal-surface');
      expect(button).toHaveClass('border-mythos-terminal-error');
      expect(button).toHaveClass('text-mythos-terminal-error');
    });

    it('renders with portal icon and correct properties', () => {
      render(<LogoutButton {...defaultProps} />);

      const icon = screen.getByTestId('icon-portal');
      expect(icon).toBeInTheDocument();
      expect(icon).toHaveAttribute('data-size', '16');
      expect(icon).toHaveAttribute('data-variant', 'error');
    });
  });

  describe('Interactions', () => {
    it('calls onLogout when clicked', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} />);

      const button = screen.getByRole('button');
      fireEvent.click(button);

      expect(onLogout).toHaveBeenCalledTimes(1);
    });

    it('is not disabled by default', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).not.toBeDisabled();
    });

    it('can be disabled when disabled prop is true', () => {
      render(<LogoutButton {...defaultProps} disabled={true} />);

      const button = screen.getByRole('button');
      expect(button).toBeDisabled();
    });

    it('does not call onLogout when disabled and clicked', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} disabled={true} />);

      const button = screen.getByRole('button');
      fireEvent.click(button);

      expect(onLogout).not.toHaveBeenCalled();
    });
  });

  describe('Accessibility', () => {
    it('has correct ARIA label', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveAttribute('aria-label', 'Exit the realm and return to login screen');
    });

    it('has correct title attribute', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveAttribute('title', 'Exit the realm and return to login screen (Ctrl+Q)');
    });

    it('is focusable via keyboard', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      button.focus();
      expect(button).toHaveFocus();
    });

    it('has focus ring styling for keyboard navigation', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveClass('focus:outline-hidden');
      expect(button).toHaveClass('focus:ring-2');
      expect(button).toHaveClass('focus:ring-offset-2');
      expect(button).toHaveClass('focus:ring-mythos-terminal-error');
    });

    it('responds to keyboard activation (Enter key)', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} />);

      const button = screen.getByRole('button');
      button.focus();
      fireEvent.keyDown(button, { key: 'Enter', code: 'Enter' });

      expect(onLogout).toHaveBeenCalledTimes(1);
    });

    it('responds to keyboard activation (Space key)', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} />);

      const button = screen.getByRole('button');
      button.focus();
      fireEvent.keyDown(button, { key: ' ', code: 'Space' });

      expect(onLogout).toHaveBeenCalledTimes(1);
    });
  });

  describe('Keyboard Shortcut', () => {
    it('sets up Ctrl+Q keyboard shortcut on mount', () => {
      const addEventListenerSpy = vi.spyOn(document, 'addEventListener');
      render(<LogoutButton {...defaultProps} />);

      expect(addEventListenerSpy).toHaveBeenCalledWith('keydown', expect.any(Function));
    });

    it('calls onLogout when Ctrl+Q is pressed', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} />);

      fireEvent.keyDown(document, { key: 'q', code: 'KeyQ', ctrlKey: true });

      expect(onLogout).toHaveBeenCalledTimes(1);
    });

    it('does not call onLogout when Q is pressed without Ctrl', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} />);

      fireEvent.keyDown(document, { key: 'q', code: 'KeyQ', ctrlKey: false });

      expect(onLogout).not.toHaveBeenCalled();
    });

    it('does not call onLogout when other keys are pressed with Ctrl', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} />);

      fireEvent.keyDown(document, { key: 'w', code: 'KeyW', ctrlKey: true });

      expect(onLogout).not.toHaveBeenCalled();
    });

    it('cleans up keyboard shortcut listener on unmount', () => {
      const removeEventListenerSpy = vi.spyOn(document, 'removeEventListener');
      const { unmount } = render(<LogoutButton {...defaultProps} />);

      unmount();

      expect(removeEventListenerSpy).toHaveBeenCalledWith('keydown', expect.any(Function));
    });
  });

  describe('Visual States', () => {
    it('shows hover effects', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveClass('hover:bg-mythos-terminal-error');
      expect(button).toHaveClass('hover:text-mythos-terminal-background');
      expect(button).toHaveClass('hover:animate-eldritch-glow');
    });

    it('shows disabled state styling', () => {
      render(<LogoutButton {...defaultProps} disabled={true} />);

      const button = screen.getByRole('button');
      expect(button).toHaveClass('opacity-50');
      expect(button).toHaveClass('cursor-not-allowed');
      expect(button).toHaveClass('hover:animate-none');
    });

    it('shows active state styling', () => {
      render(<LogoutButton {...defaultProps} />);

      const button = screen.getByRole('button');
      expect(button).toHaveClass('hover:animate-eldritch-scale');
    });
  });

  describe('Loading State', () => {
    it('shows loading state when isLoggingOut is true', () => {
      render(<LogoutButton {...defaultProps} isLoggingOut={true} />);

      const button = screen.getByRole('button');
      expect(button).toBeDisabled();
      expect(screen.getByText('Exiting...')).toBeInTheDocument();
      expect(screen.queryByText('Exit the Realm')).not.toBeInTheDocument();
    });

    it('does not call onLogout when in loading state and clicked', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} isLoggingOut={true} />);

      const button = screen.getByRole('button');
      fireEvent.click(button);

      expect(onLogout).not.toHaveBeenCalled();
    });

    it('does not respond to Ctrl+Q when in loading state', () => {
      const onLogout = vi.fn();
      render(<LogoutButton onLogout={onLogout} isLoggingOut={true} />);

      fireEvent.keyDown(document, { key: 'q', code: 'KeyQ', ctrlKey: true });

      expect(onLogout).not.toHaveBeenCalled();
    });
  });
});
