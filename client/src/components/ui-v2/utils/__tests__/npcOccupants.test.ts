import { describe, expect, it } from 'vitest';
import { normalizeNpcOccupants, normalizeOptionalNpcOccupants, npcNames } from '../npcOccupants';

describe('normalizeNpcOccupants', () => {
  it('keeps well-formed entries, in order, duplicates included', () => {
    const raw = [
      { name: 'Rat', disposition: 'passive_mob' },
      { name: 'Rat', disposition: 'aggressive_mob' },
      { name: 'Merchant', disposition: 'shopkeeper' },
      { name: 'Elder', disposition: 'quest_giver' },
    ];
    expect(normalizeNpcOccupants(raw)).toEqual(raw);
  });

  it('falls back to passive_mob for an unknown or missing disposition (matches the server)', () => {
    expect(normalizeNpcOccupants([{ name: 'Odd', disposition: 'friendly' }, { name: 'Bare' }])).toEqual([
      { name: 'Odd', disposition: 'passive_mob' },
      { name: 'Bare', disposition: 'passive_mob' },
    ]);
  });

  it('drops legacy bare strings and other junk instead of upgrading them', () => {
    expect(
      normalizeNpcOccupants(['Goblin', null, 7, { name: '' }, { name: 3 }, { disposition: 'shopkeeper' }])
    ).toEqual([]);
  });

  it('treats a non-array as an empty list', () => {
    expect(normalizeNpcOccupants('not-an-array')).toEqual([]);
    expect(normalizeNpcOccupants(undefined)).toEqual([]);
  });
});

describe('normalizeOptionalNpcOccupants', () => {
  it('keeps "omitted" distinct from an authoritative empty list', () => {
    expect(normalizeOptionalNpcOccupants(undefined)).toBeUndefined();
    expect(normalizeOptionalNpcOccupants([])).toEqual([]);
  });
});

describe('npcNames', () => {
  it('lists names for the flat occupants list', () => {
    expect(
      npcNames([
        { name: 'Rat', disposition: 'passive_mob' },
        { name: 'Merchant', disposition: 'shopkeeper' },
      ])
    ).toEqual(['Rat', 'Merchant']);
  });
});
