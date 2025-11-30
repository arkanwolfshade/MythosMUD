import { describe, expect, it, beforeEach, vi } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useSessionManagement } from '../useSessionManagement';

// Mock logger
vi.mock('../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
  },
}));

describe('useSessionManagement', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should initialize with generated session ID', () => {
    // Act
    const { result } = renderHook(() => useSessionManagement());

    // Assert
    expect(result.current.sessionId).toBeDefined();
    expect(result.current.sessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
  });

  it('should initialize with provided session ID', () => {
    // Arrange
    const initialSessionId = 'session_custom_12345';

    // Act
    const { result } = renderHook(() =>
      useSessionManagement({
        initialSessionId,
      })
    );

    // Assert
    expect(result.current.sessionId).toBe(initialSessionId);
  });

  it('should create new session', () => {
    // Arrange
    const { result } = renderHook(() => useSessionManagement());
    const originalSessionId = result.current.sessionId;

    // Act
    let newSessionId: string;
    act(() => {
      newSessionId = result.current.createNewSession();
    });

    // Assert
    expect(newSessionId!).toBeDefined();
    expect(newSessionId!).not.toBe(originalSessionId);
    expect(result.current.sessionId).toBe(newSessionId!);
  });

  it('should call onSessionChange when creating new session', () => {
    // Arrange
    const onSessionChange = vi.fn();
    const { result } = renderHook(() =>
      useSessionManagement({
        onSessionChange,
      })
    );

    // Act
    act(() => {
      result.current.createNewSession();
    });

    // Assert
    expect(onSessionChange).toHaveBeenCalled();
    expect(onSessionChange).toHaveBeenCalledWith(expect.stringMatching(/^session_\d+_[a-z0-9]+$/));
  });

  it('should switch to different session', () => {
    // Arrange
    const { result } = renderHook(() => useSessionManagement());
    const originalSessionId = result.current.sessionId;
    const newSessionId = 'session_switch_67890';

    // Act
    act(() => {
      result.current.switchToSession(newSessionId);
    });

    // Assert
    expect(result.current.sessionId).toBe(newSessionId);
    expect(result.current.sessionId).not.toBe(originalSessionId);
  });

  it('should not switch if session ID is the same', () => {
    // Arrange
    const { result } = renderHook(() => useSessionManagement());
    const originalSessionId = result.current.sessionId;
    const onSessionChange = vi.fn();

    const { result: result2 } = renderHook(() =>
      useSessionManagement({
        initialSessionId: originalSessionId,
        onSessionChange,
      })
    );

    // Act
    act(() => {
      result2.current.switchToSession(originalSessionId);
    });

    // Assert - onSessionChange should not be called for same session
    expect(onSessionChange).not.toHaveBeenCalled();
  });

  it('should call onSessionChange when switching sessions', () => {
    // Arrange
    const onSessionChange = vi.fn();
    const { result } = renderHook(() =>
      useSessionManagement({
        onSessionChange,
      })
    );
    const newSessionId = 'session_switch_12345';

    // Act
    act(() => {
      result.current.switchToSession(newSessionId);
    });

    // Assert
    expect(onSessionChange).toHaveBeenCalledWith(newSessionId);
  });

  it('should update session ID', () => {
    // Arrange
    const { result } = renderHook(() => useSessionManagement());
    const newSessionId = 'session_update_99999';

    // Act
    act(() => {
      result.current.updateSessionId(newSessionId);
    });

    // Assert
    expect(result.current.sessionId).toBe(newSessionId);
  });

  it('should handle onSessionChange callback changes', () => {
    // Arrange
    const onSessionChange1 = vi.fn();
    const { result, rerender } = renderHook(
      ({ onSessionChange }) =>
        useSessionManagement({
          onSessionChange,
        }),
      {
        initialProps: {
          onSessionChange: onSessionChange1,
        },
      }
    );

    act(() => {
      result.current.createNewSession();
    });

    expect(onSessionChange1).toHaveBeenCalled();

    // Change callback
    const onSessionChange2 = vi.fn();
    rerender({ onSessionChange: onSessionChange2 });

    // Act
    act(() => {
      result.current.createNewSession();
    });

    // Assert - new callback should be called
    expect(onSessionChange2).toHaveBeenCalled();
  });

  it('should generate valid session ID format', () => {
    // Act
    const { result } = renderHook(() => useSessionManagement());

    // Assert
    expect(result.current.sessionId).toMatch(/^session_\d+_[a-z0-9]+$/);
  });

  it('should generate unique session IDs', () => {
    // Arrange
    const sessionIds = new Set<string>();

    // Act
    for (let i = 0; i < 10; i++) {
      const { result } = renderHook(() => useSessionManagement());
      sessionIds.add(result.current.sessionId);
    }

    // Assert - all session IDs should be unique
    expect(sessionIds.size).toBe(10);
  });
});
