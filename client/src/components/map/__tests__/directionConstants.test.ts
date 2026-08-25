/**
 * Tests that the map editor's direction constants stay in sync with the server's Direction
 * enum (server/models/command_base.py). See #627: the exit-creation API only accepts these
 * ten values, so offering more here (the editor previously also listed 'in'/'out') would let
 * a save silently 422.
 */

import { describe, expect, it } from 'vitest';
import { STANDARD_DIRECTIONS } from '../edgeModalLogic';
import { MAP_EDITOR_DIRECTIONS } from '../RoomMapEditorRuntime.hooks';

const SERVER_DIRECTIONS = [
  'north',
  'south',
  'east',
  'west',
  'up',
  'down',
  'northeast',
  'northwest',
  'southeast',
  'southwest',
];

describe('direction constants', () => {
  it('MAP_EDITOR_DIRECTIONS matches the server Direction enum exactly', () => {
    expect(new Set(MAP_EDITOR_DIRECTIONS)).toEqual(new Set(SERVER_DIRECTIONS));
  });

  it('STANDARD_DIRECTIONS matches the server Direction enum exactly', () => {
    expect(new Set(STANDARD_DIRECTIONS)).toEqual(new Set(SERVER_DIRECTIONS));
  });

  it('does not offer "in" or "out", which the exit API has never recognized', () => {
    expect(MAP_EDITOR_DIRECTIONS).not.toContain('in');
    expect(MAP_EDITOR_DIRECTIONS).not.toContain('out');
    expect(STANDARD_DIRECTIONS).not.toContain('in');
    expect(STANDARD_DIRECTIONS).not.toContain('out');
  });
});
