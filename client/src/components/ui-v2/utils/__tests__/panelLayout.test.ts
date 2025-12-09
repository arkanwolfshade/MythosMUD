import { describe, expect, it } from 'vitest';
import { createDefaultPanelLayout } from '../panelLayout';

describe('panelLayout', () => {
  describe('createDefaultPanelLayout', () => {
    it('should create a default panel layout with all required panels', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout).toBeDefined();
      expect(layout.chatHistory).toBeDefined();
      expect(layout.location).toBeDefined();
      expect(layout.roomDescription).toBeDefined();
      expect(layout.occupants).toBeDefined();
      expect(layout.gameInfo).toBeDefined();
      expect(layout.characterInfo).toBeDefined();
      expect(layout.commandHistory).toBeDefined();
      expect(layout.commandInput).toBeDefined();
    });

    it('should create panels with correct IDs', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout.chatHistory.id).toBe('chatHistory');
      expect(layout.location.id).toBe('location');
      expect(layout.roomDescription.id).toBe('roomDescription');
      expect(layout.occupants.id).toBe('occupants');
      expect(layout.gameInfo.id).toBe('gameInfo');
      expect(layout.characterInfo.id).toBe('characterInfo');
      expect(layout.commandHistory.id).toBe('commandHistory');
      expect(layout.commandInput.id).toBe('commandInput');
    });

    it('should create panels with correct titles', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout.chatHistory.title).toBe('Chat History');
      expect(layout.location.title).toBe('Location');
      expect(layout.roomDescription.title).toBe('Room Description');
      expect(layout.occupants.title).toBe('Occupants');
      expect(layout.gameInfo.title).toBe('Game Info');
      expect(layout.characterInfo.title).toBe('Character Info');
      expect(layout.commandHistory.title).toBe('Command History');
      expect(layout.commandInput.title).toBe('Command Input');
    });

    it('should create panels with correct initial state', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      Object.values(layout).forEach(panel => {
        expect(panel.isMinimized).toBe(false);
        expect(panel.isMaximized).toBe(false);
        expect(panel.isVisible).toBe(true);
        expect(panel.zIndex).toBeGreaterThan(0);
      });
    });

    it('should calculate correct column widths for three-column layout', () => {
      const viewportWidth = 1920;
      const padding = 20;
      const expectedColumnWidth = (viewportWidth - padding * 4) / 3;

      const layout = createDefaultPanelLayout(viewportWidth, 1080);

      // Left column panels should have same width
      expect(layout.chatHistory.size.width).toBe(expectedColumnWidth);
      expect(layout.location.size.width).toBe(expectedColumnWidth);
      expect(layout.roomDescription.size.width).toBe(expectedColumnWidth);
      expect(layout.occupants.size.width).toBe(expectedColumnWidth);

      // Middle column panel
      expect(layout.gameInfo.size.width).toBe(expectedColumnWidth);

      // Right column panels should have same width
      expect(layout.characterInfo.size.width).toBe(expectedColumnWidth);
      expect(layout.commandHistory.size.width).toBe(expectedColumnWidth);
      expect(layout.commandInput.size.width).toBe(expectedColumnWidth);
    });

    it('should position panels in correct columns', () => {
      const viewportWidth = 1920;
      const padding = 20;
      const columnWidth = (viewportWidth - padding * 4) / 3;

      const layout = createDefaultPanelLayout(viewportWidth, 1080);

      const leftColumnX = padding;
      const middleColumnX = padding * 2 + columnWidth;
      const rightColumnX = padding * 3 + columnWidth * 2;

      // Left column panels
      expect(layout.chatHistory.position.x).toBe(leftColumnX);
      expect(layout.location.position.x).toBe(leftColumnX);
      expect(layout.roomDescription.position.x).toBe(leftColumnX);
      expect(layout.occupants.position.x).toBe(leftColumnX);

      // Middle column panel
      expect(layout.gameInfo.position.x).toBe(middleColumnX);

      // Right column panels
      expect(layout.characterInfo.position.x).toBe(rightColumnX);
      expect(layout.commandHistory.position.x).toBe(rightColumnX);
      expect(layout.commandInput.position.x).toBe(rightColumnX);
    });

    it('should position panels below header', () => {
      const viewportHeight = 1080;
      const headerHeight = 48;
      const padding = 20;

      const layout = createDefaultPanelLayout(1920, viewportHeight);

      Object.values(layout).forEach(panel => {
        expect(panel.position.y).toBeGreaterThanOrEqual(headerHeight + padding);
      });
    });

    it('should set minimum sizes for panels', () => {
      const layout = createDefaultPanelLayout(1920, 1080);

      expect(layout.chatHistory.minSize).toBeDefined();
      expect(layout.chatHistory.minSize?.width).toBeGreaterThan(0);
      expect(layout.chatHistory.minSize?.height).toBeGreaterThan(0);

      expect(layout.location.minSize).toBeDefined();
      expect(layout.location.minSize?.width).toBeGreaterThan(0);
      expect(layout.location.minSize?.height).toBeGreaterThan(0);

      expect(layout.roomDescription.minSize).toBeDefined();
      expect(layout.roomDescription.minSize?.width).toBeGreaterThan(0);
      expect(layout.roomDescription.minSize?.height).toBeGreaterThan(0);

      expect(layout.occupants.minSize).toBeDefined();
      expect(layout.occupants.minSize?.width).toBeGreaterThan(0);
      expect(layout.occupants.minSize?.height).toBeGreaterThan(0);

      expect(layout.gameInfo.minSize).toBeDefined();
      expect(layout.gameInfo.minSize?.width).toBeGreaterThan(0);
      expect(layout.gameInfo.minSize?.height).toBeGreaterThan(0);

      expect(layout.characterInfo.minSize).toBeDefined();
      expect(layout.characterInfo.minSize?.width).toBeGreaterThan(0);
      expect(layout.characterInfo.minSize?.height).toBeGreaterThan(0);

      expect(layout.commandHistory.minSize).toBeDefined();
      expect(layout.commandHistory.minSize?.width).toBeGreaterThan(0);
      expect(layout.commandHistory.minSize?.height).toBeGreaterThan(0);

      expect(layout.commandInput.minSize).toBeDefined();
      expect(layout.commandInput.minSize?.width).toBeGreaterThan(0);
      expect(layout.commandInput.minSize?.height).toBeGreaterThan(0);
    });

    it('should handle different viewport sizes', () => {
      const smallLayout = createDefaultPanelLayout(800, 600);
      const largeLayout = createDefaultPanelLayout(3840, 2160);

      // All panels should exist in both layouts
      expect(smallLayout.chatHistory).toBeDefined();
      expect(largeLayout.chatHistory).toBeDefined();

      // Panel sizes should scale with viewport
      expect(largeLayout.chatHistory.size.width).toBeGreaterThan(smallLayout.chatHistory.size.width);
      expect(largeLayout.chatHistory.size.height).toBeGreaterThan(smallLayout.chatHistory.size.height);
    });

    it('should create panels with unique z-index values', () => {
      const layout = createDefaultPanelLayout(1920, 1080);
      const zIndices = Object.values(layout).map(panel => panel.zIndex);
      const uniqueZIndices = new Set(zIndices);

      // All z-indices should be unique
      expect(uniqueZIndices.size).toBe(zIndices.length);
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
