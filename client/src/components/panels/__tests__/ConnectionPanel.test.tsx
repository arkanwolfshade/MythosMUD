/**
 * Tests for ConnectionPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { ConnectionPanel } from '../ConnectionPanel';

// Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
};

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock,
});

describe('ConnectionPanel', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorageMock.getItem.mockReturnValue(null);
  });

  it('should render with default placeholder text', () => {
    render(<ConnectionPanel />);
    expect(screen.getByText('Connection Panel')).toBeInTheDocument();
  });

  it('should render with custom placeholder text', () => {
    render(<ConnectionPanel placeholderText="Custom Panel Title" />);
    expect(screen.getByText('Custom Panel Title')).toBeInTheDocument();
  });

  it('should render tick verbosity checkbox', () => {
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i);
    expect(checkbox).toBeInTheDocument();
  });

  it('should initialize checkbox from localStorage', () => {
    localStorageMock.getItem.mockReturnValue('true');
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;
    expect(checkbox.checked).toBe(true);
  });

  it('should initialize checkbox as unchecked when localStorage is false', () => {
    localStorageMock.getItem.mockReturnValue('false');
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;
    expect(checkbox.checked).toBe(false);
  });

  it('should initialize checkbox as unchecked when localStorage is null', () => {
    localStorageMock.getItem.mockReturnValue(null);
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;
    expect(checkbox.checked).toBe(false);
  });

  it('should toggle checkbox and update localStorage', () => {
    localStorageMock.getItem.mockReturnValue('false');
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;

    expect(checkbox.checked).toBe(false);
    fireEvent.click(checkbox);

    expect(checkbox.checked).toBe(true);
    expect(localStorageMock.setItem).toHaveBeenCalledWith('showTickVerbosity', 'true');
  });

  it('should toggle checkbox from true to false', () => {
    localStorageMock.getItem.mockReturnValue('true');
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;

    expect(checkbox.checked).toBe(true);
    fireEvent.click(checkbox);

    expect(checkbox.checked).toBe(false);
    expect(localStorageMock.setItem).toHaveBeenCalledWith('showTickVerbosity', 'false');
  });

  it('should show explanation text when checkbox is checked', () => {
    localStorageMock.getItem.mockReturnValue('true');
    render(<ConnectionPanel />);
    expect(screen.getByText(/Game ticks will be displayed in the terminal every 10 ticks/i)).toBeInTheDocument();
  });

  it('should not show explanation text when checkbox is unchecked', () => {
    localStorageMock.getItem.mockReturnValue('false');
    render(<ConnectionPanel />);
    expect(screen.queryByText(/Game ticks will be displayed in the terminal every 10 ticks/i)).not.toBeInTheDocument();
  });

  it('should show explanation text after checking checkbox', () => {
    localStorageMock.getItem.mockReturnValue('false');
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;

    expect(screen.queryByText(/Game ticks will be displayed in the terminal every 10 ticks/i)).not.toBeInTheDocument();

    fireEvent.click(checkbox);

    expect(screen.getByText(/Game ticks will be displayed in the terminal every 10 ticks/i)).toBeInTheDocument();
  });

  it('should hide explanation text after unchecking checkbox', () => {
    localStorageMock.getItem.mockReturnValue('true');
    render(<ConnectionPanel />);
    const checkbox = screen.getByLabelText(/Show Game Tick Verbosity/i) as HTMLInputElement;

    expect(screen.getByText(/Game ticks will be displayed in the terminal every 10 ticks/i)).toBeInTheDocument();

    fireEvent.click(checkbox);

    expect(screen.queryByText(/Game ticks will be displayed in the terminal every 10 ticks/i)).not.toBeInTheDocument();
  });
});
