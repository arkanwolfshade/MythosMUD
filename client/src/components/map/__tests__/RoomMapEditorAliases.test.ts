import { describe, expect, it } from 'vitest';

import { RoomMapEditor as RoomMapEditorAlias } from '../RoomMapEditor';
import { RoomMapEditor as RoomMapEditorCoreAlias } from '../RoomMapEditorCore';
import { RoomMapEditor as RoomMapEditorFeatureAlias } from '../RoomMapEditorFeature';
import { RoomMapEditor as RoomMapEditorImplAlias } from '../RoomMapEditorImpl';
import { RoomMapEditor as RoomMapEditorRuntime } from '../RoomMapEditorRuntime';
import { RoomMapEditor as RoomMapEditorSceneAlias } from '../RoomMapEditorScene';

describe('RoomMapEditor alias exports', () => {
  it('all aliases resolve to RoomMapEditorRuntime export', () => {
    expect(RoomMapEditorAlias).toBe(RoomMapEditorRuntime);
    expect(RoomMapEditorCoreAlias).toBe(RoomMapEditorRuntime);
    expect(RoomMapEditorFeatureAlias).toBe(RoomMapEditorRuntime);
    expect(RoomMapEditorImplAlias).toBe(RoomMapEditorRuntime);
    expect(RoomMapEditorSceneAlias).toBe(RoomMapEditorRuntime);
  });
});
