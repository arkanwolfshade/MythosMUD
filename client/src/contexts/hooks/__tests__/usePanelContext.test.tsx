import { describe, expect, it, beforeEach } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { PanelProvider } from '../../PanelContext';
import { usePanel, usePanelActions, usePanelLayout } from '../usePanelContext';
import React from 'react';

describe('usePanelContext Hooks', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  const wrapper = ({ children }: { children: React.ReactNode }) => <PanelProvider>{children}</PanelProvider>;

  describe('usePanel', () => {
    it('should return panel and update function', () => {
      // Act
      const { result } = renderHook(() => usePanel('chat'), { wrapper });

      // Assert
      expect(result.current.panel).toBeDefined();
      expect(result.current.panel?.id).toBe('chat');
      expect(result.current.updatePanel).toBeDefined();
      expect(typeof result.current.updatePanel).toBe('function');
    });

    it('should update panel using update function', () => {
      // Arrange
      const { result } = renderHook(() => usePanel('chat'), { wrapper });

      // Act
      act(() => {
        result.current.updatePanel({ title: 'Updated Chat', isVisible: false });
      });

      // Assert
      expect(result.current.panel?.title).toBe('Updated Chat');
      expect(result.current.panel?.isVisible).toBe(false);
    });

    it('should return undefined panel for non-existent panel', () => {
      // Act
      const { result } = renderHook(() => usePanel('nonexistent'), { wrapper });

      // Assert
      expect(result.current.panel).toBeUndefined();
    });
  });

  describe('usePanelActions', () => {
    it('should provide panel action functions', () => {
      // Act
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Assert
      expect(result.current.toggleVisibility).toBeDefined();
      expect(result.current.toggleMinimized).toBeDefined();
      expect(result.current.toggleMaximized).toBeDefined();
      expect(result.current.move).toBeDefined();
      expect(result.current.resize).toBeDefined();
      expect(result.current.bringToFront).toBeDefined();
      expect(typeof result.current.toggleVisibility).toBe('function');
      expect(typeof result.current.toggleMinimized).toBe('function');
      expect(typeof result.current.toggleMaximized).toBe('function');
      expect(typeof result.current.move).toBe('function');
      expect(typeof result.current.resize).toBe('function');
      expect(typeof result.current.bringToFront).toBe('function');
    });

    it('should call toggle visibility action', () => {
      // Arrange
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.toggleVisibility();
        });
      }).not.toThrow();
    });

    it('should call toggle minimized action', () => {
      // Arrange
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.toggleMinimized();
        });
      }).not.toThrow();
    });

    it('should call toggle maximized action', () => {
      // Arrange
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.toggleMaximized();
        });
      }).not.toThrow();
    });

    it('should call move action', () => {
      // Arrange
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.move({ x: 150, y: 200 });
        });
      }).not.toThrow();
    });

    it('should call resize action', () => {
      // Arrange
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.resize({ width: 700, height: 500 });
        });
      }).not.toThrow();
    });

    it('should call bring to front action', () => {
      // Arrange
      const { result } = renderHook(() => usePanelActions('chat'), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.bringToFront();
        });
      }).not.toThrow();
    });
  });

  describe('usePanelLayout', () => {
    it('should return panels and resetLayout function', () => {
      // Act
      const { result } = renderHook(() => usePanelLayout(), { wrapper });

      // Assert
      expect(result.current.panels).toBeDefined();
      expect(Object.keys(result.current.panels).length).toBeGreaterThan(0);
      expect(result.current.resetLayout).toBeDefined();
      expect(typeof result.current.resetLayout).toBe('function');
    });

    it('should call reset layout function', () => {
      // Arrange
      const { result } = renderHook(() => usePanelLayout(), { wrapper });

      // Act & Assert - just verify the function can be called without error
      expect(() => {
        act(() => {
          result.current.resetLayout();
        });
      }).not.toThrow();
    });
  });
});
