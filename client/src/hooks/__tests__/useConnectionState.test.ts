import { describe, expect, it, beforeEach, vi } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useConnectionState } from '../useConnectionState';
import { connectionMachine } from '../useConnectionStateMachine';
import { useMachine } from '@xstate/react';

// Mock the XState useMachine hook
vi.mock('@xstate/react', () => ({
  useMachine: vi.fn(),
}));

describe('useConnectionState', () => {
  const mockSend = vi.fn();
  const mockState = {
    value: 'disconnected',
    context: {
      sessionId: null,
      reconnectAttempts: 0,
      maxReconnectAttempts: 5,
      lastError: null,
      connectionStartTime: null,
      lastConnectedTime: null,
      sseUrl: null,
      wsUrl: null,
    },
  };

  beforeEach(() => {
    vi.clearAllMocks();
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([mockState, mockSend]);
  });

  it('should initialize with disconnected state', () => {
    // Act
    const { result } = renderHook(() => useConnectionState());

    // Assert
    expect(result.current.state).toBe('disconnected');
    expect(result.current.isDisconnected).toBe(true);
    expect(result.current.isConnecting).toBe(false);
    expect(result.current.isConnected).toBe(false);
  });

  it('should provide connect function', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.connect();
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'CONNECT' });
  });

  it('should provide disconnect function', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.disconnect();
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'DISCONNECT' });
  });

  it('should provide reconnect function', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.reconnect();
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'RECONNECT' });
  });

  it('should provide reset function', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.reset();
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'RESET' });
  });

  it('should provide onSSEConnected handler', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.onSSEConnected('session-123');
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'SSE_CONNECTED', sessionId: 'session-123' });
  });

  it('should provide onSSEFailed handler', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.onSSEFailed('Connection failed');
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'SSE_FAILED', error: 'Connection failed' });
  });

  it('should provide onWSConnected handler', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.onWSConnected();
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'WS_CONNECTED' });
  });

  it('should provide onWSFailed handler', () => {
    // Arrange
    const { result } = renderHook(() => useConnectionState());

    // Act
    act(() => {
      result.current.onWSFailed('WebSocket error');
    });

    // Assert
    expect(mockSend).toHaveBeenCalledWith({ type: 'WS_FAILED', error: 'WebSocket error' });
  });

  it('should correctly identify connecting states', () => {
    // Arrange
    const connectingState = {
      ...mockState,
      value: 'connecting_sse',
    };
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([connectingState, mockSend]);

    // Act
    const { result } = renderHook(() => useConnectionState());

    // Assert
    expect(result.current.isConnecting).toBe(true);
    expect(result.current.isDisconnected).toBe(false);
  });

  it('should correctly identify fully connected state', () => {
    // Arrange
    const connectedState = {
      ...mockState,
      value: 'fully_connected',
      context: {
        ...mockState.context,
        sessionId: 'session-123',
      },
    };
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([connectedState, mockSend]);

    // Act
    const { result } = renderHook(() => useConnectionState());

    // Assert
    expect(result.current.isConnected).toBe(true);
    expect(result.current.isConnecting).toBe(false);
    expect(result.current.sessionId).toBe('session-123');
  });

  it('should correctly identify reconnecting state', () => {
    // Arrange
    const reconnectingState = {
      ...mockState,
      value: 'reconnecting',
    };
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([reconnectingState, mockSend]);

    // Act
    const { result } = renderHook(() => useConnectionState());

    // Assert
    expect(result.current.isReconnecting).toBe(true);
  });

  it('should correctly identify failed state', () => {
    // Arrange
    const failedState = {
      ...mockState,
      value: 'failed',
      context: {
        ...mockState.context,
        lastError: 'Connection failed',
      },
    };
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([failedState, mockSend]);

    // Act
    const { result } = renderHook(() => useConnectionState());

    // Assert
    expect(result.current.isFailed).toBe(true);
    expect(result.current.lastError).toBe('Connection failed');
  });

  it('should accept maxReconnectAttempts option', () => {
    // Arrange
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([mockState, mockSend]);

    // Act
    renderHook(() =>
      useConnectionState({
        maxReconnectAttempts: 10,
      })
    );

    // Assert
    expect(useMachine).toHaveBeenCalledWith(
      connectionMachine,
      expect.objectContaining({
        context: expect.objectContaining({
          maxReconnectAttempts: 10,
        }),
      })
    );
  });

  it('should call onStateChange callback when state changes', () => {
    // Arrange
    const onStateChange = vi.fn();
    const state1 = { ...mockState, value: 'disconnected' };
    const state2 = { ...mockState, value: 'connecting_sse' };
    (useMachine as ReturnType<typeof vi.fn>)
      .mockReturnValueOnce([state1, mockSend])
      .mockReturnValueOnce([state2, mockSend]);

    // Act
    const { rerender } = renderHook(() =>
      useConnectionState({
        onStateChange,
      })
    );

    // Update state
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([state2, mockSend]);
    rerender();

    // Assert - onStateChange should be called when state changes
    // Note: This will be called via useEffect when state.value changes
    expect(onStateChange).toHaveBeenCalled();
  });

  it('should return context data', () => {
    // Arrange
    const stateWithContext = {
      ...mockState,
      context: {
        ...mockState.context,
        sessionId: 'session-123',
        reconnectAttempts: 3,
        lastError: 'Error message',
      },
    };
    (useMachine as ReturnType<typeof vi.fn>).mockReturnValue([stateWithContext, mockSend]);

    // Act
    const { result } = renderHook(() => useConnectionState());

    // Assert
    expect(result.current.context).toEqual(stateWithContext.context);
    expect(result.current.sessionId).toBe('session-123');
    expect(result.current.reconnectAttempts).toBe(3);
    expect(result.current.lastError).toBe('Error message');
  });
});
