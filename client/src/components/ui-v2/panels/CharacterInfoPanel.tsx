import React, { useMemo } from 'react';
import type { HealthStatus } from '../../../types/health';
import type { LucidityStatus } from '../../../types/lucidity';
import { HealthMeter } from '../../health/HealthMeter';
import { LucidityMeter } from '../../lucidity/LucidityMeter';
import { MagicPointsMeter, type MagicPointsStatus } from '../../magic/MagicPointsMeter';
import type { Player } from '../types';

interface CharacterInfoPanelProps {
  player: Player | null;
  healthStatus: HealthStatus | null;
  lucidityStatus: LucidityStatus | null;
}

function StatRow({ label, value }: { label: string; value: React.ReactNode }) {
  return (
    <div className="flex items-center justify-between">
      <span className="text-base text-mythos-terminal-text-secondary">{label}</span>
      <span className="text-base text-mythos-terminal-text">{value}</span>
    </div>
  );
}

function AttributeCell({ label, value }: { label: string; value: number }) {
  return (
    <div className="flex items-center gap-2">
      <span className="text-mythos-terminal-text-secondary">{label}:</span>
      <span className="text-mythos-terminal-text">{value}</span>
    </div>
  );
}

function CharacterIdentityHeader({ player }: { player: Player }) {
  if (!player.name) return null;
  return (
    <div className="border-b border-mythos-terminal-border pb-2">
      <div className="flex items-center justify-between">
        <span className="text-base text-mythos-terminal-text-secondary">Character:</span>
        <span className="text-base text-mythos-terminal-text font-bold" data-testid="current-character-name">
          {player.name}
        </span>
      </div>
      {player.profession_name && (
        <div className="flex items-center justify-between mt-1">
          <span className="text-sm text-mythos-terminal-text-secondary">Profession:</span>
          <span className="text-sm text-mythos-terminal-primary">{player.profession_name}</span>
        </div>
      )}
    </div>
  );
}

function CoreAttributesGrid({ stats }: { stats: NonNullable<Player['stats']> }) {
  const entries: Array<[string, number | undefined]> = [
    ['STR', stats.strength],
    ['DEX', stats.dexterity],
    ['CON', stats.constitution],
    ['SIZ', stats.size],
    ['INT', stats.intelligence],
    ['POW', stats.power],
    ['EDU', stats.education],
    ['CHA', stats.charisma],
    ['LUCK', stats.luck],
  ];
  const visible = entries.filter(([, value]) => value !== undefined);
  if (visible.length === 0) return null;

  return (
    <div className="border-t border-mythos-terminal-border pt-2">
      <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Core Attributes:</h5>
      <div className="grid grid-cols-2 gap-1 text-sm">
        {visible.map(([label, value]) => (
          <AttributeCell key={label} label={label} value={value as number} />
        ))}
      </div>
    </div>
  );
}

function HorrorStatsGrid({ stats }: { stats: NonNullable<Player['stats']> }) {
  if (stats.occult === undefined && stats.corruption === undefined) return null;
  return (
    <div className="border-t border-mythos-terminal-border pt-2">
      <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Horror Stats:</h5>
      <div className="grid grid-cols-2 gap-1 text-sm">
        {stats.occult !== undefined && <AttributeCell label="Occult" value={stats.occult} />}
        {stats.corruption !== undefined && <AttributeCell label="Corruption" value={stats.corruption} />}
      </div>
    </div>
  );
}

function CharacterStatusSection({
  player,
  healthStatus,
  lucidityStatus,
  magicPointsStatus,
}: {
  player: Player;
  healthStatus: HealthStatus | null;
  lucidityStatus: LucidityStatus | null;
  magicPointsStatus: MagicPointsStatus | null;
}) {
  return (
    <div className="space-y-2">
      <HealthMeter status={healthStatus} />
      <LucidityMeter status={lucidityStatus} className="mt-2" />
      <MagicPointsMeter status={magicPointsStatus} className="mt-2" />
      {player.level !== undefined && <StatRow label="Level:" value={player.level} />}
      {player.xp !== undefined && <StatRow label="XP:" value={player.xp} />}
      {player.stats?.position && (
        <StatRow label="Posture:" value={<span data-testid="player-posture">{player.stats.position}</span>} />
      )}
      {player.in_combat !== undefined && (
        <div className="flex items-center justify-between">
          <span className="text-base text-mythos-terminal-text-secondary inline-flex items-center gap-2">
            <span
              data-testid="combat-indicator-dot"
              aria-hidden="true"
              className={`w-2 h-2 rounded-full ${player.in_combat ? 'bg-mythos-terminal-error' : 'bg-mythos-terminal-border opacity-60'}`}
            />
            In Combat:
          </span>
          <span
            className={`text-base ${player.in_combat ? 'text-mythos-terminal-error' : 'text-mythos-terminal-success'}`}
          >
            {player.in_combat ? 'Yes' : 'No'}
          </span>
        </div>
      )}
    </div>
  );
}

export const CharacterInfoPanel: React.FC<CharacterInfoPanelProps> = ({ player, healthStatus, lucidityStatus }) => {
  const magicPoints = player?.stats?.magic_points;
  const maxMagicPoints = player?.stats?.max_magic_points;
  const magicPointsStatus: MagicPointsStatus | null = useMemo(() => {
    if (magicPoints !== undefined && maxMagicPoints !== undefined && maxMagicPoints > 0) {
      return { current: magicPoints, max: maxMagicPoints };
    }
    return null;
  }, [magicPoints, maxMagicPoints]);

  if (!player?.stats) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No character information available</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-4">
      <CharacterIdentityHeader player={player} />
      <CharacterStatusSection
        player={player}
        healthStatus={healthStatus}
        lucidityStatus={lucidityStatus}
        magicPointsStatus={magicPointsStatus}
      />
      <CoreAttributesGrid stats={player.stats} />
      <HorrorStatsGrid stats={player.stats} />
    </div>
  );
};
