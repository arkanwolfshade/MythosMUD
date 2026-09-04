import '@testing-library/jest-dom';
import { act, renderHook } from '@testing-library/react';
import React, { useContext } from 'react';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import { PanelContext, PanelProvider, type PanelState } from '../PanelContextRuntime';

const useRuntimePanelContext = () => {
  const ctx = useContext(PanelContext);
  if (!ctx) {
    throw new Error('PanelContext missing');
  }
  return ctx;
};

describe('PanelContextRuntime', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  afterEach(() => {
    localStorage.clear();
  });

  const wrapper = ({ children }: { children: React.ReactNode }) => <PanelProvider>{children}</PanelProvider>;

  it('togglePanelMaximized clears minimized for consistent state', () => {
    const { result } = renderHook(() => useRuntimePanelContext(), { wrapper });

    act(() => {
      result.current.togglePanelMinimized('chat');
    });
    expect(result.current.panels.chat.isMinimized).toBe(true);

    act(() => {
      result.current.togglePanelMaximized('chat');
    });
    expect(result.current.panels.chat.isMaximized).toBe(true);
    expect(result.current.panels.chat.isMinimized).toBe(false);

    act(() => {
      result.current.togglePanelMinimized('chat');
    });
    expect(result.current.panels.chat.isMinimized).toBe(true);
    expect(result.current.panels.chat.isMaximized).toBe(false);
  });

  it('bringToFront assigns strictly greater zIndex than any other panel', () => {
    const { result } = renderHook(() => useRuntimePanelContext(), { wrapper });
    const maxBefore = Math.max(...Object.values(result.current.panels).map((p: PanelState) => p.zIndex));

    act(() => {
      result.current.bringToFront('commands');
    });
    expect(result.current.panels.commands.zIndex).toBeGreaterThan(maxBefore);
  });

  it('updatePanel deep-merges into existing panel state', () => {
    const { result } = renderHook(() => useRuntimePanelContext(), { wrapper });
    const prevSize = result.current.panels.chat.size;

    act(() => {
      result.current.updatePanel('chat', { position: { x: 999, y: 1 } });
    });
    expect(result.current.panels.chat.position).toEqual({ x: 999, y: 1 });
    expect(result.current.panels.chat.size).toEqual(prevSize);
  });

  it('getNextZIndex is one greater than current maximum', () => {
    const { result } = renderHook(() => useRuntimePanelContext(), { wrapper });
    const maxZ = Math.max(...Object.values(result.current.panels).map((p: PanelState) => p.zIndex));

    expect(result.current.getNextZIndex()).toBe(maxZ + 1);
  });

  it('resetPanelLayout restores defaults and clears ad-hoc keys', () => {
    const { result } = renderHook(() => useRuntimePanelContext(), { wrapper });

    act(() => {
      result.current.addPanel('extra', 'Extra');
    });
    expect(result.current.panels.extra).toBeDefined();

    act(() => {
      result.current.resetPanelLayout();
    });
    expect(result.current.panels.extra).toBeUndefined();
    expect(result.current.panels.chat.title).toBe('Chat');
  });
});
