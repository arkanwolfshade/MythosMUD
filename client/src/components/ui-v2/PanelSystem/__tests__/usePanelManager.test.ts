import { describe, it, expect, vi } from 'vitest';
import { renderHook } from '@testing-library/react';
import React from 'react';
import { usePanelManager } from '../usePanelManager';
import { PanelManagerContext } from '../PanelManagerContext';
import type { PanelManagerContextValue } from '../PanelManagerContext';
import type { ReactNode } from 'react';

describe('usePanelManager', () => {
  const mockContextValue: PanelManagerContextValue = {
    panels: {},
    updatePosition: vi.fn(),
    updateSize: vi.fn(),
    toggleMinimize: vi.fn(),
    toggleMaximize: vi.fn(),
    setVisibility: vi.fn(),
    focusPanel: vi.fn(),
    closePanel: vi.fn(),
    getPanel: vi.fn(),
    scalePanelsToViewport: vi.fn(),
  };

  const createWrapper = (contextValue: PanelManagerContextValue) => {
    return ({ children }: { children: ReactNode }) =>
      React.createElement(PanelManagerContext.Provider, { value: contextValue }, children);
  };

  it('should return context value when used within provider', () => {
    const { result } = renderHook(() => usePanelManager(), {
      wrapper: createWrapper(mockContextValue),
    });

    expect(result.current).toBe(mockContextValue);
    expect(result.current.panels).toBeDefined();
    expect(result.current.updatePosition).toBeDefined();
    expect(result.current.updateSize).toBeDefined();
    expect(result.current.toggleMinimize).toBeDefined();
    expect(result.current.toggleMaximize).toBeDefined();
    expect(result.current.setVisibility).toBeDefined();
    expect(result.current.focusPanel).toBeDefined();
    expect(result.current.closePanel).toBeDefined();
    expect(result.current.getPanel).toBeDefined();
    expect(result.current.scalePanelsToViewport).toBeDefined();
  });

  it('should throw error when used outside provider', () => {
    // Suppress console.error for this test
    const consoleError = vi.spyOn(console, 'error').mockImplementation(() => {});

    expect(() => {
      renderHook(() => usePanelManager());
    }).toThrow('usePanelManager must be used within PanelManagerProvider');

    consoleError.mockRestore();
  });

  it('should return all context methods', () => {
    const { result } = renderHook(() => usePanelManager(), {
      wrapper: createWrapper(mockContextValue),
    });

    expect(typeof result.current.updatePosition).toBe('function');
    expect(typeof result.current.updateSize).toBe('function');
    expect(typeof result.current.toggleMinimize).toBe('function');
    expect(typeof result.current.toggleMaximize).toBe('function');
    expect(typeof result.current.setVisibility).toBe('function');
    expect(typeof result.current.focusPanel).toBe('function');
    expect(typeof result.current.closePanel).toBe('function');
    expect(typeof result.current.getPanel).toBe('function');
    expect(typeof result.current.scalePanelsToViewport).toBe('function');
  });
});
