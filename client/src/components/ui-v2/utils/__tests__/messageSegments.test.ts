import { describe, expect, it } from 'vitest';
import { buildLine, validateSegments } from '../messageSegments';

const LINE = 'You attack Rat for 5 damage.';
const GOOD = [{ text: 'You attack ' }, { text: 'Rat', category: 'npc.aggressive_mob' }, { text: ' for 5 damage.' }];

describe('validateSegments', () => {
  it('keeps well-formed spans that join back to the text', () => {
    expect(validateSegments(GOOD, LINE)).toEqual(GOOD);
  });

  it('drops every span unless the texts join to exactly the message (loses colour, never words)', () => {
    expect(validateSegments(GOOD, 'You attack Rat for 6 damage.')).toBeUndefined();
    expect(validateSegments([{ text: 'Rat', category: 'npc.aggressive_mob' }], LINE)).toBeUndefined();
  });

  it('treats an unknown category as a plain span without discarding the rest of the line', () => {
    const result = validateSegments(
      [
        { text: 'You attack ' },
        { text: 'Rat', category: 'npc.aggressive_mob' },
        { text: ' for 5 damage.', category: 'lore.tome' },
      ],
      LINE
    );
    expect(result).toEqual(GOOD);
  });

  it('rejects anything that is not a list of {text} objects', () => {
    expect(validateSegments(undefined, LINE)).toBeUndefined();
    expect(validateSegments('Rat', LINE)).toBeUndefined();
    expect(validateSegments([LINE], LINE)).toBeUndefined();
    expect(validateSegments([{ text: 5 }], '5')).toBeUndefined();
    expect(validateSegments([null], '')).toBeUndefined();
  });

  it('returns nothing when no span is styled, since plain text is already the whole story', () => {
    expect(validateSegments([{ text: LINE }], LINE)).toBeUndefined();
    expect(validateSegments([{ text: LINE, category: 'bogus.thing' }], LINE)).toBeUndefined();
  });
});

describe('buildLine', () => {
  it('joins parts into text and keeps spans only when something is styled', () => {
    const styled = buildLine(['You attack ', { text: 'Rat', category: 'npc.passive_mob' }, '.']);
    expect(styled.text).toBe('You attack Rat.');
    expect(styled.segments).toEqual([
      { text: 'You attack ' },
      { text: 'Rat', category: 'npc.passive_mob' },
      { text: '.' },
    ]);

    const plain = buildLine(['You attack ', 'Rat', '.']);
    expect(plain.text).toBe('You attack Rat.');
    expect(plain.segments).toBeUndefined();
  });

  it('round-trips through validateSegments', () => {
    const line = buildLine(['Dealt 5 damage to ', { text: 'Rat', category: 'npc.aggressive_mob' }, '.']);
    expect(validateSegments(line.segments, line.text)).toEqual(line.segments);
  });
});
