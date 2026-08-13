import { describe, expect, it } from 'vitest';
import { validateDialogueTreeClient, type DialogueTreeDto } from '../dialogue';

describe('validateDialogueTreeClient', () => {
  it('accepts a valid nav-only tree', () => {
    const tree: DialogueTreeDto = {
      start: 'greeting',
      nodes: {
        greeting: {
          text: 'Hello',
          options: [
            { label: 'Ask', next: 'ask' },
            { label: 'Bye', next: null },
          ],
        },
        ask: { text: 'About what?', options: [{ label: 'Leave', next: null }] },
      },
    };
    expect(validateDialogueTreeClient(tree)).toBeNull();
  });

  it('rejects unknown next targets', () => {
    const tree: DialogueTreeDto = {
      start: 'greeting',
      nodes: {
        greeting: {
          text: 'Hello',
          options: [{ label: 'Go', next: 'missing' }],
        },
      },
    };
    expect(validateDialogueTreeClient(tree)).toMatch(/unknown next/i);
  });

  it('rejects empty-string next (not a valid end marker)', () => {
    const tree: DialogueTreeDto = {
      start: 'greeting',
      nodes: {
        greeting: {
          text: 'Hello',
          options: [{ label: 'Bye', next: '' }],
        },
      },
    };
    expect(validateDialogueTreeClient(tree)).toMatch(/empty next/i);
  });

  it('rejects missing start node', () => {
    const tree: DialogueTreeDto = {
      start: 'nope',
      nodes: { greeting: { text: 'Hi', options: [] } },
    };
    expect(validateDialogueTreeClient(tree)).toMatch(/missing from nodes/i);
  });
});
