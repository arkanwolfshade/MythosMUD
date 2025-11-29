import { describe, expect, it } from 'vitest';
import { render, screen } from '@testing-library/react';
import { PanelManager } from '../PanelManager';
import React from 'react';

describe('PanelManager', () => {
  it('should render children', () => {
    // Arrange & Act
    render(
      <PanelManager>
        <div data-testid="child">Child Content</div>
      </PanelManager>
    );

    // Assert
    expect(screen.getByTestId('child')).toBeInTheDocument();
    expect(screen.getByText('Child Content')).toBeInTheDocument();
  });

  it('should render multiple children', () => {
    // Arrange & Act
    render(
      <PanelManager>
        <div data-testid="child1">Child 1</div>
        <div data-testid="child2">Child 2</div>
      </PanelManager>
    );

    // Assert
    expect(screen.getByTestId('child1')).toBeInTheDocument();
    expect(screen.getByTestId('child2')).toBeInTheDocument();
  });

  it('should have proper CSS classes', () => {
    // Act
    const { container } = render(
      <PanelManager>
        <div>Test</div>
      </PanelManager>
    );

    // Assert
    const manager = container.firstChild as HTMLElement;
    expect(manager).toHaveClass('h-full', 'w-full');
  });

  it('should render with no children', () => {
    // Act & Assert - should not throw
    const { container } = render(<PanelManager>{null}</PanelManager>);
    expect(container.firstChild).toBeInTheDocument();
  });
});
