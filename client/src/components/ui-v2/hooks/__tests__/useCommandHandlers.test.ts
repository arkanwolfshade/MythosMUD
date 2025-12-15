/**
 * Tests for useCommandHandlers hook.
 */

import { act, renderHook } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { useCommandHandlers } from '../useCommandHandlers';

// Mock dependencies
vi.mock('../../../utils/logger', () => ({
  logger: {
    error: vi.fn(),
  },
}));

vi.mock('../../../utils/security', () => ({
  inputSanitizer: {
    sanitizeCommand: (cmd: string) => cmd.trim(),
  },
}));

describe('useCommandHandlers', () => {
  const mockSendCommand = vi.fn().mockResolvedValue(true);
  const mockSetGameState = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should return handleCommandSubmit function', () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    expect(result.current.handleCommandSubmit).toBeDefined();
    expect(typeof result.current.handleCommandSubmit).toBe('function');
  });

  it('should not send command when not connected', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: false,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('test command');
    });

    expect(mockSendCommand).not.toHaveBeenCalled();
  });

  it('should not send empty command', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('   ');
    });

    expect(mockSendCommand).not.toHaveBeenCalled();
  });

  it('should send command when connected', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('look');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('look', []);
  });

  it('should normalize direction shortcuts', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('n');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('go', ['north']);
  });

  it('should normalize go commands with direction shortcuts', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('go n');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('go', ['north']);
  });

  it('should normalize look commands with direction shortcuts', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('look s');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('look', ['south']);
  });

  it('should add command to history', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('test command');
    });

    expect(mockSetGameState).toHaveBeenCalled();
  });

  it('should handle command send failure', async () => {
    const mockSendCommandFail = vi.fn().mockResolvedValue(false);
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommandFail,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('test');
    });

    expect(mockSendCommandFail).toHaveBeenCalled();
  });

  it('should split command into name and args', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('say hello world');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('say', ['hello', 'world']);
  });
});
