/**
 * Tests for CharacterInfoPanel component.
 */

import '@testing-library/jest-dom/vitest';
import { render, screen } from '@testing-library/react';
import React from 'react';
import { describe, expect, it } from 'vitest';
import type { HealthStatus } from '../../../../types/health';
import type { LucidityStatus } from '../../../../types/lucidity';
import type { Player } from '../../types';
import { CharacterInfoPanel } from '../CharacterInfoPanel';

describe('CharacterInfoPanel', () => {
  const mockHealthStatus: HealthStatus = {
    current: 100,
    max: 100,
    tier: 'vigorous',
    posture: 'standing',
    inCombat: false,
  };

  const mockLucidityStatus: LucidityStatus = {
    current: 50,
    max: 100,
    tier: 'lucid',
    liabilities: [],
  };

  /** Dedupe CharacterInfoPanel render + default health/lucidity fixtures. */
  function renderCharacterPanel(
    player: Player | null,
    overrides: Partial<{
      healthStatus: HealthStatus | null;
      lucidityStatus: LucidityStatus | null;
    }> = {}
  ) {
    return render(
      <CharacterInfoPanel
        player={player}
        healthStatus={overrides.healthStatus !== undefined ? overrides.healthStatus : mockHealthStatus}
        lucidityStatus={overrides.lucidityStatus !== undefined ? overrides.lucidityStatus : mockLucidityStatus}
      />
    );
  }

  it('should render "No character information available" when player is null', () => {
    renderCharacterPanel(null, { healthStatus: null, lucidityStatus: null });
    expect(screen.getByText('No character information available')).toBeInTheDocument();
  });

  it('should render "No character information available" when player has no stats', () => {
    const playerWithoutStats = {
      id: 'player1',
      name: 'TestPlayer',
    } as Player;

    renderCharacterPanel(playerWithoutStats);
    expect(screen.getByText('No character information available')).toBeInTheDocument();
  });

  it('should render character name when player has stats', () => {
    const player: Player = {
      id: 'player1',
      name: 'TestPlayer',
      stats: {
        current_dp: 100,
        max_dp: 100,
        lucidity: 50,
        strength: 10,
        dexterity: 10,
        constitution: 10,
        intelligence: 10,
        power: 10,
        charisma: 10,
      },
    };

    renderCharacterPanel(player);
    expect(screen.getByText('TestPlayer')).toBeInTheDocument();
  });

  it('should render profession when available', () => {
    const player: Player = {
      id: 'player1',
      name: 'TestPlayer',
      profession_name: 'Professor',
      stats: {
        current_dp: 100,
        max_dp: 100,
        lucidity: 50,
      },
    };

    renderCharacterPanel(player);
    expect(screen.getByText('Professor')).toBeInTheDocument();
  });

  it('should render level when available', () => {
    const player: Player = {
      id: 'player1',
      name: 'TestPlayer',
      level: 5,
      stats: {
        current_dp: 100,
        max_dp: 100,
        lucidity: 50,
      },
    };

    renderCharacterPanel(player);
    expect(screen.getByText('5')).toBeInTheDocument();
  });

  it('should render magic points meter when magic points are available', () => {
    const player: Player = {
      id: 'player1',
      name: 'TestPlayer',
      stats: {
        current_dp: 100,
        max_dp: 100,
        lucidity: 50,
        magic_points: 25,
        max_magic_points: 50,
      },
    };

    renderCharacterPanel(player);
    // Magic points meter should be rendered
    expect(screen.getByText(/Magic Points/i)).toBeInTheDocument();
  });

  it('should not render magic points meter when magic points are not available', () => {
    const player: Player = {
      id: 'player1',
      name: 'TestPlayer',
      stats: {
        current_dp: 100,
        max_dp: 100,
        lucidity: 50,
      },
    };

    renderCharacterPanel(player);
    // Magic points meter should not be rendered
    expect(screen.queryByText(/Magic Points/i)).not.toBeInTheDocument();
  });

  it('should show a combat indicator dot when in_combat is true', () => {
    const player: Player = {
      id: 'player1',
      name: 'TestPlayer',
      in_combat: true,
      stats: {
        current_dp: 100,
        max_dp: 100,
        lucidity: 50,
      },
    };

    renderCharacterPanel(player);

    const dot = screen.getByTestId('combat-indicator-dot');
    expect(dot).toHaveClass('bg-mythos-terminal-error');
  });
});
