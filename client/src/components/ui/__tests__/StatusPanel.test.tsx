import { render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  AllStats,
  CommandsCount,
  ConnectionStatus,
  CoreAttributes,
  HealthStat,
  HorrorStats,
  MessagesCount,
  PlayerName,
  PlayerStats,
  LucidityStat,
  StatusPanel,
} from '../StatusPanel';

describe('StatusPanel Compound Component', () => {
  const defaultProps = {
    player: {
      id: 'player-1',
      name: 'TestPlayer',
      stats: {
        current_health: 100,
        max_health: 100,
        lucidity: 80,
        strength: 10,
        dexterity: 12,
        constitution: 14,
        intelligence: 16,
        wisdom: 13,
        charisma: 15,
        occult_knowledge: 5,
        fear: 2,
        corruption: 1,
        cult_affiliation: 0,
      },
      level: 5,
    },
    isConnected: true,
    isConnecting: false,
    playerName: 'TestPlayer',
    messagesCount: 5,
    commandsCount: 10,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('StatusPanel Provider', () => {
    it('should provide context to child components', () => {
      render(
        <StatusPanel {...defaultProps}>
          <ConnectionStatus />
        </StatusPanel>
      );

      expect(screen.getByText('Connected')).toBeInTheDocument();
    });

    it('should throw error when child components are used outside provider', () => {
      // Suppress console.error for this test
      const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      expect(() => {
        render(<ConnectionStatus />);
      }).toThrow('useStatusPanel must be used within a StatusPanel');

      consoleSpy.mockRestore();
    });
  });

  describe('ConnectionStatus', () => {
    it('should display connected status', () => {
      render(
        <StatusPanel {...defaultProps}>
          <ConnectionStatus />
        </StatusPanel>
      );

      expect(screen.getByText('Connection:')).toBeInTheDocument();
      expect(screen.getByText('Connected')).toBeInTheDocument();
    });

    it('should display disconnected status', () => {
      render(
        <StatusPanel {...defaultProps} isConnected={false} isConnecting={false}>
          <ConnectionStatus />
        </StatusPanel>
      );

      expect(screen.getByText('Disconnected')).toBeInTheDocument();
    });

    it('should display connecting status', () => {
      render(
        <StatusPanel {...defaultProps} isConnected={false} isConnecting={true}>
          <ConnectionStatus />
        </StatusPanel>
      );

      expect(screen.getByText('Connecting...')).toBeInTheDocument();
    });
  });

  describe('PlayerName', () => {
    it('should display player name', () => {
      render(
        <StatusPanel {...defaultProps}>
          <PlayerName />
        </StatusPanel>
      );

      expect(screen.getByText('Player:')).toBeInTheDocument();
      expect(screen.getByText('TestPlayer')).toBeInTheDocument();
    });
  });

  describe('HealthStat', () => {
    it('should display health when player has stats', () => {
      render(
        <StatusPanel {...defaultProps}>
          <HealthStat />
        </StatusPanel>
      );

      expect(screen.getByText('Health:')).toBeInTheDocument();
      expect(screen.getByText('100 / 100')).toBeInTheDocument();
    });

    it('should not display when player has no stats', () => {
      render(
        <StatusPanel {...defaultProps} player={null}>
          <HealthStat />
        </StatusPanel>
      );

      expect(screen.queryByText('Health:')).not.toBeInTheDocument();
    });

    it('should not display when player has no health stat', () => {
      const playerWithoutHealth = {
        ...defaultProps.player,
        stats: { ...defaultProps.player.stats, current_health: undefined },
      };

      render(
        <StatusPanel {...defaultProps} player={playerWithoutHealth}>
          <HealthStat />
        </StatusPanel>
      );

      expect(screen.queryByText('Health:')).not.toBeInTheDocument();
    });
  });

  describe('LucidityStat', () => {
    it('should display lucidity when player has stats', () => {
      render(
        <StatusPanel {...defaultProps}>
          <LucidityStat />
        </StatusPanel>
      );

      expect(screen.getByText('lucidity:')).toBeInTheDocument();
      expect(screen.getByText('80')).toBeInTheDocument();
    });

    it('should not display when player has no stats', () => {
      render(
        <StatusPanel {...defaultProps} player={null}>
          <LucidityStat />
        </StatusPanel>
      );

      expect(screen.queryByText('lucidity:')).not.toBeInTheDocument();
    });
  });

  describe('CoreAttributes', () => {
    it('should display all core attributes when available', () => {
      render(
        <StatusPanel {...defaultProps}>
          <CoreAttributes />
        </StatusPanel>
      );

      expect(screen.getByText('Core Attributes:')).toBeInTheDocument();
      expect(screen.getByText('STR:')).toBeInTheDocument();
      expect(screen.getByText('10')).toBeInTheDocument();
      expect(screen.getByText('DEX:')).toBeInTheDocument();
      expect(screen.getByText('12')).toBeInTheDocument();
      expect(screen.getByText('CON:')).toBeInTheDocument();
      expect(screen.getByText('14')).toBeInTheDocument();
      expect(screen.getByText('INT:')).toBeInTheDocument();
      expect(screen.getByText('16')).toBeInTheDocument();
      expect(screen.getByText('WIS:')).toBeInTheDocument();
      expect(screen.getByText('13')).toBeInTheDocument();
      expect(screen.getByText('CHA:')).toBeInTheDocument();
      expect(screen.getByText('15')).toBeInTheDocument();
    });

    it('should not display when player has no stats', () => {
      render(
        <StatusPanel {...defaultProps} player={null}>
          <CoreAttributes />
        </StatusPanel>
      );

      expect(screen.queryByText('Core Attributes:')).not.toBeInTheDocument();
    });

    it('should only display available attributes', () => {
      const playerWithLimitedStats = {
        ...defaultProps.player,
        stats: {
          current_health: 100,
          lucidity: 80,
          strength: 10,
          dexterity: 12,
        },
      };

      render(
        <StatusPanel {...defaultProps} player={playerWithLimitedStats}>
          <CoreAttributes />
        </StatusPanel>
      );

      expect(screen.getByText('STR:')).toBeInTheDocument();
      expect(screen.getByText('DEX:')).toBeInTheDocument();
      expect(screen.queryByText('CON:')).not.toBeInTheDocument();
      expect(screen.queryByText('INT:')).not.toBeInTheDocument();
    });
  });

  describe('HorrorStats', () => {
    it('should display all horror stats when available', () => {
      render(
        <StatusPanel {...defaultProps}>
          <HorrorStats />
        </StatusPanel>
      );

      expect(screen.getByText('Horror Stats:')).toBeInTheDocument();
      expect(screen.getByText('Occult:')).toBeInTheDocument();
      expect(screen.getByText('5')).toBeInTheDocument();
      expect(screen.getByText('Fear:')).toBeInTheDocument();
      expect(screen.getByText('2')).toBeInTheDocument();
      expect(screen.getByText('Corruption:')).toBeInTheDocument();
      expect(screen.getByText('1')).toBeInTheDocument();
      expect(screen.getByText('Cult:')).toBeInTheDocument();
      expect(screen.getByText('0')).toBeInTheDocument();
    });

    it('should not display when player has no stats', () => {
      render(
        <StatusPanel {...defaultProps} player={null}>
          <HorrorStats />
        </StatusPanel>
      );

      expect(screen.queryByText('Horror Stats:')).not.toBeInTheDocument();
    });

    it('should only display available horror stats', () => {
      const playerWithLimitedHorrorStats = {
        ...defaultProps.player,
        stats: {
          current_health: 100,
          lucidity: 80,
          occult_knowledge: 5,
          fear: 2,
        },
      };

      render(
        <StatusPanel {...defaultProps} player={playerWithLimitedHorrorStats}>
          <HorrorStats />
        </StatusPanel>
      );

      expect(screen.getByText('Occult:')).toBeInTheDocument();
      expect(screen.getByText('Fear:')).toBeInTheDocument();
      expect(screen.queryByText('Corruption:')).not.toBeInTheDocument();
      expect(screen.queryByText('Cult:')).not.toBeInTheDocument();
    });
  });

  describe('MessagesCount', () => {
    it('should display messages count', () => {
      render(
        <StatusPanel {...defaultProps}>
          <MessagesCount />
        </StatusPanel>
      );

      expect(screen.getByText('Messages:')).toBeInTheDocument();
      expect(screen.getByText('5')).toBeInTheDocument();
    });
  });

  describe('CommandsCount', () => {
    it('should display commands count', () => {
      render(
        <StatusPanel {...defaultProps}>
          <CommandsCount />
        </StatusPanel>
      );

      expect(screen.getByText('Commands:')).toBeInTheDocument();
      expect(screen.getByText('10')).toBeInTheDocument();
    });
  });

  describe('PlayerStats', () => {
    it('should display all player stats when available', () => {
      render(
        <StatusPanel {...defaultProps}>
          <PlayerStats />
        </StatusPanel>
      );

      expect(screen.getByText('Health:')).toBeInTheDocument();
      expect(screen.getByText('lucidity:')).toBeInTheDocument();
      expect(screen.getByText('Core Attributes:')).toBeInTheDocument();
      expect(screen.getByText('Horror Stats:')).toBeInTheDocument();
    });

    it('should not display when player has no stats', () => {
      render(
        <StatusPanel {...defaultProps} player={null}>
          <PlayerStats />
        </StatusPanel>
      );

      expect(screen.queryByText('Health:')).not.toBeInTheDocument();
      expect(screen.queryByText('lucidity:')).not.toBeInTheDocument();
    });
  });

  describe('AllStats', () => {
    it('should display all status information', () => {
      render(
        <StatusPanel {...defaultProps}>
          <AllStats />
        </StatusPanel>
      );

      expect(screen.getByText('Connection:')).toBeInTheDocument();
      expect(screen.getByText('Player:')).toBeInTheDocument();
      expect(screen.getByText('Health:')).toBeInTheDocument();
      expect(screen.getByText('lucidity:')).toBeInTheDocument();
      expect(screen.getByText('Core Attributes:')).toBeInTheDocument();
      expect(screen.getByText('Horror Stats:')).toBeInTheDocument();
      expect(screen.getByText('Messages:')).toBeInTheDocument();
      expect(screen.getByText('Commands:')).toBeInTheDocument();
    });
  });

  describe('Custom Composition', () => {
    it('should allow custom composition of components', () => {
      render(
        <StatusPanel {...defaultProps}>
          <ConnectionStatus />
          <PlayerName />
          <HealthStat />
          <MessagesCount />
        </StatusPanel>
      );

      expect(screen.getByText('Connection:')).toBeInTheDocument();
      expect(screen.getByText('Player:')).toBeInTheDocument();
      expect(screen.getByText('Health:')).toBeInTheDocument();
      expect(screen.getByText('Messages:')).toBeInTheDocument();
      // Should not display components not included
      expect(screen.queryByText('lucidity:')).not.toBeInTheDocument();
      expect(screen.queryByText('Commands:')).not.toBeInTheDocument();
    });
  });
});
