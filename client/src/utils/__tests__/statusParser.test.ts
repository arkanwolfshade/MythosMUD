import { describe, expect, it } from 'vitest';
import type { ParsedPlayerData } from '../statusParser';
import { convertToPlayerInterface, parseStatusResponse } from '../statusParser';

describe('Status Parser Utilities', () => {
  describe('parseStatusResponse', () => {
    it('should parse name from status response', () => {
      // Arrange
      const statusResponse = 'Name: TestPlayer\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.name).toBe('TestPlayer');
    });

    it('should parse location from status response', () => {
      // Arrange
      const statusResponse = 'Location: Arkham City - Library\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.location).toBe('Arkham City - Library');
    });

    it('should parse health from status response', () => {
      // Arrange
      const statusResponse = 'Health: 85/100\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.health).toEqual({ current: 85, max: 100 });
    });

    it('should parse lucidity from status response', () => {
      // Arrange
      const statusResponse = 'lucidity: 70/100\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.lucidity).toEqual({ current: 70, max: 100 });
    });

    it('should parse profession information', () => {
      // Arrange
      const statusResponse = `Profession: Investigator
Description: A seeker of truth
Background: You have seen things...\n`;

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.profession).toBeDefined();
      expect(parsed.profession?.name).toBe('Investigator');
      expect(parsed.profession?.description).toBe('A seeker of truth');
      expect(parsed.profession?.flavor_text).toBe('You have seen things...');
    });

    it('should parse numeric stats', () => {
      // Arrange
      const statusResponse = `Fear: 25
Corruption: 10
Occult Knowledge: 50\n`;

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.fear).toBe(25);
      expect(parsed.corruption).toBe(10);
      expect(parsed.occult_knowledge).toBe(50);
    });

    it('should parse position', () => {
      // Arrange
      const statusResponse = 'Position: Standing\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.position).toBe('standing');
    });

    it('should parse combat status', () => {
      // Arrange
      const statusResponse = 'In Combat: Yes\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.in_combat).toBe(true);
    });

    it('should parse XP', () => {
      // Arrange
      const statusResponse = 'XP: 1500\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.xp).toBe(1500);
    });

    it('should parse complete status response', () => {
      // Arrange
      const statusResponse = `Name: TestPlayer
Location: Arkham City - Library
Health: 85/100
lucidity: 70/100
Profession: Investigator
Description: A seeker of truth
Background: You have seen things...
Fear: 25
Corruption: 10
Occult Knowledge: 50
Position: Standing
In Combat: No
XP: 1500\n`;

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.name).toBe('TestPlayer');
      expect(parsed.location).toBe('Arkham City - Library');
      expect(parsed.health).toEqual({ current: 85, max: 100 });
      expect(parsed.lucidity).toEqual({ current: 70, max: 100 });
      expect(parsed.profession?.name).toBe('Investigator');
      expect(parsed.fear).toBe(25);
      expect(parsed.corruption).toBe(10);
      expect(parsed.occult_knowledge).toBe(50);
      expect(parsed.position).toBe('standing');
      expect(parsed.in_combat).toBe(false);
      expect(parsed.xp).toBe(1500);
    });

    it('should handle empty status response', () => {
      // Arrange
      const statusResponse = '';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed).toEqual({});
    });

    it('should handle status response with extra whitespace', () => {
      // Arrange
      const statusResponse = '  Name:  TestPlayer  \n  Health:  85  /  100  \n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.name).toBe('TestPlayer');
      expect(parsed.health).toEqual({ current: 85, max: 100 });
    });

    it('should handle invalid health format gracefully', () => {
      // Arrange
      const statusResponse = 'Health: invalid\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.health).toBeUndefined();
    });

    it('should handle invalid numeric stats gracefully', () => {
      // Arrange
      const statusResponse = 'Fear: invalid\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.fear).toBeUndefined();
    });

    it('should handle profession description without profession name', () => {
      // Arrange
      const statusResponse = 'Description: Some description\n';

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.profession).toBeUndefined();
    });

    it('should handle multiline status response', () => {
      // Arrange
      const statusResponse = `Name: TestPlayer
Location: Arkham City

Health: 85/100
lucidity: 70/100

Profession: Investigator`;

      // Act
      const parsed = parseStatusResponse(statusResponse);

      // Assert
      expect(parsed.name).toBe('TestPlayer');
      expect(parsed.location).toBe('Arkham City');
      expect(parsed.health).toEqual({ current: 85, max: 100 });
    });
  });

  describe('convertToPlayerInterface', () => {
    it('should convert parsed data to player interface', () => {
      // Arrange
      const parsedData: ParsedPlayerData = {
        name: 'TestPlayer',
        location: 'Arkham City',
        health: { current: 85, max: 100 },
        lucidity: { current: 70, max: 100 },
        profession: {
          name: 'Investigator',
          description: 'A seeker of truth',
          flavor_text: 'You have seen things...',
        },
        fear: 25,
        corruption: 10,
        occult_knowledge: 50,
        position: 'standing',
        in_combat: false,
        xp: 1500,
      };

      // Act
      const player = convertToPlayerInterface(parsedData);

      // Assert
      expect(player.name).toBe('TestPlayer');
      expect(player.profession_name).toBe('Investigator');
      expect(player.profession_description).toBe('A seeker of truth');
      expect(player.profession_flavor_text).toBe('You have seen things...');
      expect(player.stats.current_dp).toBe(85);
      expect(player.stats.max_dp).toBe(100);
      expect(player.stats.lucidity).toBe(70);
      expect(player.stats.max_lucidity).toBe(100);
      expect(player.stats.fear).toBe(25);
      expect(player.stats.corruption).toBe(10);
      expect(player.stats.occult_knowledge).toBe(50);
      expect(player.position).toBe('standing');
      expect(player.in_combat).toBe(false);
      expect(player.xp).toBe(1500);
    });

    it('should use defaults for missing data', () => {
      // Arrange
      const parsedData: ParsedPlayerData = {
        name: 'TestPlayer',
      };

      // Act
      const player = convertToPlayerInterface(parsedData);

      // Assert
      expect(player.name).toBe('TestPlayer');
      expect(player.stats.current_dp).toBe(100);
      expect(player.stats.max_dp).toBe(100);
      expect(player.stats.lucidity).toBe(100);
      expect(player.stats.max_lucidity).toBe(100);
      expect(player.stats.fear).toBe(0);
      expect(player.stats.corruption).toBe(0);
      expect(player.stats.occult_knowledge).toBe(0);
    });

    it('should handle missing name', () => {
      // Arrange
      const parsedData: ParsedPlayerData = {};

      // Act
      const player = convertToPlayerInterface(parsedData);

      // Assert
      expect(player.name).toBe('');
    });

    it('should handle missing profession', () => {
      // Arrange
      const parsedData: ParsedPlayerData = {
        name: 'TestPlayer',
      };

      // Act
      const player = convertToPlayerInterface(parsedData);

      // Assert
      expect(player.profession_name).toBeUndefined();
      expect(player.profession_description).toBeUndefined();
      expect(player.profession_flavor_text).toBeUndefined();
    });

    it('should handle missing optional fields', () => {
      // Arrange
      const parsedData: ParsedPlayerData = {
        name: 'TestPlayer',
        health: { current: 85, max: 100 },
      };

      // Act
      const player = convertToPlayerInterface(parsedData);

      // Assert
      expect(player.in_combat).toBeUndefined();
      expect(player.xp).toBeUndefined();
    });

    it('should preserve position in stats', () => {
      // Arrange
      const parsedData: ParsedPlayerData = {
        name: 'TestPlayer',
        position: 'sitting',
      };

      // Act
      const player = convertToPlayerInterface(parsedData);

      // Assert
      expect(player.position).toBe('sitting');
      expect(player.stats.position).toBe('sitting');
    });
  });
});
