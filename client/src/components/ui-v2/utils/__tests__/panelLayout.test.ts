import { describe, expect, it } from 'vitest';
import {
  MINIMIZED_BAR_HEIGHT,
  MINIMIZED_DOCK_PADDING,
  computeMinimizedDockPosition,
  preparePanelForRestore,
} from '../../PanelSystem/panelMinimizeDock';
import { createDefaultPanelLayout } from '../panelLayout';

const HEADER_HEIGHT = 48;
const PADDING = 20;

function geometry(viewportWidth: number, viewportHeight: number) {
  const columnWidth = (viewportWidth - PADDING * 4) / 3;
  return {
    columnWidth,
    leftColumnX: PADDING,
    middleColumnX: PADDING * 2 + columnWidth,
    rightColumnX: PADDING * 3 + columnWidth * 2,
    top: HEADER_HEIGHT + PADDING,
    availableHeight: viewportHeight - HEADER_HEIGHT - PADDING * 2,
  };
}

describe('panelLayout', () => {
  describe('createDefaultPanelLayout', () => {
    it('should create exactly the expected panels (no dock Settings panel)', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(Object.keys(layout).sort()).toEqual([
        'characterInfo',
        'chatHistory',
        'commandHistory',
        'commandInput',
        'gameInfo',
        'inventory',
        'location',
        'minimap',
        'occupants',
        'questLog',
        'roomDescription',
      ]);
    });

    it('should create panels with correct IDs and titles', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      Object.entries(layout).forEach(([key, panel]) => expect(panel.id).toBe(key));
      expect(layout.chatHistory.title).toBe('Chat History');
      expect(layout.location.title).toBe('Location');
      expect(layout.roomDescription.title).toBe('Room Description');
      expect(layout.occupants.title).toBe('Occupants');
      expect(layout.gameInfo.title).toBe('Game Info');
      expect(layout.characterInfo.title).toBe('Character Info');
      expect(layout.minimap.title).toBe('Map');
      expect(layout.questLog.title).toBe('Journal');
      expect(layout.commandInput.title).toBe('Command Input');
      expect(layout.commandHistory.title).toBe('Command History');
      expect(layout.inventory.title).toBe('Inventory');
    });

    it('should open every panel except Command History and Inventory (#1018)', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      Object.values(layout).forEach(panel => {
        expect(panel.isMaximized).toBe(false);
        expect(panel.isVisible).toBe(true);
        expect(panel.zIndex).toBeGreaterThan(0);
      });

      const minimized = Object.values(layout)
        .filter(panel => panel.isMinimized)
        .map(panel => panel.id)
        .sort();
      expect(minimized).toEqual(['commandHistory', 'inventory']);
    });

    it('should place panels in the three columns', () => {
      const { leftColumnX, middleColumnX, rightColumnX, columnWidth } = geometry(1920, 1080);
      const layout = createDefaultPanelLayout(1920, 1080);

      for (const id of ['chatHistory', 'location', 'roomDescription', 'occupants'] as const) {
        expect(layout[id].position.x).toBe(leftColumnX);
        expect(layout[id].size.width).toBe(columnWidth);
      }
      expect(layout.gameInfo.position.x).toBe(middleColumnX);
      expect(layout.gameInfo.size.width).toBe(columnWidth);
      for (const id of ['characterInfo', 'minimap', 'questLog', 'commandInput'] as const) {
        expect(layout[id].position.x).toBe(rightColumnX);
        expect(layout[id].size.width).toBe(columnWidth);
      }
    });

    it('should keep Command Input in the right column only, not spanning the middle', () => {
      const { middleColumnX, columnWidth } = geometry(1920, 1080);
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout.commandInput.position.x).toBeGreaterThan(middleColumnX + columnWidth);
    });

    it('should give Game Info the full column height', () => {
      const { top, availableHeight } = geometry(1920, 1080);
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout.gameInfo.position.y).toBe(top);
      expect(layout.gameInfo.size.height).toBe(availableHeight);
    });

    it('should stack the left column contiguously and stop above the dock tray', () => {
      const { top } = geometry(1920, 1080);
      const layout = createDefaultPanelLayout(1920, 1080);
      const stack = [layout.chatHistory, layout.location, layout.roomDescription, layout.occupants];

      expect(stack[0].position.y).toBe(top);
      for (let i = 1; i < stack.length; i++) {
        expect(stack[i].position.y).toBeCloseTo(stack[i - 1].position.y + stack[i - 1].size.height, 6);
      }
      const bottom = stack[3].position.y + stack[3].size.height;
      expect(bottom).toBeLessThanOrEqual(1080 - MINIMIZED_BAR_HEIGHT - MINIMIZED_DOCK_PADDING);
      // Chat and room description dominate; occupants takes the remainder.
      expect(layout.chatHistory.size.height).toBeGreaterThan(layout.location.size.height);
      expect(layout.roomDescription.size.height).toBeGreaterThan(layout.location.size.height);
    });

    it('should stack the right column contiguously and fill it to the bottom margin', () => {
      const { top, availableHeight } = geometry(1920, 1080);
      const layout = createDefaultPanelLayout(1920, 1080);
      const stack = [layout.characterInfo, layout.minimap, layout.questLog, layout.commandInput];

      expect(stack[0].position.y).toBe(top);
      for (let i = 1; i < stack.length; i++) {
        expect(stack[i].position.y).toBeCloseTo(stack[i - 1].position.y + stack[i - 1].size.height, 6);
      }
      const bottom = stack[3].position.y + stack[3].size.height;
      expect(bottom).toBeCloseTo(top + availableHeight, 6);
      // Character Info dominates the column.
      expect(layout.characterInfo.size.height).toBeGreaterThan(layout.minimap.size.height);
      expect(layout.characterInfo.size.height).toBeGreaterThan(layout.commandInput.size.height);
    });

    it('should dock the minimized panels in the tray but remember where they open', () => {
      const layout = createDefaultPanelLayout(1920, 1080);
      const { commandHistory, inventory } = layout;

      expect(commandHistory.position).toEqual(computeMinimizedDockPosition(0, 1920, 1080));
      expect(inventory.position).toEqual(computeMinimizedDockPosition(1, 1920, 1080));

      // Expanding must restore the open geometry, not leave a full-size panel at the dock slot.
      for (const panel of [commandHistory, inventory]) {
        expect(panel.preMinimizePosition).toBeDefined();
        const restored = preparePanelForRestore(panel);
        expect(restored.isMinimized).toBe(false);
        expect(restored.position).toEqual(panel.preMinimizePosition);
        expect(restored.position.y + restored.size.height).toBeLessThanOrEqual(1080);
      }
    });

    it('should open the docked panels above their neighbours', () => {
      const layout = createDefaultPanelLayout(1920, 1080);
      const openZ = Math.max(
        ...Object.values(layout)
          .filter(panel => !panel.isMinimized)
          .map(panel => panel.zIndex)
      );

      expect(layout.commandHistory.zIndex).toBeGreaterThan(openZ);
      expect(layout.inventory.zIndex).toBeGreaterThan(openZ);
    });

    it('should keep the same height ratios at any viewport size', () => {
      const small = createDefaultPanelLayout(1920, 1080);
      const large = createDefaultPanelLayout(3840, 2160);
      const smallAvail = geometry(1920, 1080).availableHeight;
      const largeAvail = geometry(3840, 2160).availableHeight;

      expect(large.characterInfo.size.height / largeAvail).toBeCloseTo(small.characterInfo.size.height / smallAvail, 6);
      expect(large.questLog.size.height / largeAvail).toBeCloseTo(small.questLog.size.height / smallAvail, 6);
      expect(large.chatHistory.size.height / large.location.size.height).toBeCloseTo(
        small.chatHistory.size.height / small.location.size.height,
        6
      );
    });

    // Regression (#1018 e2e): at 1280x720 the right column's ratio heights fell below Command Input's
    // minSize, so it overflowed the viewport by 5px and focusing it scrolled the root, shifting the dock.
    it.each([
      [1280, 720],
      [1366, 768],
      [1920, 1080],
      [2513, 1301],
      [3840, 2160],
    ])('should respect minSize and stay inside the viewport at %ix%i', (width, height) => {
      const layout = createDefaultPanelLayout(width, height);
      const open = Object.values(layout).filter(panel => !panel.isMinimized);

      open.forEach(panel => {
        expect(panel.size.height, `${panel.id} height`).toBeGreaterThanOrEqual(panel.minSize?.height ?? 0);
        expect(panel.size.width, `${panel.id} width`).toBeGreaterThanOrEqual(panel.minSize?.width ?? 0);
        expect(panel.position.y + panel.size.height, `${panel.id} bottom`).toBeLessThanOrEqual(
          height - PADDING + 0.001
        );
        expect(panel.position.x + panel.size.width, `${panel.id} right`).toBeLessThanOrEqual(width - PADDING + 0.001);
      });
    });

    it('should fill the right column exactly at a short viewport', () => {
      const { top, availableHeight } = geometry(1280, 720);
      const layout = createDefaultPanelLayout(1280, 720);
      const stack = [layout.characterInfo, layout.minimap, layout.questLog, layout.commandInput];

      const bottom = stack[3].position.y + stack[3].size.height;
      expect(bottom).toBeCloseTo(top + availableHeight, 6);
    });

    it('should position panels below header', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      Object.values(layout)
        .filter(panel => !panel.isMinimized)
        .forEach(panel => {
          expect(panel.position.y).toBeGreaterThanOrEqual(HEADER_HEIGHT + PADDING);
        });
    });

    it('should set minimum sizes for every panel', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      Object.values(layout).forEach(panel => {
        expect(panel.minSize).toBeDefined();
        expect(panel.minSize?.width).toBeGreaterThan(0);
        expect(panel.minSize?.height).toBeGreaterThan(0);
      });
    });

    it('should keep the minimap opaque with a minimum height', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout.minimap.opaque).toBe(true);
      expect(layout.minimap.minHeight).toBe(100);
    });

    it('should handle different viewport sizes', () => {
      const smallLayout = createDefaultPanelLayout(800, 600);
      const largeLayout = createDefaultPanelLayout(3840, 2160);

      expect(smallLayout.chatHistory).toBeDefined();
      expect(largeLayout.chatHistory).toBeDefined();
      expect(largeLayout.chatHistory.size.width).toBeGreaterThan(smallLayout.chatHistory.size.width);
      expect(largeLayout.chatHistory.size.height).toBeGreaterThan(smallLayout.chatHistory.size.height);
    });

    it('should create panels with unique z-index values', () => {
      const layout = createDefaultPanelLayout(1920, 1080);
      const zIndices = Object.values(layout).map(panel => panel.zIndex);

      expect(new Set(zIndices).size).toBe(zIndices.length);
    });

    it('should create panels with valid position and size values', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      Object.values(layout).forEach(panel => {
        expect(panel.position.x).toBeGreaterThanOrEqual(0);
        expect(panel.position.y).toBeGreaterThanOrEqual(0);
        expect(panel.size.width).toBeGreaterThan(0);
        expect(panel.size.height).toBeGreaterThan(0);
      });
    });
  });
});
