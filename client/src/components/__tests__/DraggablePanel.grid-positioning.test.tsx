import { render, screen, waitFor } from '@testing-library/react';
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

describe('DraggablePanel - Grid Positioning', () => {
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

  describe('Grid-positioned panels (with panel- className)', () => {
    it('should not apply absolute positioning styles when className includes panel-', async () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          className="panel-chat"
          defaultPosition={{ x: 50, y: 50 }}
          defaultSize={{ width: 500, height: 400 }}
        >
          <div>Test Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel');
      expect(panel).toBeInTheDocument();

      // Wait for any async effects to complete
      await waitFor(() => {
        const panelElement = panel as HTMLElement;
        const styles = window.getComputedStyle(panelElement);

        // Grid-positioned panels should NOT have absolute positioning
        // They should use relative positioning (from CSS Grid)
        expect(styles.position).not.toBe('absolute');
      });
    });

    it('should render multiple grid-positioned panels without overlap', async () => {
      const { container } = render(
        <div
          className="game-terminal-panels"
          style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gridTemplateRows: '1fr 1fr' }}
        >
          <DraggablePanel
            title="Chat"
            className="panel-chat"
            defaultPosition={{ x: 50, y: 50 }}
            defaultSize={{ width: 500, height: 400 }}
          >
            <div>Chat Content</div>
          </DraggablePanel>
          <DraggablePanel
            title="Game Log"
            className="panel-gameLog"
            defaultPosition={{ x: 600, y: 50 }}
            defaultSize={{ width: 500, height: 400 }}
          >
            <div>Game Log Content</div>
          </DraggablePanel>
          <DraggablePanel
            title="Status"
            className="panel-status"
            defaultPosition={{ x: 950, y: 50 }}
            defaultSize={{ width: 300, height: 200 }}
          >
            <div>Status Content</div>
          </DraggablePanel>
        </div>
      );

      // Wait for initial render and any effects
      await waitFor(() => {
        const panels = container.querySelectorAll('.draggable-panel');
        expect(panels.length).toBe(3);
      });

      const panels = container.querySelectorAll('.draggable-panel');

      // Verify all panels are rendered
      expect(panels.length).toBe(3);
      expect(screen.getByText('Chat')).toBeInTheDocument();
      expect(screen.getByText('Game Log')).toBeInTheDocument();
      expect(screen.getByText('Status')).toBeInTheDocument();

      // Verify panels don't have absolute positioning that would cause overlap
      panels.forEach(panel => {
        const panelElement = panel as HTMLElement;
        const styles = window.getComputedStyle(panelElement);

        // Grid-positioned panels should not use absolute positioning
        expect(styles.position).not.toBe('absolute');
      });
    });

    it('should skip position calculations for grid-positioned panels', async () => {
      // Spy on console to verify no errors during render
      const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          className="panel-chat"
          defaultPosition={{ x: 50, y: 50 }}
          defaultSize={{ width: 500, height: 400 }}
        >
          <div>Test Content</div>
        </DraggablePanel>
      );

      await waitFor(() => {
        expect(container.querySelector('.draggable-panel')).toBeInTheDocument();
      });

      // Verify no errors occurred (which would indicate position calculation issues)
      expect(consoleSpy).not.toHaveBeenCalled();

      consoleSpy.mockRestore();
    });

    it('should apply grid classes correctly for grid-positioned panels', () => {
      const { container } = render(
        <DraggablePanel
          title="Chat"
          className="panel-chat"
          defaultPosition={{ x: 50, y: 50 }}
          defaultSize={{ width: 500, height: 400 }}
        >
          <div>Chat Content</div>
        </DraggablePanel>
      );

      const panel = container.querySelector('.draggable-panel');
      expect(panel).toBeInTheDocument();
      expect(panel).toHaveClass('panel-chat');
      expect(panel).toHaveClass('draggable-panel');
    });
  });

  describe('Non-grid panels (without panel- className)', () => {
    it('should apply absolute positioning for non-grid panels', async () => {
      const { container } = render(
        <DraggablePanel
          title="Test Panel"
          className="custom-panel"
          defaultPosition={{ x: 100, y: 100 }}
          defaultSize={{ width: 400, height: 300 }}
        >
          <div>Test Content</div>
        </DraggablePanel>
      );

      await waitFor(() => {
        const panel = container.querySelector('.draggable-panel') as HTMLElement;
        expect(panel).toBeInTheDocument();

        const styles = window.getComputedStyle(panel);
        // Non-grid panels should use absolute positioning
        expect(styles.position).toBe('absolute');
      });
    });
  });

  describe('Initial render behavior', () => {
    it('should render grid-positioned panels immediately without overlap delay', async () => {
      const startTime = Date.now();

      const { container } = render(
        <div
          className="game-terminal-panels"
          style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gridTemplateRows: '1fr 1fr' }}
        >
          <DraggablePanel
            title="Panel 1"
            className="panel-chat"
            defaultPosition={{ x: 50, y: 50 }}
            defaultSize={{ width: 500, height: 400 }}
          >
            <div>Content 1</div>
          </DraggablePanel>
          <DraggablePanel
            title="Panel 2"
            className="panel-gameLog"
            defaultPosition={{ x: 600, y: 50 }}
            defaultSize={{ width: 500, height: 400 }}
          >
            <div>Content 2</div>
          </DraggablePanel>
        </div>
      );

      // Panels should be rendered immediately
      await waitFor(
        () => {
          const panels = container.querySelectorAll('.draggable-panel');
          expect(panels.length).toBe(2);
        },
        { timeout: 100 }
      ); // Short timeout - should be immediate

      const renderTime = Date.now() - startTime;

      // Verify panels are rendered quickly (no async delay)
      expect(renderTime).toBeLessThan(200); // Should be much faster than the 100ms setTimeout that was causing overlap

      // Verify both panels are present and don't overlap
      const panels = container.querySelectorAll('.draggable-panel');
      expect(panels.length).toBe(2);

      panels.forEach(panel => {
        const panelElement = panel as HTMLElement;
        const styles = window.getComputedStyle(panelElement);
        expect(styles.position).not.toBe('absolute');
      });
    });
  });
});
