import type { PanelState } from '../types';

// Panel layout utilities for default three-column layout
// Based on findings from "Spatial Organization in Non-Euclidean Interfaces" - Dr. Armitage, 1928

type LayoutMetrics = {
  headerHeight: number;
  padding: number;
  leftColumnX: number;
  leftColumnWidth: number;
  middleColumnX: number;
  middleColumnWidth: number;
  rightColumnX: number;
  rightColumnWidth: number;
  availableHeight: number;
  leftPanelHeight: number;
};

function layoutMetrics(viewportWidth: number, viewportHeight: number): LayoutMetrics {
  const headerHeight = 48;
  const padding = 20;
  const columnWidth = (viewportWidth - padding * 4) / 3;
  const availableHeight = viewportHeight - headerHeight - padding * 2;
  return {
    headerHeight,
    padding,
    leftColumnX: padding,
    leftColumnWidth: columnWidth,
    middleColumnX: padding * 2 + columnWidth,
    middleColumnWidth: columnWidth,
    rightColumnX: padding * 3 + columnWidth * 2,
    rightColumnWidth: columnWidth,
    availableHeight,
    leftPanelHeight: availableHeight / 4,
  };
}

function leftColumnPanels(m: LayoutMetrics): Record<string, PanelState> {
  const top = m.headerHeight + m.padding;
  return {
    chatHistory: {
      id: 'chatHistory',
      title: 'Chat History',
      position: { x: m.leftColumnX, y: top },
      size: { width: m.leftColumnWidth, height: m.leftPanelHeight * 2 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1000,
      minSize: { width: 300, height: 200 },
    },
    location: {
      id: 'location',
      title: 'Location',
      position: { x: m.leftColumnX, y: top + m.leftPanelHeight * 2 },
      size: { width: m.leftColumnWidth, height: m.leftPanelHeight * 0.5 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1001,
      minSize: { width: 200, height: 80 },
    },
    roomDescription: {
      id: 'roomDescription',
      title: 'Room Description',
      position: { x: m.leftColumnX, y: top + m.leftPanelHeight * 2.5 },
      size: { width: m.leftColumnWidth, height: m.leftPanelHeight * 0.75 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1002,
      minSize: { width: 200, height: 100 },
    },
    occupants: {
      id: 'occupants',
      title: 'Occupants',
      position: { x: m.leftColumnX, y: top + m.leftPanelHeight * 3.25 },
      size: { width: m.leftColumnWidth, height: m.leftPanelHeight * 0.75 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1003,
      minSize: { width: 200, height: 100 },
    },
  };
}

function middleColumnPanels(m: LayoutMetrics): Record<string, PanelState> {
  const top = m.headerHeight + m.padding;
  return {
    gameInfo: {
      id: 'gameInfo',
      title: 'Game Info',
      position: { x: m.middleColumnX, y: top },
      size: { width: m.middleColumnWidth, height: m.availableHeight * 0.55 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1004,
      minSize: { width: 300, height: 200 },
    },
    questLog: {
      id: 'questLog',
      title: 'Journal',
      position: { x: m.middleColumnX, y: top + m.availableHeight * 0.55 },
      size: { width: m.middleColumnWidth, height: m.availableHeight * 0.45 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1009,
      minSize: { width: 250, height: 180 },
    },
  };
}

function rightColumnPanels(m: LayoutMetrics): Record<string, PanelState> {
  const top = m.headerHeight + m.padding;
  return {
    characterInfo: {
      id: 'characterInfo',
      title: 'Character Info',
      position: { x: m.rightColumnX, y: top },
      size: { width: m.rightColumnWidth, height: m.availableHeight * 0.45 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1005,
      minSize: { width: 250, height: 200 },
    },
    minimap: {
      id: 'minimap',
      title: 'Map',
      position: { x: m.rightColumnX, y: top + m.availableHeight * 0.45 },
      size: {
        width: m.rightColumnWidth,
        height: Math.max(m.availableHeight * 0.2, 120),
      },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1006,
      minSize: { width: 150, height: 100 },
      opaque: true,
      minHeight: 100,
    },
    commandHistory: {
      id: 'commandHistory',
      title: 'Command History',
      position: { x: m.rightColumnX, y: top + m.availableHeight * 0.65 },
      size: { width: m.rightColumnWidth, height: m.availableHeight * 0.15 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1007,
      minSize: { width: 200, height: 150 },
    },
    commandInput: {
      id: 'commandInput',
      title: 'Command Input',
      position: { x: m.rightColumnX, y: top + m.availableHeight * 0.8 },
      size: { width: m.rightColumnWidth, height: m.availableHeight * 0.2 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1008,
      minSize: { width: 200, height: 100 },
    },
  };
}

export const createDefaultPanelLayout = (viewportWidth: number, viewportHeight: number): Record<string, PanelState> => {
  const m = layoutMetrics(viewportWidth, viewportHeight);
  return {
    ...leftColumnPanels(m),
    ...middleColumnPanels(m),
    ...rightColumnPanels(m),
  };
};
