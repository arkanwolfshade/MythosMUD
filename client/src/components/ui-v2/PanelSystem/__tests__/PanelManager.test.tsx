/**
 * Tests for PanelManager component and hook.
 */

import { act, renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import React from 'react';
import { PanelManager } from '../../../../components/PanelManager';
import { PanelManagerProvider } from '../PanelManager';
import { usePanelManager } from '../usePanelManager';
import type { PanelState } from '../../types';

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

    it('should handle corrupted localStorage data gracefully', () => {
      localStorageMock.setItem('mythosmud-ui-v2-panel-layout', 'invalid-json');

      const { result } = renderHook(() => usePanelManager(), { wrapper });

      // Should initialize with default panels (empty in this case)
      act(() => {
        // Wait for useEffect
      });
      expect(result.current.panels).toEqual({});
    });

    it('should update panel position', () => {
      const panelsWithPanel1: Record<string, PanelState> = {
        panel1: {
          id: 'panel1',
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
