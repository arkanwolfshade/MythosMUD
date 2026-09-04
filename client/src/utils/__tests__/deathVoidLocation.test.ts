import { describe, expect, it } from 'vitest';
import { locationIndicatesDeathVoid, requiredAliveButDeadMessage } from '../deathVoidLocation';

describe('locationIndicatesDeathVoid', () => {
  it('treats Location Death > Void as void even when Game Info still has a foyer room id', () => {
    const body = [
      'Location',
      'Death > Void',
      'Game Info',
      'earth_arkhamcity_sanitarium_room_foyer_001',
      'Occupants (1)',
    ].join('\n');
    expect(locationIndicatesDeathVoid(body)).toBe(true);
  });

  it('does not treat stale Game Info void dumps as current location when Location is foyer', () => {
    const body = [
      'Location',
      'Arkham Sanitarium > Main Foyer',
      'Game Info',
      'limbo_death_void_limbo_death_void',
      'Death > Void',
    ].join('\n');
    expect(locationIndicatesDeathVoid(body)).toBe(false);
  });
});

describe('requiredAliveButDeadMessage', () => {
  it('names the player and blames current test or previous-test cleanup', () => {
    const msg = requiredAliveButDeadMessage('Ithaqua');
    expect(msg).toContain('Ithaqua');
    expect(msg).toMatch(/this test/i);
    expect(msg).toMatch(/previous test/i);
  });
});
