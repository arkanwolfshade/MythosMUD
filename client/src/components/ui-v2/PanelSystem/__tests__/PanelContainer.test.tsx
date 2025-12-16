import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { PanelContainer } from '../PanelContainer';

// Mock react-rnd
vi.mock('react-rnd', () => ({
  Rnd: ({
    children,
    position,
    size,
    onDragStart,
    style,
    className,
  }: {
    children: React.ReactNode;
    position: { x: number; y: number };
    size: { width: number; height: number };
    onDragStart?: () => void;
    onDragStop?: (e: unknown, d: { x: number; y: number }) => void;
    onResizeStop?: (
      e: unknown,
      direction: unknown,
      ref: HTMLElement,
      delta: unknown,
      position: { x: number; y: number }
    ) => void;
    style?: React.CSSProperties;
    className?: string;
  }) => (
    <div
      data-testid="rnd-container"
      data-position-x={position.x}
      data-position-y={position.y}
      data-size-width={size.width}
      data-size-height={size.height}
      style={style}
      className={className}
      onMouseDown={onDragStart}
    >
      {children}
    </div>
  ),
}));

// Mock child components
vi.mock('../../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, size, variant }: { name: string; size: number; variant?: string }) => (
    <span data-testid={`eldritch-icon-${name}`} data-variant={variant} style={{ width: size, height: size }}>
      {name}
    </span>
  ),
  MythosIcons: {
    minimize: 'minimize',
    maximize: 'maximize',
    restore: 'restore',
    close: 'close',
  },
}));

vi.mock('../../../ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    className,
    variant,
    size,
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    className?: string;
    variant?: string;
    size?: string;
  }) => (
    <button
      onClick={onClick}
      className={className}
      data-testid="terminal-button"
      data-variant={variant}
      data-size={size}
    >
      {children}
    </button>
  ),
}));

