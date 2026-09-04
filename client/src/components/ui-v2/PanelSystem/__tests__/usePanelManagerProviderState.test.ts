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

  it('toggleMinimize docks panel at bottom and restores saved layout', async () => {
    Object.defineProperty(window, 'innerWidth', { configurable: true, writable: true, value: 1280 });
    Object.defineProperty(window, 'innerHeight', { configurable: true, writable: true, value: 800 });

    const panels: Record<string, PanelState> = {
      chatHistory: {
        id: 'chatHistory',
        title: 'Chat History',
        position: { x: 20, y: 80 },
        size: { width: 320, height: 240 },
        zIndex: 1000,
        isMinimized: false,
        isMaximized: false,
        isVisible: true,
      },
    };

    const { result } = renderHook(() => usePanelManagerProviderState(panels));
    await waitFor(() => expect(result.current.getPanel('chatHistory')).toBeDefined());

    act(() => {
      result.current.toggleMinimize('chatHistory');
    });

    const minimized = result.current.getPanel('chatHistory');
    expect(minimized?.isMinimized).toBe(true);
    expect(minimized?.position.y).toBe(752);
    expect(minimized?.preMinimizePosition).toEqual({ x: 20, y: 80 });
    expect(minimized?.preMinimizeSize).toEqual({ width: 320, height: 240 });

    act(() => {
      result.current.toggleMinimize('chatHistory');
    });

    const restored = result.current.getPanel('chatHistory');
    expect(restored?.isMinimized).toBe(false);
    expect(restored?.position).toEqual({ x: 20, y: 80 });
    expect(restored?.size).toEqual({ width: 320, height: 240 });
    expect(restored?.preMinimizePosition).toBeUndefined();
  });

  it('toggleMinimize stacks multiple panels in the bottom dock', async () => {
    Object.defineProperty(window, 'innerWidth', { configurable: true, writable: true, value: 1280 });
    Object.defineProperty(window, 'innerHeight', { configurable: true, writable: true, value: 800 });

    const panels: Record<string, PanelState> = {
      chatHistory: {
        id: 'chatHistory',
        title: 'Chat History',
        position: { x: 20, y: 80 },
        size: { width: 320, height: 240 },
        zIndex: 1000,
        isMinimized: false,
        isMaximized: false,
        isVisible: true,
      },
      gameInfo: {
        id: 'gameInfo',
        title: 'Game Info',
        position: { x: 400, y: 80 },
        size: { width: 320, height: 240 },
        zIndex: 1001,
        isMinimized: false,
        isMaximized: false,
        isVisible: true,
      },
    };

    const { result } = renderHook(() => usePanelManagerProviderState(panels));
    await waitFor(() => expect(result.current.getPanel('chatHistory')).toBeDefined());

    act(() => {
      result.current.toggleMinimize('gameInfo');
      result.current.toggleMinimize('chatHistory');
    });

    const chat = result.current.getPanel('chatHistory');
    const info = result.current.getPanel('gameInfo');
    expect(chat?.position.x).toBe(8);
    expect(info?.position.x).toBe(216);
    expect(chat?.position.y).toBe(752);
    expect(info?.position.y).toBe(752);
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
