/**
 * Tests for the MythosIcons name map.
 */

import { describe, expect, it } from 'vitest';
import { MythosIcons } from '../MythosIcons';

describe('MythosIcons', () => {
  it('should map every key to its own string literal name', () => {
    for (const [key, value] of Object.entries(MythosIcons)) {
      expect(value).toBe(key);
    }
  });

  it('should include the core UI icons consumed by EldritchIcon', () => {
    expect(MythosIcons.chat).toBe('chat');
    expect(MythosIcons.connection).toBe('connection');
    expect(MythosIcons.minimize).toBe('minimize');
    expect(MythosIcons.maximize).toBe('maximize');
    expect(MythosIcons.close).toBe('close');
  });

  it('should include the channel-specific icons used by ChannelSelector', () => {
    expect(MythosIcons.global).toBe('global');
    expect(MythosIcons.local).toBe('local');
    expect(MythosIcons.whisper).toBe('whisper');
    expect(MythosIcons.system).toBe('system');
  });

  it('should include the logout button icon', () => {
    expect(MythosIcons.portal).toBe('portal');
  });

  it('should have no duplicate icon names', () => {
    const names = Object.values(MythosIcons);
    expect(new Set(names).size).toBe(names.length);
  });
});
