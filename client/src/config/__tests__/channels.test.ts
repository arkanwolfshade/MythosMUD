import { describe, expect, it } from 'vitest';
import {
  AVAILABLE_CHANNELS,
  ALL_MESSAGES_CHANNEL,
  CHAT_CHANNEL_OPTIONS,
  DEFAULT_CHANNEL,
  CHANNEL_GROUPS,
  getChannelById,
  getEnabledChannels,
  getChannelDisplayName,
} from '../channels';

describe('channels', () => {
  describe('AVAILABLE_CHANNELS', () => {
    it('should have all expected channels', () => {
      expect(AVAILABLE_CHANNELS).toBeDefined();
      expect(Array.isArray(AVAILABLE_CHANNELS)).toBe(true);
      expect(AVAILABLE_CHANNELS.length).toBeGreaterThan(0);
    });

    it('should have required channel properties', () => {
      AVAILABLE_CHANNELS.forEach(channel => {
        expect(channel).toHaveProperty('id');
        expect(channel).toHaveProperty('name');
        expect(channel).toHaveProperty('description');
        expect(channel).toHaveProperty('icon');
        expect(channel).toHaveProperty('color');
        expect(channel).toHaveProperty('shortcut');
        expect(typeof channel.id).toBe('string');
        expect(typeof channel.name).toBe('string');
      });
    });

    it('should have unique channel IDs', () => {
      const ids = AVAILABLE_CHANNELS.map(ch => ch.id);
      const uniqueIds = new Set(ids);
      expect(uniqueIds.size).toBe(ids.length);
    });

    it('should include basic channels', () => {
      const channelIds = AVAILABLE_CHANNELS.map(ch => ch.id);
      expect(channelIds).toContain('say');
      expect(channelIds).toContain('local');
      expect(channelIds).toContain('global');
      expect(channelIds).toContain('whisper');
    });
  });

  describe('ALL_MESSAGES_CHANNEL', () => {
    it('should be defined', () => {
      expect(ALL_MESSAGES_CHANNEL).toBeDefined();
    });

    it('should have id "all"', () => {
      expect(ALL_MESSAGES_CHANNEL.id).toBe('all');
    });

    it('should have required properties', () => {
      expect(ALL_MESSAGES_CHANNEL).toHaveProperty('name');
      expect(ALL_MESSAGES_CHANNEL).toHaveProperty('description');
      expect(ALL_MESSAGES_CHANNEL).toHaveProperty('icon');
      expect(ALL_MESSAGES_CHANNEL).toHaveProperty('color');
    });
  });

  describe('CHAT_CHANNEL_OPTIONS', () => {
    it('should include ALL_MESSAGES_CHANNEL first', () => {
      expect(CHAT_CHANNEL_OPTIONS[0]).toBe(ALL_MESSAGES_CHANNEL);
    });

    it('should include all available channels', () => {
      expect(CHAT_CHANNEL_OPTIONS.length).toBe(AVAILABLE_CHANNELS.length + 1);
      AVAILABLE_CHANNELS.forEach(channel => {
        expect(CHAT_CHANNEL_OPTIONS).toContain(channel);
      });
    });
  });

  describe('DEFAULT_CHANNEL', () => {
    it('should be "all"', () => {
      expect(DEFAULT_CHANNEL).toBe('all');
    });

    it('should match ALL_MESSAGES_CHANNEL id', () => {
      expect(DEFAULT_CHANNEL).toBe(ALL_MESSAGES_CHANNEL.id);
    });
  });

  describe('CHANNEL_GROUPS', () => {
    it('should have expected group categories', () => {
      expect(CHANNEL_GROUPS).toHaveProperty('basic');
      expect(CHANNEL_GROUPS).toHaveProperty('area');
      expect(CHANNEL_GROUPS).toHaveProperty('server');
      expect(CHANNEL_GROUPS).toHaveProperty('advanced');
    });

    it('should have correct channels in basic group', () => {
      expect(CHANNEL_GROUPS.basic).toContain('say');
    });

    it('should have correct channels in area group', () => {
      expect(CHANNEL_GROUPS.area).toContain('local');
    });

    it('should have correct channels in server group', () => {
      expect(CHANNEL_GROUPS.server).toContain('global');
    });

    it('should have correct channels in advanced group', () => {
      expect(CHANNEL_GROUPS.advanced).toContain('whisper');
    });
  });

  describe('getChannelById', () => {
    it('should return channel for valid ID', () => {
      const channel = getChannelById('say');
      expect(channel).toBeDefined();
      expect(channel?.id).toBe('say');
    });

    it('should return channel from CHAT_CHANNEL_OPTIONS', () => {
      const channel = getChannelById('all');
      expect(channel).toBeDefined();
      expect(channel?.id).toBe('all');
    });

    it('should return undefined for invalid ID', () => {
      const channel = getChannelById('nonexistent');
      expect(channel).toBeUndefined();
    });

    it('should return undefined for empty string', () => {
      const channel = getChannelById('');
      expect(channel).toBeUndefined();
    });

    it('should return correct channel for all available channels', () => {
      AVAILABLE_CHANNELS.forEach(expectedChannel => {
        const channel = getChannelById(expectedChannel.id);
        expect(channel).toBeDefined();
        expect(channel?.id).toBe(expectedChannel.id);
        expect(channel?.name).toBe(expectedChannel.name);
      });
    });
  });

  describe('getEnabledChannels', () => {
    it('should return an array', () => {
      const enabled = getEnabledChannels();
      expect(Array.isArray(enabled)).toBe(true);
    });

    it('should only include channels that are not disabled', () => {
      const enabled = getEnabledChannels();
      enabled.forEach(channel => {
        expect(channel.disabled).not.toBe(true);
      });
    });

    it('should exclude disabled channels', () => {
      const enabled = getEnabledChannels();
      const disabledChannels = AVAILABLE_CHANNELS.filter(ch => ch.disabled === true);
      disabledChannels.forEach(disabled => {
        expect(enabled).not.toContain(disabled);
      });
    });

    it('should include all non-disabled channels', () => {
      const enabled = getEnabledChannels();
      const expectedEnabled = AVAILABLE_CHANNELS.filter(ch => !ch.disabled);
      expect(enabled.length).toBe(expectedEnabled.length);
      expectedEnabled.forEach(expected => {
        expect(enabled).toContain(expected);
      });
    });
  });

  describe('getChannelDisplayName', () => {
    it('should return display name with shortcut prefix for channels with shortcut', () => {
      const channel = getChannelById('say');
      if (channel?.shortcut) {
        const displayName = getChannelDisplayName('say');
        expect(displayName).toContain('/');
        expect(displayName).toContain(channel.shortcut);
      }
    });

    it('should return channel name for channels without shortcut', () => {
      const displayName = getChannelDisplayName('all');
      const channel = getChannelById('all');
      expect(displayName).toBe(channel?.name || 'all');
    });

    it('should return channel ID for non-existent channel', () => {
      const displayName = getChannelDisplayName('nonexistent');
      expect(displayName).toBe('nonexistent');
    });

    it('should handle empty string', () => {
      const displayName = getChannelDisplayName('');
      expect(displayName).toBe('');
    });

    it('should format shortcut correctly', () => {
      const sayChannel = getChannelById('say');
      if (sayChannel?.shortcut) {
        const displayName = getChannelDisplayName('say');
        expect(displayName).toBe(`/${sayChannel.shortcut}`);
      }
    });

    it('should return correct display names for all available channels', () => {
      AVAILABLE_CHANNELS.forEach(channel => {
        const displayName = getChannelDisplayName(channel.id);
        if (channel.shortcut) {
          expect(displayName).toBe(`/${channel.shortcut}`);
        } else {
          expect(displayName).toBe(channel.name);
        }
      });
    });
  });
});
