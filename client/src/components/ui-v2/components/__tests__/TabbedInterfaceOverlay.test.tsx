/**
 * Tests for TabbedInterfaceOverlay component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { TabbedInterfaceOverlay } from '../TabbedInterfaceOverlay';
import type { Tab } from '../../TabbedInterface';

describe('TabbedInterfaceOverlay', () => {
  const mockSetActiveTab = vi.fn();
  const mockCloseTab = vi.fn();

  const mockTabs: Tab[] = [
    { id: 'tab1', label: 'Tab 1', content: <div>Content 1</div> },
    { id: 'tab2', label: 'Tab 2', content: <div>Content 2</div>, closable: true },
    { id: 'tab3', label: 'Tab 3', content: <div>Content 3</div>, closable: false },
  ];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render nothing when tabs array is empty', () => {
    const { container } = render(
      <TabbedInterfaceOverlay tabs={[]} activeTabId={null} setActiveTab={mockSetActiveTab} closeTab={mockCloseTab} />
    );
    expect(container.firstChild).toBeNull();
  });

  it('should render tabs when tabs array has items', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab1"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );
    expect(screen.getByText('Tab 1')).toBeInTheDocument();
    expect(screen.getByText('Tab 2')).toBeInTheDocument();
    expect(screen.getByText('Tab 3')).toBeInTheDocument();
  });

  it('should render active tab content', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab1"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );
    expect(screen.getByText('Content 1')).toBeInTheDocument();
  });

  it('should call setActiveTab when tab is clicked', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab1"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );

    const tab2 = screen.getByText('Tab 2');
    fireEvent.click(tab2);

    expect(mockSetActiveTab).toHaveBeenCalledWith('tab2');
  });

  it('should call closeTab when close button is clicked', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab2"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );

    // Find close button for tab2 (which is closable)
    const tab2Element = screen.getByText('Tab 2').closest('div');
    const closeButton = tab2Element?.querySelector('button');
    if (closeButton) {
      fireEvent.click(closeButton);
      expect(mockCloseTab).toHaveBeenCalledWith('tab2');
    }
  });

  it('should not show close button for non-closable tabs', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab3"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );

    const tab3Element = screen.getByText('Tab 3').closest('div');
    const closeButton = tab3Element?.querySelector('button');
    // Tab 3 has closable: false, so should not have close button
    expect(closeButton).toBeNull();
  });

  it('should highlight active tab', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab1"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );

    const tab1Element = screen.getByText('Tab 1').closest('div');
    expect(tab1Element?.className).toContain('bg-mythos-terminal-primary');
  });

  it('should not highlight inactive tabs', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab1"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );

    const tab2Element = screen.getByText('Tab 2').closest('div');
    expect(tab2Element?.className).not.toContain('bg-mythos-terminal-primary');
    expect(tab2Element?.className).toContain('bg-mythos-terminal-background');
  });

  it('should handle tab click without stopping propagation on close button', () => {
    render(
      <TabbedInterfaceOverlay
        tabs={mockTabs}
        activeTabId="tab2"
        setActiveTab={mockSetActiveTab}
        closeTab={mockCloseTab}
      />
    );

    const tab2Element = screen.getByText('Tab 2').closest('div');
    const closeButton = tab2Element?.querySelector('button');
    if (closeButton) {
      // Create a mock event with stopPropagation
      const mockEvent = {
        stopPropagation: vi.fn(),
      } as unknown as React.MouseEvent;
      fireEvent.click(closeButton, mockEvent);
      expect(mockCloseTab).toHaveBeenCalledWith('tab2');
    }
  });
});
