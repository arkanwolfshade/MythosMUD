import React from 'react';
import { HealthMeter } from '../../health/HealthMeter';
import { SanityMeter } from '../../sanity/SanityMeter';
import type { Player } from '../types';
import type { HealthStatus } from '../../../types/health';
import type { SanityStatus } from '../../../types/sanity';

interface CharacterInfoPanelProps {
  player: Player | null;
  healthStatus: HealthStatus | null;
  sanityStatus: SanityStatus | null;
}

// Simplified character info panel without connection status and player name (moved to header)
// Based on findings from "Character State Display in Mythos Interfaces" - Dr. Armitage, 1928
export const CharacterInfoPanel: React.FC<CharacterInfoPanelProps> = ({ player, healthStatus, sanityStatus }) => {
  if (!player?.stats) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No character information available</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-4">
      {/* Health and Sanity Bars */}
      <div className="space-y-2">
        <HealthMeter status={healthStatus} />
        <SanityMeter status={sanityStatus} className="mt-2" />
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
        player.stats.intelligence !== undefined ||
        player.stats.wisdom !== undefined ||
        player.stats.charisma !== undefined) && (
        <div className="border-t border-mythos-terminal-border pt-2">
          <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Core Attributes:</h5>
          <div className="grid grid-cols-2 gap-1 text-sm">
            {player.stats.strength !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">STR:</span>
                <span className="text-mythos-terminal-text">{player.stats.strength}</span>
              </div>
            )}
            {player.stats.dexterity !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">DEX:</span>
                <span className="text-mythos-terminal-text">{player.stats.dexterity}</span>
              </div>
            )}
            {player.stats.constitution !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">CON:</span>
                <span className="text-mythos-terminal-text">{player.stats.constitution}</span>
              </div>
            )}
            {player.stats.intelligence !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">INT:</span>
                <span className="text-mythos-terminal-text">{player.stats.intelligence}</span>
              </div>
            )}
            {player.stats.wisdom !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">WIS:</span>
                <span className="text-mythos-terminal-text">{player.stats.wisdom}</span>
              </div>
            )}
            {player.stats.charisma !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">CHA:</span>
                <span className="text-mythos-terminal-text">{player.stats.charisma}</span>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Horror Stats */}
      {(player.stats.occult_knowledge !== undefined ||
        player.stats.fear !== undefined ||
        player.stats.corruption !== undefined ||
        player.stats.cult_affiliation !== undefined) && (
        <div className="border-t border-mythos-terminal-border pt-2">
          <h5 className="text-sm text-mythos-terminal-primary font-bold mb-1">Horror Stats:</h5>
          <div className="grid grid-cols-2 gap-1 text-sm">
            {player.stats.occult_knowledge !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">Occult:</span>
                <span className="text-mythos-terminal-text">{player.stats.occult_knowledge}</span>
              </div>
            )}
            {player.stats.fear !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">Fear:</span>
                <span className="text-mythos-terminal-text">{player.stats.fear}</span>
              </div>
            )}
            {player.stats.corruption !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">Corruption:</span>
                <span className="text-mythos-terminal-text">{player.stats.corruption}</span>
              </div>
            )}
            {player.stats.cult_affiliation !== undefined && (
              <div className="flex justify-between">
                <span className="text-mythos-terminal-text-secondary">Cult:</span>
                <span className="text-mythos-terminal-text">{player.stats.cult_affiliation}</span>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
