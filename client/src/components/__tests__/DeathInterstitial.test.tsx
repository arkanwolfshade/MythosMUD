import { render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { DeathInterstitial } from '../DeathInterstitial';

describe('DeathInterstitial', () => {
  const defaultProps = {
    isVisible: true,
    deathLocation: 'Arkham Sanitarium',
    onRespawn: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render when visible', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} />);

    // Assert
    expect(screen.getByText('THE THRESHOLD CROSSED')).toBeInTheDocument();
    expect(screen.getByText(/The darkness consumes you utterly/)).toBeInTheDocument();
  });

  it('should not render when not visible', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} isVisible={false} />);

    // Assert
    expect(screen.queryByText('THE THRESHOLD CROSSED')).not.toBeInTheDocument();
  });

  it('should display death location', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} deathLocation="Dark Alley" />);

    // Assert
    expect(screen.getByText(/You perished at:/)).toBeInTheDocument();
    expect(screen.getByText('Dark Alley')).toBeInTheDocument();
  });

  it('should display default location when deathLocation is empty', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} deathLocation="" />);

    // Assert
    expect(screen.getByText('Unknown Location')).toBeInTheDocument();
  });

  it('should call onRespawn when respawn button is clicked', () => {
    // Arrange
    const onRespawn = vi.fn();
    render(<DeathInterstitial {...defaultProps} onRespawn={onRespawn} />);

    // Act
    screen.getByText('Rejoin the earthly plane').click();

    // Assert
    expect(onRespawn).toHaveBeenCalledTimes(1);
  });

  it('should show loading state when respawning', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} isRespawning={true} />);

    // Assert
    const respawnButton = screen.getByText('Returning to the mortal realm...');
    expect(respawnButton).toBeInTheDocument();
    expect(respawnButton).toBeDisabled();
    expect(screen.getByText(/The veil between worlds parts/)).toBeInTheDocument();
    // Button should show loading text, not the normal text
    expect(screen.queryByText('Rejoin the earthly plane')).not.toBeInTheDocument();
  });

  it('should show normal state when not respawning', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} isRespawning={false} />);

    // Assert
    expect(screen.getByText('Rejoin the earthly plane')).toBeInTheDocument();
    expect(screen.getByText('Rejoin the earthly plane')).not.toBeDisabled();
    expect(screen.queryByText(/The veil between worlds parts/)).not.toBeInTheDocument();
  });

  it('should render death narrative text', () => {
    // Act
    render(<DeathInterstitial {...defaultProps} />);

    // Assert
    expect(screen.getByText(/The darkness consumes you utterly/)).toBeInTheDocument();
    expect(screen.getByText(/But the threads binding you to the waking world/)).toBeInTheDocument();
  });

  it('should have proper CSS classes', () => {
    // Act
    const { container } = render(<DeathInterstitial {...defaultProps} />);

    // Assert
    const overlay = container.querySelector('.death-interstitial-overlay');
    expect(overlay).toBeInTheDocument();

    const containerDiv = container.querySelector('.death-interstitial-container');
    expect(containerDiv).toBeInTheDocument();

    const content = container.querySelector('.death-interstitial-content');
    expect(content).toBeInTheDocument();
  });
});
