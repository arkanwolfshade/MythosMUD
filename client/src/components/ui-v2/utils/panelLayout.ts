import type { PanelState } from '../types';

// Panel layout utilities for default three-column layout
// Based on findings from "Spatial Organization in Non-Euclidean Interfaces" - Dr. Armitage, 1928
// Hierarchy: chat + command are primary; auxiliary panels start minimized.

export const createDefaultPanelLayout = (viewportWidth: number, viewportHeight: number): Record<string, PanelState> => {
  const headerHeight = 48;
  const padding = 20;
  const columnWidth = (viewportWidth - padding * 4) / 3;
  const availableHeight = viewportHeight - headerHeight - padding * 2;

  const leftColumnX = padding;
  const leftColumnWidth = columnWidth;
  const middleColumnX = padding * 2 + columnWidth;
  const middleColumnWidth = columnWidth;
  const rightColumnX = padding * 3 + columnWidth * 2;
  const rightColumnWidth = columnWidth;

  // Chat dominates left column; location/room are secondary strips
  const chatHeight = availableHeight * 0.62;
  const locationHeight = availableHeight * 0.12;
  const roomDescHeight = availableHeight * 0.26;

  return {
    chatHistory: {
      id: 'chatHistory',
      title: 'Chat History',
      position: { x: leftColumnX, y: headerHeight + padding },
      size: { width: leftColumnWidth, height: chatHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1000,
      minSize: { width: 300, height: 200 },
    },
    location: {
      id: 'location',
      title: 'Location',
      position: { x: leftColumnX, y: headerHeight + padding + chatHeight },
      size: { width: leftColumnWidth, height: locationHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1001,
      minSize: { width: 200, height: 80 },
    },
    roomDescription: {
      id: 'roomDescription',
      title: 'Room Description',
      position: { x: leftColumnX, y: headerHeight + padding + chatHeight + locationHeight },
      size: { width: leftColumnWidth, height: roomDescHeight },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1002,
      minSize: { width: 200, height: 100 },
    },
    occupants: {
      id: 'occupants',
      title: 'Occupants',
      position: { x: leftColumnX, y: headerHeight + padding + availableHeight - 40 },
      size: { width: leftColumnWidth, height: availableHeight * 0.2 },
      isMinimized: true,
      isMaximized: false,
      isVisible: true,
      zIndex: 1003,
      minSize: { width: 200, height: 100 },
    },
    gameInfo: {
      id: 'gameInfo',
      title: 'Game Info',
      position: { x: middleColumnX, y: headerHeight + padding },
      size: { width: middleColumnWidth, height: availableHeight * 0.55 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1004,
      minSize: { width: 300, height: 200 },
    },
    characterInfo: {
      id: 'characterInfo',
      title: 'Character Info',
      position: { x: rightColumnX, y: headerHeight + padding },
      size: { width: rightColumnWidth, height: availableHeight * 0.35 },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1005,
      minSize: { width: 250, height: 200 },
    },
    minimap: {
      id: 'minimap',
      title: 'Map',
      position: {
        x: rightColumnX,
        y: headerHeight + padding + availableHeight * 0.35,
      },
      size: {
        width: rightColumnWidth,
        height: Math.max(availableHeight * 0.18, 120),
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
      position: {
        x: rightColumnX,
        y: headerHeight + padding + availableHeight * 0.55,
      },
      size: { width: rightColumnWidth, height: availableHeight * 0.12 },
      isMinimized: true,
      isMaximized: false,
      isVisible: true,
      zIndex: 1007,
      minSize: { width: 200, height: 150 },
    },
    commandInput: {
      id: 'commandInput',
      title: 'Command Input',
      position: {
        x: middleColumnX,
        y: headerHeight + padding + availableHeight * 0.72,
      },
      size: {
        width: middleColumnWidth + padding + rightColumnWidth,
        height: availableHeight * 0.28,
      },
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      zIndex: 1010,
      minSize: { width: 280, height: 120 },
    },
    questLog: {
      id: 'questLog',
      title: 'Journal',
      position: { x: middleColumnX, y: headerHeight + padding + availableHeight * 0.55 },
      size: { width: middleColumnWidth, height: availableHeight * 0.17 },
      isMinimized: true,
      isMaximized: false,
      isVisible: true,
      zIndex: 1009,
      minSize: { width: 250, height: 180 },
    },
  };
};
