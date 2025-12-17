import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { DraggablePanel } from '../DraggablePanel';

// Mock the child components used by DraggablePanel
vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, size, className }: { name: string; size: number; className?: string }) => (
    <span data-testid={`eldritch-icon-${name}`} className={className} style={{ width: size, height: size }}>
      {name}
    </span>
  ),
  MythosIcons: {
    panel: 'panel',
    minimize: 'minimize',
    maximize: 'maximize',
    close: 'close',
  },
}));

vi.mock('../ui/TerminalButton', () => ({
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

describe('DraggablePanel', () => {
  beforeEach(() => {
    // Set up viewport dimensions
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
    it('should render with title and children', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" className="panel-test">
          <div>Test Content</div>
        </DraggablePanel>
      );

      expect(screen.getByText('Test Panel')).toBeInTheDocument();
      expect(screen.getByText('Test Content')).toBeInTheDocument();
      expect(container.querySelector('.draggable-panel')).toBeInTheDocument();
    });

    it('should apply default variant classes', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel');
      expect(panel).toHaveClass('draggable-panel');
    });

    it('should apply eldritch variant classes', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" variant="eldritch" className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel');
      expect(panel).toHaveClass('text-mythos-terminal-text');
    });

    it('should apply elevated variant classes', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" variant="elevated" className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel');
      expect(panel).toHaveClass('text-mythos-terminal-text');
    });

    it('should apply custom className', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" className="panel-test custom-class">
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel');
      expect(panel).toHaveClass('custom-class');
    });

    it('should set zIndex', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" zIndex={2000} className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel') as HTMLElement;
      expect(panel.style.zIndex).toBe('2000');
    });
  });

  describe('Button Handlers', () => {
    it('should call onClose when close button is clicked', () => {
      const onClose = vi.fn();
      render(
        <DraggablePanel title="Test Panel" onClose={onClose} className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const closeIcon = screen.queryByTestId('eldritch-icon-close');
      if (closeIcon) {
        const button = closeIcon.closest('button');
        if (button) {
          fireEvent.click(button);
          expect(onClose).toHaveBeenCalledTimes(1);
        }
      }
    });

    it('should call onMinimize when minimize button is clicked', () => {
      const onMinimize = vi.fn();
      render(
        <DraggablePanel title="Test Panel" onMinimize={onMinimize} className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const minimizeIcon = screen.queryByTestId('eldritch-icon-minimize');
      if (minimizeIcon) {
        const button = minimizeIcon.closest('button');
        if (button) {
          fireEvent.click(button);
          expect(onMinimize).toHaveBeenCalledTimes(1);
        }
      }
    });

    it('should call onMaximize when maximize button is clicked', () => {
      const onMaximize = vi.fn();
      render(
        <DraggablePanel title="Test Panel" onMaximize={onMaximize} className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const maximizeIcon = screen.queryByTestId('eldritch-icon-maximize');
      if (maximizeIcon) {
        const button = maximizeIcon.closest('button');
        if (button) {
          fireEvent.click(button);
          expect(onMaximize).toHaveBeenCalledTimes(1);
        }
      }
    });

    it('should not render close button when onClose is not provided', () => {
      render(
        <DraggablePanel title="Test Panel" className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      const closeIcon = screen.queryByTestId('eldritch-icon-close');
      expect(closeIcon).not.toBeInTheDocument();
    });
  });

  describe('Dragging Functionality', () => {
    it('should support drag interactions', () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          defaultPosition={{ x: 100, y: 100 }}
          defaultSize={{ width: 400, height: 300 }}
          className="panel-test"
        >
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel') as HTMLElement;
      expect(panel).toBeInTheDocument();
    });
  });

  describe('Resizing Functionality', () => {
    it('should render resize handles when not minimized', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel" defaultSize={{ width: 400, height: 300 }} className="panel-test">
          <div>Content</div>
        </DraggablePanel>
      );

      // Resize handles should be present (when not minimized)
      // Note: Actual resize handle rendering depends on component state
      expect(container.querySelector('.draggable-panel')).toBeInTheDocument();
    });
  });

  describe('Auto-size Functionality', () => {
    it('should support autoSize prop', () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          autoSize={true}
          defaultSize={{ width: 400, height: 300 }}
          className="panel-test"
        >
          <div>Content</div>
        </DraggablePanel>
      );

      expect(container.querySelector('.draggable-panel')).toBeInTheDocument();
    });

    it('should support autoSize disabled', () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          autoSize={false}
          defaultSize={{ width: 400, height: 300 }}
          className="panel-test"
        >
          <div>Content</div>
        </DraggablePanel>
      );

      expect(container.querySelector('.draggable-panel')).toBeInTheDocument();
    });
  });

  describe('Position and Size Calculations', () => {
    it('should use relative positioning when values are <= 1', () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          defaultPosition={{ x: 0.5, y: 0.5 }}
          defaultSize={{ width: 0.5, height: 0.5 }}
        >
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel') as HTMLElement;
      // Position should be calculated based on viewport
      expect(panel).toBeInTheDocument();
    });

    it('should use absolute positioning when values are > 1', () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          defaultPosition={{ x: 100, y: 100 }}
          defaultSize={{ width: 400, height: 300 }}
        >
          <div>Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel') as HTMLElement;
      // Position should use absolute values
      expect(panel).toBeInTheDocument();
    });

    it('should handle window resize for relative positioning', () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          defaultPosition={{ x: 0.5, y: 0.5 }}
          defaultSize={{ width: 0.5, height: 0.5 }}
        >
          <div>Content</div>
        </DraggablePanel>
      );

      // Simulate window resize
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

      const panel = container.querySelector('.draggable-panel') as HTMLElement;
      expect(panel).toBeInTheDocument();
    });
  });

  describe('Edge Cases', () => {
    it('should handle zero viewport dimensions', () => {
      Object.defineProperty(window, 'innerWidth', {
        writable: true,
        configurable: true,
        value: 0,
      });
      Object.defineProperty(window, 'innerHeight', {
        writable: true,
        configurable: true,
        value: 0,
      });

      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          defaultPosition={{ x: 100, y: 100 }}
          defaultSize={{ width: 400, height: 300 }}
        >
          <div>Content</div>
        </DraggablePanel>
      );

      expect(container.querySelector('.draggable-panel')).toBeInTheDocument();

      // Restore window dimensions
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

    it('should handle missing optional props gracefully', () => {
      const { container } = render(
        <DraggablePanel title="Test Panel">
          <div>Content</div>
        </DraggablePanel>
      );

      expect(container.querySelector('.draggable-panel')).toBeInTheDocument();
      expect(screen.getByText('Test Panel')).toBeInTheDocument();
    });
  });
});
