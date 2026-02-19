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

// Character info panel displays character name, profession, stats, and attributes
// Login username is displayed in the header; character name is displayed here
// Based on findings from "Character State Display in Mythos Interfaces" - Dr. Armitage, 1928
export const CharacterInfoPanel: React.FC<CharacterInfoPanelProps> = ({ player, healthStatus, lucidityStatus }) => {
  // Hooks must be called before any conditional returns
  // Extract values for clearer dependency tracking
  const magicPoints = player?.stats?.magic_points;
  const maxMagicPoints = player?.stats?.max_magic_points;

  const magicPointsStatus: MagicPointsStatus | null = useMemo(() => {
    if (magicPoints !== undefined && maxMagicPoints !== undefined && maxMagicPoints > 0) {
      return {
        current: magicPoints,
        max: maxMagicPoints,
      };
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
      {/* Character Name and Profession */}
      {player.name && (
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
      )}

      {/* Health, Lucidity, and Magic Points Bars */}
      <div className="space-y-2">
        <HealthMeter status={healthStatus} />
        <LucidityMeter status={lucidityStatus} className="mt-2" />
        <MagicPointsMeter status={magicPointsStatus} className="mt-2" />
        {player.level !== undefined && (
          <div className="flex items-center justify-between">
            <span className="text-base text-mythos-terminal-text-secondary">Level:</span>
            <span className="text-base text-mythos-terminal-text">{player.level}</span>
          </div>
        )}
        {player.xp !== undefined && (
          <div className="flex items-center justify-between">
            <span className="text-base text-mythos-terminal-text-secondary">XP:</span>
            <span className="text-base text-mythos-terminal-text">{player.xp}</span>
          </div>
        )}
        {player.stats.position && (
          <div className="flex items-center justify-between">
            <span className="text-base text-mythos-terminal-text-secondary">Posture:</span>
            <span className="text-base text-mythos-terminal-text">{player.stats.position}</span>
          </div>
        )}
        {player.in_combat !== undefined && (
          <div className="flex items-center justify-between">
            <span className="text-base text-mythos-terminal-text-secondary">In Combat:</span>
            <span
              className={`text-base ${player.in_combat ? 'text-mythos-terminal-error' : 'text-mythos-terminal-success'}`}
            >
              {player.in_combat ? 'Yes' : 'No'}
            </span>
          </div>
        )}
      </div>

      {/* Core Attributes */}
      {(player.stats.strength !== undefined ||
        player.stats.dexterity !== undefined ||
        player.stats.constitution !== undefined ||
        player.stats.size !== undefined ||
        player.stats.intelligence !== undefined ||
        player.stats.power !== undefined ||
        player.stats.education !== undefined ||
        player.stats.charisma !== undefined ||
        player.stats.luck !== undefined) && (
        <div className="border-t border-mythos-terminal-border pt-2">
          <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Core Attributes:</h5>
          <div className="grid grid-cols-2 gap-1 text-sm">
            {player.stats.strength !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">STR:</span>
                <span className="text-mythos-terminal-text">{player.stats.strength}</span>
              </div>
            )}
            {player.stats.dexterity !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">DEX:</span>
                <span className="text-mythos-terminal-text">{player.stats.dexterity}</span>
              </div>
            )}
            {player.stats.constitution !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">CON:</span>
                <span className="text-mythos-terminal-text">{player.stats.constitution}</span>
              </div>
            )}
            {player.stats.size !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">SIZ:</span>
                <span className="text-mythos-terminal-text">{player.stats.size}</span>
              </div>
            )}
            {player.stats.intelligence !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">INT:</span>
                <span className="text-mythos-terminal-text">{player.stats.intelligence}</span>
              </div>
            )}
            {player.stats.power !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">POW:</span>
                <span className="text-mythos-terminal-text">{player.stats.power}</span>
              </div>
            )}
            {player.stats.education !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">EDU:</span>
                <span className="text-mythos-terminal-text">{player.stats.education}</span>
              </div>
            )}
            {player.stats.charisma !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">CHA:</span>
                <span className="text-mythos-terminal-text">{player.stats.charisma}</span>
              </div>
            )}
            {player.stats.luck !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">LUCK:</span>
                <span className="text-mythos-terminal-text">{player.stats.luck}</span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Horror Stats */}
      {(player.stats.occult !== undefined || player.stats.corruption !== undefined) && (
        <div className="border-t border-mythos-terminal-border pt-2">
          <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Horror Stats:</h5>
          <div className="grid grid-cols-2 gap-1 text-sm">
            {player.stats.occult !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">Occult:</span>
                <span className="text-mythos-terminal-text">{player.stats.occult}</span>
              </div>
            )}
            {player.stats.corruption !== undefined && (
              <div className="flex items-center gap-2">
                <span className="text-mythos-terminal-text-secondary">Corruption:</span>
                <span className="text-mythos-terminal-text">{player.stats.corruption}</span>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
