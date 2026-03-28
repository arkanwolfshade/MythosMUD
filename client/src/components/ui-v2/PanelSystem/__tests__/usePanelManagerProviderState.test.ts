import { act, renderHook, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { PanelState } from '../../types';
import { usePanelManagerProviderState } from '../usePanelManagerProviderState';

vi.mock('../panelLayoutBootstrap', () => ({
  resolveInitialPanelLayout: vi.fn((defaults: Record<string, PanelState>) => ({ ...defaults })),
}));

const localStorageMock = (() => {
  let store: Record<string, string> = {};
  return {
    getItem: (key: string) => store[key] ?? null,
    setItem: (key: string, value: string) => {
      store[key] = value;
    },
    clear: () => {
      store = {};
    },
  };
})();

Object.defineProperty(window, 'localStorage', { value: localStorageMock });

function chatPanel(): PanelState {
  return {
    id: 'chat',
    title: 'Chat',
    position: { x: 20, y: 80 },
    size: { width: 320, height: 240 },
    zIndex: 1000,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
  };
}

const defaultPanels: Record<string, PanelState> = {
  chat: chatPanel(),
};

describe('usePanelManagerProviderState', () => {
  beforeEach(() => {
    localStorageMock.clear();
  });

  it('toggleMinimize dispatches and flips isMinimized', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.toggleMinimize('chat');
    });
    expect(result.current.getPanel('chat')?.isMinimized).toBe(true);

    act(() => {
      result.current.toggleMinimize('chat');
    });
    expect(result.current.getPanel('chat')?.isMinimized).toBe(false);
  });

  it('toggleMaximize dispatches and sets isMaximized', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.toggleMaximize('chat');
    });
    expect(result.current.getPanel('chat')?.isMaximized).toBe(true);
    expect(result.current.getPanel('chat')?.isMinimized).toBe(false);
  });

  it('setVisibility dispatches and updates isVisible', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.setVisibility('chat', false);
    });
    expect(result.current.getPanel('chat')?.isVisible).toBe(false);
  });

  it('closePanel dispatches and removes the panel', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.closePanel('chat');
    });
    expect(result.current.getPanel('chat')).toBeUndefined();
  });

  it('updatePosition dispatches and moves the panel', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.updatePosition('chat', { x: 99, y: 120 });
    });
    expect(result.current.getPanel('chat')?.position).toEqual({ x: 99, y: 120 });
  });

  it('updateSize dispatches and resizes the panel', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.updateSize('chat', { width: 400, height: 300 });
    });
    expect(result.current.getPanel('chat')?.size).toEqual({ width: 400, height: 300 });
  });

  it('focusPanel dispatches and raises zIndex', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    act(() => {
      result.current.focusPanel('chat');
    });
    expect(result.current.getPanel('chat')?.zIndex).toBe(1001);
  });

  it('scalePanelsToViewport dispatches and applies scaled layout for normal panels', async () => {
    const { result } = renderHook(() => usePanelManagerProviderState(defaultPanels));
    await waitFor(() => expect(result.current.getPanel('chat')).toBeDefined());

    const before = result.current.getPanel('chat')!;

    act(() => {
      result.current.scalePanelsToViewport(1000, 800, () => ({
        chat: {
          ...before,
          position: { x: 0, y: 48 },
          size: { width: 500, height: 400 },
        },
      }));
    });

    const after = result.current.getPanel('chat');
    expect(after).toBeDefined();
    expect(after!.position.x).toBe(0);
    expect(after!.position.y).toBe(48);
    expect(after!.size.width).toBe(500);
    expect(after!.size.height).toBe(400);
  });
});
