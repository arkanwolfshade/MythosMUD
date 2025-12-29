/**
 * Tests for useCommandHandlers hook.
 */

import { act, renderHook } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { useCommandHandlers } from '../useCommandHandlers';

// Mock dependencies
vi.mock('../../../../utils/logger', () => ({
  logger: {
    error: vi.fn(),
    warn: vi.fn(),
  },
}));

vi.mock('../../../../utils/security', () => ({
  inputSanitizer: {
    sanitizeCommand: vi.fn((cmd: string) => cmd.trim()),
    sanitizeChatMessage: vi.fn((msg: string) => msg.trim()),
  },
}));

describe('useCommandHandlers', () => {
  const mockSendCommand = vi.fn().mockResolvedValue(true);
  const mockSetGameState = vi.fn();

  beforeEach(async () => {
    vi.clearAllMocks();
    // Reset and restore default mock implementations
    const securityModule = await import('../../../../utils/security');
    vi.mocked(securityModule.inputSanitizer.sanitizeCommand).mockReset();
    vi.mocked(securityModule.inputSanitizer.sanitizeChatMessage).mockReset();
    vi.mocked(securityModule.inputSanitizer.sanitizeCommand).mockImplementation((cmd: string) => cmd.trim());
    vi.mocked(securityModule.inputSanitizer.sanitizeChatMessage).mockImplementation((msg: string) => msg.trim());
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

  it('should handle all direction shortcuts', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    const directions = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'u', 'd', 'up', 'down'];
    for (const dir of directions) {
      await act(async () => {
        await result.current.handleCommandSubmit(dir);
      });
    }

    expect(mockSendCommand).toHaveBeenCalledTimes(directions.length);
  });

  it('should handle go command with full direction names', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('go north');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('go', ['north']);
  });

  it('should handle look command with full direction names', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('look east');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('look', ['east']);
  });

  it('should not normalize commands that are not directions', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('attack goblin');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('attack', ['goblin']);
  });

  it('should handle commands with multiple words that are not directions', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('say hello to everyone');
    });

    expect(mockSendCommand).toHaveBeenCalledWith('say', ['hello', 'to', 'everyone']);
  });

  it('should handle commands with three or more parts', async () => {
    const { result } = renderHook(() =>
      useCommandHandlers({
        isConnected: true,
        sendCommand: mockSendCommand,
        setGameState: mockSetGameState,
      })
    );

    await act(async () => {
      await result.current.handleCommandSubmit('go north then east');
    });

    // Should not normalize since it has more than 2 parts
    expect(mockSendCommand).toHaveBeenCalledWith('go', ['north', 'then', 'east']);
  });

  it('should preserve command history when command fails', async () => {
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

    // Command should still be added to history even if send fails
    expect(mockSetGameState).toHaveBeenCalled();
  });

  it('should handle empty command after trimming', async () => {
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

    // Should not send if command is empty after trimming
    expect(mockSendCommand).not.toHaveBeenCalled();
  });

  describe('handleChatMessage', () => {
    it('should send chat message when connected', async () => {
      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: true,
          sendCommand: mockSendCommand,
          setGameState: mockSetGameState,
        })
      );

      await act(async () => {
        await result.current.handleChatMessage('Hello world', 'say');
      });

      expect(mockSendCommand).toHaveBeenCalledWith('chat', ['say', 'Hello world']);
    });

    it('should not send chat message when not connected', async () => {
      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: false,
          sendCommand: mockSendCommand,
          setGameState: mockSetGameState,
        })
      );

      await act(async () => {
        await result.current.handleChatMessage('Hello', 'say');
      });

      expect(mockSendCommand).not.toHaveBeenCalled();
    });

    it('should not send empty chat message', async () => {
      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: true,
          sendCommand: mockSendCommand,
          setGameState: mockSetGameState,
        })
      );

      await act(async () => {
        await result.current.handleChatMessage('   ', 'say');
      });

      expect(mockSendCommand).not.toHaveBeenCalled();
    });

    it('should handle sanitized chat message that becomes empty', async () => {
      const securityModule = await import('../../../../utils/security');
      vi.mocked(securityModule.inputSanitizer.sanitizeChatMessage).mockImplementationOnce(() => '');

      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: true,
          sendCommand: mockSendCommand,
          setGameState: mockSetGameState,
        })
      );

      await act(async () => {
        await result.current.handleChatMessage('test', 'say');
      });

      expect(mockSendCommand).not.toHaveBeenCalled();
    });

    it('should handle chat message send failure', async () => {
      const mockSendCommandFail = vi.fn().mockResolvedValue(false);
      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: true,
          sendCommand: mockSendCommandFail,
          setGameState: mockSetGameState,
        })
      );

      await act(async () => {
        await result.current.handleChatMessage('Hello', 'say');
      });

      expect(mockSendCommandFail).toHaveBeenCalled();
    });
  });

  describe('handleClearMessages', () => {
    it('should clear messages', () => {
      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: true,
          sendCommand: mockSendCommand,
          setGameState: mockSetGameState,
        })
      );

      act(() => {
        result.current.handleClearMessages();
      });

      expect(mockSetGameState).toHaveBeenCalled();
    });
  });

  describe('handleClearHistory', () => {
    it('should clear command history', () => {
      const { result } = renderHook(() =>
        useCommandHandlers({
          isConnected: true,
          sendCommand: mockSendCommand,
          setGameState: mockSetGameState,
        })
      );

      act(() => {
        result.current.handleClearHistory();
      });

      expect(mockSetGameState).toHaveBeenCalled();
    });
  });
});
