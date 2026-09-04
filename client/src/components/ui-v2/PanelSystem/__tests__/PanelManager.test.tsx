/**
 * Tests for PanelManager component and hook.
 */

import '@testing-library/jest-dom/vitest';
import { act, render, renderHook, screen } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { PanelManager } from '../../../../components/PanelManager';
import type { PanelState } from '../../types';
import { PanelManagerProvider } from '../PanelManager';
import { usePanelManager } from '../usePanelManager';

function panelStateFixture(id: string, z: number): PanelState {
  return {
    id,
    title: id,
    position: { x: 50, y: 50 },
    size: { width: 320, height: 240 },
    zIndex: z,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
  };
}

// Mock localStorage
const localStorageMock = (() => {
  let store: Record<string, string> = {};

  return {
    getItem: (key: string) => store[key] || null,
    setItem: (key: string, value: string) => {
      store[key] = value.toString();
    },
    removeItem: (key: string) => {
      delete store[key];
    },
    clear: () => {
      store = {};
    },
  };
})();

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock,
});

describe('PanelManager', () => {
  beforeEach(() => {
    localStorageMock.clear();
    vi.clearAllMocks();
  });

  describe('Component Rendering', () => {
    it('should render children', () => {
      render(
        <PanelManager>
          <div data-testid="child">Child Content</div>
        </PanelManager>
      );

      expect(screen.getByTestId('child')).toBeInTheDocument();
      expect(screen.getByText('Child Content')).toBeInTheDocument();
    });

    it('should render multiple children', () => {
      render(
        <PanelManager>
          <div data-testid="child1">Child 1</div>
          <div data-testid="child2">Child 2</div>
        </PanelManager>
      );

      expect(screen.getByTestId('child1')).toBeInTheDocument();
      expect(screen.getByTestId('child2')).toBeInTheDocument();
    });

    it('should have proper CSS classes', () => {
      const { container } = render(
        <PanelManager>
          <div>Test</div>
        </PanelManager>
      );

      const manager = container.firstChild as HTMLElement;
      expect(manager).toHaveClass('h-full', 'w-full');
    });

    it('should render with no children', () => {
      const { container } = render(<PanelManager>{null}</PanelManager>);
      expect(container.firstChild).toBeInTheDocument();
    });
  });

  describe('usePanelManager Hook', () => {
    const defaultPanels: Record<string, PanelState> = {};

    const wrapper = ({ children }: { children: React.ReactNode }) => (
      <PanelManagerProvider defaultPanels={defaultPanels}>{children}</PanelManagerProvider>
    );

    it('should initialize with empty panels', () => {
      const { result } = renderHook(() => usePanelManager(), { wrapper });

      expect(result.current.panels).toEqual({});
    });

    it('should initialize panels from localStorage', () => {
      const savedPanels: Record<string, PanelState> = {
        panel1: {
          id: 'panel1',
          title: 'Panel 1',
          position: { x: 100, y: 100 },
          size: { width: 400, height: 300 },
          zIndex: 1000,
          isMinimized: false,
          isMaximized: false,
          isVisible: true,
        },
      };

      localStorageMock.setItem('mythosmud-ui-v2-panel-layout', JSON.stringify(savedPanels));

      const { result } = renderHook(() => usePanelManager(), { wrapper });

      // Wait for useEffect to run
      act(() => {
        // Force a re-render to trigger useEffect
      });

      expect(result.current.panels).toHaveProperty('panel1');
      expect(result.current.panels.panel1.position).toEqual({ x: 100, y: 100 });
    });

    it('should clamp oversized stored layout to viewport and persist', () => {
      const savedPanels: Record<string, PanelState> = {
        panel1: {
          id: 'panel1',
          title: 'Panel 1',
          position: { x: 0, y: 0 },
          size: { width: 2000, height: 400 },
          zIndex: 1000,
          isMinimized: false,
          isMaximized: false,
          isVisible: true,
        },
      };

      localStorageMock.setItem('mythosmud-ui-v2-panel-layout', JSON.stringify(savedPanels));

      const innerSpy = vi.spyOn(window, 'innerWidth', 'get').mockReturnValue(800);
      const innerHSpy = vi.spyOn(window, 'innerHeight', 'get').mockReturnValue(600);

      const { result } = renderHook(() => usePanelManager(), { wrapper });

      act(() => {});

      expect(result.current.panels.panel1.size.width).toBeLessThanOrEqual(800);
      const raw = localStorageMock.getItem('mythosmud-ui-v2-panel-layout');
      expect(raw).toBeTruthy();
      const persisted = JSON.parse(raw as string) as Record<string, PanelState>;
      expect(persisted.panel1.size.width).toBe(result.current.panels.panel1.size.width);

      innerSpy.mockRestore();
      innerHSpy.mockRestore();
    });

    it('should persist z-index when focusing a panel', () => {
      const twoPanels: Record<string, PanelState> = {
        a: panelStateFixture('a', 1000),
        b: panelStateFixture('b', 1001),
      };

      const wrapperTwo = ({ children }: { children: React.ReactNode }) => (
        <PanelManagerProvider defaultPanels={twoPanels}>{children}</PanelManagerProvider>
      );

      const { result } = renderHook(() => usePanelManager(), { wrapper: wrapperTwo });

      act(() => {});

      act(() => {
        result.current.focusPanel('a');
      });

      const raw = localStorageMock.getItem('mythosmud-ui-v2-panel-layout');
      expect(raw).toBeTruthy();
      const persisted = JSON.parse(raw as string) as Record<string, PanelState>;
      expect(persisted.a.zIndex).toBeGreaterThan(persisted.b.zIndex);
    });

    it('should handle corrupted localStorage data gracefully', () => {
      localStorageMock.setItem('mythosmud-ui-v2-panel-layout', 'invalid-json');

      // Suppress expected console.warn from loadPanelLayout catch (invalid JSON)
      const warnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

      const { result } = renderHook(() => usePanelManager(), { wrapper });

      // Should initialize with default panels (empty in this case)
      act(() => {
        // Wait for useEffect
      });
      expect(result.current.panels).toEqual({});

      warnSpy.mockRestore();
    });

    it('should reject valid JSON with invalid panel shape and use default panels', () => {
      // Valid JSON but missing required PanelState fields (e.g. title, size)
      localStorageMock.setItem('mythosmud-ui-v2-panel-layout', JSON.stringify({ panel1: { id: 'panel1' } }));

      const warnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

      const { result } = renderHook(() => usePanelManager(), { wrapper });

      act(() => {});

      expect(result.current.panels).toEqual({});
      expect(warnSpy).toHaveBeenCalledWith('Invalid panel layout in localStorage');

      warnSpy.mockRestore();
    });

    it('should update panel position', () => {
      const panelsWithPanel1: Record<string, PanelState> = {
        panel1: {
          id: 'panel1',
          title: 'Panel 1',
          position: { x: 100, y: 100 },
          size: { width: 400, height: 300 },
          zIndex: 1000,
          isMinimized: false,
          isMaximized: false,
          isVisible: true,
        },
      };

      const wrapperWithPanels = ({ children }: { children: React.ReactNode }) => (
        <PanelManagerProvider defaultPanels={panelsWithPanel1}>{children}</PanelManagerProvider>
      );

      const { result } = renderHook(() => usePanelManager(), { wrapper: wrapperWithPanels });

      act(() => {
        // Wait for initialization
      });

      act(() => {
        result.current.updatePosition('panel1', { x: 200, y: 200 });
      });

      expect(result.current.panels.panel1.position).toEqual({ x: 200, y: 200 });
      expect(localStorageMock.getItem('mythosmud-ui-v2-panel-layout')).toBeTruthy();
    });

    it('should not update position for non-existent panel', () => {
      const { result } = renderHook(() => usePanelManager(), { wrapper });

      act(() => {
        result.current.updatePosition('non-existent', { x: 200, y: 200 });
      });

      expect(result.current.panels).not.toHaveProperty('non-existent');
    });

    it('should not update size for non-existent panel', () => {
      const { result } = renderHook(() => usePanelManager(), { wrapper });

      act(() => {
        result.current.updateSize('non-existent', { width: 500, height: 400 });
      });

      expect(result.current.panels).not.toHaveProperty('non-existent');
    });
  });
});
