import { describe, expect, it, beforeEach, vi } from 'vitest';
import { render, screen, act, waitFor } from '@testing-library/react';
import React from 'react';
import { renderHook } from '@testing-library/react';
import { PanelProvider } from '../PanelContext';
import { usePanelContext } from '../hooks/usePanelContext';
import type { PanelPosition, PanelSize } from '../PanelContext';

describe('PanelContext', () => {
  beforeEach(() => {
    localStorage.clear();
    vi.clearAllMocks();
  });

  const wrapper = ({ children }: { children: React.ReactNode }) => <PanelProvider>{children}</PanelProvider>;

  describe('PanelProvider', () => {
    it('should provide default panels', () => {
      // Arrange
      const TestComponent = () => {
        const { panels } = usePanelContext();
        return <div data-testid="panels">{Object.keys(panels).join(',')}</div>;
      };

      // Act
      render(
        <PanelProvider>
          <TestComponent />
        </PanelProvider>
      );

      // Assert
      const panelsText = screen.getByTestId('panels').textContent;
      expect(panelsText).toContain('chat');
      expect(panelsText).toContain('game-log');
      expect(panelsText).toContain('commands');
    });

    it('should load panels from localStorage', () => {
      // Arrange
      const savedPanels = {
        chat: {
          id: 'chat',
          title: 'Chat',
          isVisible: false,
          isMinimized: false,
          isMaximized: false,
          position: { x: 100, y: 100 },
          size: { width: 600, height: 500 },
          zIndex: 10,
        },
      };
      localStorage.setItem('mythosmud-panel-layout', JSON.stringify(savedPanels));

      const TestComponent = () => {
        const { panels } = usePanelContext();
        return <div data-testid="panels">{JSON.stringify(panels.chat)}</div>;
      };

      // Act
      render(
        <PanelProvider>
          <TestComponent />
        </PanelProvider>
      );

      // Assert
      const panelsElement = screen.getByTestId('panels');
      const chatPanel = JSON.parse(panelsElement.textContent || '{}');
      expect(chatPanel.position.x).toBe(100);
      expect(chatPanel.position.y).toBe(100);
    });

    it('should handle invalid localStorage data gracefully', () => {
      // Arrange
      localStorage.setItem('mythosmud-panel-layout', 'invalid json');

      const TestComponent = () => {
        const { panels } = usePanelContext();
        return <div data-testid="panels">{Object.keys(panels).length}</div>;
      };

      // Act & Assert - should not throw and use defaults
      render(
        <PanelProvider>
          <TestComponent />
        </PanelProvider>
      );

      expect(screen.getByTestId('panels').textContent).toBeTruthy();
    });

    it('should accept initial panels', () => {
      // Arrange
      const customPanels = {
        custom: {
          id: 'custom',
          title: 'Custom Panel',
          isVisible: true,
          isMinimized: false,
          isMaximized: false,
          position: { x: 0, y: 0 },
          size: { width: 200, height: 200 },
          zIndex: 1,
        },
      };

      const TestComponent = () => {
        const { panels } = usePanelContext();
        return <div data-testid="panels">{Object.keys(panels).join(',')}</div>;
      };

      // Act
      render(
        <PanelProvider initialPanels={customPanels}>
          <TestComponent />
        </PanelProvider>
      );

      // Assert
      expect(screen.getByTestId('panels').textContent).toContain('custom');
    });
  });

  describe('Panel Management Functions', () => {
    it('should add panel', () => {
      // Arrange & Act
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      act(() => {
        result.current.addPanel('test', 'Test Panel');
      });

      // Assert
      expect(result.current.panels.test).toBeDefined();
      expect(result.current.panels.test?.title).toBe('Test Panel');
      expect(result.current.panels.test?.isVisible).toBe(true);
    });

    it('should add panel with custom position and size', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });
      const position: PanelPosition = { x: 150, y: 200 };
      const size: PanelSize = { width: 500, height: 400 };

      // Act
      act(() => {
        result.current.addPanel('custom', 'Custom Panel', position, size);
      });

      // Assert
      expect(result.current.panels.custom).toBeDefined();
      expect(result.current.panels.custom?.position).toEqual(position);
      expect(result.current.panels.custom?.size).toEqual(size);
    });

    it('should remove panel', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.removePanel('chat');
      });

      // Assert
      expect(result.current.panels.chat).toBeUndefined();
    });

    it('should toggle panel visibility', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });
      const initialVisibility = result.current.panels.chat?.isVisible;

      // Act
      act(() => {
        result.current.togglePanelVisibility('chat');
      });

      // Assert
      expect(result.current.panels.chat?.isVisible).toBe(!initialVisibility);
    });

    it('should toggle panel minimized state', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.togglePanelMinimized('chat');
      });

      // Assert
      expect(result.current.panels.chat?.isMinimized).toBe(true);
      expect(result.current.panels.chat?.isMaximized).toBe(false); // Should unmaximize
    });

    it('should toggle panel maximized state', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.togglePanelMaximized('chat');
      });

      // Assert
      expect(result.current.panels.chat?.isMaximized).toBe(true);
      expect(result.current.panels.chat?.isMinimized).toBe(false); // Should unminimize
    });

    it('should move panel', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.movePanel('chat', { x: 200, y: 300 });
      });

      // Assert
      expect(result.current.panels.chat?.position).toEqual({ x: 200, y: 300 });
    });

    it('should resize panel', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.resizePanel('chat', { width: 800, height: 600 });
      });

      // Assert
      expect(result.current.panels.chat?.size).toEqual({ width: 800, height: 600 });
    });

    it('should bring panel to front', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });
      const initialZIndex = result.current.panels.chat?.zIndex || 0;

      // Act
      act(() => {
        result.current.bringToFront('chat');
      });

      // Assert
      expect(result.current.panels.chat?.zIndex).toBeGreaterThan(initialZIndex);
    });

    it('should reset panel layout', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Add a panel first
      act(() => {
        result.current.addPanel('test', 'Test');
      });
      expect(result.current.panels.test).toBeDefined();

      // Act
      act(() => {
        result.current.resetPanelLayout();
      });

      // Assert - should reset to defaults (test panel should be gone)
      expect(result.current.panels.test).toBeUndefined();
      expect(result.current.panels.chat).toBeDefined();
    });

    it('should get next z-index', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      const nextZIndex = result.current.getNextZIndex();

      // Assert
      expect(nextZIndex).toBeGreaterThan(0);
      expect(typeof nextZIndex).toBe('number');
    });

    it('should update panel with partial updates', () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.updatePanel('chat', { title: 'Updated Chat', isVisible: false });
      });

      // Assert
      expect(result.current.panels.chat?.title).toBe('Updated Chat');
      expect(result.current.panels.chat?.isVisible).toBe(false);
      // Other properties should remain unchanged
      expect(result.current.panels.chat?.position).toBeDefined();
    });

    it('should save panels to localStorage when they change', async () => {
      // Arrange
      const { result } = renderHook(() => usePanelContext(), { wrapper });

      // Act
      act(() => {
        result.current.addPanel('test-save', 'Test Save');
      });

      // Wait for effect to run
      await waitFor(() => {
        const saved = localStorage.getItem('mythosmud-panel-layout');
        expect(saved).toBeTruthy();
        if (saved) {
          const parsed = JSON.parse(saved);
          expect(parsed['test-save']).toBeDefined();
        }
      });
    });
  });

  describe('usePanelContext hook', () => {
    it('should throw error when used outside provider', () => {
      // Arrange - Render hook without wrapper/provider
      const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      // Act & Assert - Should throw when hook is used outside provider
      expect(() => {
        renderHook(() => usePanelContext());
      }).toThrow('usePanelContext must be used within a PanelProvider');

      consoleErrorSpy.mockRestore();
    });
  });
});
