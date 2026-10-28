import { fireEvent, render, renderHook, screen } from '@testing-library/react';
import { useState } from 'react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { ThemeProvider } from '../../../../contexts/ThemeContext';
import { MainMenuModal } from '../../../MainMenuModal';
import type { GameClientV2MergedSlice } from '../gameClientV2ContainerTypes';
import { useGameClientV2ContainerEscapeMenuEffect } from '../useGameClientV2ContainerEscapeMenuEffect';

function buildSlice(overrides: {
  isMainMenuOpen?: boolean;
  showMap?: boolean;
  isDead?: boolean;
  setIsMainMenuOpen?: (value: boolean) => void;
}): GameClientV2MergedSlice {
  return {
    isMainMenuOpen: overrides.isMainMenuOpen ?? false,
    showMap: overrides.showMap ?? false,
    setIsMainMenuOpen: overrides.setIsMainMenuOpen ?? vi.fn(),
    gameState: { isDead: overrides.isDead ?? false },
  } as unknown as GameClientV2MergedSlice;
}

const pressEscape = () => fireEvent.keyDown(window, { key: 'Escape' });

describe('useGameClientV2ContainerEscapeMenuEffect', () => {
  afterEach(() => {
    localStorage.clear();
  });

  it('opens the menu on Escape when it is closed', () => {
    const setIsMainMenuOpen = vi.fn();
    renderHook(() => useGameClientV2ContainerEscapeMenuEffect(buildSlice({ setIsMainMenuOpen })));

    pressEscape();

    expect(setIsMainMenuOpen).toHaveBeenCalledWith(true);
  });

  it('ignores Escape while the menu is open (MainMenuModal owns it then)', () => {
    const setIsMainMenuOpen = vi.fn();
    renderHook(() => useGameClientV2ContainerEscapeMenuEffect(buildSlice({ isMainMenuOpen: true, setIsMainMenuOpen })));

    pressEscape();

    expect(setIsMainMenuOpen).not.toHaveBeenCalled();
  });

  it('ignores Escape while dead or while the map is showing', () => {
    const setIsMainMenuOpen = vi.fn();
    renderHook(() => useGameClientV2ContainerEscapeMenuEffect(buildSlice({ isDead: true, setIsMainMenuOpen })));
    renderHook(() => useGameClientV2ContainerEscapeMenuEffect(buildSlice({ showMap: true, setIsMainMenuOpen })));

    pressEscape();

    expect(setIsMainMenuOpen).not.toHaveBeenCalled();
  });

  it('ignores other keys', () => {
    const setIsMainMenuOpen = vi.fn();
    renderHook(() => useGameClientV2ContainerEscapeMenuEffect(buildSlice({ setIsMainMenuOpen })));

    fireEvent.keyDown(window, { key: 'Enter' });

    expect(setIsMainMenuOpen).not.toHaveBeenCalled();
  });

  it('stops listening on unmount', () => {
    const setIsMainMenuOpen = vi.fn();
    const { unmount } = renderHook(() => useGameClientV2ContainerEscapeMenuEffect(buildSlice({ setIsMainMenuOpen })));

    unmount();
    pressEscape();

    expect(setIsMainMenuOpen).not.toHaveBeenCalled();
  });

  // Regression: both this hook and MainMenuModal listen for Escape on window. The hook used to
  // toggle the menu, so Escape inside Settings closed the whole menu instead of stepping back.
  describe('with the real MainMenuModal', () => {
    function Harness() {
      const [isMainMenuOpen, setIsMainMenuOpen] = useState(false);
      useGameClientV2ContainerEscapeMenuEffect(buildSlice({ isMainMenuOpen, setIsMainMenuOpen }));
      return (
        <ThemeProvider>
          <MainMenuModal isOpen={isMainMenuOpen} onClose={() => setIsMainMenuOpen(false)} onLogoutClick={vi.fn()} />
        </ThemeProvider>
      );
    }

    it('Escape opens the menu, steps back out of Settings, then closes it', () => {
      render(<Harness />);
      expect(screen.queryByRole('dialog')).not.toBeInTheDocument();

      pressEscape();
      expect(screen.getByRole('heading', { name: 'Main Menu' })).toBeInTheDocument();

      fireEvent.click(screen.getByRole('button', { name: 'Settings' }));
      expect(screen.getByRole('heading', { name: 'Settings' })).toBeInTheDocument();

      pressEscape();
      expect(screen.getByRole('heading', { name: 'Main Menu' })).toBeInTheDocument();

      pressEscape();
      expect(screen.queryByRole('dialog')).not.toBeInTheDocument();
    });

    it('Escape can reopen the menu after it was closed', () => {
      render(<Harness />);

      pressEscape();
      pressEscape();
      expect(screen.queryByRole('dialog')).not.toBeInTheDocument();

      pressEscape();
      expect(screen.getByRole('heading', { name: 'Main Menu' })).toBeInTheDocument();
    });
  });
});
