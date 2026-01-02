import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { MainMenuModal } from '../MainMenuModal';

// Mock createPortal to render in the same tree
vi.mock('react-dom', () => ({
  createPortal: (children: React.ReactNode) => children,
}));

describe('MainMenuModal', () => {
  const defaultProps = {
    isOpen: true,
    onClose: vi.fn(),
    onLogoutClick: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    // Reset body styles
    document.body.style.overflow = '';
    // Create a game container for tests
    const gameContainer = document.createElement('div');
    gameContainer.setAttribute('data-game-container', 'true');
    document.body.appendChild(gameContainer);
  });

  afterEach(() => {
    // Clean up
    document.body.style.overflow = '';
    const gameContainer = document.querySelector('[data-game-container]');
    if (gameContainer) {
      gameContainer.remove();
    }
  });

  it('should render when isOpen is true', () => {
    // Act
    render(<MainMenuModal {...defaultProps} />);

    // Assert
    expect(screen.getByText('Main Menu')).toBeInTheDocument();
    expect(screen.getByText('Map (New Tab)')).toBeInTheDocument();
    expect(screen.getByText('Logout')).toBeInTheDocument();
  });

  it('should not render when isOpen is false', () => {
    // Act
    render(<MainMenuModal {...defaultProps} isOpen={false} />);

    // Assert
    expect(screen.queryByText('Main Menu')).not.toBeInTheDocument();
  });

  it('should call onClose when close button is clicked', () => {
    // Arrange
    const onClose = vi.fn();
    render(<MainMenuModal {...defaultProps} onClose={onClose} />);

    // Act
    const closeButton = screen.getByLabelText('Close menu');
    fireEvent.click(closeButton);

    // Assert
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should call onClose when clicking backdrop', () => {
    // Arrange
    const onClose = vi.fn();
    render(<MainMenuModal {...defaultProps} onClose={onClose} />);

    // Act
    const backdrop = screen.getByRole('dialog');
    fireEvent.click(backdrop);

    // Assert
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should not call onClose when clicking modal content', () => {
    // Arrange
    const onClose = vi.fn();
    render(<MainMenuModal {...defaultProps} onClose={onClose} />);

    // Act
    const modalContent = screen.getByText('Main Menu').closest('div');
    if (modalContent) {
      fireEvent.click(modalContent);
    }

    // Assert - clicking inside should not close
    expect(onClose).not.toHaveBeenCalled();
  });

  it('should call onClose when ESC key is pressed', () => {
    // Arrange
    const onClose = vi.fn();
    render(<MainMenuModal {...defaultProps} onClose={onClose} />);

    // Act
    fireEvent.keyDown(window, { key: 'Escape' });

    // Assert
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should call onLogoutClick when logout button is clicked', () => {
    // Arrange
    const onLogoutClick = vi.fn();
    const onClose = vi.fn();
    render(<MainMenuModal {...defaultProps} onLogoutClick={onLogoutClick} onClose={onClose} />);

    // Act
    const logoutButton = screen.getByText('Logout');
    fireEvent.click(logoutButton);

    // Assert
    expect(onLogoutClick).toHaveBeenCalledTimes(1);
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should open map in new tab when currentRoom is provided', () => {
    // Arrange
    const windowOpenSpy = vi.spyOn(window, 'open').mockImplementation(() => null);
    const currentRoom = {
      id: 'room-123',
      plane: 'earth',
      zone: 'arkhamcity',
      subZone: 'library',
    };

    render(<MainMenuModal {...defaultProps} currentRoom={currentRoom} />);

    // Act
    const mapButton = screen.getByText(/^Map/);
    fireEvent.click(mapButton);

    // Assert
    expect(windowOpenSpy).toHaveBeenCalledWith(
      '/map?roomId=room-123&plane=earth&zone=arkhamcity&subZone=library',
      '_blank'
    );
    expect(defaultProps.onClose).toHaveBeenCalled();

    windowOpenSpy.mockRestore();
  });

  it('should open map in new tab without room params when no currentRoom', () => {
    // Arrange
    const windowOpenSpy = vi.spyOn(window, 'open').mockImplementation(() => null);
    render(<MainMenuModal {...defaultProps} currentRoom={null} />);

    // Act
    const mapButton = screen.getByText(/^Map/);
    fireEvent.click(mapButton);

    // Assert
    expect(windowOpenSpy).toHaveBeenCalledWith('/map', '_blank');
    expect(defaultProps.onClose).toHaveBeenCalled();

    windowOpenSpy.mockRestore();
  });

  it('should always open map in new tab regardless of deprecated props', () => {
    // Arrange
    // Note: onMapClick and openMapInNewTab are deprecated - map always opens in new tab
    const onMapClick = vi.fn();
    const windowOpenSpy = vi.spyOn(window, 'open').mockImplementation(() => null);
    const currentRoom = {
      id: 'room-123',
      plane: 'earth',
      zone: 'arkhamcity',
    };
    render(
      <MainMenuModal {...defaultProps} currentRoom={currentRoom} onMapClick={onMapClick} openMapInNewTab={false} />
    );

    // Act
    const mapButton = screen.getByText(/^Map/);
    fireEvent.click(mapButton);

    // Assert - should always open in new tab, ignoring deprecated props
    expect(windowOpenSpy).toHaveBeenCalledWith('/map?roomId=room-123&plane=earth&zone=arkhamcity', '_blank');
    expect(onMapClick).not.toHaveBeenCalled(); // Deprecated prop is ignored
    expect(defaultProps.onClose).toHaveBeenCalled();

    windowOpenSpy.mockRestore();
  });

  it('should disable body scroll when open', () => {
    // Arrange
    const { rerender } = render(<MainMenuModal {...defaultProps} isOpen={false} />);
    expect(document.body.style.overflow).toBe('');

    // Act
    rerender(<MainMenuModal {...defaultProps} isOpen={true} />);

    // Assert
    expect(document.body.style.overflow).toBe('hidden');
  });

  it('should restore body scroll when closed', () => {
    // Arrange
    const { rerender } = render(<MainMenuModal {...defaultProps} isOpen={true} />);
    expect(document.body.style.overflow).toBe('hidden');

    // Act
    rerender(<MainMenuModal {...defaultProps} isOpen={false} />);

    // Assert
    expect(document.body.style.overflow).toBe('');
  });

  it('should disable pointer events on game container when open', () => {
    // Arrange
    const gameContainer = document.querySelector('[data-game-container]') as HTMLElement;
    const { rerender } = render(<MainMenuModal {...defaultProps} isOpen={false} />);

    // Act
    rerender(<MainMenuModal {...defaultProps} isOpen={true} />);

    // Assert
    expect(gameContainer.style.pointerEvents).toBe('none');
  });

  it('should restore pointer events on game container when closed', () => {
    // Arrange
    const gameContainer = document.querySelector('[data-game-container]') as HTMLElement;
    const { rerender } = render(<MainMenuModal {...defaultProps} isOpen={true} />);
    expect(gameContainer.style.pointerEvents).toBe('none');

    // Act
    rerender(<MainMenuModal {...defaultProps} isOpen={false} />);

    // Assert
    expect(gameContainer.style.pointerEvents).toBe('');
  });

  it('should show "(New Tab)" text when currentRoom is provided', () => {
    // Arrange
    const currentRoom = {
      id: 'room-123',
      plane: 'earth',
      zone: 'arkhamcity',
    };

    // Act
    render(<MainMenuModal {...defaultProps} currentRoom={currentRoom} />);

    // Assert
    expect(screen.getByText('Map (New Tab)')).toBeInTheDocument();
  });

  it('should show Settings button as disabled', () => {
    // Act
    render(<MainMenuModal {...defaultProps} />);

    // Assert
    const settingsButton = screen.getByLabelText('Settings (coming soon)');
    expect(settingsButton).toBeDisabled();
    expect(settingsButton).toHaveTextContent('Settings');
  });

  it('should show "Press ESC to close" hint', () => {
    // Act
    render(<MainMenuModal {...defaultProps} />);

    // Assert
    expect(screen.getByText('Press ESC to close')).toBeInTheDocument();
  });

  it('should use openMapInNewTab prop when explicitly set to true', () => {
    // Arrange
    const windowOpenSpy = vi.spyOn(window, 'open').mockImplementation(() => null);
    const currentRoom = {
      id: 'room-123',
      plane: 'earth',
      zone: 'arkhamcity',
    };

    render(<MainMenuModal {...defaultProps} currentRoom={currentRoom} openMapInNewTab={true} />);

    // Act
    const mapButton = screen.getByText(/^Map/);
    fireEvent.click(mapButton);

    // Assert - should open in new tab
    expect(windowOpenSpy).toHaveBeenCalled();

    windowOpenSpy.mockRestore();
  });

  it('should always open map in new tab even when deprecated openMapInNewTab is false', () => {
    // Arrange
    // Note: openMapInNewTab is deprecated - map always opens in new tab
    const onMapClick = vi.fn();
    const windowOpenSpy = vi.spyOn(window, 'open').mockImplementation(() => null);
    const currentRoom = {
      id: 'room-123',
      plane: 'earth',
      zone: 'arkhamcity',
    };

    render(
      <MainMenuModal {...defaultProps} currentRoom={currentRoom} onMapClick={onMapClick} openMapInNewTab={false} />
    );

    // Act
    const mapButton = screen.getByText(/^Map/);
    fireEvent.click(mapButton);

    // Assert - should always open in new tab, ignoring deprecated prop
    expect(windowOpenSpy).toHaveBeenCalledWith('/map?roomId=room-123&plane=earth&zone=arkhamcity', '_blank');
    expect(onMapClick).not.toHaveBeenCalled(); // Deprecated prop is ignored

    windowOpenSpy.mockRestore();
  });

  it('should clean up event listeners on unmount', () => {
    // Arrange
    const onClose = vi.fn();
    const addEventListenerSpy = vi.spyOn(window, 'addEventListener');
    const removeEventListenerSpy = vi.spyOn(window, 'removeEventListener');

    const { unmount } = render(<MainMenuModal {...defaultProps} onClose={onClose} />);

    // Act
    unmount();

    // Assert
    expect(removeEventListenerSpy).toHaveBeenCalledWith('keydown', expect.any(Function));

    addEventListenerSpy.mockRestore();
    removeEventListenerSpy.mockRestore();
  });

  it('should handle room without subZone', () => {
    // Arrange
    const windowOpenSpy = vi.spyOn(window, 'open').mockImplementation(() => null);
    const currentRoom = {
      id: 'room-123',
      plane: 'earth',
      zone: 'arkhamcity',
    };

    render(<MainMenuModal {...defaultProps} currentRoom={currentRoom} />);

    // Act
    const mapButton = screen.getByText(/^Map/);
    fireEvent.click(mapButton);

    // Assert
    expect(windowOpenSpy).toHaveBeenCalledWith('/map?roomId=room-123&plane=earth&zone=arkhamcity', '_blank');

    windowOpenSpy.mockRestore();
  });

  it('should have proper ARIA attributes', () => {
    // Act
    render(<MainMenuModal {...defaultProps} />);

    // Assert
    const dialog = screen.getByRole('dialog');
    expect(dialog).toHaveAttribute('aria-modal', 'true');
    expect(dialog).toHaveAttribute('aria-labelledby', 'main-menu-title');
    expect(screen.getByText('Main Menu')).toHaveAttribute('id', 'main-menu-title');
  });
});
