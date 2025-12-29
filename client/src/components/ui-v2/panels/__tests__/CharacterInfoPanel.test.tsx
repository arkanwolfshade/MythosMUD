/**
 * Tests for CharacterInfoPanel component.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import type { HealthStatus } from '../../../../types/health';
import type { LucidityStatus } from '../../../../types/lucidity';
import { CharacterInfoPanel } from '../CharacterInfoPanel';
import type { Player } from '../../types';

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

  it('should render "No character information available" when player is null', () => {
    render(<CharacterInfoPanel player={null} healthStatus={null} lucidityStatus={null} />);
    expect(screen.getByText('No character information available')).toBeInTheDocument();
  });

  it('should render "No character information available" when player has no stats', () => {
    const playerWithoutStats = {
      id: 'player1',
      name: 'TestPlayer',
    } as Player;

    render(
      <CharacterInfoPanel
        player={playerWithoutStats}
        healthStatus={mockHealthStatus}
        lucidityStatus={mockLucidityStatus}
      />
    );
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
        wisdom: 10,
        charisma: 10,
      },
    };

    render(
      <CharacterInfoPanel player={player} healthStatus={mockHealthStatus} lucidityStatus={mockLucidityStatus} />
    );
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

    render(
      <CharacterInfoPanel player={player} healthStatus={mockHealthStatus} lucidityStatus={mockLucidityStatus} />
    );
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

    render(
      <CharacterInfoPanel player={player} healthStatus={mockHealthStatus} lucidityStatus={mockLucidityStatus} />
    );
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

    render(
      <CharacterInfoPanel player={player} healthStatus={mockHealthStatus} lucidityStatus={mockLucidityStatus} />
    );
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

    render(
      <CharacterInfoPanel player={player} healthStatus={mockHealthStatus} lucidityStatus={mockLucidityStatus} />
    );
    // Magic points meter should not be rendered
    expect(screen.queryByText(/Magic Points/i)).not.toBeInTheDocument();
  });
});
