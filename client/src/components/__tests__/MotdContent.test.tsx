import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { MotdContent } from '../MotdContent';

describe('MotdContent', () => {
  it('should render title', () => {
    // Act
    render(<MotdContent />);

    // Assert
    expect(screen.getByText('MYTHOS MUD')).toBeInTheDocument();
    expect(screen.getByText('Welcome to the Dreamlands')).toBeInTheDocument();
  });

  it('should render welcome text', () => {
    // Act
    render(<MotdContent />);

    // Assert
    expect(screen.getByText(/Greetings, seeker of forbidden knowledge/)).toBeInTheDocument();
    expect(screen.getByText(/As noted in the restricted archives/)).toBeInTheDocument();
  });

  it('should render warning message', () => {
    // Act
    render(<MotdContent />);

    // Assert
    expect(screen.getByText(/⚠️ WARNING: Prolonged exposure to eldritch knowledge/)).toBeInTheDocument();
  });

  it('should render realm status section', () => {
    // Act
    render(<MotdContent />);

    // Assert
    expect(screen.getByText('Current Realm Status')).toBeInTheDocument();
    expect(screen.getByText(/Active Players:/)).toBeInTheDocument();
    expect(screen.getByText(/Known Zones:/)).toBeInTheDocument();
    expect(screen.getByText(/Reality Stability:/)).toBeInTheDocument();
  });

  it('should render available commands section', () => {
    // Act
    render(<MotdContent />);

    // Assert
    expect(screen.getByText('Available Commands:')).toBeInTheDocument();
    expect(screen.getByText(/look/)).toBeInTheDocument();
    expect(screen.getByText(/move \[direction\]/)).toBeInTheDocument();
  });

  it('should render Yellow Sign', () => {
    // Act
    const { container } = render(<MotdContent />);

    // Assert
    const yellowSign = container.querySelector('.yellow-sign');
    expect(yellowSign).toBeInTheDocument();
    // Check for some Yellow Sign content
    expect(yellowSign?.textContent).toContain('*');
  });

  it('should have proper CSS classes', () => {
    // Act
    const { container } = render(<MotdContent />);

    // Assert
    const mainContainer = container.querySelector('.container');
    expect(mainContainer).toBeInTheDocument();

    const title = container.querySelector('.title');
    expect(title).toBeInTheDocument();

    const welcomeText = container.querySelector('.welcome-text');
    expect(welcomeText).toBeInTheDocument();
  });
});
