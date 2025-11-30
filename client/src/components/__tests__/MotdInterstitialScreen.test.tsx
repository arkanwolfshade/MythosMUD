import { describe, expect, it, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { MotdInterstitialScreen } from '../MotdInterstitialScreen';
import React from 'react';

// Mock MotdContent component
vi.mock('../MotdContent', () => ({
  MotdContent: () => <div data-testid="motd-content">MOTD Content</div>,
}));

describe('MotdInterstitialScreen', () => {
  const defaultProps = {
    onContinue: vi.fn(),
    onReturnToLogin: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render MOTD content', () => {
    // Act
    render(<MotdInterstitialScreen {...defaultProps} />);

    // Assert
    expect(screen.getByTestId('motd-content')).toBeInTheDocument();
  });

  it('should render Continue button', () => {
    // Act
    render(<MotdInterstitialScreen {...defaultProps} />);

    // Assert
    expect(screen.getByText('Enter the Realm')).toBeInTheDocument();
  });

  it('should render Return to Login button', () => {
    // Act
    render(<MotdInterstitialScreen {...defaultProps} />);

    // Assert
    expect(screen.getByText('Return to Login')).toBeInTheDocument();
  });

  it('should call onContinue when Continue button is clicked', () => {
    // Arrange
    const onContinue = vi.fn();
    render(<MotdInterstitialScreen {...defaultProps} onContinue={onContinue} />);

    // Act
    screen.getByText('Enter the Realm').click();

    // Assert
    expect(onContinue).toHaveBeenCalledTimes(1);
  });

  it('should call onReturnToLogin when Return to Login button is clicked', () => {
    // Arrange
    const onReturnToLogin = vi.fn();
    render(<MotdInterstitialScreen {...defaultProps} onReturnToLogin={onReturnToLogin} />);

    // Act
    screen.getByText('Return to Login').click();

    // Assert
    expect(onReturnToLogin).toHaveBeenCalledTimes(1);
  });

  it('should have proper layout structure', () => {
    // Act
    const { container } = render(<MotdInterstitialScreen {...defaultProps} />);

    // Assert
    const mainDiv = container.firstChild as HTMLElement;
    expect(mainDiv).toHaveClass('min-h-screen', 'w-full');
  });
});
