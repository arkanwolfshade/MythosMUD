/**
 * Tests for TabbedInterface component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { TabbedInterface } from '../TabbedInterface';

// Mock lucide-react
vi.mock('lucide-react', () => ({
  X: () => <span data-testid="close-icon">×</span>,
}));

describe('TabbedInterface', () => {
  const mockTabs = [
    { id: 'tab1', label: 'Tab 1', content: <div>Content 1</div> },
    { id: 'tab2', label: 'Tab 2', content: <div>Content 2</div> },
  ];

  it('should render with initial tabs', () => {
    render(<TabbedInterface initialTabs={mockTabs} />);
    expect(screen.getByText('Tab 1')).toBeInTheDocument();
    expect(screen.getByText('Tab 2')).toBeInTheDocument();
  });

  it('should render empty state when no tabs', () => {
    render(<TabbedInterface initialTabs={[]} />);
    expect(screen.getByText('No tabs open')).toBeInTheDocument();
  });

  it('should switch active tab when clicked', () => {
    render(<TabbedInterface initialTabs={mockTabs} />);
    expect(screen.getByText('Content 1')).toBeInTheDocument();

    fireEvent.click(screen.getByText('Tab 2'));
    expect(screen.getByText('Content 2')).toBeInTheDocument();
  });

  it('should close tab when close button is clicked', () => {
    render(<TabbedInterface initialTabs={mockTabs} />);
    const closeButtons = screen.getAllByTestId('close-icon');
    fireEvent.click(closeButtons[0].closest('button')!);

    expect(screen.queryByText('Tab 1')).not.toBeInTheDocument();
    expect(screen.getByText('Tab 2')).toBeInTheDocument();
  });

  it('should switch to another tab when active tab is closed', () => {
    render(<TabbedInterface initialTabs={mockTabs} />);
    const closeButtons = screen.getAllByTestId('close-icon');
    fireEvent.click(closeButtons[0].closest('button')!);

    expect(screen.getByText('Content 2')).toBeInTheDocument();
  });

  it('should call onTabsChange when tab is closed', () => {
    const onTabsChange = vi.fn();
    render(<TabbedInterface initialTabs={mockTabs} onTabsChange={onTabsChange} />);
    const closeButtons = screen.getAllByTestId('close-icon');
    fireEvent.click(closeButtons[0].closest('button')!);

    expect(onTabsChange).toHaveBeenCalledWith([mockTabs[1]]);
  });

  it('should not show tab bar when showTabBar is false', () => {
    render(<TabbedInterface initialTabs={mockTabs} showTabBar={false} />);
    expect(screen.queryByText('Tab 1')).not.toBeInTheDocument();
  });

  it('should handle non-closable tabs', () => {
    const tabsWithNonClosable = [
      { id: 'tab1', label: 'Tab 1', content: <div>Content 1</div>, closable: false },
      { id: 'tab2', label: 'Tab 2', content: <div>Content 2</div> },
    ];
    render(<TabbedInterface initialTabs={tabsWithNonClosable} />);
    const closeButtons = screen.getAllByTestId('close-icon');
    expect(closeButtons.length).toBe(1); // Only tab2 should have close button
  });
});
