import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { MythosPanel } from './MythosPanel';

// Mock the EldritchIcon component
vi.mock('./EldritchIcon', () => ({
  EldritchIcon: ({ className }: { className?: string }) => (
    <div data-testid="eldritch-icon" className={className}>
      EldritchIcon
    </div>
  ),
}));

describe('MythosPanel', () => {
  it('should render with default props', () => {
    render(<MythosPanel>Test Content</MythosPanel>);

    expect(screen.getByText('Test Content')).toBeInTheDocument();
  });

  it('should render with custom title', () => {
    render(<MythosPanel title="Custom Title">Test Content</MythosPanel>);

    expect(screen.getByText('Custom Title')).toBeInTheDocument();
    expect(screen.getByText('Test Content')).toBeInTheDocument();
  });

  it('should render with custom subtitle', () => {
    render(
      <MythosPanel title="Test Title" subtitle="Custom Subtitle">
        Test Content
      </MythosPanel>
    );

    expect(screen.getByText('Custom Subtitle')).toBeInTheDocument();
    expect(screen.getByText('Test Content')).toBeInTheDocument();
  });

  it('should render with both custom title and subtitle', () => {
    render(
      <MythosPanel title="Custom Title" subtitle="Custom Subtitle">
        Test Content
      </MythosPanel>
    );

    expect(screen.getByText('Custom Title')).toBeInTheDocument();
    expect(screen.getByText('Custom Subtitle')).toBeInTheDocument();
    expect(screen.getByText('Test Content')).toBeInTheDocument();
  });

  it('should apply custom className', () => {
    render(<MythosPanel className="custom-class">Test Content</MythosPanel>);

    const panel = screen.getByText('Test Content').closest('div');
    expect(panel?.parentElement).toHaveClass('custom-class');
  });

  it('should render children content', () => {
    render(
      <MythosPanel>
        <div data-testid="child-content">Child Content</div>
      </MythosPanel>
    );

    expect(screen.getByTestId('child-content')).toBeInTheDocument();
    expect(screen.getByText('Child Content')).toBeInTheDocument();
  });

  it('should have proper styling classes', () => {
    render(<MythosPanel>Test Content</MythosPanel>);

    const panel = screen.getByText('Test Content').closest('div');
    expect(panel?.parentElement).toHaveClass('font-mono', 'border', 'rounded', 'bg-mythos-terminal-surface');
  });
});
