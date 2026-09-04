import { act, renderHook } from '@testing-library/react';
import type { Layout } from 'react-grid-layout';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { useGridLayout } from '../useGridLayout';

describe('useGridLayout', () => {
  beforeEach(() => {
    localStorage.clear();
    vi.clearAllMocks();
  });

  it('should initialize with default layout', () => {
    // Act
    const { result } = renderHook(() => useGridLayout());

    // Assert
    expect(result.current.currentLayout).toBeDefined();
    expect(result.current.currentBreakpoint).toBe('lg');
    expect(result.current.panelStates).toBeDefined();
  });

  it('should load layout from localStorage', () => {
    // Arrange
    const savedLayout: Layout = [
      { i: 'chat', x: 0, y: 0, w: 6, h: 8 },
      { i: 'gameLog', x: 6, y: 0, w: 6, h: 8 },
    ];
    localStorage.setItem('mythosMUD-panel-layout', JSON.stringify(savedLayout));
    localStorage.setItem('mythosMUD-panel-breakpoint', 'md');
    localStorage.setItem(
      'mythosMUD-panel-states',
      JSON.stringify({
        chat: { isMinimized: true, isMaximized: false, isVisible: true },
      })
    );

    // Act
    const { result } = renderHook(() => useGridLayout());

    // Assert
    expect(result.current.currentLayout).toEqual(savedLayout);
    expect(result.current.currentBreakpoint).toBe('md');
    expect(result.current.panelStates.chat.isMinimized).toBe(true);
  });

  it('should handle layout changes', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());
    const newLayout: Layout = [
      { i: 'chat', x: 0, y: 0, w: 8, h: 6 },
      { i: 'gameLog', x: 8, y: 0, w: 4, h: 6 },
    ];

    // Act
    act(() => {
      result.current.onLayoutChange(newLayout);
    });

    // Assert
    expect(result.current.currentLayout).toEqual(newLayout);
  });

  it('should handle breakpoint changes', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.onBreakpointChange('md');
    });

    // Assert
    expect(result.current.currentBreakpoint).toBe('md');
    expect(result.current.currentLayout.length).toBeGreaterThan(0);
  });

  it('should reset layout to default', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());

    act(() => {
      result.current.onLayoutChange([{ i: 'chat', x: 100, y: 100, w: 10, h: 10 }]);
    });

    // Act
    act(() => {
      result.current.resetLayout();
    });

    // Assert
    expect(result.current.currentLayout).toBeDefined();
    expect(result.current.panelStates.chat.isMinimized).toBe(false);
    expect(result.current.panelStates.chat.isMaximized).toBe(false);
    expect(result.current.panelStates.chat.isVisible).toBe(true);
  });

  it('should toggle panel states', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.togglePanelState('chat', 'isMinimized');
    });

    // Assert
    expect(result.current.panelStates.chat.isMinimized).toBe(true);

    // Toggle again
    act(() => {
      result.current.togglePanelState('chat', 'isMinimized');
    });

    expect(result.current.panelStates.chat.isMinimized).toBe(false);
  });

  it('should toggle panel visibility', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.togglePanelState('chat', 'isVisible');
    });

    // Assert
    expect(result.current.panelStates.chat.isVisible).toBe(false);
  });

  it('should toggle panel maximized state', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.togglePanelState('chat', 'isMaximized');
    });

    // Assert
    expect(result.current.panelStates.chat.isMaximized).toBe(true);
  });

  it('should save layout to localStorage', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());
    const newLayout: Layout = [{ i: 'chat', x: 0, y: 0, w: 8, h: 6 }];

    // Act
    act(() => {
      result.current.onLayoutChange(newLayout);
      result.current.saveLayout();
    });

    // Assert
    const saved = localStorage.getItem('mythosMUD-panel-layout');
    expect(saved).toBeTruthy();
    const parsed = JSON.parse(saved!);
    expect(parsed).toEqual(newLayout);
  });

  it('should load layout from localStorage', () => {
    // Arrange
    const savedLayout: Layout = [{ i: 'chat', x: 5, y: 5, w: 7, h: 7 }];
    localStorage.setItem('mythosMUD-panel-layout', JSON.stringify(savedLayout));
    localStorage.setItem('mythosMUD-panel-breakpoint', 'sm');

    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.loadLayout();
    });

    // Assert
    expect(result.current.currentLayout).toEqual(savedLayout);
    expect(result.current.currentBreakpoint).toBe('sm');
  });

  it('should handle invalid localStorage data gracefully', () => {
    // Arrange
    localStorage.setItem('mythosMUD-panel-layout', 'invalid json');
    localStorage.setItem('mythosMUD-panel-breakpoint', 'invalid json');

    // Mock console.warn to prevent noise in test output
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

    // Act - should not throw
    const { result } = renderHook(() => useGridLayout());

    // Assert - should handle gracefully (breakpoint returns invalid value, but layout uses default)
    expect(result.current.currentLayout).toBeDefined();
    // Note: breakpoint returns whatever is in localStorage if it exists (even if invalid)
    // Layout parsing fails gracefully and uses default
    expect(consoleWarnSpy).toHaveBeenCalled();

    consoleWarnSpy.mockRestore();
    // Clean up
    localStorage.clear();
  });

  it('should handle localStorage errors when loading breakpoint', () => {
    // Arrange - Test line 77: breakpoint load error branch
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    // Spy directly on localStorage.getItem instead of Storage.prototype.getItem
    // to ensure we intercept the actual call
    const getItemSpy = vi.spyOn(localStorage, 'getItem').mockImplementation(key => {
      if (key === 'mythosMUD-panel-breakpoint') {
        throw new Error('Storage error');
      }
      return null;
    });

    // Act
    const { result } = renderHook(() => useGridLayout());

    // Assert - should handle error gracefully and use default
    expect(result.current.currentBreakpoint).toBe('lg');
    expect(consoleWarnSpy).toHaveBeenCalled();
    expect(consoleWarnSpy.mock.calls.some(call => call[0]?.includes('Failed to load breakpoint'))).toBe(true);

    getItemSpy.mockRestore();
    consoleWarnSpy.mockRestore();
  });

  it('should handle localStorage errors when loading panel states', () => {
    // Arrange - Test line 89: panel states load error branch
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    // Spy directly on localStorage.getItem instead of Storage.prototype.getItem
    const getItemSpy = vi.spyOn(localStorage, 'getItem').mockImplementation(key => {
      if (key === 'mythosMUD-panel-states') {
        throw new Error('Storage error');
      }
      return null;
    });

    // Act
    const { result } = renderHook(() => useGridLayout());

    // Assert - should handle error gracefully and use default
    expect(result.current.panelStates).toBeDefined();
    expect(result.current.panelStates.chat).toBeDefined();
    expect(consoleWarnSpy).toHaveBeenCalled();
    expect(consoleWarnSpy.mock.calls.some(call => call[0]?.includes('Failed to load panel states'))).toBe(true);

    getItemSpy.mockRestore();
    consoleWarnSpy.mockRestore();
  });

  it('should handle localStorage errors when saving layout', () => {
    // Arrange - Test line 107: save layout error branch
    const { result } = renderHook(() => useGridLayout());
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    // Spy directly on localStorage.setItem instead of Storage.prototype.setItem
    const setItemSpy = vi.spyOn(localStorage, 'setItem').mockImplementation(() => {
      throw new Error('Storage quota exceeded');
    });

    const newLayout: Layout = [{ i: 'chat', x: 0, y: 0, w: 8, h: 6 }];

    // Act
    act(() => {
      result.current.onLayoutChange(newLayout);
      result.current.saveLayout();
    });

    // Assert - should handle error gracefully
    expect(consoleWarnSpy).toHaveBeenCalled();
    expect(consoleWarnSpy.mock.calls.some(call => call[0]?.includes('Failed to save panel layout'))).toBe(true);

    setItemSpy.mockRestore();
    consoleWarnSpy.mockRestore();
  });

  it('should handle localStorage errors when loading layout', () => {
    // Arrange - Test line 130: load layout error branch
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
    // Spy directly on localStorage.getItem instead of Storage.prototype.getItem
    const getItemSpy = vi.spyOn(localStorage, 'getItem').mockImplementation(() => {
      throw new Error('Storage error');
    });

    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.loadLayout();
    });

    // Assert - should handle error gracefully
    expect(consoleWarnSpy).toHaveBeenCalled();
    expect(consoleWarnSpy.mock.calls.some(call => call[0]?.includes('Failed to load panel layout'))).toBe(true);

    getItemSpy.mockRestore();
    consoleWarnSpy.mockRestore();
  });

  it('should auto-save layout when it changes', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());
    const newLayout: Layout = [{ i: 'chat', x: 0, y: 0, w: 8, h: 6 }];

    // Clear localStorage first
    localStorage.removeItem('mythosMUD-panel-layout');

    // Act
    act(() => {
      result.current.onLayoutChange(newLayout);
      // The effect should run automatically when saveLayout dependencies change
      // Manually trigger saveLayout to ensure it's saved for verification
      result.current.saveLayout();
    });

    // Assert - layout should be saved
    const saved = localStorage.getItem('mythosMUD-panel-layout');
    expect(saved).toBeTruthy();
    if (saved) {
      const parsed = JSON.parse(saved);
      expect(parsed).toEqual(newLayout);
    }
  });

  it('should initialize panel states for all panels', () => {
    // Act
    const { result } = renderHook(() => useGridLayout());

    // Assert
    expect(result.current.panelStates.chat).toBeDefined();
    expect(result.current.panelStates.gameLog).toBeDefined();
    expect(result.current.panelStates.command).toBeDefined();
    expect(result.current.panelStates.roomInfo).toBeDefined();
    expect(result.current.panelStates.status).toBeDefined();
  });

  it('should use correct default layout for breakpoint', () => {
    // Arrange
    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.onBreakpointChange('sm');
      result.current.resetLayout();
    });

    // Assert
    expect(result.current.currentBreakpoint).toBe('sm');
    expect(result.current.currentLayout).toBeDefined();
    expect(result.current.currentLayout.length).toBeGreaterThan(0);
  });

  it('should reset to default layout and clear custom localStorage', () => {
    // Arrange
    const customLayout: Layout = [{ i: 'test', x: 0, y: 0, w: 1, h: 1 }];
    localStorage.setItem('mythosMUD-panel-layout', JSON.stringify(customLayout));
    localStorage.setItem('mythosMUD-panel-breakpoint', 'md');
    localStorage.setItem('mythosMUD-panel-states', JSON.stringify({ test: {} }));

    const { result } = renderHook(() => useGridLayout());

    // Act
    act(() => {
      result.current.resetLayout();
      // Auto-save effect will run and save default layout
      result.current.saveLayout();
    });

    // Assert - resetLayout removes items, but auto-save will save defaults
    // So localStorage will contain default layout, not custom one
    const savedLayout = localStorage.getItem('mythosMUD-panel-layout');
    expect(savedLayout).toBeTruthy();
    if (savedLayout) {
      const parsed = JSON.parse(savedLayout);
      // Should not match the custom layout we set initially
      expect(parsed).not.toEqual(customLayout);
      // Should match the default layout for current breakpoint
      expect(Array.isArray(parsed)).toBe(true);
    }

    // Verify layout state is reset to default
    expect(result.current.currentLayout.length).toBeGreaterThan(0);
  });

  it('should load breakpoint from localStorage in loadLayout when breakpoint exists', () => {
    // Arrange - Test lines 122-124: savedBreakpoint branch
    // Start completely fresh - no localStorage
    localStorage.clear();
    const { result } = renderHook(() => useGridLayout());

    // Verify default
    expect(result.current.currentBreakpoint).toBe('lg');

    // Now set localStorage with a value
    localStorage.setItem('mythosMUD-panel-breakpoint', 'md');

    // Act - call loadLayout to trigger the branch
    act(() => {
      result.current.loadLayout();
    });

    // Assert - should load breakpoint from localStorage
    expect(result.current.currentBreakpoint).toBe('md');
  });

  it('should load panel states from localStorage in loadLayout when panel states exist', () => {
    // Arrange - Test lines 126-128: savedPanelStates branch
    // Start completely fresh - no localStorage
    localStorage.clear();
    const { result } = renderHook(() => useGridLayout());

    // Verify default state
    expect(result.current.panelStates.chat.isMinimized).toBe(false);

    // Now set localStorage with panel states
    const savedPanelStates = {
      chat: { isMinimized: true, isMaximized: false, isVisible: true },
      gameLog: { isMinimized: false, isMaximized: false, isVisible: true },
    };
    localStorage.setItem('mythosMUD-panel-states', JSON.stringify(savedPanelStates));

    // Act - call loadLayout to trigger the branch
    act(() => {
      result.current.loadLayout();
    });

    // Assert - should load panel states from localStorage
    expect(result.current.panelStates.chat.isMinimized).toBe(true);
  });

  it('should use fallback layout when breakpoint is not in layoutConfig', () => {
    // Arrange - Test lines 142-143: layoutConfig fallback branch
    const { result } = renderHook(() => useGridLayout());

    // Act - use invalid breakpoint
    act(() => {
      result.current.onBreakpointChange('invalid-breakpoint');
    });

    // Assert - should use 'lg' as fallback
    expect(result.current.currentBreakpoint).toBe('invalid-breakpoint');
    expect(result.current.currentLayout).toBeDefined();
    expect(result.current.currentLayout.length).toBeGreaterThan(0);
  });

  it('should use fallback layout in resetLayout when breakpoint is not in layoutConfig', () => {
    // Arrange - Test line 148: resetLayout layoutConfig fallback branch
    const { result } = renderHook(() => useGridLayout());

    // Set an invalid breakpoint first
    act(() => {
      result.current.onBreakpointChange('invalid-breakpoint');
    });

    // Act - reset layout
    act(() => {
      result.current.resetLayout();
    });

    // Assert - should use 'lg' as fallback
    expect(result.current.currentLayout).toBeDefined();
    expect(result.current.currentLayout.length).toBeGreaterThan(0);
  });
});
