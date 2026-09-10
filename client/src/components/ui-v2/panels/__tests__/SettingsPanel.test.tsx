/**
 * Tests for SettingsPanel component (#804).
 */

import { fireEvent, render, screen } from '@testing-library/react';
import type { ReactElement } from 'react';
import { beforeEach, describe, expect, it } from 'vitest';
import { ThemeProvider } from '../../../../contexts/ThemeContext';
import { SettingsPanel } from '../SettingsPanel';

function renderPanel(ui: ReactElement) {
  return render(<ThemeProvider>{ui}</ThemeProvider>);
}

describe('SettingsPanel', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('renders without a ThemeProvider crash and shows the corruption grain toggle', () => {
    renderPanel(<SettingsPanel />);
    expect(screen.getByTestId('settings-panel')).toBeInTheDocument();
    expect(screen.getByLabelText('Corruption grain')).toBeInTheDocument();
  });

  it('defaults the corruption grain toggle to on', () => {
    renderPanel(<SettingsPanel />);
    const toggle = screen.getByLabelText('Corruption grain') as HTMLInputElement;
    expect(toggle.checked).toBe(true);
  });

  it('toggling corruption grain persists the preference to localStorage', () => {
    renderPanel(<SettingsPanel />);
    const toggle = screen.getByLabelText('Corruption grain') as HTMLInputElement;
    fireEvent.click(toggle);
    expect(toggle.checked).toBe(false);
    const saved = JSON.parse(localStorage.getItem('mythosmud-ui-preferences') ?? '{}');
    expect(saved.chatGrain).toBe(false);
  });

  it('renders the other dormant preference toggles', () => {
    renderPanel(<SettingsPanel />);
    expect(screen.getByLabelText('Animations')).toBeInTheDocument();
    expect(screen.getByLabelText('Compact mode')).toBeInTheDocument();
    expect(screen.getByLabelText('High contrast')).toBeInTheDocument();
    expect(screen.getByLabelText('Reduced motion')).toBeInTheDocument();
    expect(screen.getByLabelText('Debug info')).toBeInTheDocument();
  });
});