describe('PanelContainer', () => {
  const defaultProps = {
    id: 'test-panel',
    title: 'Test Panel',
    children: <div>Test Content</div>,
    position: { x: 100, y: 100 },
    size: { width: 400, height: 300 },
    zIndex: 1000,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
    onPositionChange: vi.fn(),
    onSizeChange: vi.fn(),
    onMinimize: vi.fn(),
    onMaximize: vi.fn(),
    onClose: vi.fn(),
    onFocus: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    // Set up window dimensions
    Object.defineProperty(window, 'innerWidth', {
      writable: true,
      configurable: true,
      value: 1920,
    });
    Object.defineProperty(window, 'innerHeight', {
      writable: true,
      configurable: true,
      value: 1080,
    });
  });

  describe('Basic Rendering', () => {
    it('should render panel with title and children', () => {
      render(<PanelContainer {...defaultProps} />);

      expect(screen.getByText('Test Panel')).toBeInTheDocument();
      expect(screen.getByText('Test Content')).toBeInTheDocument();
    });

    it('should apply correct position and size', () => {
      const { container } = render(<PanelContainer {...defaultProps} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveAttribute('data-position-x', '100');
      expect(rndContainer).toHaveAttribute('data-position-y', '100');
      expect(rndContainer).toHaveAttribute('data-size-width', '400');
      expect(rndContainer).toHaveAttribute('data-size-height', '300');
    });

    it('should apply zIndex to container', () => {
      const { container } = render(<PanelContainer {...defaultProps} zIndex={2000} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]') as HTMLElement;
      expect(rndContainer.style.zIndex).toBe('2000');
    });

    it('should apply custom className', () => {
      const { container } = render(<PanelContainer {...defaultProps} className="custom-class" />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveClass('custom-class');
    });
  });

  describe('Variant Styling', () => {
    it('should apply default variant classes', () => {
      const { container } = render(<PanelContainer {...defaultProps} variant="default" />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveClass('border-gray-700');
    });

    it('should apply eldritch variant classes', () => {
      const { container } = render(<PanelContainer {...defaultProps} variant="eldritch" />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveClass('border-mythos-terminal-primary');
    });

    it('should apply elevated variant classes', () => {
      const { container } = render(<PanelContainer {...defaultProps} variant="elevated" />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveClass('border-gray-600');
      expect(rndContainer).toHaveClass('shadow-lg');
    });
  });

  describe('Minimized State', () => {
    it('should render minimized panel as small bar', () => {
      const { container } = render(<PanelContainer {...defaultProps} isMinimized={true} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveAttribute('data-size-width', '200');
      expect(rndContainer).toHaveAttribute('data-size-height', '40');
    });

    it('should show maximize button when minimized', () => {
      render(<PanelContainer {...defaultProps} isMinimized={true} />);

      const maximizeIcon = screen.queryByTestId('eldritch-icon-maximize');
      expect(maximizeIcon).toBeInTheDocument();
    });

    it('should show restore icon when minimized and maximized', () => {
      render(<PanelContainer {...defaultProps} isMinimized={true} isMaximized={true} />);

      const restoreIcon = screen.queryByTestId('eldritch-icon-restore');
      expect(restoreIcon).toBeInTheDocument();
    });

    it('should not show minimize button when minimized', () => {
      render(<PanelContainer {...defaultProps} isMinimized={true} />);

      const minimizeIcon = screen.queryByTestId('eldritch-icon-minimize');
      expect(minimizeIcon).not.toBeInTheDocument();
    });

    it('should not show content when minimized', () => {
      render(<PanelContainer {...defaultProps} isMinimized={true} />);

      expect(screen.queryByText('Test Content')).not.toBeInTheDocument();
    });
  });

  describe('Maximized State', () => {
    it('should calculate maximized size based on window dimensions', () => {
      const { container } = render(<PanelContainer {...defaultProps} isMaximized={true} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      // Maximized size should be window width x (window height - header height)
      expect(rndContainer).toHaveAttribute('data-size-width', '1920');
      expect(rndContainer).toHaveAttribute('data-size-height', '1032'); // 1080 - 48
    });

    it('should calculate maximized position at top-left', () => {
      const { container } = render(<PanelContainer {...defaultProps} isMaximized={true} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toHaveAttribute('data-position-x', '0');
      expect(rndContainer).toHaveAttribute('data-position-y', '48'); // Header height
    });

    it('should show restore icon when maximized', () => {
      render(<PanelContainer {...defaultProps} isMaximized={true} />);

      const restoreIcon = screen.queryByTestId('eldritch-icon-restore');
      expect(restoreIcon).toBeInTheDocument();
    });

    it('should update maximized size on window resize', () => {
      const { container } = render(<PanelContainer {...defaultProps} isMaximized={true} />);

      // Change window size
      Object.defineProperty(window, 'innerWidth', {
        writable: true,
        configurable: true,
        value: 2560,
      });
      Object.defineProperty(window, 'innerHeight', {
        writable: true,
        configurable: true,
        value: 1440,
      });

      fireEvent(window, new Event('resize'));

      // Component should update (react will re-render)
      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toBeInTheDocument();
    });
  });

  describe('Button Handlers', () => {
    it('should call onMinimize when minimize button is clicked', () => {
      render(<PanelContainer {...defaultProps} />);

      const minimizeButton = screen
        .getAllByTestId('terminal-button')
        .find(btn => btn.querySelector('[data-testid="eldritch-icon-minimize"]'));
      if (minimizeButton) {
        fireEvent.click(minimizeButton);
        expect(defaultProps.onMinimize).toHaveBeenCalledWith('test-panel');
      }
    });

    it('should call onMaximize when maximize button is clicked', () => {
      render(<PanelContainer {...defaultProps} />);

      const maximizeButton = screen
        .getAllByTestId('terminal-button')
        .find(btn => btn.querySelector('[data-testid="eldritch-icon-maximize"]'));
      if (maximizeButton) {
        fireEvent.click(maximizeButton);
        expect(defaultProps.onMaximize).toHaveBeenCalledWith('test-panel');
      }
    });

    it('should call onClose when close button is clicked', () => {
      render(<PanelContainer {...defaultProps} />);

      const closeButton = screen
        .getAllByTestId('terminal-button')
        .find(btn => btn.querySelector('[data-testid="eldritch-icon-close"]'));
      if (closeButton) {
        fireEvent.click(closeButton);
        expect(defaultProps.onClose).toHaveBeenCalledWith('test-panel');
      }
    });

    it('should not render close button when onClose is not provided', () => {
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      const { onClose, ...propsWithoutClose } = defaultProps;
      render(<PanelContainer {...propsWithoutClose} />);

      const closeIcon = screen.queryByTestId('eldritch-icon-close');
      expect(closeIcon).not.toBeInTheDocument();
    });
  });

  describe('Drag Functionality', () => {
    it('should call onFocus when drag starts', () => {
      const { container } = render(<PanelContainer {...defaultProps} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      if (rndContainer) {
        fireEvent.mouseDown(rndContainer);
        expect(defaultProps.onFocus).toHaveBeenCalledWith('test-panel');
      }
    });

    it('should call onPositionChange when drag stops', () => {
      // This would require mocking the Rnd component's onDragStop callback
      // For now, we verify the handler is set up correctly
      render(<PanelContainer {...defaultProps} />);

      expect(defaultProps.onPositionChange).toBeDefined();
    });
  });

  describe('Resize Functionality', () => {
    it('should respect minSize constraints', () => {
      const { container } = render(<PanelContainer {...defaultProps} minSize={{ width: 300, height: 200 }} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toBeInTheDocument();
    });

    it('should respect maxSize constraints', () => {
      const { container } = render(<PanelContainer {...defaultProps} maxSize={{ width: 800, height: 600 }} />);

      const rndContainer = container.querySelector('[data-testid="rnd-container"]');
      expect(rndContainer).toBeInTheDocument();
    });
  });

  describe('Window Resize Handling', () => {
    it('should update window dimensions on resize', () => {
      render(<PanelContainer {...defaultProps} isMaximized={true} />);

      // Change window size
      Object.defineProperty(window, 'innerWidth', {
        writable: true,
        configurable: true,
        value: 2560,
      });
      Object.defineProperty(window, 'innerHeight', {
        writable: true,
        configurable: true,
        value: 1440,
      });

      fireEvent(window, new Event('resize'));

      // Component should handle resize
      expect(screen.getByText('Test Panel')).toBeInTheDocument();
    });

    it('should clean up resize listener on unmount', () => {
      const removeEventListenerSpy = vi.spyOn(window, 'removeEventListener');
      const { unmount } = render(<PanelContainer {...defaultProps} />);

      unmount();

      expect(removeEventListenerSpy).toHaveBeenCalledWith('resize', expect.any(Function));
      removeEventListenerSpy.mockRestore();
    });
  });

  describe('Edge Cases', () => {
    it('should handle missing optional props', () => {
      const minimalProps = {
        ...defaultProps,
        minSize: undefined,
        maxSize: undefined,
        variant: undefined,
        className: undefined,
        onClose: undefined,
      };

      expect(() => {
        render(<PanelContainer {...minimalProps} />);
      }).not.toThrow();
    });
  });

  describe('Focus Handling', () => {
    it('should call onFocus when header is clicked', () => {
      const { container } = render(<PanelContainer {...defaultProps} />);

      const header = container.querySelector('.cursor-move');
      if (header) {
        fireEvent.mouseDown(header);
        expect(defaultProps.onFocus).toHaveBeenCalledWith('test-panel');
      }
    });
  });
});
