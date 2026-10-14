/**
 * Tests for SettingsToggles component (#804).
 */

import { fireEvent, render, screen } from '@testing-library/react';
import type { ReactElement } from 'react';
import { beforeEach, describe, expect, it } from 'vitest';
import { ThemeProvider } from '../../contexts/ThemeContext';
import { SettingsToggles } from '../SettingsToggles';

function renderPanel(ui: ReactElement) {
  return render(<ThemeProvider>{ui}</ThemeProvider>);
}

describe('SettingsToggles', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('renders without a ThemeProvider crash and shows the corruption grain toggle', () => {
    renderPanel(<SettingsToggles />);
    expect(screen.getByTestId('settings-toggles')).toBeInTheDocument();
    expect(screen.getByLabelText('Corruption grain')).toBeInTheDocument();
  });

  it('defaults the corruption grain toggle to on', () => {
    renderPanel(<SettingsToggles />);
    const toggle = screen.getByLabelText('Corruption grain') as HTMLInputElement;
    expect(toggle.checked).toBe(true);
  });

  it('toggling corruption grain persists the preference to localStorage', () => {
    renderPanel(<SettingsToggles />);
    const toggle = screen.getByLabelText('Corruption grain') as HTMLInputElement;
    fireEvent.click(toggle);
    expect(toggle.checked).toBe(false);
    const saved = JSON.parse(localStorage.getItem('mythosmud-ui-preferences') ?? '{}');
    expect(saved.chatGrain).toBe(false);
  });

  it('adds a Text labels toggle (default off) that sets the class on <html> and persists', () => {
    renderPanel(<SettingsToggles />);
    const toggle = screen.getByLabelText('Text labels') as HTMLInputElement;
    expect(toggle.checked).toBe(false);
    fireEvent.click(toggle);
    expect(toggle.checked).toBe(true);
    expect(document.documentElement.classList.contains('text-labels')).toBe(true);
    expect(JSON.parse(localStorage.getItem('mythosmud-ui-preferences') ?? '{}').textLabels).toBe(true);
  });

  it('applies the High contrast toggle to <html>', () => {
    renderPanel(<SettingsToggles />);
    fireEvent.click(screen.getByLabelText('High contrast'));
    expect(document.documentElement.classList.contains('high-contrast')).toBe(true);
  });

  it('renders the other dormant preference toggles', () => {
    renderPanel(<SettingsToggles />);
    expect(screen.getByLabelText('Animations')).toBeInTheDocument();
    expect(screen.getByLabelText('Compact mode')).toBeInTheDocument();
    expect(screen.getByLabelText('High contrast')).toBeInTheDocument();
    expect(screen.getByLabelText('Reduced motion')).toBeInTheDocument();
    expect(screen.getByLabelText('Debug info')).toBeInTheDocument();
  });
});
